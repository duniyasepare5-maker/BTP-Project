"""
train.py
Model training, grouped cross-validation, hyperparameter tuning,
and physics-constrained model selection for DPRF load-sharing prediction.
"""

import os
import json
import joblib
import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import GroupKFold, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb

from preprocessing import (
    FEATURE_COLS, PRIMARY_TARGET, GROUP_COL,
    get_feature_and_target_matrices, split_by_group, fit_scaler, transform_with_scaler
)
from physics_constraints import PhysicsConstrainedModelWrapper

def calculate_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {"R2": round(r2, 4), "MAE": round(mae, 4), "MSE": round(mse, 4), "RMSE": round(rmse, 4)}

def train_and_compare_models(df: pd.DataFrame, output_dir: str, models_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)
    
    # 1. Grouped train/test split to prevent cross-experiment leakage
    train_df, test_df = split_by_group(df, test_size=0.20, random_state=42)
    print(f"Train samples: {len(train_df)} ({train_df[GROUP_COL].nunique()} experiments)")
    print(f"Test samples:  {len(test_df)} ({test_df[GROUP_COL].nunique()} experiments)")
    
    X_train, y_train, groups_train = get_feature_and_target_matrices(train_df)
    X_test, y_test, groups_test = get_feature_and_target_matrices(test_df)
    
    # 2. Strict featurization ordering: fit scaler ONLY on train set
    scaler, X_train_scaled = fit_scaler(X_train)
    X_test_scaled = transform_with_scaler(scaler, X_test)
    
    # Define candidate models
    candidate_models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Polynomial Regression (Deg 2)": Pipeline([
            ("poly", PolynomialFeatures(degree=2)),
            ("ridge", Ridge(alpha=10.0))
        ]),
        "Support Vector Regressor (SVR)": SVR(C=50.0, epsilon=0.1, gamma="scale"),
        "Decision Tree Regressor": DecisionTreeRegressor(max_depth=5, random_state=42),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42),
        "Gradient Boosting Regressor": GradientBoostingRegressor(n_estimators=100, learning_rate=0.08, max_depth=4, random_state=42),
        "XGBoost Regressor": xgb.XGBRegressor(n_estimators=100, learning_rate=0.08, max_depth=4, random_state=42)
    }
    
    results = []
    gkf = GroupKFold(n_splits=min(5, groups_train.nunique()))
    
    for name, model in candidate_models.items():
        # Evaluate using GroupKFold Cross Validation
        cv_r2, cv_mae, cv_rmse = [], [], []
        
        # Decide whether to use scaled or unscaled features
        use_scaled = name in ["Linear Regression", "Ridge Regression", "Polynomial Regression (Deg 2)", "Support Vector Regressor (SVR)"]
        X_tr = X_train_scaled if use_scaled else X_train
        X_te = X_test_scaled if use_scaled else X_test
        
        for tr_idx, val_idx in gkf.split(X_tr, y_train, groups_train):
            X_cv_tr, X_cv_val = X_tr.iloc[tr_idx], X_tr.iloc[val_idx]
            y_cv_tr, y_cv_val = y_train.iloc[tr_idx], y_train.iloc[val_idx]
            
            model.fit(X_cv_tr, y_cv_tr)
            y_val_pred = model.predict(X_cv_val)
            
            cv_r2.append(r2_score(y_cv_val, y_val_pred))
            cv_mae.append(mean_absolute_error(y_cv_val, y_val_pred))
            cv_rmse.append(np.sqrt(mean_squared_error(y_cv_val, y_val_pred)))
            
        # Fit on full training set
        model.fit(X_tr, y_train)
        train_pred = model.predict(X_tr)
        test_pred = model.predict(X_te)
        
        train_metrics = calculate_metrics(y_train, train_pred)
        test_metrics = calculate_metrics(y_test, test_pred)
        
        results.append({
            "Model": name,
            "CV_R2_Mean": round(np.mean(cv_r2), 4),
            "CV_MAE_Mean": round(np.mean(cv_mae), 4),
            "CV_RMSE_Mean": round(np.mean(cv_rmse), 4),
            "Train_R2": train_metrics["R2"],
            "Train_MAE": train_metrics["MAE"],
            "Train_RMSE": train_metrics["RMSE"],
            "Test_R2": test_metrics["R2"],
            "Test_MAE": test_metrics["MAE"],
            "Test_RMSE": test_metrics["RMSE"]
        })
        
    results_df = pd.DataFrame(results).sort_values("Test_R2", ascending=False)
    results_csv = os.path.join(output_dir, "model_comparison.csv")
    results_df.to_csv(results_csv, index=False)
    print("\n--- Model Benchmark Results ---")
    print(results_df.to_string(index=False))
    
    # 3. Hyperparameter Tuning for Ensemble Models
    print("\nPerforming Hyperparameter Tuning for Ensemble Models...")
    cv_splits = list(gkf.split(X_train, y_train, groups_train))
    
    rf_params = {
        "n_estimators": [50, 100, 150],
        "max_depth": [4, 6, 8, None],
        "min_samples_split": [2, 3, 5]
    }
    rf_grid = GridSearchCV(
        RandomForestRegressor(random_state=42),
        rf_params,
        cv=cv_splits,
        scoring="neg_root_mean_squared_error",
        n_jobs=1
    )
    rf_grid.fit(X_train, y_train)
    best_rf = rf_grid.best_estimator_
    
    xgb_params = {
        "n_estimators": [50, 100, 150],
        "max_depth": [3, 4, 5],
        "learning_rate": [0.03, 0.08, 0.15]
    }
    xgb_grid = GridSearchCV(
        xgb.XGBRegressor(random_state=42),
        xgb_params,
        cv=cv_splits,
        scoring="neg_root_mean_squared_error",
        n_jobs=1
    )
    xgb_grid.fit(X_train, y_train)
    best_xgb = xgb_grid.best_estimator_
    
    # Compare tuned models on Test Set
    rf_test_pred = best_rf.predict(X_test)
    xgb_test_pred = best_xgb.predict(X_test)
    
    rf_metrics = calculate_metrics(y_test, rf_test_pred)
    xgb_metrics = calculate_metrics(y_test, xgb_test_pred)
    
    if rf_metrics["Test_R2" if "Test_R2" in rf_metrics else "R2"] >= xgb_metrics["Test_R2" if "Test_R2" in xgb_metrics else "R2"]:
        best_model = best_rf
        best_name = "Tuned Random Forest Regressor"
        best_metrics = rf_metrics
        scaler_to_save = None
    else:
        best_model = best_xgb
        best_name = "Tuned XGBoost Regressor"
        best_metrics = xgb_metrics
        scaler_to_save = None

    print(f"\nSelected Best Model: {best_name}")
    print(f"Test Set Performance: R2={best_metrics['R2']}, MAE={best_metrics['MAE']}, RMSE={best_metrics['RMSE']}")
    
    # 4. Wrap with Physics Constrained Predictor
    constrained_model = PhysicsConstrainedModelWrapper(
        base_model=best_model,
        feature_names=FEATURE_COLS,
        scaler=scaler_to_save
    )
    
    # Save artifacts
    model_path = os.path.join(models_dir, "best_model.pkl")
    scaler_path = os.path.join(models_dir, "scaler.pkl")
    joblib.dump(best_model, model_path)
    joblib.dump(scaler, scaler_path)
    
    meta = {
        "best_model_name": best_name,
        "feature_names": FEATURE_COLS,
        "primary_target": PRIMARY_TARGET,
        "test_metrics": best_metrics,
        "n_train_samples": len(train_df),
        "n_test_samples": len(test_df),
        "train_experiments": list(train_df[GROUP_COL].unique()),
        "test_experiments": list(test_df[GROUP_COL].unique())
    }
    with open(os.path.join(models_dir, "model_metadata.json"), "w") as f:
        json.dump(meta, f, indent=4)
        
    # Save predictions dataframe for evaluation
    test_df_copy = test_df.copy()
    test_p_pred, test_r_pred = constrained_model.predict(test_df)
    test_df_copy["pred_pile_load_share_pct"] = np.round(test_p_pred, 2)
    test_df_copy["pred_raft_load_share_pct"] = np.round(test_r_pred, 2)
    test_df_copy["pred_pile_group_load_kn"] = np.round(test_df_copy["applied_load_kn"] * (test_p_pred / 100.0), 3)
    test_df_copy["pred_raft_load_kn"] = np.round(test_df_copy["applied_load_kn"] * (test_r_pred / 100.0), 3)
    test_df_copy.to_csv(os.path.join(output_dir, "test_predictions.csv"), index=False)
    
    print(f"Models and metadata successfully saved to {models_dir}")
    return constrained_model, results_df

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cleaned_csv = os.path.join(base_dir, "data", "processed", "dprf_cleaned_dataset.csv")
    out_dir = os.path.join(base_dir, "outputs", "results")
    mod_dir = os.path.join(base_dir, "models")
    df = pd.read_csv(cleaned_csv)
    train_and_compare_models(df, out_dir, mod_dir)
