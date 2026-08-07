---
title: RxnCLF: Contrastive Transformation-Aware Reaction Foundation Model for Improved Reactivity Prediction
url: http://arxiv.org/abs/2608.06259v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_16-51-23Z_RxnCLF_ContrastiveTransformation_AwareReactionFoun.md
generated_at: 2026-08-06 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RxnCLF, a contrastive learning foundation model designed to predict reaction yields by learning rich representations of chemical transformations. By using a condensed reaction graph that merges reactants and products into one unified structure, RxnCLF captures transformation-specific features while generalizing across diverse reactions. Fine‑tuning on multiple benchmarks shows superior performance compared with traditional graph or sequence models.

## Key Takeaways
- RxnCLF leverages a self‑supervised contrastive framework to learn a compact latent space that encodes both reaction‑center details and side‑chain contexts, enabling transformation‑aware representations.  
- The model is pretrained on 1.7 million Pistachio reactions, allowing it to generalize beyond the limited labeled data typical of yield prediction tasks.  
- Fine‑tuned RxnCLF consistently improves R² scores across Buchwald‑Hartwig, Pd‑catalyzed BH coupling, and proprietary HTE C‑N/amide datasets, outperforming graph and sequence baselines.

## Context
Reaction yield prediction suffers from data scarcity and the sparsity of reaction space, which hampers model generalization. Existing approaches rely on isolated encodings that fail to capture the holistic nature of chemical transformations. RxnCLF addresses these limitations by unifying reactant and product information into a single graph, offering a scalable foundation for many downstream tasks.

## Implications
This work demonstrates that CRG‑based models can serve as robust reaction foundations, supporting not only yield prediction but also regioselectivity, enantioselectivity, and condition optimization. For industry, it reduces reliance on large labeled datasets and accelerates the development of predictive tools across pharmaceutical and fine‑chemical sectors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06259v1)
