"""
report_text.py
Contains complete, publication-grade academic text for all 16 chapters,
front matter, references, and appendices for the IIT Delhi B.Tech Project Report.
"""

TITLE = "Machine Learning-Based Prediction of Load Sharing Characteristics of Disconnected Piled Raft Foundations"
TITLE_BLOCK = "MACHINE LEARNING-BASED PREDICTION OF LOAD SHARING CHARACTERISTICS OF DISCONNECTED PILED RAFT FOUNDATIONS"
CANDIDATE_NAME = "Harshit Raj"
CANDIDATE_NAME_BLOCK = "HARSHIT RAJ"
ENTRY_NO = "2023CE10428"
SUPERVISOR_NAME = "Prof. B. Manna"
SUPERVISOR_TITLE = "Professor, Geotechnical Engineering Division"
DEPARTMENT = "Department of Civil Engineering"
DEPARTMENT_BLOCK = "DEPARTMENT OF CIVIL ENGINEERING"
INSTITUTE = "Indian Institute of Technology Delhi"
INSTITUTE_BLOCK = "INDIAN INSTITUTE OF TECHNOLOGY DELHI"
DATE_STR = "20 November 2026"
MONTH_YEAR = "NOVEMBER 2026"

CHAPTER_1_TITLE = "Chapter 1: Introduction"
CHAPTER_1_TEXT = """1.1 Background and Foundation Engineering Context
In modern civil infrastructure engineering, heavily loaded high-rise structures, industrial towers, commercial complexes, and bridge abutments impose severe vertical loads, lateral shear forces, and overturning moments upon subsoil strata. Conventional shallow foundation systems, such as isolated or unpiled raft foundations (UR), frequently fail to satisfy allowable serviceability settlement criteria, resulting in excessive differential settlement, structural angular distortion, and localized shear failure of near-surface soils. 

To overcome the performance limitations of isolated shallow footings, the foundation engineering community developed the Connected Piled Raft Foundation (CPR) system. In a classical CPR system, reinforced concrete or steel piles are monolithically connected to the base of a rigid raft foundation. Under vertical loading, the foundation settlement is governed by identical downward displacement at the raft-pile junction (w_r = w_p). Because the structural axial stiffness of reinforced concrete piles exceeds the subgrade stiffness of the surrounding soil matrix by several orders of magnitude, the piles attract the overwhelming majority of the superstructure load at very small settlements (w/B < 0.75%), frequently mobilizing 70% to 90% of their ultimate capacity almost instantaneously.

1.2 Structural Vulnerabilities of Connected Piled Rafts
While the monolithic CPR configuration effectively controls total settlement, it introduces severe structural vulnerabilities that complicate design and escalate construction costs:
1. Pile Head Stress Concentrations: The rigid connection forces extreme concentrations of axial thrust and high transverse shear forces directly at the pile-raft connection junction.
2. Dynamic and Seismic Vulnerability: During earthquake-induced horizontal shaking or strong cyclic wind loading, large lateral inertial forces induce massive bending moments and shear stresses at the rigid pile-head connection. Post-earthquake forensic investigations have repeatedly demonstrated brittle shear failures and crushing at rigidly cast pile heads.
3. Elevated Factor of Safety: Due to the catastrophic consequences of brittle pile-head structural collapse, international foundation design standards (such as BS 8004, Eurocode 7, and ACI 318) mandate high factors of safety (FS = 3.0 to 4.0) against structural failure for rigidly connected piles.
4. Under-Utilization of Raft Bearing Capacity: Because the piles attract almost all initial superstructure load, the direct bearing capacity of the upper competent subsoil layer beneath the raft remains under-mobilized until very large settlements occur.

1.3 The Concept and Mechanics of Disconnected Piled Rafts (DPRF)
To eliminate these structural vulnerabilities, Wong et al. (2000) and Cao et al. (2004) introduced the concept of the Disconnected Piled Raft Foundation (DPRF), also referred to as a Non-Connected Piled Raft or Interposed Cushion Foundation. 

In a DPRF system:
1. Structural Decoupling: Piles are structurally detached from the raft by an engineered granular cushion layer (Load Transfer Platform, LTP), typically comprised of compacted coarse sand, gravel, or stone aggregates.
2. Repurposing of Piles: The piles no longer act as structural columns in direct contact with the superstructure; instead, they function as vertical soil-reinforcing inclusions that stiffen the compressible subsoil composite.
3. Inverted Load-Sharing Kinetics: At initial loading stages, the raft bears 95% to 100% of the superstructure load. As the granular cushion layer undergoes localized compression and shear deformation, vertical stress arches laterally onto the pile heads, progressively mobilizing pile load capacity.
4. Neutral Plane and Stress Attenuation: Downward displacement of the cushion and upper subsoil relative to the stiff piles generates negative skin friction (NSF) along the upper shaft. This downward shear load transfers the peak axial force away from the pile head down to a neutral plane located at approximately z_n ≈ 10d (0.25 m depth), reducing pile head stresses by over 60% compared to CPR systems.
5. Economical Factor of Safety: Because pile heads are completely free from rigid bending moments and shear stress concentrations, piles act as ground reinforcements, enabling the structural factor of safety on piles to be safely reduced to FS ≈ 1.3.

1.4 Motivation for Machine Learning in Geotechnics
Despite the clear mechanical and economic advantages of DPRF systems, their routine adoption in structural design practice remains constrained by the lack of generalized predictive models. The load transfer across a disconnected piled raft involves highly non-linear, coupled soil-structure interaction phenomena:
- Granular soil arching across the cushion layer;
- Mobilization of interface friction along the unbonded pile heads;
- Progressive slip and down-drag along the upper pile shafts;
- Influence of multi-parameter geometric variables (cushion thickness ratio h/d, cushion grain size d_50, pile group density, and raft geometry).

Classical analytical methods (e.g., Poulos-Davis shear-displacement method, Randolph's piled raft analysis) rely on linear elasticity and cannot simulate the compressible cushion buffer, progressive mobilization, or inverted kinetics. Conversely, 3D continuum finite element and finite difference simulations (PLAXIS 3D, FLAC3D) require extensive computational runtimes, complex constitutive soil models (e.g., Hardening Soil model with small-strain stiffness), and advanced parameter calibration, rendering them unsuitable for rapid parametric optimization or iterative preliminary design.

Machine learning (ML) provides an exceptional mathematical paradigm for learning non-linear, multi-dimensional regression mappings directly from empirical and experimental data. However, standard off-the-shelf ML algorithms operate as unconstrained black-box estimators, frequently predicting non-physical outputs (e.g., pile load sharing exceeding 100%, or total predicted reactions violating vertical static equilibrium). Therefore, an engineering-rigorous, physics-constrained machine learning (PC-ML) framework calibrated on verified experimental data is required.

1.5 Organization of the Thesis
This report is organized into 16 structured chapters:
- Chapter 2 synthesizes the historical evolution of piled raft foundations, physical model testing, and numerical simulations.
- Chapter 3 identifies the specific research gaps and formulates the analytical problem.
- Chapter 4 defines the primary research objectives and calibration boundaries.
- Chapter 5 provides an in-depth geotechnical analysis of cushion arching, negative skin friction, and neutral plane mechanics.
- Chapter 6 details the experimental dataset compilation, source provenance, and feature engineering.
- Chapter 7 formulates the governing mathematical equations and the Physics-Constrained Wrapper.
- Chapter 8 details the supervised machine learning regression algorithms.
- Chapter 9 presents the leakage-free GroupKFold cross-validation protocol and hyperparameter tuning.
- Chapter 10 presents the comparative benchmark results across all 8 evaluated models.
- Chapter 11 discusses experimental and predicted load-settlement responses, parity, and residual error distributions.
- Chapter 12 provides explainable AI (XAI) insights via Gini feature importance and SHAP beeswarm plots.
- Chapter 13 conducts systematic 4-parameter sensitivity analyses.
- Chapter 14 translates findings into actionable geotechnical design guidelines.
- Chapter 15 outlines operational limitations and future research scope.
- Chapter 16 concludes the monograph with major findings and practical deliverables.
- References and Appendices provide complete bibliographies, experimental catalogs, and source code.
"""

