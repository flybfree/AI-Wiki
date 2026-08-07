# Summary: 2026-08-06_15-18-35Z_CogVis_MustOpen_VocabularyChangeDetectionPerceivet.md
Saved: 2026-08-06 20:46
Source: 2026-08-06_15-18-35Z_CogVis_MustOpen_VocabularyChangeDetectionPerceivet.md
Model: None

---

## Summary  
The paper tackles the challenge of open‑vocabulary change detection (OVCD), which must recognize arbitrary semantic categories while perceiving the scene anew for every query. Existing methods suffer from unstable results because they fuse temporal perception, semantic discrimination, and region verification into a single pipeline. CogVis addresses this by reformulating OVCD as a cognitive memory‑guided framework that separates these stages. The contribution is a reusable, category‑agnostic change prior extracted from frozen bi‑temporal features, a query‑specific decision threshold calibrated per image, and an adaptive filter that improves both accuracy and inference speed.

## Key Contributions  
- [Finding 1] A Scene Change Perceptron (SCP) extracts a reusable, category‑agnostic change prior directly from frozen bi‑temporal features, decoupling temporal evidence from semantic decisions.  
- [Finding 2] The Semantic Memory Calibrator (SMC) dynamically estimates an image‑query specific decision threshold to compensate for category‑dependent score shifts.  
- [Finding 3] An Adaptive Region Filter (ARF) combines learned semantic, temporal, and structural reliability metrics to prune connected candidates efficiently.

## Methodology  
CogVis adopts a perception‑memory‑verification paradigm: first, the SCP processes frozen bi‑temporal frames to produce a global change prior; second, the SMC computes a per‑query threshold that aligns scores with the target category; third, the ARF filters candidate regions using a learned reliability score that integrates semantic plausibility, temporal consistency, and geometric connectivity. This modular design avoids redundant computation across queries.

## Results  
Experiments on seven benchmarks covering semantic change detection, binary change localization, and building‑damage assessment demonstrate that CogVis achieves state‑of‑the‑art performance across all datasets. Moreover, the framework reduces inference throughput by 28.50% compared with prior methods while maintaining or improving accuracy.

## Significance  
By sharing scene‑level perception among queries, CogVis eliminates repeated category‑agnostic temporal processing, leading to faster, more reliable change detection for real‑time monitoring applications such as satellite imagery analysis and infrastructure health assessment.

## Related Concepts  
Open‑Vocabulary Change Detection (OVCD), Scene Change Perceptron (SCP), Semantic Memory Calibrator (SMC), Adaptive Region Filter (ARF), bi‑temporal features, cognitive memory‑guided framework.
