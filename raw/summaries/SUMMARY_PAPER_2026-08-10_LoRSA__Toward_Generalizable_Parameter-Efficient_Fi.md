---
title: LoRSA: Toward Generalizable Parameter-Efficient Fine-Tuning for Biomedical Downstream Tasks
url: http://arxiv.org/abs/2608.07749v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_20-30-35Z_LoRSA_TowardGeneralizableParameter_EfficientFine_T.md
generated_at: 2026-08-10 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes LoRSA a global‑residual adaptation framework for parameter‑efficient fine‑tuning of vision models in biomedical tasks. It jointly learns a dense low‑rank component and a dynamic sparse component to capture both globally coordinated task structure and localized residuals, achieving state‑of‑the‑art external‑domain performance on breast‑density classification.

## Key Takeaways
- LoRSA introduces two complementary adaptation components: a dense low‑rank part that encodes globally coordinated changes and a structured sparse part whose support evolves during training.
- The framework demonstrates that about 92% of the energy in each component lies outside the bilateral singular subspace of the other, showing largely complementary update directions.
- On MammosighTR LoRSA improves macro‑F1 by 2.15 points over the best competitor and on RSNA it gains 3.09 points.

## Context
Parameter‑efficient fine‑tuning is essential for deploying vision models in resource‑constrained medical settings where full retraining is infeasible. Existing methods often limit adaptation to a single low‑rank subspace, which can hinder performance across diverse imaging domains.

## Implications
Organizing adaptation into distinct global and residual pathways may become a standard design principle for biomedical AI systems seeking robust cross‑domain generalization. Practitioners can leverage LoRSA’s complementary updates to build models that retain core knowledge while adapting locally to new data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07749v1)
