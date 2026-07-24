# Summary: 2026-07-21_19-25-44Z_EquilibriumCausalGames_Separation_Identification_a.md
Saved: 2026-07-24 01:14
Source: 2026-07-21_19-25-44Z_EquilibriumCausalGames_Separation_Identification_a.md
Model: None

---

## Summary  
The paper investigates how causal conclusions can be drawn from equilibrium data in systems where latent states evolve cyclically and are observed through imperfect sensors. By formalising an **Equilibrium Causal Game (ECG)** that couples game dynamics, hidden inputs, sensor maps, and intervention rules, the authors analyse when the system is *separable* (i.e., distinct variables can be distinguished) and when it is *identifiable* (i.e., the true parameters can be recovered). Their work shows that while some separation routes exist—such as back‑door or half‑trek paths—the identifiability of the full parameter set \((H,B)\) remains problematic under many realistic conditions, especially when unknown wiring and sensing are present. The study therefore delineates a taxonomy of which causal conclusions are supported by equilibrium data versus those that require targeted experiments.

## Key Contributions  
- [ECG‑separation is sound but incomplete; back‑door/half‑trek routes identify observed queries, yet full parameter identification fails for many cyclic models.]  
- [Under passive stable linear models with unknown wiring and full‑rank sensing, the block matrix \(B\) is completely unidentified when the number of latent variables \(d \ge 2\).]  
- [Non‑Gaussian sources (LiNG) eliminate source rotation ambiguity; mechanism interventions can separate sensing from interactions, allowing identification up to declared equivalence.]

## Methodology  
The authors construct a cyclic causal model where hidden states \(H\) are updated by feedback loops and observed through a sensor map \(\mathcal{S}\). They define *interventions* that edit declared objects (e.g., nodes or blocks) and recompute the equilibrium. Using concepts from structural equation modelling—such as back‑door, half‑trek, and LiNG (Linear Non‑Gaussian)—they assess separation routes and identify which queries are observable. The analysis proceeds in two regimes: passive linear models without self‑effects and active nonlinear sensing, exploring how assumptions on support, invariance, positivity, rank, and irreducibility affect identifiability.

## Results  
- In passive stable linear systems with unknown wiring and full‑rank sensing, the block \(B\) cannot be identified for any \(d \ge 2\); only a source‑frame rotation remains identifiable.  
- When non‑Gaussian sources are present (LiNG), the hidden rotation disappears, and mechanism interventions can separate sensing from interactions, yielding identification up to declared equivalence.  
- For passive models with unknown support, invariant sensing, aligned responses, and well‑posed single‑target interventions, the pair \((H,B)\) is identified only up to block permutation and blockwise coordinate changes; downstream mechanisms or sensor/interaction splits remain ambiguous.  
- Empirically, \(d-1\) targets suffice exactly when the sole untargeted node directly parents all others; otherwise \(d\) targets are required.

## Significance  
These results clarify which causal conclusions can be drawn from equilibrium data in complex feedback systems and highlight the need for targeted experiments to resolve hidden wiring or sensor ambiguities. By distinguishing between *separation* (observable query routes) and *identification* (recovering true parameters), the paper provides a principled framework for designing efficient observational strategies in applications such as power‑grid monitoring, market dynamics, and population interactions.

## Related Concepts  
- **Equilibrium Causal Game**: A model linking game dynamics with cyclic latent states.  
- **Cyclic Latent States**: Hidden variables that evolve through feedback loops.  
- **Back‑door / Half‑trek routes**: Standard separation concepts adapted to equilibrium settings.  
- **LiNG (Linear Non‑Gaussian)**: Assumption that non‑Gaussian sources remove source rotation ambiguity.  
- **Block matrix \(B\)**: Represents wiring between latent blocks; identifiability depends on model assumptions.
