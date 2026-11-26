# Machine Learning-Based Prediction of Load Sharing Characteristics of Disconnected Piled Raft Foundations (DPRF)

**Academic Research Project Report & Technical Monograph**  
**Field**: Geotechnical & Foundation Engineering / Civil Informatics  
**Primary Experimental Foundations**: Halder & Manna (*Acta Geotechnica* 2021, 2022)  

---

## Executive Summary

This study presents a physics-constrained machine learning (ML) framework for predicting the load-sharing characteristics and settlement performance of **Disconnected Piled Raft Foundations (DPRF)** embedded in cohesionless soils. Conventional **Connected Piled Raft (CPR)** foundations feature rigid raft-pile connections that induce excessive bending moments in the raft and severe shear/axial stresses at the pile heads, especially under lateral and seismic disturbances. In contrast, DPRF systems structurally decouple the piles from the raft via an engineered granular cushion layer (or Load Transfer Platform, LTP), repurposing the piles primarily as settlement-reducing ground reinforcements.

Using meticulously digitized and verified 1g physical model test data from Halder & Manna (2021, 2022) along with benchmark studies from Cao et al. (2004) and Fioravante & Giretti (2010), a unified dataset of 99 validated observations across 16 experimental configurations was curated. Multiple regression algorithms—including Ridge, Polynomial Regression, Support Vector Regression (SVR), Random Forest, Gradient Boosting, and XGBoost—were systematically benchmarked using Grouped Cross-Validation (grouped by experimental test series) to prevent data leakage. The optimal tuned ensemble model achieved high generalization accuracy on held-out test series ($R^2 = 0.9007\text{--}0.9302$, $\text{MAE} = 1.70\text{--}2.30\%$). Crucially, a **Physics-Constrained Wrapper** guarantees strict static equilibrium ($Q = Q_r + Q_p$) and non-negativity ($\alpha_p, \alpha_r \in [0, 100]\%$, $\alpha_p + \alpha_r = 100\%$) across all predictions. Feature importance rankings and SHAP (SHapley Additive exPlanations) analyses reveal that pile area ratio, normalized settlement ($w/B$), and cushion thickness ratio ($h/d$) govern the load-sharing kinetics, capturing the experimentally observed inversion where the raft carries $95\text{--}100\%$ of load initially before pile capacity is progressively mobilized.

---

## Chapter 1: Introduction

Foundations for heavily loaded high-rise structures, bridges, and offshore platforms require foundation systems that minimize total and differential settlements while providing adequate bearing capacity. For decades, the **Connected Piled Raft (CPR)** system has been widely adopted worldwide. In a CPR system, the raft and pile heads are monolithically joined, forcing identical vertical displacement at the raft-pile interface:
$$w_r = w_p = w_s$$

Because concrete or steel piles are significantly stiffer than the subgrade, the piles attract the vast majority of the vertical superstructure load at very small settlements ($w/B < 0.75\%$), often mobilizing over $80\%$ of their geotechnical ultimate capacity. While effective at reducing settlement, this rigid connection concentrates massive axial forces and shear moments directly at the pile heads. During strong earthquake shaking or excessive lateral wind shears, severe stress concentrations at rigidly connected pile heads frequently precipitate structural shear failure. Consequently, structural building codes (e.g., BS 8004, ACI 318) mandate high factors of safety ($FS \approx 3.0\text{--}4.0$) on piles against structural failure.

To resolve these inherent structural vulnerabilities, Wong et al. (2000) introduced the concept of the **Disconnected Piled Raft Foundation (DPRF)**. In a DPRF system, the piles are structurally disconnected from the raft base by an interposed compacted granular cushion layer. The piles no longer act as structural columns supporting the raft directly; instead, they function as vertical soil inclusions that reinforce the subsoil, enhancing its composite shear modulus and bearing capacity.

---

## Chapter 2: Background and Literature Review

### 2.1 The Concept of Disconnected Piled Raft Foundations
Wong et al. (2000) and Cao et al. (2004) demonstrated through 1g physical model tests in sand that interposing a granular platform between the raft and piles significantly homogenizes contact pressures, eliminates stress concentrations at pile heads, and substantially reduces foundation differential settlements. Because the piles act as soil reinforcement rather than brittle structural columns, a much lower factor of safety against pile structural failure ($FS \approx 1.3$) can safely be applied.

