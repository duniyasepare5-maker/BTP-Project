"""
parametric_study.py
Conducts sensitivity and parametric studies using the trained physics-constrained model:
1. Variation with cushion thickness ratio (h/d)
2. Variation with cushion mean particle size (d50)
3. Variation with pile group size (n_p)
4. Variation with normalized settlement (w/B)
Generates publication-quality parametric comparison curves.
"""

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from physics_constraints import PhysicsConstrainedModelWrapper
from preprocessing import FEATURE_COLS

plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams.update({"font.size": 11, "figure.dpi": 300, "savefig.dpi": 300})

def run_parametric_study(models_dir: str, figures_dir: str, results_dir: str):
    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)
    
    best_model = joblib.load(os.path.join(models_dir, "best_model.pkl"))
    scaler = None
    if os.path.exists(os.path.join(models_dir, "scaler.pkl")):
        # Only use scaler if model requires it
        pass
        
    wrapper = PhysicsConstrainedModelWrapper(best_model, FEATURE_COLS, scaler=scaler)
    
    # Baseline configuration: 3x3 DPRF with CM2 in dense sand at w/B = 10%
    baseline = {
        "is_disconnected": 1,
        "n_piles": 9,
        "pile_diameter_mm": 25.4,
        "pile_length_m": 1.0,
        "pile_spacing_ratio": 3.0,
        "raft_width_mm": 300.0,
        "raft_thickness_mm": 25.0,
        "pile_area_ratio": (9 * np.pi * (25.4 ** 2) / 4.0) / (300.0 ** 2),
        "cushion_thickness_ratio": 2.0,
        "cushion_d50_mm": 2.0,
        "cushion_friction_deg": 51.0,
        "cushion_gamma_kn_m3": 17.5,
        "soil_d50_mm": 0.3,
        "soil_friction_deg": 40.7,
        "soil_relative_density_pct": 70.0,
        "soil_gamma_kn_m3": 15.9,
        "applied_load_kn": 19.4,
        "settlement_mm": 30.0,
        "normalized_settlement_pct": 10.0,
        "applied_pressure_kpa": 19.4 / (0.3 ** 2)
    }
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    records = []
    
    # -------------------------------------------------------------
    # 1. Parametric: Cushion Thickness (h/d)
    # -------------------------------------------------------------
    hd_range = np.linspace(0.5, 4.0, 15)
    p_hd, r_hd = [], []
    for hd in hd_range:
        inp = baseline.copy()
        inp["cushion_thickness_ratio"] = hd
        res = wrapper.predict_single(inp)
        p_hd.append(res["pile_load_share_pct"])
        r_hd.append(res["raft_load_share_pct"])
        records.append({"parameter": "cushion_thickness_ratio", "value": hd, **res})
        
    ax1.plot(hd_range, p_hd, "b-o", linewidth=2.2, label="Pile Share $\\alpha_p$ (%)")
    ax1.plot(hd_range, r_hd, "k--s", linewidth=2.2, label="Raft Share $\\alpha_r$ (%)")
    ax1.set_xlabel("Cushion Thickness Ratio ($h/d$)")
    ax1.set_ylabel("Load Share (%)")
    ax1.set_title("(a) Sensitivity to Cushion Thickness ($h/d$)")
    ax1.legend()
    ax1.grid(True, alpha=0.4)
    
    # -------------------------------------------------------------
    # 2. Parametric: Cushion Particle Size (d50)
    # -------------------------------------------------------------
    d50_range = np.linspace(0.5, 4.5, 15)
    p_d50, r_d50 = [], []
    for d50 in d50_range:
        inp = baseline.copy()
        inp["cushion_d50_mm"] = d50
        # Friction angle correlates with d50 in experimental cushion sands
        inp["cushion_friction_deg"] = 46.0 + 2.2 * d50
        res = wrapper.predict_single(inp)
        p_d50.append(res["pile_load_share_pct"])
        r_d50.append(res["raft_load_share_pct"])
        records.append({"parameter": "cushion_d50_mm", "value": d50, **res})
        
    ax2.plot(d50_range, p_d50, "m-D", linewidth=2.2, label="Pile Share $\\alpha_p$ (%)")
    ax2.plot(d50_range, r_d50, "k--^", linewidth=2.2, label="Raft Share $\\alpha_r$ (%)")
    ax2.set_xlabel("Cushion Particle Size, $d_{50}$ (mm)")
    ax2.set_ylabel("Load Share (%)")
    ax2.set_title("(b) Sensitivity to Cushion Granularity ($d_{50}$)")
    ax2.legend()
    ax2.grid(True, alpha=0.4)
    
    # -------------------------------------------------------------
    # 3. Parametric: Normalized Settlement (w/B)
    # -------------------------------------------------------------
    wb_range = np.linspace(0.5, 10.0, 20)
    p_wb, r_wb = [], []
    for wb in wb_range:
        inp = baseline.copy()
        inp["normalized_settlement_pct"] = wb
        inp["settlement_mm"] = wb * 3.0
        # Load follows non-linear curve up to 19.4 kN
        inp["applied_load_kn"] = 19.4 * (wb / 10.0) ** 0.65
        inp["applied_pressure_kpa"] = inp["applied_load_kn"] / (0.3 ** 2)
        res = wrapper.predict_single(inp)
        p_wb.append(res["pile_load_share_pct"])
        r_wb.append(res["raft_load_share_pct"])
        records.append({"parameter": "normalized_settlement_pct", "value": wb, **res})
        
    ax3.plot(wb_range, p_wb, "g-^", linewidth=2.2, label="Pile Share $\\alpha_p$ (%)")
    ax3.plot(wb_range, r_wb, "k--v", linewidth=2.2, label="Raft Share $\\alpha_r$ (%)")
    ax3.set_xlabel("Normalized Settlement, $w/B$ (%)")
    ax3.set_ylabel("Load Share (%)")
    ax3.set_title("(c) Load-Sharing Kinetics vs. Settlement ($w/B$)")
    ax3.legend()
    ax3.grid(True, alpha=0.4)
    
    # -------------------------------------------------------------
    # 4. Parametric: Number of Piles (n_p)
    # -------------------------------------------------------------
    np_range = [1, 4, 9]
    p_np, r_np = [], []
    for np_val in np_range:
        inp = baseline.copy()
        inp["n_piles"] = np_val
        inp["pile_area_ratio"] = (np_val * np.pi * (25.4 ** 2) / 4.0) / (300.0 ** 2)
        res = wrapper.predict_single(inp)
        p_np.append(res["pile_load_share_pct"])
        r_np.append(res["raft_load_share_pct"])
        records.append({"parameter": "n_piles", "value": np_val, **res})
        
    ax4.bar([str(x) + " Piles" for x in np_range], p_np, color=["skyblue", "royalblue", "darkblue"], width=0.4, label="Pile Share $\\alpha_p$ (%)")
    ax4.set_xlabel("Pile Group Configuration")
    ax4.set_ylabel("Pile Load Share, $\\alpha_p$ (%)")
    ax4.set_title("(d) Influence of Pile Group Reinforcement Density")
    ax4.set_ylim(0, 50)
    for i, v in enumerate(p_np):
        ax4.text(i, v + 1.0, f"{v:.1f}%", ha="center", fontweight="bold")
    ax4.grid(True, alpha=0.4)
    
    plt.suptitle("Parametric Sensitivity Analysis of Disconnected Piled Raft Foundations", y=1.02, fontsize=15)
    plt.tight_layout()
    fig10_path = os.path.join(figures_dir, "fig10_parametric_study.png")
    plt.savefig(fig10_path)
    plt.close()
    print(f"Saved: {fig10_path}")
    
    # Save CSV
    df_res = pd.DataFrame(records)
    df_res.to_csv(os.path.join(results_dir, "parametric_study_results.csv"), index=False)
    print(f"Parametric study completed and saved.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    m_dir = os.path.join(base_dir, "models")
    f_dir = os.path.join(base_dir, "outputs", "figures")
    r_dir = os.path.join(base_dir, "outputs", "results")
    run_parametric_study(m_dir, f_dir, r_dir)