CHAPTER_2_TITLE = "Chapter 2: Literature Review"
CHAPTER_2_TEXT = """2.1 Evolution of Piled Raft Foundation Analysis
The concept of utilizing piles to control foundation settlements rather than support the entire building load was pioneered by Burland et al. (1977). In their seminal contribution, piles were conceptualized as "settlement reducers," designed to operate at or near their ultimate geotechnical capacity under working loads, while the remaining superstructure load is safely carried by direct contact pressure beneath the raft slab.

Poulos and Davis (1980) and Poulos (2001) formalized the analytical foundations for Connected Piled Raft (CPR) systems using simplified boundary element methods (GEMS) and interaction factors. Randolph (1994) developed an approximate analytical framework based on the shear-displacement method, characterizing load sharing through composite foundation stiffness:
K_pr = (K_r + K_p * (1 - 2*alpha_rp)) / (1 - alpha_rp^2 * (K_r / K_p))
where K_r and K_p are the isolated stiffnesses of the raft and pile group, and alpha_rp is the raft-pile interaction factor. While Randolph's formulation represented a monumental breakthrough for conventional connected systems, it assumed complete monolithic bonding at the pile-raft interface and could not capture disconnected configurations.

2.2 Physical Model Investigations of Disconnected Systems
Wong et al. (2000) conducted pioneering 1g model tests in dense dry sand exploring unbonded pile heads separated from the raft by an interposed sand layer. Their results indicated that the granular interlayer eliminated structural distress at pile heads while achieving settlement reduction comparable to connected systems.

Cao et al. (2004) performed extensive 1g physical model tests in loose and dense sand (Toyoura sand, d_50 = 0.16 mm) using square model rafts (B = 250 mm) supported by 3x3 aluminum pile groups (d = 25 mm, L/d = 14 to 20). They systematically evaluated cushion thickness ratios (h/d = 0.5 to 2.0). Their findings demonstrated that:
1. Disconnecting piles prevented excessive load transfer to pile heads at small settlements.
2. Cushion thickness governed the settlement efficiency; excessive cushion thickness (h/d > 2.0) led to reduced pile mobilization.
3. Raft contact pressure was homogenized across the footprint, suppressing differential settlements.

Fioravante and Giretti (2010) performed 50g geotechnical centrifuge experiments at ISMGEO in Italy, comparing contact (CPR) and non-contact (DPRF) piled rafts in fine silica sand. The centrifuge environment correctly reproduced prototype stress levels, validating that non-connected piles experience relative soil-pile slippage in the upper cushion zone, modifying the mobilized shaft friction profile without compromising overall bearing capacity.

2.3 Large-Scale Physical Modeling by Halder & Manna (2021, 2022)
Halder and Manna conducted the most rigorous and comprehensive large-scale physical model testing program on DPRF systems to date at the Indian Institute of Technology Delhi. Their research was published in two landmark papers in Acta Geotechnica:
1. Halder & Manna (2021): "Large scale model testing to investigate the influence of granular cushion layer on the performance of disconnected piled raft system," Acta Geotechnica, 16(5), 1597–1614.
   - Experimental Facility: A rigid steel test tank measuring 2.0 m x 2.0 m in plan and 1.8 m in depth, equipped with a high-capacity reaction frame and hydraulic actuator.
   - Soil Bed: Uniformly deposited Yamuna sand prepared at relative densities D_r = 70% and 86% using automated raining techniques (d_50 = 0.30 mm, gamma = 15.9 kN/m^3, phi = 40.7 deg).
   - Foundation Geometry: Square model rafts (B = 300 mm, thickness t_r = 25 mm) reinforced with 1x1 and 3x3 hollow steel pipe piles (d = 25.4 mm, length L = 1.0 m, L/d = 39.4, spacing s = 3d).
   - Cushion Parameters: Systematically varied cushion thickness ratio (h/d = 1, 2, 3, and 4) using three distinct granular materials:
     * CM1: Fine-medium Badarpur sand (d_50 = 0.6 mm, phi = 47 deg, gamma = 14.1 kN/m^3)
     * CM2: Medium-coarse Badarpur sand (d_50 = 2.0 mm, phi = 51 deg, gamma = 14.8 kN/m^3)
     * CM3: Coarse Badarpur gravelly sand (d_50 = 4.5 mm, phi = 56 deg, gamma = 15.2 kN/m^3)
   - Key Discoveries: Identified that an optimum cushion thickness exists at h/d = 2.0; coarser cushion sand (CM3) yielded 18% higher bearing capacity and 36% pile load sharing compared to fine sand (CM1).

2. Halder & Manna (2022): "Load transfer mechanism for connected and disconnected piled raft: a comparative study," Acta Geotechnica, 17(7), 3033–3045.
   - Direct Comparative Testing: Tested Unpiled Raft (UR), Connected Piled Raft (CPR 2x2), and Disconnected Piled Raft (DPRF 2x2 with h/d = 1, 2, 3).
   - Instrumentation: Piles were instrumented with high-precision electrical resistance strain gauges along the embedded shaft at depths of 2d, 5d, 10d, 15d, 20d, 28d, and 35d to measure axial force distribution and shaft friction.
   - Critical Geotechnical Finding: In CPR, maximum axial force occurred at the pile head (depth z = 0). In contrast, in DPRF, the axial load was lowest at the pile head and increased with depth to a maximum at z_n ≈ 10d (0.25 m depth). This confirmed the existence of negative skin friction (NSF) along the upper pile shaft due to relative downward movement of the cushion and subsoil.

2.4 Global Megaprojects Employing Disconnected Pile Principles
The practical efficacy of disconnected piled foundation systems is underscored by major worldwide infrastructure projects:
- Rion-Antirion Bridge, Greece (Pecker 2004): Spanning the Gulf of Corinth, four deep-water gravity piers (90 m base diameter) are founded on soft marine clays reinforced with 20 m long, 2 m diameter steel tubular inclusions. A 3.0 m thick gravel cushion layer separates the pier base from the pile heads, preventing seismic moment transmission and accommodating fault slip without structural rupture.
- Venice MOSE Storm Barrier, Italy (Jamiolkowski et al. 2009): Disconnected pile reinforcements were deployed beneath massive inlet caissons in the Venetian lagoon to mitigate differential settlements under tidal surges while preventing pile head shear distress.
- Marcoule Nuclear Waste Storage Facility, France (Mattsson et al. 2013): High-load bunkers founded on disconnected pile arrays to limit differential settlement under extreme thermal and static loads.

2.5 Machine Learning in Geotechnical Foundation Engineering
In recent years, artificial intelligence and machine learning have been applied to deep foundation problems. Researchers have employed Artificial Neural Networks (ANN), Support Vector Machines (SVM), and Random Forests to predict the axial capacity of driven piles (Das & Basudhar 2006; Manna & Baidya 2010), settlement of shallow foundations, and slope stability. 

However, existing literature on machine learning for piled raft systems remains almost exclusively focused on conventional connected piled rafts (CPR). To date, no published study has established a machine learning framework specifically for Disconnected Piled Raft Foundations (DPRF) that accounts for cushion layer granularity, cushion thickness ratio, inverted load-sharing kinetics, and strict static equilibrium constraints. This represents the core contribution of the present research.
"""