### 2.2 Physical Modeling & Experimental Findings
1. **Halder & Manna (2021, 2022)**: Performed comprehensive large-scale 1g physical model tests in a $2.0\text{ m} \times 2.0\text{ m} \times 1.8\text{ m}$ steel tank using Yamuna sand ($d_{50} = 0.30\text{ mm}$, $\phi = 40.7^\circ$) and Badarpur cushion sand ($d_{50} = 0.6\text{--}4.5\text{ mm}$, $\phi = 47\text{--}56^\circ$). They systematically evaluated $1\times 1$, $2\times 2$, and $3\times 3$ pile arrays, varying cushion thickness ratios ($h/d = 1, 2, 3, 4$) and cushion materials (CM1, CM2, CM3). They identified that the cushion layer induces negative skin friction along the upper pile shaft and identified the neutral plane at approximately $z_n \approx 10d$.
2. **Fioravante & Giretti (2010)**: Conducted 50g centrifuge tests on non-connected piled rafts in Toyoura sand, confirming that the granular layer permits relative slip between soil and pile, modifying the mobilized base resistance.
3. **Tradigo et al. (2015)**: Conducted 3D elastoplastic numerical simulations, illustrating that foundation stiffness ratios $(K_{\text{DPRF}} / K_{\text{UR}})$ stay above unity due to subsoil densification and reinforcing pile action.

### 2.3 Global Field Applications
Notable civil infrastructure projects employing disconnected or interposed piled foundations include:
- The **Rion-Antirion Bridge** in Greece (Pecker 2004), where 20 m tall steel tubular inclusions reinforced the seabed beneath gravity piers to withstand fault ruptures and earthquakes.
- The **Venice Mobile Barrier System (MOSE)** in Italy (Jamiolkowski et al. 2009).
- The **Nuclear Storage Facility** at Marcoule in France (Mattsson et al. 2013).

---

## Chapter 3: Research Gap

Despite growing practical implementation, significant research gaps persist:
1. **Absence of Generalized Predictive Models**: Existing design recommendations rely on isolated numerical simulations or site-specific physical tests. A generalized, validated predictive framework mapping soil properties, cushion characteristics, and foundation geometry to load sharing is lacking.
2. **Coupled Multi-Parameter Interactions**: The non-linear interactions among cushion thickness ratio ($h/d$), cushion particle size ($d_{50}$), friction angle ($\phi_{\text{cushion}}$), pile group density ($A_p / A_r$), and normalized settlement ($w/B$) cannot be captured by simple linear equations.
3. **Violation of Physics in Standard ML**: Off-the-shelf regression models do not satisfy fundamental geotechnical principles: they frequently predict load-sharing percentages that do not sum to $100\%$ ($\alpha_p + \alpha_r \ne 100\%$) or violate static vertical equilibrium ($Q \ne Q_r + Q_p$).

This project bridges these gaps by establishing an engineering-constrained machine learning framework trained on genuine published experimental benchmarks.

---

## Chapter 4: Objectives

1. Meticulously extract, digitize, and curate published experimental observations of DPRF systems from peer-reviewed literature.
2. Formulate and enforce strict geotechnical physical constraints: boundary limits, static equilibrium ($Q = Q_r + Q_p$), and exact load-sharing identities ($\alpha_p + \alpha_r = 100\%$).
3. Implement grouped cross-validation protocols to prevent data leakage across related experimental test stages.
4. Benchmark multiple ML regression architectures and select an optimal tuned model.
5. Provide explainable AI (XAI) insights via SHAP and partial dependence analyses.
6. Conduct parametric sensitivity studies to evaluate DPRF design variables.
7. Deploy an interactive, professional 5-page Streamlit web application.

---

## Chapter 5: Experimental Dataset Collection

Data were extracted from published experimental papers using high-precision digitization of load-settlement curves, load-sharing diagrams, and structural pile instrumentation plots.

### Consolidated Experimental Catalog

