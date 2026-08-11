---
title: Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts
url: http://arxiv.org/abs/2608.08853v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_18-31-16Z_BeyondRouting_DecouplingExpertDispatchandAggregati.md
generated_at: 2026-08-10 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the two functions of a sparse Mixture‑of‑Experts router — selecting which experts to use (dispatch) and weighting their outputs (aggregation) — should be linked together. By keeping expert selection fixed but varying only aggregation, they introduce Fixed‑Dispatch Adaptive Aggregation (FDAA), a lightweight head that adapts the output weights directly with the language‑modeling objective while freezing the backbone, router, and experts. On OLMoE‑1B‑7B, FDAA yields a delta cross‑entropy of –0.1523 across three seeds on WikiText‑103, showing measurable gains.

## Key Takeaways
- The router’s top‑scored expert is the counterfactual best vertex only 17.2 % of the time, indicating that dispatch alone does not guarantee optimal commitment.
- Full‑horizon cross‑entropy improves by 0.0160 ± 0.0039 when using a structured oracle for aggregation, highlighting the benefit of decoupled optimization.
- FDAA’s headroom remains significant on WikiText and C4, while router Top1 identifies the best expert in only 12.5 % and 16.7 % of audited examples.

## Context
Sparse MoE architectures aim to balance compute efficiency with model capacity, but current implementations often couple dispatch and aggregation, limiting flexibility. This work demonstrates that separating these roles can lead to better adaptation without retraining large components.

## Implications
For practitioners, FDAA offers a practical way to fine‑tune router behavior on existing models, reducing the need for full retraining. The findings suggest that industry deployments could adopt decoupled dispatch and aggregation to improve efficiency and performance across diverse datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08853v1)
