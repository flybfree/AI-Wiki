---
title: When to Review: Spaced Repetition for Continual Pre-Training of Language Models
url: http://arxiv.org/abs/2608.17530v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_08-51-47Z_WhentoReview_SpacedRepetitionforContinualPre_Train.md
generated_at: 2026-08-18 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Spaced Repetition Training (SRT) to improve continual pre-training of language models by scheduling which historical examples are reviewed at each step, based on a cognitive‑science inspired recall signal derived from SuperMemo‑2. Experiments on Wikipedia and code corpora show that SRT recovers 5–37 percentage points of old‑knowledge accuracy lost by naive replay while maintaining or improving new‑knowledge gains, preserving benchmark performance across model scales.

## Key Takeaways
- SRT schedules review using a per‑example recall signal mapped from perplexity to retention quality, allowing the training loop to decide which examples are revisited.  
- The framework retains the original model, objective and optimizer, only changing the sampling strategy for historical data.  
- On temporally separated corpora, SRT improves the stability‑plasticity trade‑off, recovering up to 37 percentage points of old‑knowledge accuracy while preserving new‑knowledge acquisition.

## Context
Continual pre‑training is a core challenge in scaling language models because standard replay mixes all past data uniformly, causing forgetting. The adaptive scheduling approach aligns with cognitive memory principles and could be applied beyond text to vision or tabular domains when paired with an appropriate recall metric.

## Implications
For researchers, SRT offers a simple yet effective way to mitigate catastrophic forgetting without architectural changes. Practitioners can adopt the per‑example review state in existing continual learning pipelines, potentially boosting model stability across diverse data streams.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17530v1)