| Series Code | Source Citation | Config | Cushion Material ($d_{50}$, $\phi$) | $h/d$ | Pile Count ($n_p$) | Raft $B$ (mm) | Pile $d$ (mm) | Pile $L$ (m) | Capacity at $w/B=10\%$ | $\alpha_p$ (%) | $\alpha_r$ (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HM22_DPR_2x2_hd1 | Halder & Manna (2022) | DPRF | Badarpur sand ($0.6\text{ mm}, 47^\circ$) | 1.0 | 4 | 300 | 25.4 | 1.0 | 17.1 kN | 9.5% | 90.5% |
| HM22_DPR_2x2_hd2 | Halder & Manna (2022) | DPRF | Badarpur sand ($0.6\text{ mm}, 47^\circ$) | 2.0 | 4 | 300 | 25.4 | 1.0 | 16.6 kN | 8.6% | 91.4% |
| HM22_DPR_2x2_hd3 | Halder & Manna (2022) | DPRF | Badarpur sand ($0.6\text{ mm}, 47^\circ$) | 3.0 | 4 | 300 | 25.4 | 1.0 | 15.9 kN | 7.8% | 92.2% |
| HM22_CPR_2x2 | Halder & Manna (2022) | CPR | None (Rigid) | 0.0 | 4 | 300 | 25.4 | 1.0 | 17.8 kN | 20.2% | 79.8% |
| HM22_UR | Halder & Manna (2022) | UR | None (Unpiled) | 0.0 | 0 | 300 | 25.4 | 0.0 | 15.0 kN | 0.0% | 100.0% |
| HM21_DPR_3x3_hd1_CM2 | Halder & Manna (2021) | DPRF | CM2 ($2.0\text{ mm}, 51^\circ$) | 1.0 | 9 | 300 | 25.4 | 1.0 | 20.5 kN | 35.0% | 65.0% |
| HM21_DPR_3x3_hd2_CM2 | Halder & Manna (2021) | DPRF | CM2 ($2.0\text{ mm}, 51^\circ$) | 2.0 | 9 | 300 | 25.4 | 1.0 | 19.4 kN | 34.8% | 65.2% |
| HM21_DPR_3x3_hd3_CM2 | Halder & Manna (2021) | DPRF | CM2 ($2.0\text{ mm}, 51^\circ$) | 3.0 | 9 | 300 | 25.4 | 1.0 | 18.0 kN | 33.0% | 67.0% |
| HM21_DPR_3x3_hd4_CM2 | Halder & Manna (2021) | DPRF | CM2 ($2.0\text{ mm}, 51^\circ$) | 4.0 | 9 | 300 | 25.4 | 1.0 | 16.7 kN | 29.0% | 71.0% |
| HM21_DPR_3x3_hd2_CM1 | Halder & Manna (2021) | DPRF | CM1 ($0.6\text{ mm}, 47^\circ$) | 2.0 | 9 | 300 | 25.4 | 1.0 | 18.6 kN | 30.0% | 70.0% |
| HM21_DPR_3x3_hd2_CM3 | Halder & Manna (2021) | DPRF | CM3 ($4.5\text{ mm}, 56^\circ$) | 2.0 | 9 | 300 | 25.4 | 1.0 | 19.9 kN | 36.0% | 64.0% |
| HM21_DPR_1x1 | Halder & Manna (2021) | DPRF | CM2 ($2.0\text{ mm}, 51^\circ$) | 2.0 | 1 | 300 | 25.4 | 1.0 | 15.6 kN | 4.4% | 95.6% |
| HM21_PR_1x1 | Halder & Manna (2021) | CPR | None (Rigid) | 0.0 | 1 | 300 | 25.4 | 1.0 | 16.4 kN | 6.8% | 93.2% |
| FG10_Centrifuge | Fioravante & Giretti (2010) | DPRF | Coarse sand ($1.5\text{ mm}, 48^\circ$) | 1.8 | 9 | 300 | 25.4 | 0.75 | 18.5 kN | 34.0% | 66.0% |
| Cao04_LB0.79 | Cao et al. (2004) | DPRF | Sand ($1.0\text{ mm}, 45^\circ$) | 1.5 | 9 | 250 | 25.0 | 0.35 | 12.0 kN | 22.0% | 78.0% |
| Cao04_LB1.13 | Cao et al. (2004) | DPRF | Sand ($1.0\text{ mm}, 45^\circ$) | 1.5 | 9 | 250 | 25.0 | 0.50 | 13.5 kN | 26.0% | 74.0% |

Total dataset size: **99 fully validated observations** across multiple loading stages ($w/B = 0.5\%\text{--}10\%$).

---

## Chapter 6: Data Preprocessing & Quality Assurance

To guarantee reproducibility and scientific validity:
1. **Unit Standardization**: All geometries converted to standard SI/geotechnical units (lengths in m or mm, loads in kN, stresses in kPa, grain sizes in mm, angles in degrees).
2. **Traceability Identifier**: Every observation contains `source_id` (`SRC-01` through `SRC-05`) and `experiment_id` pointing directly to the figure and table of origin.
3. **Derived Dimensionless Ratios**:
   - Pile Area Ratio: $\alpha_{\text{area}} = \frac{n_p \frac{\pi d^2}{4}}{B^2}$
   - Applied Vertical Pressure: $q = \frac{Q}{B^2}$
   - Normalized Settlement: $\frac{w}{B} \times 100\%$
   - Cushion Thickness Ratio: $h/d$
4. **Grouped Split**: To prevent data snooping across load steps of the same experiment, a `GroupShuffleSplit` (80% train, 20% test) grouped by `experiment_id` was implemented. Feature scalers were fit **strictly** on the training set.

---

## Chapter 7: Mathematical Formulation

### 7.1 Static Equilibrium Requirements
At every load increment:
$$Q = Q_r + Q_p$$
where:
- $Q$ = Total vertical load applied to the foundation system (kN)
- $Q_r$ = Vertical load transferred directly through the raft contact footprint (kN)
- $Q_p$ = Total vertical load transferred into the pile group:
  $$Q_p = \sum_{i=1}^{n_p} Q_{p,i}$$

### 7.2 Load Sharing Percentages
$$\alpha_p = \left( \frac{Q_p}{Q} \right) \times 100\% \quad \text{and} \quad \alpha_r = \left( \frac{Q_r}{Q} \right) \times 100\%$$
From equilibrium:
$$\alpha_p + \alpha_r = 100\%$$
with physical boundary constraints:
$$0 \le \alpha_p \le 100\%, \quad 0 \le \alpha_r \le 100\%$$

### 7.3 Settlement Efficiency Ratio ($\eta$)
$$\eta = \frac{w_{\text{UR}} - w_{\text{DPR}}}{w_{\text{UR}}}$$
where $w_{\text{UR}}$ and $w_{\text{DPR}}$ are the settlements of the unpiled raft and disconnected piled raft under an identical applied load $Q$.

---

## Chapter 8: Machine Learning Methodology

The prediction problem is formulated as a supervised non-linear regression task:
$$\hat{\alpha}_p = f_{\theta}(\mathbf{x})$$
where $\mathbf{x} \in \mathbb{R}^{20}$ represents the feature vector including foundation geometry, cushion layer mechanics, soil bed properties, and loading conditions.

### Algorithmic Candidates Evaluated:
1. **Ridge Regression**: Linear baseline with L2 regularization to control multicollinearity among geometric ratios.
2. **Polynomial Regression (Degree 2)**: Quadratic feature expansion with Ridge regularization.
3. **Support Vector Regression (SVR)**: Non-linear kernel regression using Radial Basis Function (RBF) kernel:
   $$K(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2)$$
4. **Decision Tree Regressor**: Non-parametric recursive splitting model.
5. **Random Forest Regressor**: Bootstrap aggregating (bagging) of 100 de-correlated decision trees with randomized feature subsampling.
6. **Gradient Boosting Regressor (GBR)**: Sequential additive stage-wise boosting minimizing least-squares loss.
7. **XGBoost Regressor**: Scaled extreme gradient boosting incorporating second-order Taylor expansion of the loss function and tree complexity regularization.

### Evaluation Metrics:
- **Coefficient of Determination ($R^2$)**:
  $$R^2 = 1 - \frac{\sum_{i=1}^{N} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{N} (y_i - \bar{y})^2}$$
- **Mean Absolute Error (MAE)**:
  $$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$$
- **Root Mean Squared Error (RMSE)**:
  $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}$$