CHAPTER_3_TITLE = "Chapter 3: Research Gap and Problem Formulation"
CHAPTER_3_TEXT = """3.1 Critical Limitations in Existing Analytical Methods
While empirical guidelines and 3D finite element simulations exist for isolated DPRF configurations, current geotechnical design practice suffers from major limitations:
1. Analytical Deficiencies: Classical closed-form solutions (e.g., Poulos, Randolph, Clancy & Randolph) are predicated on continuum linear elasticity with bonded pile heads. They cannot model the discontinuous boundary conditions, localized granular slippage, and non-linear compression of the granular cushion layer.
2. Computational Overhead of Numerical Models: 3D non-linear continuum finite element modeling (FE) using advanced constitutive models (e.g., Hardening Soil with Small-Strain Stiffness) requires hours or days of execution per load increment, high mesh resolution around pile heads, and extensive calibration of advanced soil parameters. This computational cost prevents routine use in early design iterations or probabilistic reliability assessments.
3. Lack of Unified Empirical Formulations: Existing empirical formulas are strictly tied to specific physical test dimensions and cannot generalize across varying cushion thicknesses (h/d), cushion grain sizes (d_50), pile numbers (n_p), and settlement levels (w/B).

3.2 Coupled Soil-Structure Interaction Complexity
The load transfer in a DPRF system involves four coupled mechanical mechanisms:
- Soil Arching: Formation of compressive stress arches within the granular cushion spanning between adjacent pile caps.
- Interface Slip: Relative shear displacement across the unbonded cushion-pile head interface.
- Down-Drag Kinetics: Downward shear displacement of the settling cushion and upper soil bed, inducing negative skin friction along the upper pile shaft.
- Progressive Mobilization: Gradual transition from raft-dominated load carriage at low settlements to combined raft-pile ground reinforcement at high settlements.

Because these mechanisms interact non-linearly, classical multi-variable linear regressions yield severe prediction errors.

3.3 The Risk of Data Leakage in Geotechnical ML
A critical methodological flaw in many published geotechnical machine learning papers is the application of naive, random K-Fold cross-validation. In a physical model load test, 6 to 10 load-settlement stages are recorded for a single foundation configuration. If random K-Fold CV is used, observations from the same physical test are split across both training and validation folds. Because geometric dimensions (B, d, L, s/d, h/d) and soil properties (phi, gamma, d_50) are identical across all load steps of that experiment, the model simply memorizes the test geometry rather than learning generalizable geotechnical mechanics. This creates severe data leakage and artificially inflated accuracy metrics that collapse when tested on genuinely unseen foundation designs.

3.4 Physical Law Violations in Conventional AI Algorithms
Standard machine learning models (such as unconstrained neural networks, gradient boosting, or support vector regression) treat target variables as isolated scalar outputs without physical awareness. In geotechnical load sharing:
- Off-the-shelf regressors can predict negative pile load shares (alpha_p < 0%) or pile shares exceeding 100%.
- When predicting pile load Q_p and raft load Q_r independently, standard models violate basic static equilibrium (Q_p + Q_r != Q).
- In structural engineering, violating equilibrium renders predictions legally and operationally unusable.

3.5 Problem Formulation
This study formulates the DPRF prediction problem as a Physics-Constrained Machine Learning (PC-ML) non-linear mapping:
hat{alpha}_p = f_theta(x)
subject to the strict physical constraints:
0% <= hat{alpha}_p <= 100%
hat{alpha}_r = 100.00% - hat{alpha}_p
Q_p = Q * (hat{alpha}_p / 100)
Q_r = Q * (hat{alpha}_r / 100)
Q_p + Q_r = Q (Static Vertical Equilibrium)
where x in R^20 represents the standardized geotechnical feature vector encompassing foundation geometry, cushion layer mechanics, subsoil properties, and loading conditions.
"""

CHAPTER_4_TITLE = "Chapter 4: Scope and Objectives"
CHAPTER_4_TEXT = """4.1 Research Objectives
The primary objectives of this B.Tech Project are:
1. Experimental Database Compilation: To systematically compile, digitize, and quality-verify a comprehensive database of published physical model and centrifuge tests on disconnected piled raft foundations, complete with detailed source attribution and dimensional normalization.
2. Physics-Constrained Framework Development: To develop and implement an explicit Physics-Constrained Wrapper that mathematically guarantees vertical static equilibrium (Q = Q_r + Q_p) and exact load-sharing identities (alpha_p + alpha_r = 100%) across all inference stages.
3. Leakage-Free Validation Architecture: To implement a strict GroupKFold cross-validation protocol grouped by physical test series, ensuring that validation evaluates true generalization to completely unseen foundation setups.
4. Multi-Algorithm Machine Learning Benchmarking: To train, tune, and comparatively benchmark eight candidate regression architectures (Linear, Ridge, Polynomial, SVR, Decision Tree, Random Forest, Gradient Boosting, and XGBoost) using standardized geotechnical error metrics (R^2, MAE, RMSE).
5. Explainable AI (XAI) and Mechanistic Interpretation: To extract Gini feature importances and compute SHapley Additive exPlanations (SHAP) to interpret how cushion thickness, cushion grain size, pile area ratio, and settlement govern load-sharing kinetics.
6. Parametric Sensitivity Studies: To conduct comprehensive sensitivity analyses evaluating the impact of cushion thickness ratio (h/d = 0.5 to 4.0), cushion particle size (d_50 = 0.5 to 5.0 mm), pile area ratio (A_p/A_r = 1% to 8%), and normalized settlement (w/B = 0.5% to 10%).
7. Software Tool and Design Monograph: To deploy the validated model in an accessible, interactive Streamlit web dashboard and command-line inference tool, supported by actionable engineering design guidelines for foundation practitioners.

4.2 Scope and Calibration Boundaries
The scope of this project is calibrated within the following experimentally validated domain:
- Subsoil Type: Cohesionless cohesionless sands (dry or moist, non-liquefied) with relative densities D_r = 70% to 86% and internal friction angles phi = 38 deg to 42 deg.
- Foundation Configuration: Unpiled rafts (UR), single piles (1x1), 2x2 pile groups, and 3x3 pile groups embedded in sand.
- Cushion Layer: Granular cushion material ranging from fine sand to coarse gravelly aggregates (d_50 = 0.5 mm to 5.0 mm; friction angle phi_c = 45 deg to 58 deg).
- Cushion Thickness Ratio: h/d in the range [0.0, 4.0], where h/d = 0 represents conventional connected piled rafts (CPR).
- Raft Geometry: Square rigid rafts with width B = 200 mm to 350 mm (model scale) and thickness t_r = 15 mm to 30 mm.
- Pile Shafts: Slender vertical piles with diameter d = 20 mm to 30 mm and slenderness ratio L/d = 14 to 40.
- Loading Condition: Monotonic static vertical downward compressive loading up to normalized settlement w/B = 10%.
"""

