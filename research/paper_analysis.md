# Research Paper Comparative Analysis: Disconnected Piled Raft Foundations (DPRF)

## 1. Primary Experimental References

### Paper 1: Halder & Manna (2022)
- **Title**: *Load transfer mechanism for connected and disconnected piled raft: a comparative study*
- **Journal**: *Acta Geotechnica* (2022) 17:3033–3045
- **DOI**: 10.1007/s11440-021-01409-0
- **Authors**: Prasun Halder, Bappaditya Manna (Department of Civil Engineering, IIT Delhi, India)
- **Experimental Setup**:
  - Test tank: $2.0\text{ m} \times 2.0\text{ m} \times 1.8\text{ m}$ mild steel tank on strong floor.
  - Scale effects: $d/d_{50} = 25.4 / 0.3 = 84.7 > 50$, well above scale effect threshold.
  - Subsoil: Yamuna Sand (YS), poorly graded sand (SP), $d_{50} = 0.3\text{ mm}$, $C_u = 2.13$, $C_c = 1.1$, $G_s = 2.65$, $\gamma_{d,\min} = 13.8\text{ kN/m}^3$, $\gamma_{d,\max} = 16.8\text{ kN/m}^3$, $\phi = 40.7^\circ$, $c = 0$, $D_r = 70\%$.
  - Granular Cushion: Badarpur Sand (BS), $d_{50} = 0.6\text{ mm}$, $\phi = 47^\circ$, $c = 0$, $D_r = 70\%$, $\gamma_{d,\max} = 17.0\text{ kN/m}^3$.
  - Foundation Model:
    - Model Raft: Square aluminum plate $B = 300\text{ mm}$, thickness $t_r = 25\text{ mm}$ ($E = 69,230\text{ MPa}$, $\nu = 0.33$). Represents prototype $B = 4.65\text{ m}$, $t = 0.388\text{ m}$ (scaling factor $n = 15.5$).
    - Model Piles: Aluminum pipe $d = 25.4\text{ mm}$, thickness $t = 2\text{ mm}$, length $L = 1.0\text{ m}$ ($L/d \approx 40$).
    - Configuration: $2 \times 2$ pile group ($n_p = 4$), spacing $s = 3d = 76.2\text{ mm}$.
    - Cushion thicknesses: $h/d = 1$ ($25.4\text{ mm}$), $h/d = 2$ ($50.8\text{ mm}$), $h/d = 3$ ($76.2\text{ mm}$).
  - Comparative Baseline: Unpiled Raft (UR: $300\times 300\times 25\text{ mm}$), Isolated Single Pile (ISP: $1\times 1$), Connected Piled Raft ($2 \times 2$ CPR).
  - Loading: Static vertical displacement-controlled test at $0.02\text{ mm/s}$ up to $w = 30\text{ mm}$ ($w/B = 10\%$).

### Paper 2: Halder & Manna (2021)
- **Title**: *Large scale model testing to investigate the influence of granular cushion layer on the performance of disconnected piled raft system*
- **Journal**: *Acta Geotechnica* (2021) 16:1597–1614
- **DOI**: 10.1007/s11440-020-01121-5
- **Authors**: Prasun Halder, Bappaditya Manna (Department of Civil Engineering, IIT Delhi, India)
- **Experimental Setup**:
  - Foundation: Raft $B = 300\text{ mm}$, $t_r = 25\text{ mm}$; Piles $d = 25.4\text{ mm}$, $L = 1.0\text{ m}$.
  - Soil Bed: Yamuna sand (YS, $d_{50} = 0.3\text{ mm}$, $\phi = 40.7^\circ$, $D_r = 70\%$).
  - Configurations Tested:
    - Unpiled Raft (UR)
    - $1 \times 1$ Piled Raft (PR - connected)
    - $1 \times 1$ Disconnected Piled Raft (DPR, $h/d = 2$, CM2)
    - $3 \times 3$ Disconnected Piled Raft ($n_p = 9$, $s/d = 3$) with varying cushion thickness: $h/d \in \{1, 2, 3, 4\}$ (CM2).
    - $3 \times 3$ Disconnected Piled Raft ($n_p = 9$, $s/d = 3$, $h/d = 2$) with varying cushion materials:
      - CM1: $d_{50} = 0.6\text{ mm}$, $\phi = 47^\circ$, $\gamma_d = 17.0\text{ kN/m}^3$
      - CM2: $d_{50} = 2.0\text{ mm}$, $\phi = 51^\circ$, $\gamma_d = 17.5\text{ kN/m}^3$
      - CM3: $d_{50} = 4.5\text{ mm}$, $\phi = 56^\circ$, $\gamma_d = 18.2\text{ kN/m}^3$
  - Instrumentation: 5 electrical resistance strain gauges per pile at $0.01L, 0.25L, 0.50L, 0.75L, 0.99L$ to determine axial loads and unit skin friction.

---

## 2. Secondary & Literature Benchmark Studies

1. **Wong, Chang & Cao (2000)** / **Cao, Wong & Chang (2004)**:
   - Evaluated model rafts on pile-reinforced sand bed. First experimental demonstration that disconnecting piles reduces pile head stress concentration and differential settlement.
   - Piles function primarily as settlement-reducing structural reinforcement.
2. **Fioravante & Giretti (2010)**:
   - Centrifuge tests on connected vs. non-connected piled rafts ($3 \times 3$, $h/d = 1.8$).
   - Confirmed load transfer mechanics through interposed granular cushion and mobilized base resistance.
3. **Tradigo, Pisano, di Prisco & Mussi (2015)**:
   - Non-linear 3D finite element simulation of DPRF with $h/d = 1$ and $h/d = 2$.
   - Validated settlement efficiency ($\eta$) trends and non-uniform contact stress distribution.
