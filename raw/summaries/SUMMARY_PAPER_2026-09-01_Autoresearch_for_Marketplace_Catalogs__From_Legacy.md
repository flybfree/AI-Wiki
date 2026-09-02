---
title: Autoresearch for Marketplace Catalogs: From Legacy Forms to AI-Native Matching
url: http://arxiv.org/abs/2609.00274v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_19-18-07Z_AutoresearchforMarketplaceCatalogs_FromLegacyForms.md
generated_at: 2026-09-01 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an autoresearch loop that automatically generates occupation-specific preference taxonomies for two‑sided service marketplaces using large language models. By treating each occupation as a separate generation problem the system iteratively proposes tag sets, scores them with a calibrated LLM judge and a weighted 7‑critic panel, then maps legacy request forms back to these tags. The approach replaces fixed form fields with probabilistic matching grounded in inferred intent.

## Key Takeaways
- The autoresearch loop generates occupation‑specific taxonomy by iterative propose‑evaluate‑keep cycles using a six‑rubric LLM judge and a 7‑critic persona panel without hard vetoes.
- Legacy request forms are mapped to the generated tags via inference of provider attributes rather than literal translation, providing both coverage signals and QA interfaces.
- The system spans 132 occupations in production since April 2026 demonstrating scalability across diverse service categories.

## Context
This work addresses a growing shift in marketplace design from deterministic forms to AI‑driven probabilistic matching. By leveraging LLMs for intent inference the paper contributes to the broader field of automated taxonomy generation and demonstrates how generative models can underwrite user‑provider alignment without manual curation.

## Implications
For practitioners, the autoresearch framework reduces the burden of maintaining static preference schemas while improving match relevance. It also offers a scalable model for other two‑sided platforms seeking AI‑native matching that respects provider interpretability and marketplace efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00274v1)