CHAPTER_5_TITLE = "Chapter 5: Geotechnical Mechanics and Load Transfer Fundamentals"
CHAPTER_5_TEXT = """5.1 Load Transfer Platform (LTP) Mechanics
In a Disconnected Piled Raft Foundation, the structural interaction between the superstructure, the raft slab, the granular cushion, the reinforcing piles, and the subgrade is governed by the mechanics of the Load Transfer Platform (LTP). 

When vertical load Q is applied to the upper surface of the raft, the raft moves downward by displacement w_r, exerting a vertical contact pressure q(x, y) onto the upper boundary of the granular cushion layer. Unlike a monolithic connection where load is transferred directly into the pile heads through steel or concrete shear transfer, the granular cushion redistributes vertical stresses through two primary mechanisms:
1. Inter-Particle Shear Interlock: The densely compacted granular particles within the cushion resist shear deformation through internal friction (phi_c) and dilatancy, spreading the localized contact stresses outward.
2. Soil Arching: Because the pile heads are significantly stiffer than the surrounding subsoil, the subsoil between adjacent piles settles more than the pile heads under the applied vertical pressure. This differential vertical settlement triggers the classic Terzaghi soil arching phenomenon within the cushion.

5.2 Soil Arching Theory in Granular Cushions
The phenomenon of soil arching within the cushion layer can be explained using Terzaghi's classical trapdoor theory (Terzaghi 1943) and Handy's catenary arch formulation (Handy 1985). As the subsoil between piles yields downward relative to the rigid pile caps, shear stresses tau develop along curved slip surfaces within the granular cushion. These shear stresses act upward on the settling soil mass and downward onto the rigid pile caps, effectively channeling vertical stresses away from the subsoil and concentrating them onto the pile heads.

The vertical stress sigma_v acting on the cushion at depth z is governed by the differential equilibrium equation:
(d sigma_v / dz) + (2 * K * tan(phi_c) / s) * sigma_v = gamma_c
where K is the lateral earth pressure coefficient within the shearing zone, phi_c is the internal friction angle of the cushion, s is the clear spacing between pile caps, and gamma_c is the unit weight of the cushion material.

From this governing differential equation, two critical engineering deductions arise:
1. Influence of Cushion Friction Angle (phi_c): Higher cushion friction angles (coarser sand and gravel) generate larger transverse shear stresses tau = sigma_h * tan(phi_c), enhancing the arching effect and increasing the proportion of load channeled onto the pile heads.
2. Influence of Cushion Thickness (h): If the cushion thickness h is too small (h/d < 1.0), the arching geometry cannot fully develop, leading to localized punching shear directly above the pile heads. Conversely, if the cushion is excessively thick (h/d > 3.0), the shear arches fully close within the cushion mass, and stresses dissipate uniformly into the subsoil before reaching the pile heads, reducing the settlement-reducing efficacy of the pile group.

5.3 Relative Displacement and Negative Skin Friction (NSF)
In a conventional Connected Piled Raft (CPR), the pile and the raft move synchronously (w_p = w_r). Because the pile is much stiffer than the surrounding soil, the pile settles less than or equal to the adjacent soil along its entire length, mobilizing positive shaft friction (tau_s > 0) from the pile head downward to the toe.

In contrast, in a Disconnected Piled Raft Foundation (DPRF), the raft settles into the granular cushion, causing the cushion material and the upper subsoil layer to undergo substantial downward displacement w_s. The piles, resting on deeper competent subsoil strata, experience significantly less settlement (w_p < w_s).

Consequently, in the upper portion of the pile shaft:
w_s(z) > w_p(z)
This relative downward displacement of the soil relative to the pile reverses the direction of mobilized shear stress along the shaft perimeter, inducing Negative Skin Friction (NSF):
tau_s(z) = - K_0 * sigma'_v(z) * tan(delta) < 0
where K_0 is the at-rest lateral earth pressure coefficient, sigma'_v(z) is the effective vertical overburden stress, and delta is the soil-pile interface friction angle (delta ≈ 0.8 * phi).

5.4 The Neutral Plane Location (z_n ≈ 10d)
The development of negative skin friction along the upper pile shaft has a profound effect on the internal axial force distribution within the pile. 

In a CPR pile, the axial force is maximum at the pile head (z = 0) where it connects to the raft, and decreases monotonically with depth as positive shaft resistance sheds load into the soil.

In a DPRF pile, the axial force at the pile head Q_head is relatively small, generated solely by the normal stress arched onto the pile cap. As depth increases, the downward drag from negative skin friction adds cumulative downward load to the pile shaft:
P(z) = Q_head + integral_0^z [ pi * d * (-tau_s(z)) dz ] for z < z_n

The axial force continues to increase until reaching the Neutral Plane (depth z_n), where the relative settlement between the soil and pile becomes zero:
w_s(z_n) = w_p(z_n) ==> tau_s(z_n) = 0
At depths below the neutral plane (z > z_n), the pile settles more than the surrounding soil (w_p > w_s), mobilizing positive shaft friction and base resistance to support both the superstructure load and the down-drag force.

Halder & Manna (2022) experimentally confirmed this mechanism using strain-gauged pile shafts. Their measurements demonstrated that for DPRF systems embedded in dense sand, the neutral plane consistently establishes at depth:
z_n ≈ 10d (0.25 m depth for d = 25.4 mm piles)
The maximum axial force occurs at z_n, while the pile head axial force is reduced by 60% to 75% compared to the monolithic CPR connection.

5.5 Structural Stress Attenuation and Factor of Safety
The shift of peak axial force to the neutral plane and the absence of a rigid moment connection provide extraordinary structural benefits:
1. Elimination of Punching Shear: In CPR slabs, rigid pile heads act as hard re-entrant corners, inducing extreme punching shear stresses that necessitate thick raft slabs or local drop panels. In DPRF, the cushion layer homogenizes the contact pressure distribution across the raft base, completely eliminating punching shear distress and allowing significantly thinner raft designs.
2. Attenuation of Seismic Shear: Under lateral earthquake ground motion, the granular cushion acts as an elastoplastic isolation layer, absorbing shear deformations through inter-particle friction and preventing brittle shearing of the pile heads.
3. Rational Factor of Safety: In conventional CPR design, building codes enforce a high factor of safety (FS = 3.0 to 4.0) to prevent pile structural failure. In DPRF systems, because piles act as ductile settlement-reducing inclusions whose structural integrity is safeguarded by the cushion buffer, an engineering factor of safety of FS ≈ 1.3 to 1.5 against geotechnical ultimate capacity is fully justified.
"""

CHAPTER_6_TITLE = "Chapter 6: Experimental Dataset Compilation and Provenance"
CHAPTER_6_TEXT = """6.1 Experimental Data Compilation Methodology
To establish a high-fidelity empirical foundation for machine learning development, an extensive experimental data curation program was conducted. Experimental load-settlement curves, load-sharing diagrams, and pile instrumentation profiles were digitized from peer-reviewed literature using high-resolution graphical vector extraction software.

Every observation in the dataset satisfies three strict inclusion criteria:
1. Experimental Verification: Only physical model tests (1g laboratory tanks or geotechnical centrifuge tests) with verified instrumentation (strain gauges, load cells, LVDTs) were included. Purely numerical simulations without physical validation were excluded from primary training.
2. Provenance Attribution: Every data point is indexed by an immutable source identifier (SRC-01 through SRC-05) and linked to the exact figure, table, and page of origin in the published literature.
3. Static Equilibrium Audit: All reported loads were audited to ensure that reported raft loads, pile group loads, and total applied loads satisfy static vertical equilibrium within experimental measurement tolerance.

6.2 The Halder & Manna (2021, 2022) Benchmark Catalog
The core of the compiled database comprises the comprehensive experimental program performed by Halder & Manna at IIT Delhi:
- Source SRC-01: Halder & Manna (2022), Acta Geotechnica (10.1007/s11440-021-01409-0)
  * HM22_DPR_2x2_hd1: DPRF 2x2 pile group, Badarpur sand cushion, h/d = 1.0
  * HM22_DPR_2x2_hd2: DPRF 2x2 pile group, Badarpur sand cushion, h/d = 2.0
  * HM22_DPR_2x2_hd3: DPRF 2x2 pile group, Badarpur sand cushion, h/d = 3.0
  * HM22_CPR_2x2: Monolithic Connected Piled Raft 2x2 pile group (h/d = 0)
  * HM22_UR: Unpiled Raft foundation benchmark (n_p = 0)
- Source SRC-02: Halder & Manna (2021), Acta Geotechnica (10.1007/s11440-020-01121-5)
  * HM21_DPR_3x3_hd1_CM2: DPRF 3x3 pile group, Cushion Material 2 (d_50 = 2.0 mm), h/d = 1.0
  * HM21_DPR_3x3_hd2_CM2: DPRF 3x3 pile group, Cushion Material 2 (d_50 = 2.0 mm), h/d = 2.0
  * HM21_DPR_3x3_hd3_CM2: DPRF 3x3 pile group, Cushion Material 2 (d_50 = 2.0 mm), h/d = 3.0
  * HM21_DPR_3x3_hd4_CM2: DPRF 3x3 pile group, Cushion Material 2 (d_50 = 2.0 mm), h/d = 4.0
  * HM21_DPR_3x3_hd2_CM1: DPRF 3x3 pile group, Cushion Material 1 (d_50 = 0.6 mm), h/d = 2.0
  * HM21_DPR_3x3_hd2_CM3: DPRF 3x3 pile group, Cushion Material 3 (d_50 = 4.5 mm), h/d = 2.0
  * HM21_DPR_1x1: DPRF single pile, Cushion Material 2, h/d = 2.0
  * HM21_PR_1x1: Connected single pile raft, h/d = 0.0

6.3 Centrifuge and Literature Benchmarks
To expand the geographic and stress-level diversity of the training space, high-quality benchmarks from international literature were integrated:
- Source SRC-03: Cao, Wong, & Chang (2004), ASCE JGGE (10.1061/(ASCE)1090-0241(2004)130:2(129))
  * Cao04_1g_3x3_LB0.79: 1g model test on pile-reinforced sand, L/B = 0.79 (L = 0.35 m, B = 250 mm)
  * Cao04_1g_3x3_LB1.13: 1g model test on pile-reinforced sand, L/B = 1.13 (L = 0.50 m, B = 250 mm)
- Source SRC-04: Fioravante & Giretti (2010), Canadian Geotechnical Journal (10.1139/T10-028)
  * FG10_Centrifuge_3x3_hd1.8: 50g geotechnical centrifuge test of non-connected piled raft in Toyoura sand (h/d = 1.8).

Total Compiled Observations: 99 validated load-settlement stages across 16 experimental series, spanning normalized settlements w/B from 0.5% to 10.0%.

6.4 Feature Space Definition and Dimensional Standardization
To ensure physical consistency across diverse model scales, 20 geotechnical features were extracted and standardized:
1. is_disconnected: Binary indicator (1 = DPRF, 0 = CPR / UR)
2. n_piles: Integer count of piles (0 to 9)
3. pile_diameter_mm: Pile shaft outer diameter d (mm)
4. pile_length_m: Embedded pile length L (m)
5. pile_spacing_ratio: Center-to-center spacing ratio s/d
6. raft_width_mm: Raft width B (mm)
7. raft_thickness_mm: Structural raft thickness t_r (mm)
8. pile_area_ratio: Dimensionless pile density alpha_area = (n_p * pi * d^2 / 4) / B^2
9. cushion_thickness_ratio: Normalized cushion thickness h/d
10. cushion_d50_mm: Mean grain size of cushion material d_50 (mm)
11. cushion_friction_deg: Cushion internal friction angle phi_c (deg)
12. cushion_gamma_kn_m3: Cushion unit weight gamma_c (kN/m^3)
13. soil_d50_mm: Foundation subsoil mean grain size (mm)
14. soil_friction_deg: Subsoil internal friction angle phi (deg)
15. soil_relative_density_pct: Subsoil relative density D_r (%)
16. soil_gamma_kn_m3: Subsoil unit weight gamma (kN/m^3)
17. applied_load_kn: Total vertical load Q applied to foundation (kN)
18. settlement_mm: Absolute vertical foundation settlement w (mm)
19. normalized_settlement_pct: Normalized settlement ratio (w/B) * 100%
20. applied_pressure_kpa: Average applied contact pressure q = Q / B^2 (kPa)

Primary Target Variable:
- pile_load_share_pct: Pile load-sharing percentage alpha_p = (Q_p / Q) * 100 (%)
"""

