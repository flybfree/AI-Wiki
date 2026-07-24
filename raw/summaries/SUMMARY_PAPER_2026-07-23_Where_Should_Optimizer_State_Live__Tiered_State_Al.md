---
title: Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training
url: http://arxiv.org/abs/2607.19058v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_12-47-15Z_WhereShouldOptimizerStateLive_TieredStateAllocatio.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates how optimizer state can be allocated across different parts of a mixture-of-experts model to reduce memory consumption while maintaining training performance. It introduces SkewAdam, which allocates state tiers based on the role of dense backbone, experts, and router parameters, achieving a 60% reduction in optimizer memory usage compared with AdamW. Validation perplexity improves significantly under the same training conditions.

## Key Takeaways  
- The tiered allocation reduces optimizer state from 50.6 GB to just 1.29 GB, fitting comfortably within a 40‑GB accelerator and lowering peak training memory to 31.3 GB.  
- Accuracy gains stem primarily from retaining full first‑moment momentum; dropping it for memory savings would cause perplexity to drop as seen with Adafactor.  
- Ablation experiments show that adding more optimizer state does not further improve validation perplexity, indicating that the benefit is purely from memory efficiency.

## Context  
Mixture-of-experts models are essential for scaling language generation to billions of parameters, yet their training is constrained by memory. Efficient optimizers can unlock larger models on limited hardware, a critical issue for real‑world deployment and research.

## Implications  
The findings suggest that how optimizer state is structured matters as much as the amount of it, prompting developers to consider tiered strategies when deploying MoE systems. This could lead to more memory‑efficient training pipelines without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19058v1)