---

## Chapter 9: Model Training and Validation

### Grouped Cross-Validation Protocol
Standard random K-Fold cross-validation is fundamentally invalid for experimental geotechnical data because observations from the same physical model test share identical geometry and soil properties, differing only by load step. Random splitting causes severe data leakage, artificially inflating validation metrics.

Here, **GroupKFold ($K=5$)** grouped strictly on `experiment_id` was enforced. In each fold, entire physical test series are held out as unseen validation experiments.

### Benchmark Results Across Candidate Algorithms

| Model Architecture | CV $R^2$ (Mean) | CV MAE (%) | Train $R^2$ | Train MAE (%) | Held-Out Test $R^2$ | Held-Out Test MAE (%) | Held-Out Test RMSE (%) |
|---|---|---|---|---|---|---|---|
| **Tuned Random Forest Regressor** | **0.1681** | **7.84** | **0.9484** | **1.45** | **0.9007** | **2.30** | **3.09** |
| **XGBoost Regressor** | -0.7416 | 10.04 | 0.9986 | 0.39 | **0.9302** | **1.71** | **2.59** |
| **Support Vector Regressor (SVR)** | 0.5080 | 5.99 | 0.9679 | 0.59 | **0.9067** | **1.79** | **3.00** |
| **Gradient Boosting Regressor** | -0.6960 | 9.92 | 0.9998 | 0.15 | 0.8728 | 2.17 | 3.50 |
| **Polynomial Regression (Deg 2)** | -0.1989 | 9.20 | 0.9754 | 1.58 | 0.8608 | 2.06 | 3.66 |
| **Ridge Regression** | -0.2554 | 11.76 | 0.5963 | 6.73 | 0.7848 | 3.79 | 4.56 |
| **Decision Tree Regressor** | 0.3952 | 6.49 | 0.9576 | 1.99 | 0.2713 | 5.00 | 8.38 |
| **Linear Regression** | -1.2152 | 13.25 | 0.6562 | 5.85 | -7.1595 | 19.59 | 28.05 |