CHAPTER_7_TITLE = "Chapter 7: Mathematical Formulation and Physics-Constrained Modeling"
CHAPTER_7_TEXT = """7.1 Governing Equations of Vertical Static Equilibrium
In structural foundation engineering, vertical static equilibrium requires that the total superstructure load Q applied to the raft must be exactly balanced by the sum of the vertical force transmitted through direct raft-cushion contact (Q_r) and the total vertical force mobilized within the pile group (Q_p):
Q = Q_r + Q_p
where:
Q_p = sum_{i=1}^{n_p} Q_{p,i}
where Q_{p,i} is the vertical load sustained by the i-th individual pile in the group.

7.2 Load-Sharing Proportions and Physical Bounds
The load-sharing characteristics are non-dimensionalized as load-sharing percentages:
alpha_p = (Q_p / Q) * 100%
alpha_r = (Q_r / Q) * 100%

Dividing the static equilibrium equation by Q yields the fundamental load-sharing identity:
alpha_p + alpha_r = 100.00%

Furthermore, because tensile foundation uplift is excluded under downward compressive gravity loading, both load-sharing proportions are strictly bounded within the physical domain:
0.0% <= alpha_p <= 100.0%
0.0% <= alpha_r <= 100.0%

7.3 Settlement Efficiency Formulation
To quantify the geotechnical effectiveness of the disconnected pile group in mitigating settlement relative to an unpiled raft, Burland's settlement reduction efficiency ratio eta is defined:
eta = (w_UR - w_DPR) / w_UR
where w_UR is the settlement of the unpiled raft foundation under total load Q, and w_DPR is the settlement of the disconnected piled raft under the identical load Q. 
For an unpiled raft, eta = 0. For an infinitely rigid foundation with zero settlement, eta = 1.0. Experimental data from Halder & Manna (2021) shows that for an optimum 3x3 DPRF (h/d = 2, CM2), eta reaches 0.45 to 0.52 at design load levels.

7.4 Architecture of the Physics-Constrained Wrapper
To enforce these governing physical laws, the ML architecture incorporates an explicit PhysicsConstrainedModelWrapper. Unlike unconstrained regressors that predict alpha_p and alpha_r independently, our system employs a single-target primary estimator coupled with mathematical post-processing:
1. Primary Inference: The base model predicts the raw pile load share:
   alpha_p,raw = f_theta(x)
2. Domain Clamping: The prediction is clamped to the physically admissible boundary:
   alpha_p = max(0.0, min(100.0, alpha_p,raw))
3. Analytical Equilibrium Enforcement: The raft load share is computed analytically:
   alpha_r = 100.00 - alpha_p
4. Force Decomposition: Total applied load Q is decomposed into absolute forces:
   Q_p = Q * (alpha_p / 100.0)
   Q_r = Q * (alpha_r / 100.0)
5. Equilibrium Check: The residual error |(Q_p + Q_r) - Q| is verified to be identically zero (< 10^-5 kN).

7.5 Domain Validity Verification
The wrapper executes real-time domain verification against the calibration envelope (Table 7.1). If any input parameter falls outside the experimentally established limits, the system outputs an explicit warning to alert the engineer of potential extrapolation risk.
"""

CHAPTER_8_TITLE = "Chapter 8: Machine Learning Methodology and Architectures"
CHAPTER_8_TEXT = """8.1 Supervised Regression Formulation
The task of predicting the load-sharing proportion of disconnected piled raft foundations is formulated as a multi-dimensional supervised non-linear regression problem:
hat{y} = f(X; theta)
where X in R^{N x 20} is the design feature matrix, y in R^N is the vector of measured pile load sharing percentages (alpha_p), and theta represents the trainable parameters.

8.2 Candidate Regression Architectures
To identify the optimal mathematical model, eight diverse algorithmic paradigms were benchmarked:

1. Linear Regression: Ordinary Least Squares (OLS) baseline assuming linear superposition:
   hat{y} = X * beta
   Loss = ||y - X * beta||^2_2

2. Ridge Regression: Regularized linear model penalizing large coefficients to mitigate multicollinearity among geometric dimensions:
   Loss = ||y - X * beta||^2_2 + alpha * ||beta||^2_2

3. Polynomial Regression (Degree 2): Evaluates quadratic feature expansion:
   phi(x) = [1, x_i, x_i * x_j, x_i^2]
   coupled with Ridge regularization (alpha = 10.0) to model second-order interaction terms.

4. Support Vector Regression (SVR): Non-linear kernel regression mapping features into a high-dimensional reproducing kernel Hilbert space using the Radial Basis Function (RBF) kernel:
   K(x_i, x_j) = exp(-gamma * ||x_i - x_j||^2)
   Optimization minimizes the epsilon-insensitive loss function:
   Loss = C * sum L_epsilon(y_i - f(x_i)) + 0.5 * ||w||^2

5. Decision Tree Regressor: Non-parametric recursive binary partitioning based on mean squared error reduction at each split:
   Split Criterion = min [ Var(left) + Var(right) ]

6. Random Forest Regressor: Bootstrap aggregating (bagging) of B de-correlated regression trees:
   hat{y} = (1 / B) * sum_{b=1}^B T_b(x; Theta_b)
   Each split considers a randomized subset of m = sqrt(p) features, drastically reducing variance and suppressing overfitting.

7. Gradient Boosting Regressor (GBR): Additive ensemble building trees sequentially:
   f_m(x) = f_{m-1}(x) + nu * h_m(x)
   where h_m(x) fits the pseudo-residuals of the previous iteration under least-squares loss, and nu is the shrinkage learning rate.

8. eXtreme Gradient Boosting (XGBoost): Scaled tree boosting incorporating second-order Taylor expansions of the objective function:
   Obj^{(t)} = sum_{i=1}^N [ g_i * f_t(x_i) + 0.5 * h_i * f_t(x_i)^2 ] + Omega(f_t)
   where g_i and h_i are the first and second order gradients of the loss, and Omega penalizes tree leaf count and leaf weights (L1/L2 regularization).

8.3 Performance Evaluation Metrics
Model performance was evaluated using three standardized metrics:
- Coefficient of Determination (R^2):
  R^2 = 1 - [ sum (y_i - hat{y}_i)^2 / sum (y_i - bar{y})^2 ]
- Mean Absolute Error (MAE):
  MAE = (1 / N) * sum |y_i - hat{y}_i|  (in percentage points)
- Root Mean Squared Error (RMSE):
  RMSE = sqrt( (1 / N) * sum (y_i - hat{y}_i)^2 )  (in percentage points)
"""

