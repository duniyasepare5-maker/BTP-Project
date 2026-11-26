"""
visualization.py
Generates academic publication-quality figures for:
1. CPR vs DPR vs UR Load-Settlement Response
2. Load Sharing Kinetics (Pile % vs Raft %) as a function of Settlement (w/B)
3. Influence of Cushion Thickness (h/d) on Load Sharing & Settlement Efficiency
4. Influence of Cushion Granularity (d50) on Load Sharing & Settlement Efficiency
5. Comprehensive Correlation Heatmap
6. Model Parity & Residual Diagnostic Plots
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set publication style
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams.update({
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.fontsize": 10,
    "figure.titlesize": 14,
    "figure.dpi": 300,
    "savefig.dpi": 300
})

def generate_eda_figures(df: pd.DataFrame, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    
    # -------------------------------------------------------------
    # Figure 1: Load vs Normalized Settlement (CPR vs DPR vs UR)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Filter representative series
    series_map = {
        "HM22_UR": ("Unpiled Raft (UR)", "black", "-", "o"),
        "HM22_CPR_2x2": ("Connected Piled Raft (CPR 2x2)", "red", "--", "s"),
        "HM22_DPR_2x2_hd1": ("DPRF 2x2 (h/d=1, BS)", "blue", "-.", "^"),
        "HM22_DPR_2x2_hd2": ("DPRF 2x2 (h/d=2, BS)", "green", "-.", "D"),
        "HM22_DPR_2x2_hd3": ("DPRF 2x2 (h/d=3, BS)", "orange", "-.", "v"),
        "HM21_DPR_3x3_hd2_CM2": ("DPRF 3x3 (h/d=2, CM2)", "purple", "-", "P")
    }
    
    for exp_id, (label, color, ls, marker) in series_map.items():
        sub = df[df["experiment_id"] == exp_id].sort_values("normalized_settlement_pct")
        if not sub.empty:
            ax.plot(sub["applied_load_kn"], sub["normalized_settlement_pct"], 
                    label=label, color=color, linestyle=ls, marker=marker, markersize=5, linewidth=1.8)
            
    ax.invert_yaxis()
    ax.set_xlabel("Applied Vertical Load, $Q$ (kN)")
    ax.set_ylabel("Normalized Settlement, $w/B$ (%)")
    ax.set_title("Experimental Load-Settlement Response (1g Model Tests)")
    ax.legend(frameon=True, facecolor="white", framealpha=0.9)
    plt.tight_layout()
    fig_path = os.path.join(output_dir, "fig01_load_settlement_comparison.png")
    plt.savefig(fig_path)
    plt.close()
    print(f"Saved: {fig_path}")

    # -------------------------------------------------------------
    # Figure 2: Load Sharing Kinetics vs Normalized Settlement (CPR vs DPRF)
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # CPR 2x2
    sub_cpr = df[df["experiment_id"] == "HM22_CPR_2x2"].sort_values("normalized_settlement_pct")
    if not sub_cpr.empty:
        ax1.plot(sub_cpr["normalized_settlement_pct"], sub_cpr["pile_load_share_pct"], 
                 "r-o", label="Pile Share $\\alpha_p$ (%)", linewidth=2)
        ax1.plot(sub_cpr["normalized_settlement_pct"], sub_cpr["raft_load_share_pct"], 
                 "k--s", label="Raft Share $\\alpha_r$ (%)", linewidth=2)
        ax1.set_xlabel("Normalized Settlement, $w/B$ (%)")
        ax1.set_ylabel("Load Share (%)")
        ax1.set_title("Connected Piled Raft (CPR 2x2)")
        ax1.set_ylim(-2, 102)
        ax1.legend()
        ax1.text(2.5, 55, "Piles take majority load initially\nthen capacity yields to raft", 
                 bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    # DPR 3x3 (h/d=2, CM2)
    sub_dpr = df[df["experiment_id"] == "HM21_DPR_3x3_hd2_CM2"].sort_values("normalized_settlement_pct")
    if not sub_dpr.empty:
        ax2.plot(sub_dpr["normalized_settlement_pct"], sub_dpr["pile_load_share_pct"], 
                 "b-^", label="Pile Share $\\alpha_p$ (%)", linewidth=2)
        ax2.plot(sub_dpr["normalized_settlement_pct"], sub_dpr["raft_load_share_pct"], 
                 "k--v", label="Raft Share $\\alpha_r$ (%)", linewidth=2)
        ax2.set_xlabel("Normalized Settlement, $w/B$ (%)")
        ax2.set_ylabel("Load Share (%)")
        ax2.set_title("Disconnected Piled Raft (DPRF 3x3, $h/d=2$)")
        ax2.set_ylim(-2, 102)
        ax2.legend()
        ax2.text(2.0, 45, "Raft takes majority load initially;\npile share mobilizes with settlement", 
                 bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.5))

    plt.suptitle("Fundamental Inversion of Load-Sharing Kinetics: CPR vs DPRF", y=1.02)
    plt.tight_layout()
    fig_path = os.path.join(output_dir, "fig02_load_sharing_kinetics.png")
    plt.savefig(fig_path)
    plt.close()
    print(f"Saved: {fig_path}")

    # -------------------------------------------------------------
    # Figure 3: Influence of Cushion Thickness (h/d)
    # -------------------------------------------------------------
    sub_hd = df[(df["foundation_type"] == "DPRF") & 
                (df["n_piles"] == 9) & 
                (df["cushion_d50_mm"] == 2.0) & 
                (df["normalized_settlement_pct"] == 10.0)].sort_values("cushion_thickness_ratio")
    
    if not sub_hd.empty:
        fig, ax1 = plt.subplots(figsize=(7, 5))
        ax2 = ax1.twinx()
        
        ax1.plot(sub_hd["cushion_thickness_ratio"], sub_hd["pile_load_share_pct"], 
                 "b-o", linewidth=2.2, label="Pile Load Share $\\alpha_p$ (%)")
        ax2.plot(sub_hd["cushion_thickness_ratio"], sub_hd["settlement_efficiency_eta"], 
                 "g--s", linewidth=2.2, label="Settlement Efficiency $\\eta$")
        
        ax1.set_xlabel("Normalized Cushion Thickness ($h/d$)")
        ax1.set_ylabel("Pile Load Share, $\\alpha_p$ (%)", color="blue")
        ax2.set_ylabel("Settlement Efficiency, $\\eta$", color="green")
        ax1.set_title("Influence of Cushion Thickness ($h/d$) at $w/B = 10\\%$ (3x3 DPRF)")
        
        # Combine legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
        
        plt.tight_layout()
        fig_path = os.path.join(output_dir, "fig03_cushion_thickness_effect.png")
        plt.savefig(fig_path)
        plt.close()
        print(f"Saved: {fig_path}")

    # -------------------------------------------------------------
    # Figure 4: Influence of Cushion Granularity (d50)
    # -------------------------------------------------------------
    sub_d50 = df[(df["foundation_type"] == "DPRF") & 
                 (df["n_piles"] == 9) & 
                 (df["cushion_thickness_ratio"] == 2.0) & 
                 (df["normalized_settlement_pct"] == 10.0)].sort_values("cushion_d50_mm")
    
    if not sub_d50.empty:
        fig, ax1 = plt.subplots(figsize=(7, 5))
        ax2 = ax1.twinx()
        
        ax1.plot(sub_d50["cushion_d50_mm"], sub_d50["pile_load_share_pct"], 
                 "m-D", linewidth=2.2, label="Pile Load Share $\\alpha_p$ (%)")
        ax2.plot(sub_d50["cushion_d50_mm"], sub_d50["settlement_efficiency_eta"], 
                 "c--^", linewidth=2.2, label="Settlement Efficiency $\\eta$")
        
        ax1.set_xlabel("Cushion Mean Particle Size, $d_{50}$ (mm)")
        ax1.set_ylabel("Pile Load Share, $\\alpha_p$ (%)", color="m")
        ax2.set_ylabel("Settlement Efficiency, $\\eta$", color="c")
        ax1.set_title("Influence of Cushion Granularity ($d_{50}$) at $w/B = 10\\%$ (3x3 DPRF)")
        
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="lower right")
        
        plt.tight_layout()
        fig_path = os.path.join(output_dir, "fig04_cushion_granularity_effect.png")
        plt.savefig(fig_path)
        plt.close()
        print(f"Saved: {fig_path}")

    # -------------------------------------------------------------
    # Figure 5: Correlation Matrix Heatmap
    # -------------------------------------------------------------
    corr_cols = [
        "n_piles", "pile_area_ratio", "cushion_thickness_ratio", 
        "cushion_d50_mm", "cushion_friction_deg", "applied_load_kn", 
        "normalized_settlement_pct", "pile_load_share_pct", "settlement_efficiency_eta"
    ]
    corr_df = df[corr_cols].corr()
    
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, ax=ax, linewidths=0.5)
    ax.set_title("Pearson Correlation Heatmap of Key Geotechnical Variables")
    plt.tight_layout()
    fig_path = os.path.join(output_dir, "fig05_correlation_heatmap.png")
    plt.savefig(fig_path)
    plt.close()
    print(f"Saved: {fig_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cleaned_csv = os.path.join(base_dir, "data", "processed", "dprf_cleaned_dataset.csv")
    out_dir = os.path.join(base_dir, "outputs", "figures")
    df = pd.read_csv(cleaned_csv)
    generate_eda_figures(df, out_dir)
