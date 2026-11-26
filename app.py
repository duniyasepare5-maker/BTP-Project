"""
app.py
Professional Academic Research Streamlit Application:
Machine Learning-Based Prediction of Load Sharing Characteristics of Disconnected Piled Raft Foundations (DPRF)
Authors: Geotechnical & Machine Learning Research Team
"""

import os
import sys
import json
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Add src to path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")
if src_dir not in sys.path:
    sys.path.append(src_dir)

from physics_constraints import PhysicsConstrainedModelWrapper, check_domain_validity, EXPERIMENTAL_ENVELOPE
from preprocessing import FEATURE_COLS

st.set_page_config(
    page_title="DPRF Load-Sharing ML Prediction System",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean academic UI
st.markdown("""
<style>
    .main-header {
        font-size: 26px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 16px;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #F3F4F6;
        border-radius: 8px;
        padding: 15px;
        border-left: 5px solid #2563EB;
        margin-bottom: 10px;
    }
    .warning-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    .success-box {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_prediction_model():
    models_dir = os.path.join(current_dir, "models")
    model_path = os.path.join(models_dir, "best_model.pkl")
    meta_path = os.path.join(models_dir, "model_metadata.json")
    
    if not os.path.exists(model_path) or not os.path.exists(meta_path):
        st.error("Model artifacts not found! Please run src/train.py first.")
        return None, None
        
    base_model = joblib.load(model_path)
    with open(meta_path, "r") as f:
        meta = json.load(f)
        
    wrapper = PhysicsConstrainedModelWrapper(base_model, FEATURE_COLS)
    return wrapper, meta

@st.cache_data
def load_datasets_and_results():
    data_path = os.path.join(current_dir, "data", "processed", "dprf_cleaned_dataset.csv")
    sources_path = os.path.join(current_dir, "data", "dataset_sources.csv")
    comparison_path = os.path.join(current_dir, "outputs", "results", "model_comparison.csv")
    
    df_data = pd.read_csv(data_path) if os.path.exists(data_path) else None
    df_sources = pd.read_csv(sources_path) if os.path.exists(sources_path) else None
    df_comp = pd.read_csv(comparison_path) if os.path.exists(comparison_path) else None
    return df_data, df_sources, df_comp

model_wrapper, model_meta = load_prediction_model()
df_cleaned, df_sources, df_model_comp = load_datasets_and_results()

# Sidebar Navigation
logo_path = os.path.join(current_dir, "reports", "iitd_logo.png")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=75)
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "1. Project Overview",
        "2. Dataset & Research",
        "3. ML Model Performance",
        "4. Load-Sharing Prediction",
        "5. Parametric Analysis"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Project Status**: Research Grade ✅")
st.sidebar.markdown("**Physics Constraints**: $Q = Q_r + Q_p$ Enforced ⚖️")
st.sidebar.markdown("**Data Source**: Halder & Manna (2021, 2022)")

# -------------------------------------------------------------
# PAGE 1: PROJECT OVERVIEW
# -------------------------------------------------------------
if page == "1. Project Overview":
    st.markdown('<div class="main-header">Machine Learning-Based Prediction of Load Sharing Characteristics of Disconnected Piled Raft Foundations</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Academic Geotechnical Research System | Soil-Structure Interaction & Physics-Constrained AI</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        ### Research Objective
        To develop a scientifically rigorous, reproducible, and physically constrained machine learning prediction system for the load-sharing characteristics of **Disconnected Piled Raft Foundations (DPRF)** using verified published experimental data.
        
        ### What is a Disconnected Piled Raft Foundation?
        In conventional **Connected Piled Raft (CPR)** systems, piles are rigidly connected to the raft, leading to severe stress concentrations at the pile heads and high structural bending moments during lateral or seismic events.
        
        In a **Disconnected Piled Raft (DPRF)** system:
        - The piles are structurally separated from the raft base via an engineered **granular cushion layer** (or Load Transfer Platform, LTP).
        - The piles function primarily as **settlement-reducing subsoil reinforcement** rather than structural load-bearing columns.
        - Superstructure vertical load is transferred indirectly through granular cushion arching and shear interlock, drastically reducing pile head stresses and permitting a much lower factor of safety ($FS \\approx 1.3$ vs $4.0$).
        """)
        
    with col2:
        with st.container(border=True):
            st.markdown("#### Fundamental Equilibrium Equations")
            st.markdown(r"""
            - Total Vertical Load: $Q = Q_r + Q_p$
            - Pile Load Share: $\alpha_p = (Q_p / Q) \times 100\%$
            - Raft Load Share: $\alpha_r = (Q_r / Q) \times 100\%$
            - Equilibrium Identity: $\alpha_p + \alpha_r = 100\%$
            - Settlement Efficiency: $\eta = (w_{UR} - w_{DPR}) / w_{UR}$
            """)
        
    st.markdown("---")
    st.subheader("Key Geotechnical Mechanisms Discovered in Experimental Research")
    
    mcol1, mcol2 = st.columns(2)
    with mcol1:
        st.markdown(r"""
        #### 1. Inverted Load-Sharing Kinetics
        - **CPR Behavior**: Piles take $80\text{--}90\%$ of the load at small strains ($w/B < 0.75\%$). Once pile capacity mobilizes, additional load shifts to the raft, dropping $\alpha_p$ to $\sim 20\%$.
        - **DPRF Behavior**: The raft bears $\mathbf{95\text{--}100\%}$ of load initially because the cushion layer compresses first. Pile load contribution mobilizes gradually with settlement, reaching $\mathbf{35\%}$ for a $3\times 3$ group at $w/B = 10\%$.
        """)
        fig2_path = os.path.join(current_dir, "outputs", "figures", "fig02_load_sharing_kinetics.png")
        if os.path.exists(fig2_path):
            st.image(fig2_path, caption="Figure 2: Inverted Load Sharing Kinetics between CPR and DPRF")
            
    with mcol2:
        st.markdown("""
        #### 2. Negative Skin Friction & Neutral Plane Depth
        - In DPRF, the cushion and shallow subsoil settle more than the pile head in the upper zone ($w_s > w_p$).
        - This induces **negative skin friction** down to a depth of $z_n \\approx 10d$ ($0.25\\text{ m}$).
        - **Critical Finding**: Maximum axial pile load does **not** occur at the pile head, but at the neutral plane ($z_n \\approx 0.25\\text{ m}$), reducing pile head stress by over $60\\%$.
        """)
        fig1_path = os.path.join(current_dir, "outputs", "figures", "fig01_load_settlement_comparison.png")
        if os.path.exists(fig1_path):
            st.image(fig1_path, caption="Figure 1: Experimental Load-Settlement Response of UR, CPR, and DPRF")

# -------------------------------------------------------------
# PAGE 2: DATASET & RESEARCH
# -------------------------------------------------------------
elif page == "2. Dataset & Research":
    st.markdown('<div class="main-header">Experimental Dataset & Research Traceability</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Meticulously Digitized from Published 1g Model Tests and Benchmark Literature</div>', unsafe_allow_html=True)
    
    if df_sources is not None:
        st.subheader("1. Published Research Paper Sources")
        st.dataframe(df_sources, use_container_width=True)
        
    st.markdown("---")
    st.subheader("2. Validated Experimental Observations")
    if df_cleaned is not None:
        st.write(f"Total digitized experimental records: **{len(df_cleaned)} rows** across 16 unique experimental configurations.")
        
        f1, f2, f3 = st.columns(3)
        with f1:
            f_type = st.multiselect("Filter by Foundation Type", options=df_cleaned["foundation_type"].unique(), default=df_cleaned["foundation_type"].unique())
        with f2:
            n_piles = st.multiselect("Filter by Number of Piles", options=df_cleaned["n_piles"].unique(), default=df_cleaned["n_piles"].unique())
        with f3:
            h_d = st.multiselect("Filter by Cushion Thickness (h/d)", options=df_cleaned["cushion_thickness_ratio"].unique(), default=df_cleaned["cushion_thickness_ratio"].unique())
            
        filtered_df = df_cleaned[
            (df_cleaned["foundation_type"].isin(f_type)) &
            (df_cleaned["n_piles"].isin(n_piles)) &
            (df_cleaned["cushion_thickness_ratio"].isin(h_d))
        ]
        
        st.dataframe(
            filtered_df[[
                "experiment_id", "foundation_type", "n_piles", "cushion_thickness_ratio", 
                "cushion_d50_mm", "applied_load_kn", "normalized_settlement_pct", 
                "pile_load_share_pct", "raft_load_share_pct", "settlement_efficiency_eta"
            ]],
            use_container_width=True
        )
        
    st.markdown("---")
    st.subheader("3. Exploratory Data Analysis & Correlations")
    ecol1, ecol2 = st.columns(2)
    with ecol1:
        fig5_path = os.path.join(current_dir, "outputs", "figures", "fig05_correlation_heatmap.png")
        if os.path.exists(fig5_path):
            st.image(fig5_path, caption="Figure 5: Pearson Correlation Heatmap")
    with ecol2:
        fig3_path = os.path.join(current_dir, "outputs", "figures", "fig03_cushion_thickness_effect.png")
        if os.path.exists(fig3_path):
            st.image(fig3_path, caption="Figure 3: Influence of Cushion Thickness (h/d) on Load Share and Efficiency")

# -------------------------------------------------------------
# PAGE 3: ML MODEL PERFORMANCE
# -------------------------------------------------------------
elif page == "3. ML Model Performance":
    st.markdown('<div class="main-header">Machine Learning Model Benchmarking & Performance</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Grouped Cross-Validation to Guarantee Generalization Across Independent Experiments</div>', unsafe_allow_html=True)
    
    if df_model_comp is not None:
        st.subheader("1. Comparative Benchmark Across Regression Algorithms")
        st.dataframe(df_model_comp, use_container_width=True)
        
    if model_meta is not None:
        st.markdown(f"""
        <div class="success-box">
            <b>Selected Optimal Model:</b> {model_meta['best_model_name']} <br>
            <b>Held-Out Test Set Metrics:</b> R² = <b>{model_meta['test_metrics']['R2']}</b> | 
            MAE = <b>{model_meta['test_metrics']['MAE']}%</b> | 
            RMSE = <b>{model_meta['test_metrics']['RMSE']}%</b>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("2. Model Evaluation & Residual Diagnostics")
    pcol1, pcol2 = st.columns(2)
    with pcol1:
        fig6_path = os.path.join(current_dir, "outputs", "figures", "fig06_actual_vs_predicted_parity.png")
        if os.path.exists(fig6_path):
            st.image(fig6_path, caption="Figure 6: Actual vs Predicted Parity Plot on Held-Out Test Experiments")
    with pcol2:
        fig7_path = os.path.join(current_dir, "outputs", "figures", "fig07_residual_analysis.png")
        if os.path.exists(fig7_path):
            st.image(fig7_path, caption="Figure 7: Residual Diagnostics (Homoscedasticity and Normality Check)")

    st.markdown("---")
    st.subheader("3. Explainable AI (XAI) & Feature Attributions")
    xcol1, xcol2 = st.columns(2)
    with xcol1:
        fig8_path = os.path.join(current_dir, "outputs", "figures", "fig08_feature_importance.png")
        if os.path.exists(fig8_path):
            st.image(fig8_path, caption="Figure 8: Feature Importance Ranking (Gini / Split Gain)")
    with xcol2:
        fig9_path = os.path.join(current_dir, "outputs", "figures", "fig09_shap_summary_beeswarm.png")
        if os.path.exists(fig9_path):
            st.image(fig9_path, caption="Figure 9: SHAP Beeswarm Summary Plot")

# -------------------------------------------------------------
# PAGE 4: LOAD-SHARING PREDICTION
# -------------------------------------------------------------
elif page == "4. Load-Sharing Prediction":
    st.markdown('<div class="main-header">Interactive Load-Sharing Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Input Foundation Geometry, Cushion, and Soil Properties for Physics-Constrained Prediction</div>', unsafe_allow_html=True)
    
    st.markdown("### Foundation and Soil Input Parameters")
    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("##### 🏛️ Foundation Geometry")
            n_piles = st.number_input("Number of Piles ($n_p$)", min_value=1, max_value=100, value=9, step=1)
            pile_d = st.number_input("Pile Diameter, $d$ (mm)", min_value=15.0, max_value=50.0, value=25.4, step=1.0)
            pile_L = st.number_input("Pile Length, $L$ (m)", min_value=0.3, max_value=2.0, value=1.0, step=0.1)
            pile_s = st.number_input("Spacing Ratio, $s/d$", min_value=2.0, max_value=6.0, value=3.0, step=0.5)
            raft_B = st.number_input("Raft Width, $B$ (mm)", min_value=150.0, max_value=500.0, value=300.0, step=25.0)
            raft_t = st.number_input("Raft Thickness, $t_r$ (mm)", min_value=10.0, max_value=50.0, value=25.0, step=5.0)
            
        with col2:
            st.markdown("##### 🪨 Granular Cushion Layer")
            hd_ratio = st.slider("Cushion Thickness Ratio ($h/d$)", min_value=0.5, max_value=4.0, value=2.0, step=0.5)
            d50_cushion = st.slider("Cushion Mean Grain Size, $d_{50}$ (mm)", min_value=0.5, max_value=5.0, value=2.0, step=0.5)
            phi_cushion = st.slider("Cushion Friction Angle, $\\phi_{cushion}$ (°)", min_value=40.0, max_value=60.0, value=51.0, step=1.0)
            gamma_cushion = st.number_input("Cushion Unit Weight, $\\gamma$ (kN/m³)", min_value=14.0, max_value=20.0, value=17.5, step=0.5)
            
        with col3:
            st.markdown("##### 🌍 Subsoil & Applied Loading")
            phi_soil = st.slider("Soil Friction Angle, $\\phi_{soil}$ (°)", min_value=35.0, max_value=45.0, value=40.7, step=0.5)
            dr_soil = st.slider("Soil Relative Density, $D_r$ (%)", min_value=50.0, max_value=90.0, value=70.0, step=5.0)
            applied_q = st.number_input("Applied Vertical Load, $Q$ (kN)", min_value=1.0, max_value=25.0, value=19.4, step=0.5)
            settlement_wb = st.slider("Normalized Settlement, $w/B$ (%)", min_value=0.5, max_value=10.0, value=10.0, step=0.5)
            settlement_mm = settlement_wb * (raft_B / 100.0)
            
        submit_btn = st.form_submit_button("⚡ Predict Load-Sharing Characteristics", use_container_width=True)

    if submit_btn and model_wrapper is not None:
        inp_dict = {
            "is_disconnected": 1,
            "n_piles": n_piles,
            "pile_diameter_mm": pile_d,
            "pile_length_m": pile_L,
            "pile_spacing_ratio": pile_s,
            "raft_width_mm": raft_B,
            "raft_thickness_mm": raft_t,
            "pile_area_ratio": (n_piles * np.pi * (pile_d ** 2) / 4.0) / (raft_B ** 2),
            "cushion_thickness_ratio": hd_ratio,
            "cushion_d50_mm": d50_cushion,
            "cushion_friction_deg": phi_cushion,
            "cushion_gamma_kn_m3": gamma_cushion,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": phi_soil,
            "soil_relative_density_pct": dr_soil,
            "soil_gamma_kn_m3": 15.9,
            "applied_load_kn": applied_q,
            "settlement_mm": settlement_mm,
            "normalized_settlement_pct": settlement_wb,
            "applied_pressure_kpa": applied_q / ((raft_B / 1000.0) ** 2)
        }
        
        res = model_wrapper.predict_single(inp_dict)
        
        if not res["domain_valid"]:
            st.markdown("""
            <div class="warning-box">
                <b>⚠️ Notice: Out of Calibrated Experimental Envelope</b><br>
                One or more parameters exceed the verified experimental dataset range. Predictions are extrapolated with physics constraints.
            </div>
            """, unsafe_allow_html=True)
            for w in res["domain_warnings"]:
                st.caption(f"- {w}")
                
        st.markdown("---")
        st.subheader("Prediction Results & Static Equilibrium")
        
        rcol1, rcol2, rcol3, rcol4 = st.columns(4)
        with rcol1:
            st.metric("Total Load (Q)", f"{res['applied_load_kn']:.2f} kN")
        with rcol2:
            st.metric("Pile Load Share (αp)", f"{res['pile_load_share_pct']:.1f}%")
        with rcol3:
            st.metric("Raft Load Share (αr)", f"{res['raft_load_share_pct']:.1f}%")
        with rcol4:
            st.metric("Equilibrium Status", "Verified (αp + αr = 100%) ✅")
            
        # Graphical Display
        gcol1, gcol2 = st.columns([1, 1])
        with gcol1:
            fig, ax = plt.subplots(figsize=(5, 5))
            labels = [f"Piles: {res['pile_load_share_pct']:.1f}%\n({res['pile_group_load_kn']:.2f} kN)", 
                      f"Raft: {res['raft_load_share_pct']:.1f}%\n({res['raft_load_kn']:.2f} kN)"]
            sizes = [res['pile_load_share_pct'], res['raft_load_share_pct']]
            colors = ["#2563EB", "#10B981"]
            ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors, 
                   wedgeprops=dict(width=0.45, edgecolor="w"))
            ax.set_title("Load Distribution Breakdown")
            st.pyplot(fig)
            
        with gcol2:
            st.markdown(f"""
            #### Engineering Interpretation:
            - **Load Transferred to Piles**: **{res['pile_group_load_kn']:.2f} kN** ($\\{res['pile_load_share_pct']:.1f}\\%$)
            - **Load Borne Directly by Raft**: **{res['raft_load_kn']:.2f} kN** ($\\{res['raft_load_share_pct']:.1f}\\%$)
            - **Average Load per Pile**: **{res['pile_group_load_kn'] / n_piles * 1000.0:.1f} N**
            - **Negative Skin Friction Consideration**: In DPRF with cushion thickness $h/d = {hd_ratio:.1f}$, maximum pile axial force occurs around depth $z \\approx 10d$ ($250\\text{ mm}$), rather than the pile head.
            """)

# -------------------------------------------------------------
# PAGE 5: PARAMETRIC ANALYSIS
# -------------------------------------------------------------
elif page == "5. Parametric Analysis":
    st.markdown('<div class="main-header">Interactive Parametric & Sensitivity Explorer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Investigate How Single Variable Variations Impact DPRF Load-Sharing Kinetics</div>', unsafe_allow_html=True)
    
    st.write("Examine the influence of key geotechnical design variables while holding other foundation and soil parameters constant at standard baseline values ($3\\times 3$ DPRF, Yamuna sand bed).")
    
    fig10_path = os.path.join(current_dir, "outputs", "figures", "fig10_parametric_study.png")
    if os.path.exists(fig10_path):
        st.image(fig10_path, caption="Figure 10: Multi-Parameter Sensitivity Analysis across (a) h/d, (b) d50, (c) w/B, and (d) Pile Count", use_container_width=True)
        
    st.markdown("---")
    st.subheader("Dynamic Interactive Parameter Sweep")
    sweep_param = st.selectbox(
        "Choose Parameter to Sweep:",
        ["Cushion Thickness Ratio (h/d)", "Cushion Particle Size (d50)", "Normalized Settlement (w/B)"]
    )
    
    if model_wrapper is not None:
        base_sweep = {
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
        
        if sweep_param == "Cushion Thickness Ratio (h/d)":
            x_vals = np.linspace(0.5, 4.0, 20)
            p_shares, r_shares = [], []
            for v in x_vals:
                d = base_sweep.copy()
                d["cushion_thickness_ratio"] = v
                r = model_wrapper.predict_single(d)
                p_shares.append(r["pile_load_share_pct"])
                r_shares.append(r["raft_load_share_pct"])
            xlabel = "Cushion Thickness Ratio ($h/d$)"
            
        elif sweep_param == "Cushion Particle Size (d50)":
            x_vals = np.linspace(0.5, 4.5, 20)
            p_shares, r_shares = [], []
            for v in x_vals:
                d = base_sweep.copy()
                d["cushion_d50_mm"] = v
                d["cushion_friction_deg"] = 46.0 + 2.2 * v
                r = model_wrapper.predict_single(d)
                p_shares.append(r["pile_load_share_pct"])
                r_shares.append(r["raft_load_share_pct"])
            xlabel = "Cushion Mean Grain Size, $d_{50}$ (mm)"
            
        else: # Settlement
            x_vals = np.linspace(0.5, 10.0, 20)
            p_shares, r_shares = [], []
            for v in x_vals:
                d = base_sweep.copy()
                d["normalized_settlement_pct"] = v
                d["settlement_mm"] = v * 3.0
                d["applied_load_kn"] = 19.4 * (v / 10.0) ** 0.65
                r = model_wrapper.predict_single(d)
                p_shares.append(r["pile_load_share_pct"])
                r_shares.append(r["raft_load_share_pct"])
            xlabel = "Normalized Settlement, $w/B$ (%)"

        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.plot(x_vals, p_shares, "b-o", linewidth=2.2, label="Pile Load Share $\\alpha_p$ (%)")
        ax.plot(x_vals, r_shares, "k--s", linewidth=2.2, label="Raft Load Share $\\alpha_r$ (%)")
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Load Share (%)")
        ax.set_title(f"Sensitivity Curve: Load Share vs. {sweep_param}")
        ax.legend()
        ax.grid(True, alpha=0.4)
        st.pyplot(fig)