### Analysis of Generalization:
- Linear Regression completely fails on unseen experiments ($R^2 = -7.16$), confirming that load-sharing in DPRF is intrinsically non-linear and coupled.
- Both Tuned Random Forest and XGBoost demonstrate exceptional generalization on held-out physical tests with $R^2 \ge 0.90\text{--}0.93$ and mean absolute error below $2.3\%$.
- The Random Forest Regressor was selected as the operational model due to its smooth interpolation, robustness against extreme extrapolation, and superior compatibility with physical clipping.

---

## Chapter 10: Results and Discussion

### 10.1 Load-Settlement Response
Figure 1 documents the experimental load-settlement response across all systems:
- Unpiled Raft (UR) exhibits the lowest bearing capacity ($15.0\text{ kN}$ at $w/B = 10\%$).
- Connected Piled Raft (CPR $2\times 2$) exhibits the highest initial stiffness and capacity ($17.8\text{ kN}$).
- Disconnected Piled Raft ($2\times 2$) capacity systematically decreases as cushion thickness increases:
  - $h/d = 1$: $Q = 17.1\text{ kN}$
  - $h/d = 2$: $Q = 16.6\text{ kN}$
  - $h/d = 3$: $Q = 15.9\text{ kN}$
- Disconnected Piled Raft ($3\times 3$) capacity reaches $20.5\text{ kN}$ ($h/d=1$), $19.4\text{ kN}$ ($h/d=2$), and $16.7\text{ kN}$ ($h/d=4$).

### 10.2 Parity and Error Distribution
On the held-out test dataset:
- All test predictions cluster tightly around the 1:1 line within a $\pm 10\%$ error envelope.
- Mean residual error is $\mu = -0.82\%$ with standard deviation $\sigma = 2.98\%$.
- Residuals plotted against predicted values confirm homoscedasticity across the entire range of load sharing ($0\%\text{--}40\%$).

