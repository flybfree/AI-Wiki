---
title: MARS: Multi-Agent Re-ranking for Repeat-Order Food Delivery Recommendation
url: http://arxiv.org/abs/2607.25420v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-18-08Z_MARS_Multi_AgentRe_rankingforRepeat_OrderFoodDeliv.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MARS, a modular multi‑agent re‑ranking framework for repeat‑order food delivery recommendation that integrates large language models with lightweight collaborative signals. It demonstrates that strong pre‑trained backbones can be competitive when combined with contextual filtering and prompt‑driven reasoning on real‑world benchmarks. Evaluation shows MARS outperforms several heuristic, sequential, graph‑based, and domain‑specific baselines.

## Key Takeaways
- Strong pre‑trained LLMs achieve competitive performance in repeat‑order recommendation when paired with lightweight global preference signals from LightGCN.
- The hybrid pipeline combines Swing‑based local peer evidence, geospatial filtering, and prompt‑driven LLM reasoning to refine rankings.
- A reproducible evaluation protocol is established for hybrid LLM recommenders using DHRD‑SE and DHRD‑SG benchmarks.

## Context
This work addresses the challenge of integrating large language models into recommendation pipelines where performance gains are not always clear. By providing a transparent modular framework, it helps researchers understand how each component contributes to overall ranking quality in real‑world settings.

## Implications
Practitioners can adopt MARS as a baseline for hybrid recommender systems that balance LLM reasoning with efficient collaborative signals. The findings suggest that even without extensive fine‑tuning, LLMs can be effective when guided by structured retrieval and contextual constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25420v1)
