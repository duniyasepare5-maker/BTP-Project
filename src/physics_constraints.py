"""
physics_constraints.py
Rigorous Geotechnical Engineering Physics Constraints & Domain Validation
Enforces:
1. Load equilibrium: Q = Q_p + Q_r
2. Load-sharing proportion: alpha_p + alpha_r = 100%
3. Physical bounds: 0 <= alpha_p <= 100%, 0 <= alpha_r <= 100%
4. Domain verification: Warns when inputs exceed experimental calibration envelope
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple, Optional

# Validated experimental envelope from Halder & Manna (2021, 2022) and literature benchmarks
EXPERIMENTAL_ENVELOPE = {
    "n_piles": (0, 9),
    "pile_diameter_mm": (20.0, 30.0),
    "pile_length_m": (0.3, 1.2),
    "pile_spacing_ratio": (0.0, 4.0),
    "raft_width_mm": (200.0, 350.0),
    "raft_thickness_mm": (15.0, 30.0),
    "cushion_thickness_ratio": (0.0, 4.0),
    "cushion_d50_mm": (0.0, 5.0),
    "cushion_friction_deg": (0.0, 60.0),
    "soil_friction_deg": (35.0, 45.0),
    "normalized_settlement_pct": (0.0, 10.0),
    "applied_load_kn": (0.0, 25.0)
}

def check_domain_validity(inputs: Dict[str, float]) -> Tuple[bool, list]:
    """
    Checks if a set of input parameters falls within the experimentally validated domain.
    Returns (is_valid, warnings_list).
    """
    warnings = []
    for param, (low, high) in EXPERIMENTAL_ENVELOPE.items():
        if param in inputs:
            val = float(inputs[param])
            if val < low or val > high:
                warnings.append(
                    f"Parameter '{param}' value {val} is outside validated experimental range [{low}, {high}]."
                )
    is_valid = len(warnings) == 0
    return is_valid, warnings

def enforce_equilibrium(
    applied_load_kn: float,
    predicted_pile_share_pct: float
) -> Dict[str, float]:
    """
    Enforces exact physical equilibrium:
    - Clips pile load share into [0%, 100%]
    - Sets raft load share = 100% - pile_share
    - Decomposes applied load into Q_p and Q_r
    - Guarantees Q_p + Q_r == applied_load_kn
    """
    # Boundary constraints
    alpha_p = float(np.clip(predicted_pile_share_pct, 0.0, 100.0))
    alpha_r = 100.0 - alpha_p
    
    # Static load equilibrium
    q_total = max(0.0, float(applied_load_kn))
    q_p = q_total * (alpha_p / 100.0)
    q_r = q_total * (alpha_r / 100.0)
    
    # Equilibrium verification
    eq_error = abs((q_p + q_r) - q_total)
    assert eq_error < 1e-5, f"Equilibrium violation: {eq_error}"
    
    return {
        "applied_load_kn": q_total,
        "pile_load_share_pct": round(alpha_p, 2),
        "raft_load_share_pct": round(alpha_r, 2),
        "pile_group_load_kn": round(q_p, 3),
        "raft_load_kn": round(q_r, 3),
        "equilibrium_verified": True
    }

class PhysicsConstrainedModelWrapper:
    """
    Wraps an underlying ML regressor (e.g., Random Forest, SVR, XGBoost)
    to guarantee strictly physical and equilibrium-satisfying predictions.
    """
    def __init__(self, base_model, feature_names: list, scaler=None):
        self.base_model = base_model
        self.feature_names = feature_names
        self.scaler = scaler

    def predict(self, X: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Predicts pile load share % and raft load share %, enforcing equilibrium.
        Returns:
            alpha_p: np.ndarray (pile share %)
            alpha_r: np.ndarray (raft share %)
        """
        # Ensure correct column ordering
        X_ordered = X[self.feature_names]
        
        if self.scaler is not None:
            X_scaled = self.scaler.transform(X_ordered)
            raw_pred = self.base_model.predict(X_scaled)
        else:
            raw_pred = self.base_model.predict(X_ordered)
            
        # Constrain pile load share to [0, 100]
        alpha_p = np.clip(raw_pred, 0.0, 100.0)
        
        # Enforce exact equilibrium: alpha_r = 100 - alpha_p
        alpha_r = 100.0 - alpha_p
        
        return alpha_p, alpha_r

    def predict_single(self, input_dict: Dict[str, float]) -> Dict[str, Any]:
        """
        Makes a physical prediction for a single instance with domain checking.
        """
        is_valid, warnings = check_domain_validity(input_dict)
        
        # Build single row dataframe
        row_df = pd.DataFrame([input_dict])
        
        # If pile_area_ratio is missing, compute it
        if "pile_area_ratio" not in row_df.columns:
            npiles = row_df["n_piles"].iloc[0]
            dpile = row_df["pile_diameter_mm"].iloc[0]
            wraft = row_df["raft_width_mm"].iloc[0]
            row_df["pile_area_ratio"] = (npiles * np.pi * (dpile ** 2) / 4.0) / (wraft ** 2)
            
        # If applied_pressure_kpa is missing, compute it
        if "applied_pressure_kpa" not in row_df.columns and "applied_load_kn" in row_df.columns:
            wraft_m = row_df["raft_width_mm"].iloc[0] / 1000.0
            row_df["applied_pressure_kpa"] = row_df["applied_load_kn"].iloc[0] / (wraft_m ** 2)
            
        alpha_p, alpha_r = self.predict(row_df)
        
        p_pct = float(alpha_p[0])
        q_kn = float(input_dict.get("applied_load_kn", 0.0))
        
        result = enforce_equilibrium(q_kn, p_pct)
        result["domain_valid"] = is_valid
        result["domain_warnings"] = warnings
        return result

if __name__ == "__main__":
    test_inputs = {
        "applied_load_kn": 19.4,
        "n_piles": 9,
        "pile_diameter_mm": 25.4,
        "pile_length_m": 1.0,
        "pile_spacing_ratio": 3.0,
        "raft_width_mm": 300.0,
        "raft_thickness_mm": 25.0,
        "cushion_thickness_ratio": 2.0,
        "cushion_d50_mm": 2.0,
        "cushion_friction_deg": 51.0,
        "cushion_gamma_kn_m3": 17.5,
        "soil_d50_mm": 0.3,
        "soil_friction_deg": 40.7,
        "soil_relative_density_pct": 70.0,
        "soil_gamma_kn_m3": 15.9,
        "settlement_mm": 30.0,
        "normalized_settlement_pct": 10.0,
        "is_disconnected": 1
    }
    valid, warns = check_domain_validity(test_inputs)
    print("Domain valid:", valid, "Warnings:", warns)
    eq = enforce_equilibrium(19.4, 34.8)
    print("Equilibrium result:", eq)