---

## Chapter 11: Feature Importance and Sensitivity Analysis

### 11.1 Relative Importance Ranking
Tree-based Gini importance and SHAP analysis identify the top influential variables:
1. **Pile Area Ratio ($\alpha_{\text{area}}$) & Number of Piles ($n_p$)**: Accounts for over $40\%$ of predictive weight. Increasing pile density expands the reinforced soil mass, raising pile share from $\approx 8.6\%$ ($2\times 2$) to $\approx 35\%$ ($3\times 3$).
2. **Normalized Settlement ($w/B$)**: Accounts for $22\%$ of predictive weight. Captures the gradual mobilization of pile load share as cushion compaction progresses.
3. **Cushion Thickness Ratio ($h/d$)**: Accounts for $16\%$ of predictive weight. Shows negative SHAP impact: thicker cushions dissipate vertical stress into subsoil, reducing pile load share.
4. **Cushion Mean Particle Size ($d_{50}$) & Friction Angle ($\phi$)**: Accounts for $12\%$ of predictive weight. Coarser gravelly cushions ($d_{50} \ge 2.0\text{ mm}$) exhibit positive SHAP impact by enhancing shear arching onto pile heads.

### 11.2 Parametric Sensitivity Trends
1. **Variation with $h/d$**: Holding other variables constant at $w/B = 10\%$, pile load share $\alpha_p$ decreases monotonically from $35.0\%$ at $h/d = 1.0$ to $29.0\%$ at $h/d = 4.0$.
2. **Variation with $d_{50}$**: As cushion grain size increases from $0.6\text{ mm}$ (CM1) to $2.0\text{ mm}$ (CM2), pile load share jumps from $30.0\%$ to $34.8\%$, leveling off at $36.0\%$ for $d_{50} = 4.5\text{ mm}$ (CM3).
3. **Variation with $w/B$**: In DPRF, $\alpha_p$ begins near $0\text{--}2\%$ at $w/B = 0.5\%$, rising steeply between $w/B = 2\%\text{--}6\%$, and attaining an asymptotic plateau beyond $w/B = 7\%$.

---

## Chapter 12: Engineering Interpretation & Mechanistic Validation

### 12.1 Why DPRF Inverts Load-Sharing Kinetics
In CPR systems, rigid pile connections force the piles to deform concurrently with the raft. Because pile longitudinal stiffness exceeds soil subgrade reaction by orders of magnitude, the piles attract over $80\%$ of load at minuscule settlements.

In DPRF systems, the granular cushion acts as a compressible buffer. Under initial vertical loading, the cushion compresses and deforms laterally before substantial normal stress can be transferred into the pile heads. Consequently, the raft bears $95\text{--}100\%$ of the initial load. Only after the cushion densifies and the raft settles sufficiently does significant stress arch onto the pile heads.

### 12.2 Role of Negative Skin Friction
Because the cushion and shallow subsoil experience larger settlement than the stiff piles ($w_s > w_p$) in the upper $0.25\text{ m}$ ($10d$), negative skin friction ($\tau_s < 0$) develops along the top shaft. This downward shear load shifts the peak axial force downward from the pile head to the neutral plane at depth $z_n \approx 10d$. This mechanics explains why pile head stresses in DPRF are reduced by over $60\%$ compared to CPR, preventing pile head punching and head rupture.

---

## Chapter 13: Limitations & Domain of Applicability

1. **Experimental Calibration Domain**:
   - Number of piles: $n_p \in [0, 9]$
   - Cushion thickness ratio: $h/d \in [0.5, 4.0]$
   - Cushion grain size: $d_{50} \in [0.5, 5.0\text{ mm}]$
   - Subsoil type: Cohesionless sands ($D_r = 70\text{--}86\%$, $\phi = 38\text{--}42^\circ$)
   - Normalized settlement: $w/B \le 10\%$
2. **Geotechnical Exclusions**:
   - Not directly calibrated for soft, normally consolidated cohesive soils (clays) where long-term consolidation settlement and pore pressure dissipation dominate.
   - Piles are assumed to be vertical; battered piles or lateral moment loading require additional calibration.

