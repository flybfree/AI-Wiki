---
title: Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense
url: http://arxiv.org/abs/2608.27945v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_05-39-29Z_Cross_SessionDecompositionAttacks_ScalingRiskandIn.md
generated_at: 2026-08-30 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates cross-session decomposition attacks where benign‑looking subqueries from independent interactions are recomposed to produce harmful outputs, showing that larger models can increase the safety risk. It formalizes this scenario as compositional safety risk and proves a conditional bound linking the model’s excess loss on allowed subqueries to the transferred risk. Experiments demonstrate that intent‑aligned retrieval improves defense effectiveness.

## Key Takeaways
- The conditional risk-transfer bound shows that the gap between deployed composed risk and reference composed risk is bounded by the model's excess loss on allowed subqueries.
- Synthetic withholding experiments demonstrate that larger transformers assign lower loss to instructions not seen verbatim but recoverable from injected facts, increasing harmful capability uplift.
- IntentAlign-MiniLM outperforms larger embedding models in intent retrieval and yields the lowest learned‑retriever harmful recall across tested guardrails.

## Context
This work addresses safety concerns as language models scale, highlighting that risk may transfer across separate interactions. It contributes to understanding compositional risk and offers a lightweight defense mechanism based on intent alignment.

## Implications
Practitioners can mitigate deployment risks by integrating intent‑aligned retrieval, reducing reliance on massive embeddings. The findings suggest proactive guardrails are needed as model capabilities grow.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27945v1)
