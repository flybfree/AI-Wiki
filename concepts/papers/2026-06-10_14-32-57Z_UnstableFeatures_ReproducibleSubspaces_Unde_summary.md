---
title: "2026 06 10 14 32 57Z Unstablefeatures Reproduciblesubspaces Unde Summary"
date: 2026-06-10
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-10_14-32-57Z_UnstableFeatures_ReproducibleSubspaces_Understandi.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-10 20:59
Source: 2026-06-10_14-32-57Z_UnstableFeatures_ReproducibleSubspaces_Understandi.md
Model: None

---


## Summary  
The paper investigates why sparse autoencoders (SAEs) can yield different latent representations when trained from the same seed, focusing on a per‑feature “stability” metric that measures how often a feature reappears across independent trainings. By analyzing this stability signal across a broad range of models, layers, dictionary sizes and SAE variants, the authors demonstrate that stable features dominate reconstruction and prediction performance while unstable ones have only weak marginal impact. They also show that unstable features are not pure noise but instead concentrate in reproducible low‑rank subspaces, suggesting seed dependence reflects basis ambiguity rather than randomness. The work ultimately proposes a technique for pooling unique cross‑seed features to obtain more stable SAEs without sacrificing explained variance.

## Key Contributions  
- [Finding 1] Stable features carry most of the reconstruction‑ and prediction‑relevant signal, whereas unstable features have weak marginal impact and are dominated by low‑frequency surface‑form triggers.  
- [Finding 2] Unstable features are individually non‑reproducible but concentrate in reproducible lower‑rank subspaces, indicating that seed dependence often stems from basis ambiguity within a shared activation space.  
- [Finding 3] By pooling unique cross‑seed features, one can construct more stable SAEs while preserving the amount of explained variance.

## Methodology  
The authors define feature stability as the probability that a similar feature reappears in an independently trained SAE using a per‑feature signal derived from activation statistics and automatic explanations. They conduct a large‑scale empirical study varying seeds, models, layers, dictionary sizes, and SAE architectures to quantify this metric. To make the mechanism explicit, they build a controlled synthetic model where low‑rank ground‑truth features are recoverable at the subspace level yet remain non‑identifiable as individual latents across seeds. Finally, they evaluate the benefit of pooling unique cross‑seed features on stability and variance.

## Results  
Across the experiments, stable features account for the majority of reconstruction error reduction and prediction accuracy gains, while unstable features contribute only a small fraction of performance improvement. Geometrically, unstable features lie in a low‑dimensional subspace that is consistently reproduced across seeds but cannot be distinguished as separate latents. The synthetic model confirms that these subspaces can be recovered without identifying individual latent vectors, illustrating the basis‑ambiguity interpretation. When pooling unique cross‑seed features, the resulting SAE maintains comparable explained variance to standard models yet exhibits higher stability.

## Significance  
This research clarifies a longstanding mystery: seed dependence in SAEs is not merely a source of noise but reflects structured low‑rank structure that can be exploited for more robust representations. By providing an empirical stability metric and a practical pooling strategy, the work offers tools to improve interpretability and reproducibility without sacrificing performance.

## Related Concepts  
- Sparse autoencoders (SAEs)  
- Feature stability / per‑feature signal  
- Basis ambiguity in activation space  
- Low‑rank subspace concentration  
- Automatic explanations via activation statistics
