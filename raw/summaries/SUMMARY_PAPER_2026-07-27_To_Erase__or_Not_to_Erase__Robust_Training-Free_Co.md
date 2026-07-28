---
title: To Erase, or Not to Erase: Robust Training-Free Concept Erasure with Preservation aware Adaptive Ranked Subspace Expansion
url: http://arxiv.org/abs/2607.23492v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_06-35-31Z_ToErase_orNottoErase_RobustTraining_FreeConceptEra.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PARSE, a training‑free method for robust concept erasure in latent diffusion models that balances target removal with preservation of useful concepts. By dynamically querying the model’s vocabulary and iteratively expanding erased subspaces only when new triggers are safe, PARSE achieves high ASR under attacks while maintaining low FID scores. Experiments show it outperforms existing CET baselines across NSFW, artistic style, and object erasure tasks.

## Key Takeaways
- PARSE uses classifier‑free guidance to discover target‑inducing erase concepts and retain concepts within the model’s vocabulary, creating a dynamic concept bank that adapts to prompt steering.  
- The framework preserves nearby benign concepts by applying a projection that removes only target directions without affecting retain directions, reducing re‑emergence of erased targets under new triggers.  
- A Balanced Erasure Utility Score (BEUS) combines robustness and utility via bounded monotone transforms and harmonic mean aggregation to evaluate trade‑offs objectively.

## Context
Concept erasure is essential for safe AI generation but most existing methods rely on static concept banks that ignore how prompts influence the model, leading to fragile results. PARSE’s adaptive vocabulary indexing addresses this limitation by continuously aligning erase and retain concepts with prompt dynamics, offering a more resilient alternative without retraining.

## Implications
For practitioners deploying diffusion models in content moderation or creative tools, PARSE provides a practical way to remove harmful elements while keeping the model useful for benign requests. This reduces reliance on manual concept selection and lowers operational costs, encouraging broader adoption of safe generative AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23492v1)