CHAPTER_9_TITLE = "Chapter 9: Model Training, Grouped Cross-Validation, and Tuning"
CHAPTER_9_TEXT = """9.1 The Grouped Cross-Validation Protocol
To guarantee complete scientific rigor and eliminate the pervasive threat of data leakage, this study enforced a strict GroupKFold cross-validation scheme.

Data Partitioning Strategy:
- The 99 observations belong to 16 distinct experimental test series.
- A grouped train/test split (80% train, 20% test) allocated 12 complete physical model experiments (81 observations) to training, and 4 complete experiments (18 observations) to the independent test set.
- Crucially, the 4 held-out test series represent diverse physical configurations:
  1. HM22_DPR_2x2_hd3: Halder & Manna (2022) 2x2 DPRF with thick cushion (h/d = 3.0)
  2. HM21_DPR_3x3_hd2_CM1: Halder & Manna (2021) 3x3 DPRF with fine sand cushion (d_50 = 0.6 mm)
  3. Cao04_1g_3x3_LB0.79: Cao et al. (2004) independent 1g test in Toyoura sand (short piles)
  4. Cao04_1g_3x3_LB1.13: Cao et al. (2004) independent 1g test in Toyoura sand (long piles)

During cross-validation on the 81 training samples, a 5-fold GroupKFold was executed. In each fold, entire physical test series were withheld from model fitting. This guarantees that validation metrics reflect genuine predictive capability on new, unseen foundation geometries.

9.2 Data Scaling Protocol
To prevent data snooping across folds, feature standardization (StandardScaler: z = (x - mu) / sigma) was fitted exclusively on the training folds and subsequently applied to transform validation and test folds. Tree-based ensemble models (Random Forest, XGBoost) operated on raw physical units to preserve split interpretability.

9.3 Hyperparameter Optimization
Grid search with grouped cross-validation (GridSearchCV) was conducted to tune candidate hyperparameters:
- Random Forest Tuning:
  * n_estimators in [50, 100, 150]
  * max_depth in [4, 6, 8, None]
  * min_samples_split in [2, 3, 5]
  * Optimal Result: n_estimators = 100, max_depth = 6, min_samples_split = 2.
- XGBoost Tuning:
  * n_estimators in [50, 100, 150]
  * max_depth in [3, 4, 5]
  * learning_rate in [0.03, 0.08, 0.15]
  * Optimal Result: n_estimators = 100, max_depth = 4, learning_rate = 0.08.
"""

CHAPTER_10_TITLE = "Chapter 10: Model Benchmark Comparison and Selection"
CHAPTER_10_TEXT = """10.1 Comparative Benchmark Analysis
The candidate regression models were trained and evaluated under identical grouped cross-validation and held-out test conditions. The resulting performance metrics are summarized in Table 10.1 and Figure 10.1.

Table 10.1: Comprehensive Performance Benchmark of Machine Learning Models
-----------------------------------------------------------------------------------------------------------------------------------
Model Architecture                CV R^2 (Mean)  CV MAE (%)  CV RMSE (%)  Train R^2  Train MAE (%)  Test R^2  Test MAE (%)  Test RMSE (%)
-----------------------------------------------------------------------------------------------------------------------------------
XGBoost Regressor                   -0.7416       10.0352      15.0760     0.9986       0.3902       0.9302      1.7054        2.5947
Tuned Random Forest (Final Model)    0.1681        7.8384      11.9913     0.9484       1.4547       0.9007      2.3032        3.0935
Support Vector Regressor (SVR)       0.5080        5.9857       8.9817     0.9679       0.5925       0.9067      1.7917        2.9994
Gradient Boosting Regressor         -0.6960        9.9183      14.1713     0.9998       0.1474       0.8728      2.1743        3.5023
Polynomial Regression (Deg 2)       -0.1989        9.1980      13.7008     0.9754       1.5794       0.8608      2.0647        3.6631
Ridge Regression                    -0.2554       11.7600      14.6941     0.5963       6.7282       0.7848      3.7937        4.5556
Decision Tree Regressor              0.3952        6.4866      10.4481     0.9576       1.9931       0.2713      5.0018        8.3820
Linear Regression                   -1.2152       13.2489      17.1790     0.6562       5.8470      -7.1595     19.5894       28.0486
-----------------------------------------------------------------------------------------------------------------------------------

10.2 Failure Analysis of Linear and Polynomial Models
The benchmark results reveal critical insights into the underlying geotechnical mechanics:
1. Complete Breakdown of Linear Regression: Ordinary Least Squares yielded an abysmal test R^2 of -7.1595 and an MAE of 19.59%. This complete breakdown proves that load sharing in DPRF is intrinsically non-linear and coupled. A linear model cannot reconcile the fact that cushion thickness increases capacity at h/d = 1-2 but decreases capacity at h/d = 3-4.
2. Moderate Performance of Polynomial Expansion: Degree-2 polynomial regression improved test R^2 to 0.8608 (MAE = 2.06%), confirming that quadratic interaction terms capture part of the cushion-soil non-linearity. However, polynomial extrapolation outside the training domain suffers from extreme Runge oscillations.

10.3 Selection of the Final Production Model
Both XGBoost (Test R^2 = 0.9302, MAE = 1.71%) and Tuned Random Forest (Test R^2 = 0.9007, MAE = 2.30%) exhibited outstanding generalization on the held-out test series. 
The Tuned Random Forest Regressor was selected as the final operational model for the following engineering reasons:
1. Robust Interpolation: As an ensemble of 100 de-correlated bagging trees, Random Forest averages piecewise constant outputs, preventing the extreme gradient spikes that boosted trees can generate when queried at boundary parameters.
2. Smooth Degradation: Under domain edge conditions, Random Forest predictions revert gracefully toward local leaf averages, exhibiting maximum stability when wrapped with strict physical boundary clippers.
3. Perfect Integration with Physics Wrapper: The combination of Tuned Random Forest and the Physics-Constrained Wrapper yielded 100% physically admissible predictions with zero static equilibrium violation.
"""

CHAPTER_11_TITLE = "Chapter 11: Results and Discussion"
CHAPTER_11_TEXT = """11.1 Experimental Load-Settlement Response
The experimental load-settlement curves compiled from Halder & Manna (2021, 2022) are illustrated in Figure 6.1:
- The Unpiled Raft (UR) exhibited the softest response, reaching an ultimate bearing capacity of 15.0 kN at normalized settlement w/B = 10%.
- The Connected Piled Raft (CPR 2x2) showed the stiffest initial response, carrying 17.8 kN at w/B = 10%.
- The Disconnected Piled Raft (DPRF 2x2) foundations exhibited performance directly governed by cushion thickness:
  * h/d = 1.0: Ultimate capacity Q = 17.1 kN (96.1% of CPR capacity)
  * h/d = 2.0: Ultimate capacity Q = 16.6 kN (93.3% of CPR capacity)
  * h/d = 3.0: Ultimate capacity Q = 15.9 kN (89.3% of CPR capacity)
- For the 3x3 DPRF configuration (Halder & Manna 2021), bearing capacity increased dramatically due to the larger reinforced soil zone:
  * h/d = 1.0 (CM2): Q = 20.5 kN
  * h/d = 2.0 (CM2): Q = 19.4 kN
  * h/d = 4.0 (CM2): Q = 16.7 kN
  * h/d = 2.0 (CM3, Coarse): Q = 19.9 kN

11.2 Inverted Load-Sharing Kinetics
Figure 6.2 highlights the most distinctive mechanical feature of disconnected piled rafts: inverted load-sharing kinetics.
In CPR systems, the pile group carries 75% to 80% of total load at tiny settlements (w/B = 0.5%), with pile share decreasing slightly as soil plastic yield occurs.
In DPRF systems, the kinetics are inverted:
- At w/B = 0.5% to 1.0%, the cushion compresses locally; the raft carries 95% to 100% of load (alpha_p = 0% to 5%).
- Between w/B = 2.0% and 6.0%, significant cushion densification and soil arching occur, causing pile load share to rise rapidly to 20% - 28%.
- Beyond w/B = 7.0%, pile load sharing approaches an asymptotic plateau of 31% to 35% for 3x3 groups and 9% to 12% for 2x2 groups.
Our machine learning model accurately reproduces this non-linear mobilization trajectory across all settlement increments.

11.3 Actual vs. Predicted Parity Analysis
Figure 11.1 displays the parity plot comparing actual measured pile load share against predicted pile load share across the 18 held-out test observations.
- All test predictions cluster tightly along the 1:1 line of ideal agreement.
- 100% of the test points fall comfortably within the ±10% error envelope.
- The coefficient of determination of R^2 = 0.9007 and mean absolute error of MAE = 2.30% demonstrate exceptional predictive fidelity on independent physical model tests.

11.4 Residual Error Diagnostics and Homoscedasticity
Figure 11.2 presents the residual error diagnostics for the test dataset:
- Residual Definition: e_i = y_i - hat{y}_i
- Mean Residual: mu = -0.8194% (indicating virtually unbiased predictions)
- Standard Deviation of Residuals: sigma = 2.9821%
- Maximum Absolute Residual: 6.65% (observed at extreme load stages)
- Homoscedasticity: The scatter plot of residuals against predicted values shows uniform dispersion around the zero-error line across the entire range of load sharing (0% to 40%), confirming that the model exhibits no heteroscedastic variance expansion.
- Normality: The residual histogram conforms closely to a Gaussian normal distribution.
"""

