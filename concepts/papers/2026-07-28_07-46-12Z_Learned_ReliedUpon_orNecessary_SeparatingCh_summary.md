# Summary: 2026-07-28_07-46-12Z_Learned_ReliedUpon_orNecessary_SeparatingCheckpoin.md
Saved: 2026-07-28 22:33
Source: 2026-07-28_07-46-12Z_Learned_ReliedUpon_orNecessary_SeparatingCheckpoin.md
Model: None

---

## Summary  
The paper investigates whether the learned restriction maps in sheaf graph neural networks (GNNs) are merely artifacts of checkpoint dependence, genuine task‑level improvements, or both. By introducing two estimands—checkpoint reliance and protocol‑relative replacement—the authors separate how a single checkpoint organizes edge assignments from how the rest of the model adapts. A theoretical “task‑null” theorem explains why these claims can diverge because labels only capture transported classifier directions while leaving hidden degrees of freedom untouched. The work demonstrates that learned transport does not always constitute indispensable edge geometry and provides a clear boundary where reliance becomes unreplaced task value.

## Key Contributions  
- [Finding 1] Checkpoint reliance is defined as the ability of a fixed predictor’s maps to persist across protocol‑relative replacements, revealing whether the checkpoint alone drives performance.  
- [Finding 2] A task‑null theorem shows that label‑only training cannot distinguish between transport directions and invisible degrees of freedom in full \(d\times d\) maps, causing reliance and value claims to split.  
- [Finding 3] An exact frame model delineates the boundary where checkpoint dependence ceases to be replaceable by task‑level improvements.

## Methodology  
The authors employ estimands to quantify two regimes: (1) **checkpoint reliance**, which measures how much a single checkpoint’s edge assignments survive when the rest of the network is retrained, and (2) **protocol‑relative replacement**, where matched families are rebuilt without changing map capacity or persistent assignments. They use a theoretical “task‑null” framework to isolate label‑only transport from hidden degrees of freedom. An exact frame model computes the performance boundary between replaceable and unreplaced transport. Practically, they conduct label‑only training audits on NSD (Network Structure Dataset), DNSD (Directed Sheaf Neural Network dataset), and DSNN implementations to recover both regimes on real graphs.

## Results  
All five official DNSD benchmarks exhibit fixed‑checkpoint reliance: after retraining with assignment‑breaking or shared‑map controls, four datasets achieve full performance, while Roman‑Empire retains a 0.0675 advantage over resampled assignment and a 0.0391 advantage over a parameter‑matched shared map across ten splits. Label‑only training successfully realizes the predicted separation between reliance and task value.

## Significance  
The study clarifies that learned transport in sheaf GNNs is not always indispensable edge geometry; it can be checkpoint‑driven without contributing to task performance. This insight guides researchers to pair checkpoint interventions with matched retraining protocols, preventing misinterpretation of model behavior as proof of useful geometry.

## Related Concepts  
- Sheaf Graph Neural Networks (GNNs)  
- Checkpoint dependence vs protocol‑relative replacement  
- Task‑null theorem and invisible degrees of freedom in \(d\times d\) maps  
- Exact frame models for performance boundaries  
- DNSD benchmark suite (Network Structure Dataset, Directed Sheaf Neural Network dataset)  
- Label‑only training audits
