# Summary: 2026-07-21_12-47-15Z_WhereShouldOptimizerStateLive_TieredStateAllocatio.md
Saved: 2026-07-24 01:12
Source: 2026-07-21_12-47-15Z_WhereShouldOptimizerStateLive_TieredStateAllocatio.md
Model: None

---

## Summary  
Mixture‑of‑Experts (MoE) models suffer from a prohibitive memory burden caused by storing full optimizer states for every parameter population. The authors propose SkewAdam, an optimizer that allocates optimizer state in three tiers—full second moments for the dense backbone, factored second moments for the experts, and exact second moments for the router—while retaining float32 momentum only on the backbone. This tiered allocation reduces optimizer memory from 50 GB to ~1.3 GB (≈2.6 % of AdamW) and cuts peak training memory by more than half, enabling training on a single 40 GB accelerator. Experiments show SkewAdam improves validation perplexity over standard optimizers and achieves router load‑balance within 1 %. The key insight is that where optimizer state resides matters as much as how much of it there is.

## Key Contributions  
- **Finding 1:** Optimizer state can be partitioned among the dense backbone, experts, and router based on their parameter counts and gradient statistics.  
- **Finding 2:** A tiered allocation (full second moment for backbone, factored for experts, exact for router) reduces optimizer memory by >97 % without hurting training speed or accuracy.  
- **Finding 3:** The performance gains stem primarily from preserving float32 momentum on the backbone; dropping it to a uniform Adam‑style estimator degrades perplexity despite similar state size.

## Methodology  
The authors construct SkewAdam by applying three distinct second‑moment estimators: (i) exact BF16 second moments for the router (<0.01 % of parameters), (ii) factored BF16 second moments for the experts (≈95 %), and (iii) full float32 second moments only for the dense backbone (≈5 %). Momentum is retained in float32 exclusively on the backbone to capture its larger gradient variance. The optimizer’s state size is computed analytically, and training proceeds with standard MoE forward‑backward passes while updating each tier’s moment buffer separately.

## Results  
On a 6.78 B‑parameter MoE language model trained for 82 M tokens, SkewAdam achieved validation perplexity of **108.4**, outperforming AdamW (126.8), Muon (120.2) and Lion (393.7). Peak memory consumption dropped from 81.4 GB to 31.3 GB, fitting within a single 40 GB GPU. A tier‑ablation study confirmed that matching the allocation with twenty times more state yields identical perplexity, indicating no trade‑off between accuracy and memory savings. Tuning learning rates narrowed but did not close the gap: best AdamW (118.5) vs. tuned Adafactor (139.7). The router’s load balance varied by ≤1 % from uniform.

## Significance  
This work demonstrates that optimizer state allocation is a critical design lever for MoE training, offering a path to train large models on limited hardware without sacrificing performance. By decoupling memory‑intensive second‑moment storage from the majority of parameters, SkewAdam enables cost‑effective scaling while preserving gradient dynamics.

## Related Concepts  
- Mixture‑of‑Experts (MoE) model architecture  
- AdamW optimizer and its full state storage  
- Factored second‑moment estimators for memory efficiency  
- TensorFlow / PyTorch mixed‑precision training  
- Learning‑rate tuning in large language models
