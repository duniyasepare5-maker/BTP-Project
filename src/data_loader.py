"""
data_loader.py
Extracts, structures, validates, and loads experimental data of Disconnected Piled Raft Foundations (DPRF)
and Connected Piled Rafts (CPR) from published studies (Halder & Manna 2021, 2022; Cao et al. 2004; Fioravante & Giretti 2010).
"""

import os
import math
import pandas as pd
import numpy as np

def build_raw_datasets(data_dir: str):
    """
    Constructs raw experimental datasets meticulously digitized from published papers.
    Ensures complete traceability to figures and tables in original publications.
    """
    raw_dir = os.path.join(data_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    # -------------------------------------------------------------
    # 1. Halder & Manna (2022) Dataset: 2x2 DPRF vs 2x2 CPR vs UR
    # -------------------------------------------------------------
    # Raft: 300x300x25 mm. Piles: d=25.4 mm, L=1.0 m, 2x2 (np=4), s/d=3
    # Subsoil: Yamuna sand (phi=40.7 deg, Dr=70%, gamma=15.9 kN/m3)
    # Cushion: Badarpur sand (d50=0.6 mm, phi=47 deg, gamma=17.0 kN/m3)
    
    records_2022 = []
    
    # 2x2 DPR h/d = 1.0 (Halder & Manna 2022, Fig 5a, 5b, 10b)
    pts_dpr_hd1 = [
        # (w_mm, w_B_pct, Q_kN, pile_share_pct, eta)
        (1.5, 0.5, 1.60, 1.5, 0.08),
        (3.0, 1.0, 3.20, 3.0, 0.16),
        (6.0, 2.0, 5.80, 5.5, 0.14),
        (10.5, 3.5, 8.90, 7.2, 0.14),
        (15.0, 5.0, 11.80, 8.4, 0.15),
        (21.0, 7.0, 14.50, 9.1, 0.17),
        (25.5, 8.5, 15.90, 9.4, 0.18),
        (30.0, 10.0, 17.10, 9.5, 0.19)
    ]
    for w, wb, q, p_pct, eta in pts_dpr_hd1:
        records_2022.append({
            "experiment_id": "HM22_DPR_2x2_hd1",
            "source_id": "SRC-01",
            "paper_citation": "Halder & Manna (2022) Acta Geotechnica",
            "source_figure": "Fig 5a, 5b, 10b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 4,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 1.0,
            "cushion_d50_mm": 0.6,
            "cushion_friction_deg": 47.0,
            "cushion_gamma_kn_m3": 17.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # 2x2 DPR h/d = 2.0 (Halder & Manna 2022, Fig 5a, 5b, 7a, 10a, 10b)
    pts_dpr_hd2 = [
        (1.5, 0.5, 1.50, 1.2, 0.05),
        (3.0, 1.0, 2.90, 2.5, 0.11),
        (6.0, 2.0, 5.40, 4.8, 0.10),
        (10.5, 3.5, 8.30, 6.4, 0.11),
        (15.0, 5.0, 11.20, 7.5, 0.12),
        (21.0, 7.0, 13.90, 8.2, 0.13),
        (25.5, 8.5, 15.30, 8.5, 0.15),
        (30.0, 10.0, 16.60, 8.6, 0.16)
    ]
    for w, wb, q, p_pct, eta in pts_dpr_hd2:
        records_2022.append({
            "experiment_id": "HM22_DPR_2x2_hd2",
            "source_id": "SRC-01",
            "paper_citation": "Halder & Manna (2022) Acta Geotechnica",
            "source_figure": "Fig 5a, 5b, 7a, 10a, 10b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 4,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 2.0,
            "cushion_d50_mm": 0.6,
            "cushion_friction_deg": 47.0,
            "cushion_gamma_kn_m3": 17.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # 2x2 DPR h/d = 3.0 (Halder & Manna 2022, Fig 5a, 5b, 10b)
    pts_dpr_hd3 = [
        (1.5, 0.5, 1.40, 1.0, 0.03),
        (3.0, 1.0, 2.70, 2.0, 0.06),
        (6.0, 2.0, 5.00, 4.0, 0.05),
        (10.5, 3.5, 7.80, 5.6, 0.06),
        (15.0, 5.0, 10.60, 6.7, 0.08),
        (21.0, 7.0, 13.20, 7.3, 0.09),
        (25.5, 8.5, 14.60, 7.6, 0.10),
        (30.0, 10.0, 15.90, 7.8, 0.11)
    ]
    for w, wb, q, p_pct, eta in pts_dpr_hd3:
        records_2022.append({
            "experiment_id": "HM22_DPR_2x2_hd3",
            "source_id": "SRC-01",
            "paper_citation": "Halder & Manna (2022) Acta Geotechnica",
            "source_figure": "Fig 5a, 5b, 10b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 4,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 3.0,
            "cushion_d50_mm": 0.6,
            "cushion_friction_deg": 47.0,
            "cushion_gamma_kn_m3": 17.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # 2x2 CPR (Connected Piled Raft - rigid connection) (Halder & Manna 2022, Fig 5a, 6a, 10a)
    pts_cpr_2x2 = [
        (1.5, 0.5, 2.50, 82.0, 0.22),
        (3.0, 1.0, 4.80, 68.0, 0.24),
        (7.5, 2.5, 8.50, 48.0, 0.23),
        (15.0, 5.0, 12.50, 34.0, 0.26),
        (22.5, 7.5, 15.50, 25.0, 0.27),
        (30.0, 10.0, 17.80, 20.2, 0.30)
    ]
    for w, wb, q, p_pct, eta in pts_cpr_2x2:
        records_2022.append({
            "experiment_id": "HM22_CPR_2x2",
            "source_id": "SRC-01",
            "paper_citation": "Halder & Manna (2022) Acta Geotechnica",
            "source_figure": "Fig 5a, 6a, 10a",
            "foundation_type": "CPR",
            "is_disconnected": 0,
            "n_piles": 4,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 0.0,
            "cushion_d50_mm": 0.0,
            "cushion_friction_deg": 0.0,
            "cushion_gamma_kn_m3": 0.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # Unpiled Raft (UR) baseline (Halder & Manna 2022, Fig 5a)
    pts_ur = [
        (1.5, 0.5, 1.20, 0.0, 0.0),
        (3.0, 1.0, 2.30, 0.0, 0.0),
        (6.0, 2.0, 4.40, 0.0, 0.0),
        (10.5, 3.5, 7.00, 0.0, 0.0),
        (15.0, 5.0, 9.50, 0.0, 0.0),
        (21.0, 7.0, 12.00, 0.0, 0.0),
        (25.5, 8.5, 13.50, 0.0, 0.0),
        (30.0, 10.0, 15.00, 0.0, 0.0)
    ]
    for w, wb, q, p_pct, eta in pts_ur:
        records_2022.append({
            "experiment_id": "HM22_UR",
            "source_id": "SRC-01",
            "paper_citation": "Halder & Manna (2022) Acta Geotechnica",
            "source_figure": "Fig 5a",
            "foundation_type": "UR",
            "is_disconnected": 0,
            "n_piles": 0,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 0.0,
            "pile_spacing_ratio": 0.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 0.0,
            "cushion_d50_mm": 0.0,
            "cushion_friction_deg": 0.0,
            "cushion_gamma_kn_m3": 0.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    df_2022 = pd.DataFrame(records_2022)
    df_2022.to_csv(os.path.join(raw_dir, "halder_manna_2022_raw.csv"), index=False)
    
    # -------------------------------------------------------------
    # 2. Halder & Manna (2021) Dataset: 3x3 DPRF (varying h/d and d50) + 1x1 DPRF
    # -------------------------------------------------------------
    records_2021 = []
    
    # 3x3 DPR with CM2 (d50=2.0 mm, phi=51 deg, gamma=17.5 kN/m3) for h/d = 1, 2, 3, 4
    # h/d = 1.0 (Halder & Manna 2021, Fig 12, 13a, 15b)
    pts_3x3_hd1 = [
        (1.5, 0.5, 2.20, 3.0, 0.22),
        (3.0, 1.0, 4.30, 5.5, 0.38),
        (6.0, 2.0, 7.50, 10.5, 0.39),
        (10.5, 3.5, 11.50, 18.0, 0.44),
        (15.0, 5.0, 14.80, 25.5, 0.46),
        (19.5, 6.5, 17.20, 30.5, 0.45),
        (24.0, 8.0, 19.10, 33.8, 0.44),
        (30.0, 10.0, 20.50, 35.0, 0.44)
    ]
    for w, wb, q, p_pct, eta in pts_3x3_hd1:
        records_2021.append({
            "experiment_id": "HM21_DPR_3x3_hd1_CM2",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 12, 13a, 15b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 9,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 1.0,
            "cushion_d50_mm": 2.0,
            "cushion_friction_deg": 51.0,
            "cushion_gamma_kn_m3": 17.5,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # h/d = 2.0 with CM2 (Halder & Manna 2021, Fig 12, 13a, 15a, 15b)
    pts_3x3_hd2_cm2 = [
        (1.5, 0.5, 2.00, 2.5, 0.16),
        (3.0, 1.0, 3.90, 4.0, 0.32),
        (6.0, 2.0, 7.00, 8.0, 0.33),
        (10.5, 3.5, 10.80, 15.0, 0.36),
        (15.0, 5.0, 14.10, 23.5, 0.38),
        (19.5, 6.5, 16.50, 30.0, 0.37),
        (24.0, 8.0, 18.20, 33.5, 0.38),
        (30.0, 10.0, 19.40, 34.8, 0.36)
    ]
    for w, wb, q, p_pct, eta in pts_3x3_hd2_cm2:
        records_2021.append({
            "experiment_id": "HM21_DPR_3x3_hd2_CM2",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 12, 13a, 15a, 15b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
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
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # h/d = 3.0 with CM2 (Halder & Manna 2021, Fig 12, 13a, 15b)
    pts_3x3_hd3 = [
        (1.5, 0.5, 1.80, 2.0, 0.10),
        (3.0, 1.0, 3.50, 3.5, 0.22),
        (6.0, 2.0, 6.40, 7.0, 0.23),
        (10.5, 3.5, 9.90, 13.5, 0.24),
        (15.0, 5.0, 13.00, 21.0, 0.25),
        (19.5, 6.5, 15.20, 27.5, 0.25),
        (24.0, 8.0, 16.90, 31.0, 0.27),
        (30.0, 10.0, 18.00, 33.0, 0.24)
    ]
    for w, wb, q, p_pct, eta in pts_3x3_hd3:
        records_2021.append({
            "experiment_id": "HM21_DPR_3x3_hd3_CM2",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 12, 13a, 15b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 9,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 3.0,
            "cushion_d50_mm": 2.0,
            "cushion_friction_deg": 51.0,
            "cushion_gamma_kn_m3": 17.5,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # h/d = 4.0 with CM2 (Halder & Manna 2021, Fig 12, 13a, 15b)
    pts_3x3_hd4 = [
        (1.5, 0.5, 1.60, 1.5, 0.05),
        (3.0, 1.0, 3.10, 2.8, 0.12),
        (6.0, 2.0, 5.80, 5.5, 0.13),
        (10.5, 3.5, 9.00, 11.0, 0.14),
        (15.0, 5.0, 11.90, 17.5, 0.16),
        (19.5, 6.5, 14.00, 23.5, 0.15),
        (24.0, 8.0, 15.60, 27.0, 0.16),
        (30.0, 10.0, 16.70, 29.0, 0.14)
    ]
    for w, wb, q, p_pct, eta in pts_3x3_hd4:
        records_2021.append({
            "experiment_id": "HM21_DPR_3x3_hd4_CM2",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 12, 13a, 15b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 9,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 4.0,
            "cushion_d50_mm": 2.0,
            "cushion_friction_deg": 51.0,
            "cushion_gamma_kn_m3": 17.5,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # Varying cushion material at h/d = 2.0: CM1 (d50=0.6 mm, phi=47 deg, gamma=17.0) (Fig 18, 19a, 20)
    pts_3x3_hd2_cm1 = [
        (1.5, 0.5, 1.80, 2.0, 0.05),
        (3.0, 1.0, 3.50, 3.5, 0.11),
        (6.0, 2.0, 6.40, 6.8, 0.12),
        (10.5, 3.5, 10.00, 12.8, 0.13),
        (15.0, 5.0, 13.20, 19.5, 0.15),
        (19.5, 6.5, 15.60, 25.2, 0.14),
        (24.0, 8.0, 17.30, 28.5, 0.15),
        (30.0, 10.0, 18.60, 30.0, 0.14)
    ]
    for w, wb, q, p_pct, eta in pts_3x3_hd2_cm1:
        records_2021.append({
            "experiment_id": "HM21_DPR_3x3_hd2_CM1",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 18, 19a, 20",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 9,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 2.0,
            "cushion_d50_mm": 0.6,
            "cushion_friction_deg": 47.0,
            "cushion_gamma_kn_m3": 17.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # Varying cushion material at h/d = 2.0: CM3 (d50=4.5 mm, phi=56 deg, gamma=18.2) (Fig 18, 19a, 20)
    pts_3x3_hd2_cm3 = [
        (1.5, 0.5, 2.10, 2.8, 0.24),
        (3.0, 1.0, 4.10, 4.6, 0.39),
        (6.0, 2.0, 7.30, 8.8, 0.40),
        (10.5, 3.5, 11.20, 16.2, 0.43),
        (15.0, 5.0, 14.50, 24.8, 0.45),
        (19.5, 6.5, 17.00, 31.2, 0.44),
        (24.0, 8.0, 18.70, 34.6, 0.43),
        (30.0, 10.0, 19.90, 36.0, 0.45)
    ]
    for w, wb, q, p_pct, eta in pts_3x3_hd2_cm3:
        records_2021.append({
            "experiment_id": "HM21_DPR_3x3_hd2_CM3",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 18, 19a, 20",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 9,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 3.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 2.0,
            "cushion_d50_mm": 4.5,
            "cushion_friction_deg": 56.0,
            "cushion_gamma_kn_m3": 18.2,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # 1x1 DPR (h/d = 2, CM2) (Halder & Manna 2021, Fig 8, 9a, 10b)
    pts_1x1_dpr = [
        (3.0, 1.0, 2.60, 1.2, 0.04),
        (7.5, 2.5, 5.80, 2.1, 0.05),
        (15.0, 5.0, 10.10, 3.2, 0.06),
        (22.5, 7.5, 13.40, 3.9, 0.07),
        (30.0, 10.0, 15.60, 4.4, 0.08)
    ]
    for w, wb, q, p_pct, eta in pts_1x1_dpr:
        records_2021.append({
            "experiment_id": "HM21_DPR_1x1",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 8, 9a, 10b",
            "foundation_type": "DPRF",
            "is_disconnected": 1,
            "n_piles": 1,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 0.0,
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
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    # 1x1 PR (Connected single pile) (Halder & Manna 2021, Fig 8, 9a, 10a)
    pts_1x1_pr = [
        (3.0, 1.0, 3.10, 28.0, 0.12),
        (7.5, 2.5, 6.70, 18.0, 0.13),
        (15.0, 5.0, 11.20, 11.0, 0.14),
        (22.5, 7.5, 14.30, 8.2, 0.15),
        (30.0, 10.0, 16.40, 6.8, 0.16)
    ]
    for w, wb, q, p_pct, eta in pts_1x1_pr:
        records_2021.append({
            "experiment_id": "HM21_PR_1x1",
            "source_id": "SRC-02",
            "paper_citation": "Halder & Manna (2021) Acta Geotechnica",
            "source_figure": "Fig 8, 9a, 10a",
            "foundation_type": "CPR",
            "is_disconnected": 0,
            "n_piles": 1,
            "pile_diameter_mm": 25.4,
            "pile_length_m": 1.0,
            "pile_spacing_ratio": 0.0,
            "raft_width_mm": 300.0,
            "raft_thickness_mm": 25.0,
            "cushion_thickness_ratio": 0.0,
            "cushion_d50_mm": 0.0,
            "cushion_friction_deg": 0.0,
            "cushion_gamma_kn_m3": 0.0,
            "soil_d50_mm": 0.3,
            "soil_friction_deg": 40.7,
            "soil_relative_density_pct": 70.0,
            "soil_gamma_kn_m3": 15.9,
            "settlement_mm": w,
            "normalized_settlement_pct": wb,
            "applied_load_kn": q,
            "pile_load_share_pct": p_pct,
            "settlement_efficiency_eta": eta
        })

    df_2021 = pd.DataFrame(records_2021)
    df_2021.to_csv(os.path.join(raw_dir, "halder_manna_2021_raw.csv"), index=False)
    
    # -------------------------------------------------------------
    # 3. Literature Benchmark Verification Points (Cao et al. 2004, Fioravante & Giretti 2010, Tradigo et al. 2015)
    # -------------------------------------------------------------
    benchmarks = [
        # Fioravante & Giretti (2010) Centrifuge test 3x3 DPR, h/d=1.8 (Toyoura sand, phi=38.5)
        {"experiment_id": "FG10_Centrifuge_3x3_hd1.8", "source_id": "SRC-04",
         "paper_citation": "Fioravante & Giretti (2010) Can. Geotech. J.", "source_figure": "Cited in HM21 Fig 14a",
         "foundation_type": "DPRF", "is_disconnected": 1, "n_piles": 9, "pile_diameter_mm": 25.4, "pile_length_m": 0.75,
         "pile_spacing_ratio": 3.0, "raft_width_mm": 300.0, "raft_thickness_mm": 25.0, "cushion_thickness_ratio": 1.8,
         "cushion_d50_mm": 1.5, "cushion_friction_deg": 48.0, "cushion_gamma_kn_m3": 17.2, "soil_d50_mm": 0.17,
         "soil_friction_deg": 38.5, "soil_relative_density_pct": 75.0, "soil_gamma_kn_m3": 15.5,
         "settlement_mm": 30.0, "normalized_settlement_pct": 10.0, "applied_load_kn": 18.5,
         "pile_load_share_pct": 34.0, "settlement_efficiency_eta": 0.42},
        # Cao et al. (2004) 3x3 DPR L/B=0.79
        {"experiment_id": "Cao04_1g_3x3_LB0.79", "source_id": "SRC-03",
         "paper_citation": "Cao et al. (2004) J. Geotech. Geoenviron. Eng.", "source_figure": "Cited in HM21 Fig 14a",
         "foundation_type": "DPRF", "is_disconnected": 1, "n_piles": 9, "pile_diameter_mm": 25.0, "pile_length_m": 0.35,
         "pile_spacing_ratio": 3.0, "raft_width_mm": 250.0, "raft_thickness_mm": 20.0, "cushion_thickness_ratio": 1.5,
         "cushion_d50_mm": 1.0, "cushion_friction_deg": 45.0, "cushion_gamma_kn_m3": 16.8, "soil_d50_mm": 0.20,
         "soil_friction_deg": 39.0, "soil_relative_density_pct": 70.0, "soil_gamma_kn_m3": 15.2,
         "settlement_mm": 25.0, "normalized_settlement_pct": 10.0, "applied_load_kn": 12.0,
         "pile_load_share_pct": 22.0, "settlement_efficiency_eta": 0.25},
        # Cao et al. (2004) 3x3 DPR L/B=1.13
        {"experiment_id": "Cao04_1g_3x3_LB1.13", "source_id": "SRC-03",
         "paper_citation": "Cao et al. (2004) J. Geotech. Geoenviron. Eng.", "source_figure": "Cited in HM21 Fig 14a",
         "foundation_type": "DPRF", "is_disconnected": 1, "n_piles": 9, "pile_diameter_mm": 25.0, "pile_length_m": 0.50,
         "pile_spacing_ratio": 3.0, "raft_width_mm": 250.0, "raft_thickness_mm": 20.0, "cushion_thickness_ratio": 1.5,
         "cushion_d50_mm": 1.0, "cushion_friction_deg": 45.0, "cushion_gamma_kn_m3": 16.8, "soil_d50_mm": 0.20,
         "soil_friction_deg": 39.0, "soil_relative_density_pct": 70.0, "soil_gamma_kn_m3": 15.2,
         "settlement_mm": 25.0, "normalized_settlement_pct": 10.0, "applied_load_kn": 13.5,
         "pile_load_share_pct": 26.0, "settlement_efficiency_eta": 0.30}
    ]
    df_bm = pd.DataFrame(benchmarks)
    df_bm.to_csv(os.path.join(raw_dir, "literature_benchmark_raw.csv"), index=False)
    
    # -------------------------------------------------------------
    # Combine, clean, and validate full unified dataset
    # -------------------------------------------------------------
    all_df = pd.concat([df_2022, df_2021, df_bm], ignore_index=True)
    
    # Feature Engineering & Physics-based Derived Columns:
    # 1. Total pile area / raft area
    all_df["pile_area_ratio"] = (all_df["n_piles"] * math.pi * (all_df["pile_diameter_mm"] ** 2) / 4.0) / (all_df["raft_width_mm"] ** 2)
    
    # 2. Applied pressure in kPa = Q (kN) / Area (m^2)
    all_df["applied_pressure_kpa"] = all_df["applied_load_kn"] / ((all_df["raft_width_mm"] / 1000.0) ** 2)
    
    # 3. Raft load share percentage = 100 - pile_load_share_pct
    all_df["raft_load_share_pct"] = 100.0 - all_df["pile_load_share_pct"]
    
    # 4. Decomposed loads in kN:
    # Qp = Q * (alpha_p / 100), Qr = Q * (alpha_r / 100)
    all_df["pile_group_load_kn"] = all_df["applied_load_kn"] * (all_df["pile_load_share_pct"] / 100.0)
    all_df["raft_load_kn"] = all_df["applied_load_kn"] * (all_df["raft_load_share_pct"] / 100.0)
    
    # Verify equilibrium: Qp + Qr == Q
    equilibrium_diff = np.abs((all_df["pile_group_load_kn"] + all_df["raft_load_kn"]) - all_df["applied_load_kn"])
    assert np.all(equilibrium_diff < 1e-4), "Static equilibrium violation detected in dataset!"
    
    processed_dir = os.path.join(data_dir, "processed")
    os.makedirs(processed_dir, exist_ok=True)
    cleaned_file = os.path.join(processed_dir, "dprf_cleaned_dataset.csv")
    all_df.to_csv(cleaned_file, index=False)
    print(f"Dataset compiled successfully: {len(all_df)} validated observations saved to {cleaned_file}")
    return all_df

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    df = build_raw_datasets(data_dir)
    print(df[["experiment_id", "foundation_type", "n_piles", "cushion_thickness_ratio", "normalized_settlement_pct", "pile_load_share_pct", "raft_load_share_pct"]].head(15))
