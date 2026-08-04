---
title: Logit-Origin Centering for Singleton Test-Time Adaptation
url: http://arxiv.org/abs/2608.01074v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_08-18-56Z_Logit_OriginCenteringforSingletonTest_TimeAdaptati.md
generated_at: 2026-08-03 23:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the challenge of test-time adaptation for singleton streaming data where only unlabeled examples arrive one at a time. It introduces Prequential Logit-Origin Centering (PLOC) which shifts logit space without updating model weights and outperforms baselines on tabular benchmarks.

## Key Takeaways
- PLOC keeps the source model frozen while shifting logits per step, storing only a single running mean of past logits. This avoids batch statistics needed in one‑sample regime.
- The method requires no labels or priors and bypasses weight updates entirely, making it lightweight for strict streaming regimes.
- A deferred variant applies a static shift that preserves source ranking exactly, guaranteeing AUROC stability.

## Context
Tabular data often suffers from distribution shifts between training and test sets. Traditional fully test-time adaptation (FTTA) methods rely on batch statistics which break down when examples arrive individually. This paper shows that such batch‑dependent approaches degrade sharply in singleton streaming settings.

## Implications
For practitioners deploying models in real‑time environments, PLOC offers a simple, label‑free technique to maintain performance without retraining. It can be integrated into production pipelines with minimal overhead, supporting robust ranking under shifting distributions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01074v1)
