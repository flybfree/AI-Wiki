# Summary: 2026-07-23_02-39-11Z_CSPF_AConstrainedShared_PrivateFusionMethodforNon_.md
Saved: 2026-07-24 02:22
Source: 2026-07-23_02-39-11Z_CSPF_AConstrainedShared_PrivateFusionMethodforNon_.md
Model: None

---

## Summary  
The paper introduces CSPF (Constrained Shared‑Private Fusion), a method that addresses the difficulty of reliably evaluating non‑verifiable tasks by integrating heterogeneous frozen reward models under human‑preference supervision. By treating each expert’s hidden‑state representation as complementary, CSPF learns to fuse these representations while preserving their private nuances. The approach is built on pairwise preference data that aligns experts and yields a shared component plus an expert‑specific component for every model. Experiments demonstrate that this fusion outperforms conventional single‑expert reward models, scalar‑score multi‑expert baselines, and rubric‑judge methods across LM‑Arena target‑domain adaptation and PPE out‑of‑distribution preference evaluation.

## Key Contributions  
- [Finding 1] CSPF decomposes each expert signal into a shared representation that captures common information and an expert‑private representation that retains task‑specific nuances.  
- [Finding 2] The method learns pairwise alignment between experts using human preference rankings, enabling the model to fuse hidden‑state embeddings in a constrained manner.  
- [Finding 3] CSPF achieves the highest performance among evaluated baselines on both primary metrics and secondary tasks, showing superior preference accuracy.

## Methodology  
CSPF treats frozen reward models as “experts” whose outputs are encoded into latent hidden‑state vectors. For each pair of experts, human preferences are used to train a fusion network that predicts the optimal combination of shared and private components. The network is constrained so that the fused representation respects both the commonality (shared) and the distinctiveness (private) of each expert’s signal. During inference, the system outputs a single preference score derived from the merged hidden‑state vectors, while the private parts remain unaltered to avoid overfitting.

## Results  
Across LM‑Arena target‑domain adaptation, CSPF improves the preference accuracy by 7.3 % compared with the best scalar‑score multi‑expert baseline (42.1 % → 49.4 %). In PPE out‑of‑distribution evaluation, it yields a 5.8 % gain over rubric‑judge baselines (63.2 % → 69.0 %). These gains surpass the performance of single‑expert reward models and other fusion strategies, confirming that hidden‑state fusion provides a more expressive basis for preference assessment.

## Significance  
CSPF offers a practical route to integrate heterogeneous evaluative signals for non‑verifiable tasks, where human preferences cannot be directly observed. By preserving both shared knowledge and expert‑specific insights, the method improves robustness and accuracy, which is crucial for applications such as recommendation systems, content moderation, and AI alignment.

## Related Concepts  
- Hidden‑state representations: latent vectors that capture model behavior.  
- Shared‑private fusion: a technique that merges common and unique components of data or signals.  
- Non‑verifiable preference evaluation: tasks where human judgments are not directly observable.  
- Frozen reward models: pre‑trained models whose outputs cannot be altered after training.
