"""
evaluate.py
Evaluates trained models with comprehensive diagnostic plots:
1. Parity Plot: Actual vs Predicted Load Sharing (alpha_p and alpha_r)
2. Load Decomposition Parity: Actual vs Predicted Q_p and Q_r
3. Residual Distribution & Heteroscedasticity Analysis
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams.update({"font.size": 11, "figure.dpi": 300, "savefig.dpi": 300})

def run_evaluation(results_dir: str, figures_dir: str):
    os.makedirs(figures_dir, exist_ok=True)
    
    test_pred_path = os.path.join(results_dir, "test_predictions.csv")
    if not os.path.exists(test_pred_path):
        raise FileNotFoundError(f"Missing {test_pred_path}")
        
    df = pd.read_csv(test_pred_path)
    
    # -------------------------------------------------------------
    # Figure 6: Actual vs Predicted Parity Plots (alpha_p & Q_p)
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Subplot 1: Pile load share % (alpha_p)
    ax1.scatter(df["pile_load_share_pct"], df["pred_pile_load_share_pct"], 
                c="blue", edgecolor="k", s=70, alpha=0.8, label="Test Observations")
    min_val = 0.0
    max_val = max(df["pile_load_share_pct"].max(), df["pred_pile_load_share_pct"].max()) * 1.1
    ax1.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=1.8, label="1:1 Ideal Fit Line")
    ax1.plot([min_val, max_val], [min_val * 1.1, max_val * 1.1], "gray", linestyle=":", label="±10% Error Bound")
    ax1.plot([min_val, max_val], [min_val * 0.9, max_val * 0.9], "gray", linestyle=":")
    ax1.set_xlabel("Experimental Pile Load Share, $\\alpha_p$ (%)")
    ax1.set_ylabel("Predicted Pile Load Share, $\\hat{\\alpha}_p$ (%)")
    ax1.set_title("Parity Plot: Pile Load Share (\\%)")
    ax1.legend(loc="upper left")
    
    # Subplot 2: Decomposed Pile Group Load in kN (Q_p)
    ax2.scatter(df["pile_group_load_kn"], df["pred_pile_group_load_kn"], 
                c="crimson", edgecolor="k", s=70, alpha=0.8, label="Test Observations")
    q_max = max(df["pile_group_load_kn"].max(), df["pred_pile_group_load_kn"].max()) * 1.1
    ax2.plot([0, q_max], [0, q_max], "k--", linewidth=1.8, label="1:1 Ideal Fit Line")
    ax2.set_xlabel("Experimental Pile Group Load, $Q_p$ (kN)")
    ax2.set_ylabel("Predicted Pile Group Load, $\\hat{Q}_p$ (kN)")
    ax2.set_title("Parity Plot: Pile Group Load (kN)")
    ax2.legend(loc="upper left")
    
    plt.suptitle("Model Prediction Accuracy on Held-Out Experimental Test Series", y=1.02)
    plt.tight_layout()
    fig6_path = os.path.join(figures_dir, "fig06_actual_vs_predicted_parity.png")
    plt.savefig(fig6_path)
    plt.close()
    print(f"Saved: {fig6_path}")
    
    # -------------------------------------------------------------
    # Figure 7: Residual Diagnostic Analysis
    # -------------------------------------------------------------
    residuals = df["pred_pile_load_share_pct"] - df["pile_load_share_pct"]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Residuals vs Predicted
    ax1.scatter(df["pred_pile_load_share_pct"], residuals, c="teal", edgecolor="k", s=65, alpha=0.8)
    ax1.axhline(0, color="red", linestyle="--", linewidth=1.5)
    ax1.set_xlabel("Predicted Pile Load Share, $\\hat{\\alpha}_p$ (%)")
    ax1.set_ylabel("Residual ($\\hat{\\alpha}_p - \\alpha_p$) (%)")
    ax1.set_title("Residuals vs. Predicted Values (Homoscedasticity Check)")
    
    # Residual Distribution Histogram & KDE
    sns.histplot(residuals, kde=True, ax=ax2, color="purple", bins=10)
    ax2.axvline(0, color="red", linestyle="--", linewidth=1.5)
    ax2.set_xlabel("Residual Error (%)")
    ax2.set_ylabel("Frequency Count")
    ax2.set_title("Residual Error Distribution (Normality Check)")
    
    plt.suptitle("Statistical Residual Diagnostics for DPRF Model", y=1.02)
    plt.tight_layout()
    fig7_path = os.path.join(figures_dir, "fig07_residual_analysis.png")
    plt.savefig(fig7_path)
    plt.close()
    print(f"Saved: {fig7_path}")
    
    # Summary metrics
    metrics = {
        "n_test_eval": len(df),
        "mean_residual": round(float(np.mean(residuals)), 4),
        "std_residual": round(float(np.std(residuals)), 4),
        "max_abs_residual": round(float(np.max(np.abs(residuals))), 4)
    }
    with open(os.path.join(results_dir, "evaluation_summary.json"), "w") as f:
        json.dump(metrics, f, indent=4)
    print("Evaluation summary saved:", metrics)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    res_dir = os.path.join(base_dir, "outputs", "results")
    fig_dir = os.path.join(base_dir, "outputs", "figures")
    run_evaluation(res_dir, fig_dir)
