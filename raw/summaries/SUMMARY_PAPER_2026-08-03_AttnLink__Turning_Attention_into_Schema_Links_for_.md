---
title: AttnLink: Turning Attention into Schema Links for Text-to-SQL
url: http://arxiv.org/abs/2608.00693v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_14-44-25Z_AttnLink_TurningAttentionintoSchemaLinksforText_to.md
generated_at: 2026-08-03 20:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AttnLink, an attention-based framework that converts LLM internal attention into relevance scores for schema items in Text-to-SQL. It achieves high mAP on Spider, BIRD, and Spider2‑SQLite while providing millisecond latency. Two variants, AttnLink-U and AttnLink‑S, improve coverage and control.

## Key Takeaways
- The framework extracts attention from generation-start to candidate schema spans in a single prefill pass without autoregressive decoding.
- It uses direct supervision to align attention distribution with gold items via AttnLink‑S, adding set-mass objective and adaptive probability-floor regularizer.
- Scores enable post‑hoc precision‑recall control through temperature scaling and cumulative mass selection.

## Context
Attention mechanisms are central to modern LLMs but their use in Text-to-SQL is limited by autoregressive inefficiency. This work demonstrates that attention can be repurposed for schema linking, offering a scalable alternative to score‑based or rule‑based methods.

## Implications
Practitioners can integrate AttnLink into existing pipelines with minimal latency impact, enabling real‑time query generation at scale. The method’s high accuracy and fine‑grained control set a new benchmark for Text-to-SQL systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00693v1)
