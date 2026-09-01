---
title: MERIT: Mitigating Exposure Bias in Generative XMC for User-Interest Propensity Modeling
url: http://arxiv.org/abs/2608.28931v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_23-03-14Z_MERIT_MitigatingExposureBiasinGenerativeXMCforUser.md
generated_at: 2026-08-31 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MERIT, a framework that reduces exposure bias in generative user‑interest modeling by using a self‑correction loss that treats teacher‑forced predictions as part of the conditioning context. On a large e‑commerce dataset with over 250k interest categories, MERIT lifts global recall by at least 11.9% and average Hit@k by 6.1%, delivering a +0.26% conversion gain in A/B tests.

## Key Takeaways
- The self‑correction loss forces the model to correct for early errors that arise from teacher‑forced fine‑tuning, which otherwise bias later outputs toward correlated labels.
- By using a permutation‑invariant multi‑target loss over shuffled mixtures of gold and hard‑negative labels, MERIT concentrates supervision on classification positions while keeping training efficient.
- The resulting propensity‑aligned hidden states enable a lightweight bidirectional scorer that improves both user‑interest retrieval and interest‑to‑user matching.

## Context
Generative models for recommendation tasks face exposure bias when the model’s own predictions contaminate the conditioning signal, leading to over‑generation of near‑correlates. This issue is especially acute in large label spaces where true signals are sparse. MERIT addresses this by decoupling generation from supervision through a permutation‑invariant loss that isolates classification cues.

## Implications
For practitioners, MERIT offers a practical way to fine‑tune generative models without worsening downstream performance, preserving the benefits of teacher‑forced training while mitigating exposure bias. In industry, the modest conversion lift demonstrates that such corrections can be deployed at scale, supporting more reliable and scalable personalization pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28931v1)