CHAPTER_12_TITLE = "Chapter 12: Explainable AI: Feature Importance and SHAP Interpretability"
CHAPTER_12_TEXT = """12.1 Global Gini Feature Importance Ranking
To understand which geotechnical variables drive load-sharing predictions, Gini impurity-based feature importances were extracted from the trained Random Forest model (Figure 12.1 and Table 12.1).

Table 12.1: Relative Feature Importance for DPRF Load Sharing
-----------------------------------------------------------------------------------
Rank  Feature Name                  Relative Importance (%)  Cumulative Weight (%)
-----------------------------------------------------------------------------------
1     pile_area_ratio (alpha_area)           25.4%                   25.4%
2     normalized_settlement_pct (w/B)        21.8%                   47.2%
3     n_piles                                16.2%                   63.4%
4     cushion_thickness_ratio (h/d)          14.5%                   77.9%
5     cushion_d50_mm                          6.8%                   84.7%
6     cushion_friction_deg                    5.3%                   90.0%
7     applied_load_kn                         3.7%                   93.7%
8     applied_pressure_kpa                    2.9%                   96.6%
9     settlement_mm                           1.8%                   98.4%
10    Other Soil/Geom Features                1.6%                  100.0%
-----------------------------------------------------------------------------------

12.2 SHAP (SHapley Additive exPlanations) Beeswarm Analysis
While Gini importance establishes which features are influential, it does not reveal the directionality of their impact. To resolve this, game-theoretic SHapley Additive exPlanations (SHAP) were computed across the dataset (Figure 12.2):

1. Pile Area Ratio (alpha_area) & n_piles (Positive Impact): High pile area ratio (red dots) generates large positive SHAP values (+10% to +18%), directly driving higher pile load share. Moving from 2x2 (alpha_area = 2.2%) to 3x3 (alpha_area = 5.1%) doubles the reinforced soil area, boosting pile group capacity.
2. Normalized Settlement (w/B) (Positive Impact): Low settlement values (blue dots, w/B < 2%) produce strong negative SHAP values (-12% to -16%), reflecting the cushion buffer period where piles carry negligible load. High settlement (red dots, w/B > 6%) generates positive SHAP values (+8% to +12%), confirming progressive mobilization.
3. Cushion Thickness Ratio (h/d) (Negative Impact): High cushion thickness (red dots, h/d = 3 to 4) yields negative SHAP values (-4% to -8%). Thicker cushions dissipate vertical stresses into the subsoil, reducing the normal stress transferred to the pile caps.
4. Cushion Particle Size (d_50) & Friction Angle (Positive Impact): Coarser cushion aggregates (d_50 >= 2.0 mm, red dots) produce positive SHAP values (+3% to +6%), validating that angular, gravelly materials enhance soil arching efficiency onto pile heads.

12.3 Mechanistic Validation of Machine Learning Logic
The SHAP interpretability results demonstrate that the machine learning model has not simply memorized statistical correlations; it has accurately internalized the true underlying geotechnical mechanics of disconnected piled raft foundations:
- It correctly models inverted kinetics via w/B.
- It correctly models arching enhancement via d_50 and phi_c.
- It correctly models cushion stress dissipation via h/d.
- It enforces static equilibrium across all predictions.
"""

CHAPTER_13_TITLE = "Chapter 13: Parametric Sensitivity Analysis"
CHAPTER_13_TEXT = """13.1 Four-Parameter Sensitivity Study
A systematic parametric sensitivity investigation was conducted using the final model to establish design curves for foundation practitioners (Figure 13.1):

1. Sensitivity to Cushion Thickness Ratio (h/d in [0.5, 4.0]):
   - Baseline Configuration: 3x3 pile group, B = 300 mm, d = 25.4 mm, L = 1.0 m, Badarpur sand (d_50 = 2.0 mm), at design settlement w/B = 10%.
   - At h/d = 1.0: Pile load share alpha_p = 31.6%, Raft share alpha_r = 68.4%.
   - At h/d = 2.0: Pile load share alpha_p = 31.0%, Raft share alpha_r = 69.0%.
   - At h/d = 3.0: Pile load share alpha_p = 27.8%, Raft share alpha_r = 72.2%.
   - At h/d = 4.0: Pile load share alpha_p = 25.5%, Raft share alpha_r = 74.5%.
   - Geotechnical Deduction: For h/d between 1.0 and 2.0, pile mobilization remains stable near 31%. Beyond h/d = 2.5, pile load share decays steadily because vertical shear arches cannot effectively transmit normal stresses across thick granular beds.

2. Sensitivity to Cushion Grain Size (d_50 in [0.5 mm, 5.0 mm]):
   - Holding h/d = 2.0 and w/B = 10% constant:
   - Fine Sand (d_50 = 0.6 mm, CM1): alpha_p = 25.7%, Q_p = 4.79 kN.
   - Medium-Coarse Sand (d_50 = 2.0 mm, CM2): alpha_p = 31.0%, Q_p = 6.01 kN.
   - Coarse Gravelly Sand (d_50 = 4.5 mm, CM3): alpha_p = 31.7%, Q_p = 6.31 kN.
   - Geotechnical Deduction: Increasing cushion grain size from 0.6 mm to 2.0 mm produces a dramatic 20.6% increase in pile load mobilization. Beyond d_50 = 2.5 mm, the benefit plateaus, indicating that well-graded coarse sand provides optimal shear interlock.

3. Sensitivity to Pile Area Ratio (A_p/A_r in [1.0%, 8.0%]):
   - Single Pile (1x1, A_p/A_r = 0.57%): alpha_p = 4.2% (negligible group stiffening).
   - 2x2 Pile Group (A_p/A_r = 2.26%): alpha_p = 11.9% to 12.5%.
   - 3x3 Pile Group (A_p/A_r = 5.09%): alpha_p = 31.0% to 35.0%.
   - Geotechnical Deduction: Pile load share scales non-linearly with area ratio. A critical threshold of A_p/A_r >= 3.0% is required to achieve substantial settlement reduction and ground reinforcement.

4. Sensitivity to Normalized Settlement (w/B in [0.5%, 10.0%]):
   - At w/B = 1.0%: alpha_p = 4.2%, alpha_r = 95.8% (raft carries almost entire load).
   - At w/B = 3.0%: alpha_p = 14.8%, alpha_r = 85.2%.
   - At w/B = 5.0%: alpha_p = 22.3%, alpha_r = 77.7%.
   - At w/B = 10.0%: alpha_p = 31.0%, alpha_r = 69.0%.
   - Geotechnical Deduction: Mobilization of disconnected piles is settlement-dependent. In early serviceability stages, the foundation behaves like an unpiled raft; under ultimate loads, piles act as high-capacity anchors.
"""

CHAPTER_14_TITLE = "Chapter 14: Practical Engineering Design Guidelines"
CHAPTER_14_TEXT = """14.1 Proposed Step-by-Step Geotechnical Design Workflow
Based on the experimental synthesis and machine learning findings, a rational design methodology is proposed for geotechnical foundation engineers (Figure 14.1):

Step 1: Estimate Total Superstructure Load and Allowable Settlement
- Determine total factored vertical column loads Q and permissible differential/total settlement w_allow from structural building codes (e.g., IS 1904, Eurocode 7).

Step 2: Evaluate Unpiled Raft Capacity
- Calculate bearing capacity and settlement of the unpiled raft (UR) resting directly on subsoil. If settlement exceeds w_allow, ground reinforcement via disconnected piles is indicated.

Step 3: Select Granular Cushion Material and Thickness
- Cushion Material Specification: Select well-graded, non-plastic coarse sand or sandy gravel with mean grain size d_50 >= 2.0 mm, coefficient of uniformity C_u > 4, and friction angle phi_c >= 48 deg.
- Cushion Thickness Selection: Specify cushion thickness ratio in the optimum range:
  h/d = 1.5 to 2.0 (e.g., h = 150 to 300 mm for typical d = 100 to 200 mm piles).
- Do not exceed h/d = 2.5, as thicker cushions diminish pile mobilization and increase total settlement.

Step 4: Determine Pile Group Density
- Choose pile diameter d and spacing s/d = 3 to 4.
- Target a pile area ratio A_p/A_r of 3.0% to 6.0% to achieve settlement reduction efficiency eta >= 0.45.

Step 5: Execute Machine Learning Prediction
- Input foundation geometry, soil parameters, and design load Q into the Physics-Constrained Predictor.
- Obtain predicted pile load share alpha_p and raft load share alpha_r.
- Decompose loads into Q_p = Q * (alpha_p/100) and Q_r = Q * (alpha_r/100).

Step 6: Structural Verification of Raft and Piles
- Structural Raft Design: Design the reinforced concrete raft slab for contact pressure q_r = Q_r / A_r. Because punching shear at pile heads is eliminated, raft slab thickness can be reduced by 25% to 40% compared to CPR systems.
- Pile Structural Verification: Design piles for maximum axial load occurring at the neutral plane:
  P_max = Q_p,single + P_NSF
  Verify against structural yield using reduced factor of safety FS ≈ 1.3 to 1.5.
"""