4. **Dezfouli, Dehghani, Asakereh & Kalantari (2018)**:
   - 1g tests on non-connected pile rafts with and without geogrid-reinforced cushion layer.

---

## 3. Consolidated Comparison Table

| Investigation | Test Type | Soil Type | Cushion Material ($d_{50}$, $\phi$) | Pile Group ($n_p$) | $s/d$ | $L/d$ | $h/d$ | Capacity at $w/B=10\%$ | Pile Share $\alpha_p$ (%) | Raft Share $\alpha_r$ (%) |
|---|---|---|---|---|---|---|---|---|---|---|
| **Halder & Manna (2022)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | Badarpur sand ($0.6\text{ mm}, 47^\circ$) | $2 \times 2$ DPR ($n_p=4$) | 3.0 | 39.4 | 1.0 | 17.1 kN | 9.5% | 90.5% |
| **Halder & Manna (2022)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | Badarpur sand ($0.6\text{ mm}, 47^\circ$) | $2 \times 2$ DPR ($n_p=4$) | 3.0 | 39.4 | 2.0 | 16.6 kN | 8.6% | 91.4% |
| **Halder & Manna (2022)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | Badarpur sand ($0.6\text{ mm}, 47^\circ$) | $2 \times 2$ DPR ($n_p=4$) | 3.0 | 39.4 | 3.0 | 15.9 kN | 7.8% | 92.2% |
| **Halder & Manna (2022)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | N/A (Rigid connection) | $2 \times 2$ CPR ($n_p=4$) | 3.0 | 39.4 | 0.0 | 17.8 kN | 20.2% | 79.8% |
| **Halder & Manna (2022)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | None (Unpiled) | Raft only ($n_p=0$) | - | - | - | 15.0 kN | 0.0% | 100.0% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM2 ($2.0\text{ mm}, 51^\circ$) | $3 \times 3$ DPR ($n_p=9$) | 3.0 | 39.4 | 1.0 | 20.5 kN | 35.0% | 65.0% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM2 ($2.0\text{ mm}, 51^\circ$) | $3 \times 3$ DPR ($n_p=9$) | 3.0 | 39.4 | 2.0 | 19.4 kN | 34.8% | 65.2% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM2 ($2.0\text{ mm}, 51^\circ$) | $3 \times 3$ DPR ($n_p=9$) | 3.0 | 39.4 | 3.0 | 18.0 kN | 33.0% | 67.0% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM2 ($2.0\text{ mm}, 51^\circ$) | $3 \times 3$ DPR ($n_p=9$) | 3.0 | 39.4 | 4.0 | 16.7 kN | 29.0% | 71.0% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM1 ($0.6\text{ mm}, 47^\circ$) | $3 \times 3$ DPR ($n_p=9$) | 3.0 | 39.4 | 2.0 | 18.6 kN | 30.0% | 70.0% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM3 ($4.5\text{ mm}, 56^\circ$) | $3 \times 3$ DPR ($n_p=9$) | 3.0 | 39.4 | 2.0 | 19.9 kN | 36.0% | 64.0% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | CM2 ($2.0\text{ mm}, 51^\circ$) | $1 \times 1$ DPR ($n_p=1$) | - | 39.4 | 2.0 | 15.6 kN | 4.4% | 95.6% |
| **Halder & Manna (2021)** | 1g Physical Model | Dense sand ($\phi=40.7^\circ$) | N/A (Rigid connection) | $1 \times 1$ PR ($n_p=1$) | - | 39.4 | 0.0 | 16.4 kN | 6.8% | 93.2% |

---

## 4. Key Engineering Findings and Research Gaps

### Key Influencing Parameters:
1. **Number of Piles ($n_p$) and Group Density ($A_{\text{piles}}/A_{\text{raft}}$)**: Increasing $n_p$ from 4 ($2 \times 2$) to 9 ($3 \times 3$) dramatically increases pile load share from $\sim 8.6\%$ to $\sim 35\%$, as a broader zone of subsoil is reinforced.
2. **Cushion Thickness Ratio ($h/d$)**: Increasing cushion thickness causes greater lateral dispersion of applied vertical stress into the inter-pile subsoil, reducing load concentration on the pile heads and slightly lowering overall capacity and settlement efficiency $\eta$.
3. **Cushion Granularity ($d_{50}$) & Friction Angle ($\phi_{\text{cushion}}$)**: A coarser, higher-interlock cushion ($d_{50} \ge 2\text{ mm}$, $\phi \ge 51^\circ$) provides higher shear stiffness and more efficient load transfer into the pile heads, yielding up to a 130% increase in settlement efficiency compared to finer sand ($d_{50} = 0.6\text{ mm}$).
4. **Normalized Settlement ($w/B$)**: In DPRF, the raft takes 90–98% of the load at small strains ($w/B < 1\%$). Pile load contribution mobilizes gradually with settlement, leveling off around $w/B = 7–10\%$. This is the exact inverse of CPR behavior.

### Research Gaps Addressed by this Machine Learning System:
1. **Lack of Unified Predictive Framework**: Currently, geotechnical practitioners rely on expensive 3D FEM simulations or empirical charts specific to single cushion thicknesses.
2. **Multi-parameter Coupling**: Interaction between cushion thickness, cushion coarseness, pile group geometry, and settlement level is non-linear and coupled; ML can capture this multi-dimensional response accurately.
3. **Physical Law Enforcement**: Standard regression models violate static equilibrium ($Q \ne Q_r + Q_p$). This project establishes an engineering-constrained ML framework guaranteeing exact equilibrium and monotonic boundary conditions.
