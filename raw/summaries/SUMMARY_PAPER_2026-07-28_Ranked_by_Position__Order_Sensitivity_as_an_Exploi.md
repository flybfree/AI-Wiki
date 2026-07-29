---
title: Ranked by Position: Order Sensitivity as an Exploitable Attack Surface in LLM Listwise Recommenders
url: http://arxiv.org/abs/2607.24869v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-26_22-32-12Z_RankedbyPosition_OrderSensitivityasanExploitableAt.md
generated_at: 2026-07-28 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the order of candidate items in listwise LLM rerankers can be exploited to push low‑ranked label‑0 targets into the top‑k without altering content, labels, or model parameters. It introduces a metric promo@k and shows that with only 50 reorderings the attack succeeds up to 57% of the time. The study also demonstrates that permutation stability predicts vulnerability.

## Key Takeaways
- order sensitivity creates an exploitable attack surface where label‑0 targets can be moved into top‑k purely by permuting candidates.
- promo@k quantifies this as a fraction of label‑0 targets promoted to top‑k, reaching 0.57 with R=50 orderings across three domains.
- permutation‑consistency regularization and architectural invariance mitigate the bias while pointwise scoring avoids it but sacrifices ranking quality.

## Context
LLMs are increasingly used as listwise rerankers that rely on sequential prompts of candidate items, making them vulnerable to subtle input ordering attacks. This research highlights a previously overlooked security angle in recommendation pipelines where model output depends heavily on input sequence.

## Implications
Recommendation systems must treat candidate order as a security parameter and implement defenses such as regularization or alternative scoring methods. Practitioners should audit their reranker designs for order‑sensitivity risks before deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24869v1)