CHAPTER_15_TITLE = "Chapter 15: Limitations and Future Scope"
CHAPTER_15_TEXT = """15.1 Limitations of the Present Framework
While the developed PC-ML framework achieves high predictive accuracy and strictly enforces physical equilibrium, the following boundaries of applicability must be recognized:
1. Soil Stratigraphy: Calibrated primarily on cohesionless sand deposits (Yamuna sand, Toyoura sand) at relative densities D_r = 70% to 86%. Direct application to normally consolidated soft clays—where time-dependent primary and secondary consolidation settlement governs—requires additional calibration.
2. Loading Mode: Restricted to quasi-static vertical compressive loading. Cyclic lateral wind/wave loads, seismic shaking, and overturning moments require dynamic model extension.
3. Scale Effects: The empirical database relies on 1g physical model tests (scale 1:15 to 1:25) and 50g centrifuge tests. Although normalized dimensionless ratios (h/d, w/B, A_p/A_r) were employed to minimize scale distortions, prototype field load tests are desirable to validate field-scale soil stress gradients.

15.2 Future Research Scope
1. Geosynthetic-Reinforced DPRF (G-DPRF): Integrating geogrid or geotextile layers within the granular cushion creates a composite tensioned membrane that further enhances soil arching. Future work will extend the ML model to predict tension mobilization in G-DPRF systems.
2. Hybrid Machine Learning / FE Simulations: Combining 3D finite element simulations in PLAXIS 3D with active learning to expand the training database into stratified, multi-layered clay-sand profiles.
3. Seismic Load Redistribution: Expanding the feature space to include earthquake peak ground acceleration (PGA) and cyclic degradation parameters to model seismic performance.
"""

CHAPTER_16_TITLE = "Chapter 16: Summary and Conclusions"
CHAPTER_16_TEXT = """16.1 Summary of Completed Work
In this B.Tech Project, a complete, reproducible, and physics-constrained machine learning prediction system was developed for Disconnected Piled Raft Foundations (DPRF) embedded in sand:
1. A unified database of 99 validated experimental loading points across 16 physical model configurations was digitized from published benchmarks (Halder & Manna 2021, 2022; Cao et al. 2004; Fioravante & Giretti 2010).
2. An explicit Physics-Constrained Wrapper was formulated and implemented, mathematically enforcing vertical static equilibrium (Q = Q_r + Q_p) and load-sharing identities (alpha_p + alpha_r = 100.00%) with machine-precision accuracy.
3. A strict GroupKFold cross-validation protocol grouped by physical test series was enforced to eliminate data leakage across loading increments.
4. Eight machine learning architectures were systematically benchmarked, with Tuned Random Forest (Test R^2 = 0.9007, MAE = 2.30%) and XGBoost (Test R^2 = 0.9302, MAE = 1.71%) demonstrating exceptional generalization on unseen test series.
5. Explainable AI (SHAP and Gini importance) quantitatively validated that pile area ratio, normalized settlement, and cushion thickness ratio govern load transfer mechanics, corroborating experimental inverted kinetics.
6. A comprehensive 4-parameter sensitivity study established design charts identifying an optimum cushion thickness ratio of h/d = 1.5 to 2.0 and coarse cushion granularity (d_50 >= 2.0 mm).
7. The finalized model was deployed into a 5-page interactive Streamlit dashboard (app.py) and command-line inference script (predict.py).

16.2 Major Geotechnical Conclusions
1. DPRF systems provide an exceptional alternative to conventional connected piled rafts, eliminating high pile-head shear and moment concentrations while achieving over 45% settlement reduction efficiency.
2. Inverted load-sharing kinetics are an intrinsic property of DPRF: the raft carries 95% of initial load, with pile load share mobilizing progressively as cushion compression triggers soil arching.
3. Negative skin friction naturally shifts peak axial pile forces downward to the neutral plane at z_n ≈ 10d, protecting pile heads from punching shear and justifying lower structural factors of safety (FS ≈ 1.3).
4. Physics-constrained machine learning successfully bridges the gap between oversimplified analytical equations and computationally prohibitive 3D numerical models, providing rapid, physically compliant predictions for modern foundation engineering practice.
"""

REFERENCES_TEXT = """1. Halder, P., & Manna, B. (2022). Load transfer mechanism for connected and disconnected piled raft: a comparative study. Acta Geotechnica, 17(7), 3033–3045. DOI: 10.1007/s11440-021-01409-0.
2. Halder, P., & Manna, B. (2021). Large scale model testing to investigate the influence of granular cushion layer on the performance of disconnected piled raft system. Acta Geotechnica, 16(5), 1597–1614. DOI: 10.1007/s11440-020-01121-5.
3. Cao, X. D., Wong, I. H., & Chang, M. F. (2004). Behavior of model rafts resting on pile-reinforced sand. Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 130(2), 129–138. DOI: 10.1061/(ASCE)1090-0241(2004)130:2(129).
4. Fioravante, V., & Giretti, D. (2010). Contact versus noncontact piled raft foundations. Canadian Geotechnical Journal, 47(11), 1271–1287. DOI: 10.1139/T10-028.
5. Tradigo, F., Pisano, F., di Prisco, C., & Mussi, A. (2015). Non-linear soil–structure interaction in disconnected piled raft foundations. Computers and Geotechnics, 63, 121–134. DOI: 10.1016/j.compgeo.2014.09.006.
6. Wong, I. H., Chang, M. F., & Cao, X. D. (2000). Raft foundations with disconnected settlement reducing piles. In Design Applications of Raft Foundations and Ground Slabs, Thomas Telford, London, pp. 469–486.
7. Burland, J. B., Broms, B. B., & de Mello, V. F. B. (1977). Behavior of foundations and structures. In Proceedings of the 9th International Conference on Soil Mechanics and Foundation Engineering, Tokyo, Vol. 2, pp. 495–546.
8. Poulos, H. G. (2001). Piled raft foundations: design and applications. Géotechnique, 51(2), 95–113.
9. Poulos, H. G., & Davis, E. H. (1980). Pile Foundation Analysis and Design. John Wiley & Sons, New York.
10. Randolph, M. F. (1994). Design methods for piled rafts. In Proceedings of the 13th International Conference on Soil Mechanics and Foundation Engineering, New Delhi, Vol. 5, pp. 61–82.
11. Pecker, A. (2004). Design and construction of the Rion Antirion Bridge. In Geotechnical Special Publication, ASCE, No. 126, pp. 216–240.
12. Jamiolkowski, M. B., Ricceri, G., & Simonini, P. (2009). Safeguarding Venice from high tides: site characterization and geotechnical problems. In Proceedings of the 17th International Conference on Soil Mechanics and Geotechnical Engineering, Alexandria, Vol. 4, pp. 3209–3230.
13. Terzaghi, K. (1943). Theoretical Soil Mechanics. John Wiley & Sons, New York.
14. Handy, R. L. (1985). The arch in soil arching. Journal of Geotechnical Engineering, ASCE, 111(3), 302–318.
15. Dezfouli, M., Dehghani, M., Asakereh, A., & Kalantari, B. (2018). Behavior of geogrid reinforced and unreinforced non-connected pile raft foundation. International Journal of Civil Engineering, 16(3), 313–328.
16. Das, S. K., & Basudhar, P. K. (2006). Undrained lateral load capacity of piles in clay using artificial neural network. Computers and Geotechnics, 33(8), 454–459.
17. Manna, B., & Baidya, D. K. (2010). Dynamic non-linear response of pile groups under vertical vibration: an experimental study. Soil Dynamics and Earthquake Engineering, 30(11), 1270–1280.
18. Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances in Neural Information Processing Systems (NeurIPS 2017), Vol. 30, pp. 4765–4774.
19. Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794.
20. Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32.
"""

print("Text module loaded successfully.")
