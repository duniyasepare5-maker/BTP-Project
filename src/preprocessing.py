"""
preprocessing.py
Feature selection, data cleaning, pipeline definition, and grouped train/test splitting
to strictly prevent data leakage in experimental geotechnical datasets.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import GroupKFold, GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List

FEATURE_COLS = [
    "is_disconnected",
    "n_piles",
    "pile_diameter_mm",
    "pile_length_m",
    "pile_spacing_ratio",
    "raft_width_mm",
    "raft_thickness_mm",
    "pile_area_ratio",
    "cushion_thickness_ratio",
    "cushion_d50_mm",
    "cushion_friction_deg",
    "cushion_gamma_kn_m3",
    "soil_d50_mm",
    "soil_friction_deg",
    "soil_relative_density_pct",
    "soil_gamma_kn_m3",
    "applied_load_kn",
    "settlement_mm",
    "normalized_settlement_pct",
    "applied_pressure_kpa"
]

PRIMARY_TARGET = "pile_load_share_pct"
SECONDARY_TARGET = "settlement_efficiency_eta"
GROUP_COL = "experiment_id"

def get_feature_and_target_matrices(
    df: pd.DataFrame, 
    target_col: str = PRIMARY_TARGET
) -> Tuple[pd.DataFrame, pd.Series, pd.Series]:
    """
    Extracts features matrix X, target y, and grouping variable groups.
    """
    X = df[FEATURE_COLS].copy()
    y = df[target_col].copy()
    groups = df[GROUP_COL].copy()
    return X, y, groups

def split_by_group(
    df: pd.DataFrame,
    test_size: float = 0.20,
    random_state: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Performs GroupShuffleSplit so that observations from an entire experimental
    test setup are held out together in either train OR test, preventing data leakage.
    """
    gss = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    train_idx, test_idx = next(gss.split(df, groups=df[GROUP_COL]))
    
    train_df = df.iloc[train_idx].copy().reset_index(drop=True)
    test_df = df.iloc[test_idx].copy().reset_index(drop=True)
    return train_df, test_df

def fit_scaler(X_train: pd.DataFrame) -> Tuple[StandardScaler, pd.DataFrame]:
    """
    Fits scaler STRICTLY on training features to prevent data snooping.
    """
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X_train.columns
    )
    return scaler, X_train_scaled

def transform_with_scaler(scaler: StandardScaler, X: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms any feature matrix using previously fitted training scaler.
    """
    return pd.DataFrame(scaler.transform(X), columns=X.columns)