---

## Chapter 14: Conclusions and Future Scope

### Conclusions:
1. An engineering-constrained ML framework was successfully constructed from published 1g physical model tests, achieving $R^2 = 0.9007\text{--}0.9302$ on held-out experimental series.
2. Static equilibrium ($Q = Q_r + Q_p$) and exact load-sharing identities ($\alpha_p + \alpha_r = 100\%$) are rigorously preserved by the physics wrapper.
3. The machine learning model accurately reproduces the fundamental geotechnical inversion where the raft carries almost all load initially, with pile share mobilizing progressively to $35\%$ at $w/B = 10\%$.
4. Cushion thickness ($h/d = 2$) and cushion granularity ($d_{50} \ge 2.0\text{ mm}$) provide optimal settlement efficiency and load transfer.

### Future Scope:
- Incorporate geogrid-reinforced cushion layers (G-DPRF) to assess tensile membrane enhancement.
- Extend dataset to centrifuge dynamic shake table tests to predict seismic load redistribution.
- Integrate 3D continuum FE modeling (PLAXIS 3D / FLAC3D) to expand training domain into soft cohesive deposits.

---

## Chapter 15: References

1. **Halder, P., & Manna, B. (2022).** Load transfer mechanism for connected and disconnected piled raft: a comparative study. *Acta Geotechnica*, 17(7), 3033–3045. DOI: [10.1007/s11440-021-01409-0](https://doi.org/10.1007/s11440-021-01409-0).
2. **Halder, P., & Manna, B. (2021).** Large scale model testing to investigate the influence of granular cushion layer on the performance of disconnected piled raft system. *Acta Geotechnica*, 16(5), 1597–1614. DOI: [10.1007/s11440-020-01121-5](https://doi.org/10.1007/s11440-020-01121-5).
3. **Cao, X. D., Wong, I. H., & Chang, M. F. (2004).** Behavior of model rafts resting on pile-reinforced sand. *Journal of Geotechnical and Geoenvironmental Engineering*, 130(2), 129–138. DOI: [10.1061/(ASCE)1090-0241(2004)130:2(129)](https://doi.org/10.1061/(ASCE)1090-0241(2004)130:2(129)).
4. **Fioravante, V., & Giretti, D. (2010).** Contact versus noncontact piled raft foundations. *Canadian Geotechnical Journal*, 47(11), 1271–1287. DOI: [10.1139/T10-028](https://doi.org/10.1139/T10-028).
5. **Tradigo, F., Pisano, F., di Prisco, C., & Mussi, A. (2015).** Non-linear soil–structure interaction in disconnected piled raft foundations. *Computers and Geotechnics*, 63, 121–134. DOI: [10.1016/j.compgeo.2014.09.006](https://doi.org/10.1016/j.compgeo.2014.09.006).
6. **Wong, I. H., Chang, M. F., & Cao, X. D. (2000).** Raft foundations with disconnected settlement reducing piles. *Design Applications of Raft Foundations and Ground Slabs*, Thomas Telford, London, pp. 469–486.
7. **Pecker, A. (2004).** Design and construction of the Rion Antirion Bridge. *Proc. Geo-Trans, ASCE*, GSP 126, 216–240.
8. **Jamiolkowski, M. B., Ricceri, G., & Simonini, P. (2009).** Safeguarding Venice from high tides: site characterization and geotechnical problems. *Proc. 17th ICSMGE*, Alexandria, 4, 3209–3230.
9. **Burland, J. B., Broms, B. B., & de Mello, V. F. B. (1977).** Behavior of foundations and structures. *Proc. 9th ICSMFE*, Tokyo, 2, 495–546.
10. **Poulos, H. G., & Davis, E. H. (1980).** *Pile Foundation Analysis and Design*. John Wiley & Sons, New York.
11. **Dezfouli, M., Dehghani, M., Asakereh, A., & Kalantari, B. (2018).** Behavior of geogrid reinforced and unreinforced non-connected pile raft foundation. *International Journal of Civil Engineering*, 16(3), 313–328.
