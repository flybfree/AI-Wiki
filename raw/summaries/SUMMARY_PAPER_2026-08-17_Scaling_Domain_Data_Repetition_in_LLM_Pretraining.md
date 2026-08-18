---
title: Scaling Domain Data Repetition in LLM Pretraining
url: http://arxiv.org/abs/2608.14071v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_08-27-15Z_ScalingDomainDataRepetitioninLLMPretraining.md
generated_at: 2026-08-17 19:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how to balance the use of repeated high-quality domain data with model size in large language model pretraining, finding an optimal repetition count that grows slightly with model size and is inversely related to validation loss across domains. The study empirically evaluates these relationships across multiple domains and model sizes.

## Key Takeaways
- At a fixed tokens‑per‑parameter ratio (TPP), the optimal repetition count increases modestly as model size rises, indicating that larger models can handle slightly more repeated data without overfitting.
- The optimal repetition count is strongly negatively correlated with final domain validation loss, meaning domains that achieve lower losses during testing generally require more repetitions to maintain performance.
- Unique domain data quantity has only weak influence on the optimal repetition count, suggesting that sheer volume alone does not dictate how much repetition is needed.

## Context
Scaling LLMs requires expanding token budgets to keep TPP stable, yet high‑quality domain corpora are scarce and expensive. Researchers often rely on web data which dilutes domain signals as model size grows. This work addresses that dilution by quantifying how much repeated domain data is needed.

## Implications
Practitioners can use repetition counts derived from smaller models to guide larger training pipelines, reducing the need for costly manual data augmentation. The approach offers a scalable heuristic that aligns with real‑world token budgets and improves domain performance without overfitting.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14071v1)
