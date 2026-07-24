# Summary: 2026-07-21_19-25-44Z_EquilibriumCausalGames_Separation_Identification_a.md
Saved: 2026-07-24 01:24
Source: 2026-07-21_19-25-44Z_EquilibriumCausalGames_Separation_Identification_a.md
Model: None

---

## Summary  
The paper introduces an Equilibrium Causal Game (ECG) framework that models how feedback‑driven systems settle into unknown sensor states while allowing interventions to edit declared objects and recompute equilibria. Its primary contribution is a systematic analysis of which causal conclusions—specifically the identification of hidden latent variables \(B\) and their coupling matrix \(H\)—can be drawn from equilibrium data alone, under various assumptions about linearity, stationarity, and sensing structure. The authors demonstrate that separation (identifying \(H\)) is often incomplete or impossible for cyclic models with unknown wiring or full‑rank sensor maps, while identification of \((H,B)\) can be achieved only under strong non‑Gaussianity, well‑posed single‑target interventions, or specific structural constraints such as a single untargeted parent node. These findings clarify the limits of causal inference from equilibrium observations and guide experimental design.

## Key Contributions  
- [Finding 1] ECG‑separation is sound but incomplete for cyclic latent states; back‑door/half‑trek routes identify observed queries, yet unknown sensing introduces a separate ambiguity that prevents full identification.  
- [Finding 2] In passive stable linear models without self‑effects, unknown wiring and full‑rank unknown sensing leave the block matrix \(B\) completely unidentified for dimensions \(d \ge 2\). However, under LiNG (linearity of non‑Gaussianity) conditions, mechanism interventions separate sensing from interactions.  
- [Finding 3] For a set of \(d\) targets, exactly \(d-1\) are sufficient to identify \((H,B)\) only when the sole untargeted node directly parents all others; otherwise \(d\) targets are required.

## Methodology  
The authors construct a cyclic causal model comprising hidden latent states \(B\), a coupling matrix \(H\), and a sensor map that maps observed outputs to these states. They then formulate an equilibrium Causal Game where interventions modify declared objects, recompute the equilibrium, and generate data. The analysis proceeds through theoretical derivations of separation and identification conditions, sensitivity analyses under different assumptions (linearity, stationarity, positivity), and enumeration of minimal target sets required for full reconstruction.

## Results  
Theoretical results show that without additional structure, \(B\) cannot be uniquely identified; only the source‑frame rotation is recoverable. When LiNG holds, interventions eliminate the ambiguity between sensing and interaction effects. The identification problem reduces to a combinatorial one: either \(d-1\) or \(d\) targets suffice depending on parent‑child relationships among nodes. Known wiring provides no universal count of required probes; acquisition probes are excluded from the model.

## Significance  
Understanding these limits is crucial for designing robust causal inference protocols in complex feedback systems such as power grids, markets, and population dynamics where hidden states influence observed sensors. The paper offers a principled guide on when equilibrium data alone suffice versus when targeted experiments are necessary to break residual ambiguities.

## Related Concepts  
- Equilibrium Causal Game (ECG) framework  
- Back‑door/half‑trek identification routes  
- LiNG (linearity of non‑Gaussianity) condition  
- Source‑frame rotation ambiguity  
- Block matrix \(B\) and coupling matrix \(H\)  
- Single‑target interventions  
- Unknown wiring and full‑rank sensing  
- Minimal target set enumeration
