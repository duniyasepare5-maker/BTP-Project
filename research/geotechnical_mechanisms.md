# Geotechnical Mechanics of Disconnected Piled Raft Foundations (DPRF)

## 1. Fundamentals of Piled Raft Systems

Piled raft foundations are hybrid geotechnical systems combining:
1. A shallow structural footing (the **raft** or mat) in direct contact with the upper soil stratum.
2. An array of slender deep elements (**piles**) extending into deeper soil layers.

### Conventional Connected Piled Rafts (CPR)
In a conventional CPR system:
- The piles are cast rigidly into or threaded into the base of the raft.
- **Kinematic Constraint**: At the raft-pile interface, the vertical displacement of the raft ($w_r$), pile head ($w_p$), and the underlying soil surface ($w_s$) must be equal:
  $$w_r = w_p = w_s$$
- **Load Mobilization**: Because structural piles are much stiffer than the surrounding soil, piles attract the majority of the superstructure load at very low settlement levels ($w/B < 0.5\%$, where $\alpha_p$ often exceeds $80\%$).
- **Structural Vulnerability**: This rigid connection induces high bending moments in the raft and severe axial and shear stress concentrations at the pile head. Under seismic or horizontal loads, shear failure at the pile-raft joint is a common failure mode. A high factor of safety ($FS \approx 3.0\text{--}4.0$) is required by design codes (e.g., BS 8004).

---

## 2. Disconnected Piled Raft Foundations (DPRF)

To overcome the structural vulnerabilities of CPR systems, Wong et al. (2000) proposed introducing an engineered granular cushion layer (or load transfer platform, LTP) between the raft base and the pile heads.

### Structural and Mechanics Differences
In a DPRF system:
1. **Structural Disconnection**: The piles do not touch the raft; a compacted granular layer of thickness $h$ is interposed.
2. **Soil Reinforcement Role**: Piles do not act as direct load-bearing columns; instead, they function as vertical ground reinforcement elements that stiffen the underlying subsoil.
3. **Reduced Pile Head Stress**: The cushion redistributes vertical stresses through arching and shear particle interlock, preventing concentrated punch loads on the pile heads. A lower factor of safety against pile structural failure ($FS \approx 1.3$) can safely be applied.

---

## 3. Load Transfer & Skin Friction Distribution

The presence of the granular cushion alters the relative displacement between pile shaft and surrounding soil:

### Relative Displacement & Negative Skin Friction
Under vertical loading:
- The granular cushion and the shallow subsoil compress significantly more than the stiff pile shafts ($w_s > w_p$) in the upper depth region.
- This downward movement of the surrounding soil relative to the pile mobilizes **negative skin friction** ($\tau_s < 0$) along the upper section of the pile shaft.
- Negative skin friction acts as a dragdown load on the pile, adding downward force rather than supporting the foundation.

### Neutral Plane & Maximum Axial Load Location
- As depth increases, the soil settlement decreases while pile strain accumulates. At a specific depth $z_n$ (the **neutral plane**), relative displacement becomes zero:
  $$\Delta w(z_n) = w_s(z_n) - w_p(z_n) = 0$$
- In the Halder & Manna (2021, 2022) experimental investigations:
  - For CPR: Positive skin friction exists along the entire pile length. The neutral plane is at the pile head ($z_n = 0$). Maximum axial load occurs at the pile head ($z = 0$).
  - For DPR: The neutral plane occurs at approximately $z_n \approx 0.25\text{ m} \approx 10d$ below the pile head.
  - Above $z_n$: Negative skin friction prevails (up to $\tau_s = -7.6\text{ kPa}$).
  - Below $z_n$: Positive skin friction prevails (up to $\tau_s = +11.2\text{ kPa}$).
  - **Key Phenomenon**: The maximum axial pile load does **not** occur at the pile head, but at the neutral plane ($z \approx 10d$), with peak axial loads of $532\text{ N}$ ($h/d=1$), $490\text{ N}$ ($h/d=2$), and $423\text{ N}$ ($h/d=3$).

---

## 4. Load Sharing Kinematics & Settlement Progression

### Inverted Load Sharing Curves
A critical insight demonstrated in the Halder & Manna papers is the complete inversion of load-sharing kinetics between CPR and DPRF:

- **Connected Piled Raft (CPR)**:
  - At early loading ($w/B < 0.75\%$): Piles take $80\text{--}95\%$ of the load.
  - As settlement reaches the plastic mobilization threshold ($w/d \approx 10\%$), pile shaft resistance yields, and the raft increasingly bears subsequent load increments.
  - At $w/B = 10\%$: $\alpha_p = 20.2\%$, $\alpha_r = 79.8\%$.

- **Disconnected Piled Raft (DPRF)**:
  - At early loading ($w/B < 1\%$): The granular cushion compresses and cushions the pile heads. The raft directly bears the vast majority of load on the cushion and subsoil ($\alpha_r \approx 96\text{--}100\%$, $\alpha_p \approx 0\text{--}4\%$).
  - As settlement increases ($w/B > 2\%$), the cushion densifies, load is transferred into the pile group through shear stresses and cushion arching, and the pile contribution steadily increases.
  - At $w/B = 7\text{--}10\%$: Load-sharing proportions reach a steady plateau. For $3 \times 3$ DPRF with optimum cushion ($h/d = 2$, CM2), $\alpha_p = 34.8\%$, $\alpha_r = 65.2\%$. For $2 \times 2$ DPRF, $\alpha_p = 8.6\%$, $\alpha_r = 91.4\%$.

---

## 5. Influence of Cushion Properties

### Cushion Thickness Ratio ($h/d$)
- Increasing $h/d$ increases the spatial diffusion zone of vertical stress from the raft.
- As $h/d$ increases from 1 to 4:
  - Axial load transferred to pile heads decreases monotonically.
  - The neutral plane moves deeper down the pile shaft.
  - Settlement efficiency ($\eta$) decreases from $0.44$ ($h/d=1$) to $0.14$ ($h/d=4$).
  - Optimum trade-off identified by Halder & Manna: $h/d = 2$ provides balanced settlement reduction without excessive cushion compressibility.

### Cushion Granularity ($d_{50}$) & Shear Strength ($\phi$)
- Three cushion materials were tested by Halder & Manna (2021):
  - CM1: $d_{50} = 0.6\text{ mm}$, $\phi = 47^\circ$
  - CM2: $d_{50} = 2.0\text{ mm}$, $\phi = 51^\circ$
  - CM3: $d_{50} = 4.5\text{ mm}$, $\phi = 56^\circ$
- Coarser cushion particles provide superior interlocking, higher stiffness, and greater shear strength.
- Settlement efficiency increases by over $130\%$ when transitioning from CM1 ($d_{50}=0.6\text{ mm}$, $\eta=0.14$) to CM2 ($d_{50}=2.0\text{ mm}$, $\eta=0.36$), leveling off at CM3 ($\eta=0.45$).
- Recommendation: Cushion material should have $d_{50} \ge 2.0\text{ mm}$ (approx. $d_{50,\text{cushion}} / d_{50,\text{soil}} \ge 6.7$).
