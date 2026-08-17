---
title: Scaling Domain Data Repetition in LLM Pretraining
url: http://arxiv.org/abs/2608.14071v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_08-27-15Z_ScalingDomainDataRepetitioninLLMPretraining.md
generated_at: 2026-08-16 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how to balance the use of high-quality domain data and its repetition in large language model pretraining as model size grows, aiming to keep tokens per parameter ratio stable. It discovers that optimal repetition count rises slightly with larger models, improves validation performance across domains, and is unrelated to unique data volume.

## Key Takeaways
- At a fixed TPP the optimal repetition count increases modestly when the model becomes larger, indicating that bigger models benefit from a bit more repeated domain examples.
- The best repetition count correlates negatively with final validation loss: domains that achieve lower loss can afford higher repetitions without overfitting.
- Unique domain data does not strongly influence the optimal repetition count, suggesting reuse is driven by performance rather than diversity.

## Context
Increasing model scale demands larger token budgets to maintain TPP, yet high-quality domain corpora are scarce and expensive. Researchers often rely on generic web text, which dilutes domain relevance as models grow. This study addresses that gap by quantifying how repetition can preserve domain signal without causing overfitting.

## Implications
Practitioners can use repetition strategies tuned on smaller proxies to guide large‑scale training, reducing the need for costly new data collection. The insight streamlines scaling pipelines and improves downstream performance across specialized domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14071v1)
