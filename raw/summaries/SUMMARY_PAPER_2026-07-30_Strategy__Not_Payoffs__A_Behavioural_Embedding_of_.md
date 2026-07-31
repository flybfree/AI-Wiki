---
title: Strategy, Not Payoffs: A Behavioural Embedding of Normal-Form Games
url: http://arxiv.org/abs/2607.27536v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_00-10-21Z_Strategy_NotPayoffs_ABehaviouralEmbeddingofNormal_.md
generated_at: 2026-07-30 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a behavioural embedding that captures the entropy of Nash equilibria and the sensitivity of optimal responses in normal‑form games, showing it reliably predicts how fine‑tuned language models change their strategic abilities across different games. The authors contrast this with existing embeddings that merely memorize game identities, demonstrating that transfer is driven by decision‑making structure rather than payoff geometry.

## Key Takeaways
- A lightweight two‑feature embedding based on Nash equilibrium entropy and response sensitivity predicts performance changes on held‑out games.
- Existing structural embeddings fail to generalize because they rely on memorized game labels instead of behavioural patterns.
- The findings show that LLM strategic capability transfer is governed by the underlying decision structure, not the payoff values.

## Context
Understanding how fine‑tuning affects an agent’s reasoning in new tasks remains a central challenge for large language models. Normal‑form games provide a clear experimental framework to explore this phenomenon, making them valuable testbeds for probing model transferability and robustness.

## Implications
The behavioural embedding offers a practical tool for evaluating whether a model has truly learned strategic skills or merely memorized specific game outcomes. Practitioners can use it to guide fine‑tuning strategies and ensure models generalize beyond the training data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27536v1)
