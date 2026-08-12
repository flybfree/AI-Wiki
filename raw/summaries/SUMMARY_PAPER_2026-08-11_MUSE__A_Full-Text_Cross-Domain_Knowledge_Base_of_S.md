---
title: MUSE: A Full-Text Cross-Domain Knowledge Base of Scientific Problems, Solutions, and Rationales
url: http://arxiv.org/abs/2608.10974v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_14-31-37Z_MUSE_AFull_TextCross_DomainKnowledgeBaseofScientif.md
generated_at: 2026-08-11 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MUSE, a full‑text resource that extracts problem‑solution‑rationale (P‑S‑R) triples from scientific literature to create a large knowledge base. The authors annotate 579 paragraphs and generate 37 000 source‑grounded triplets, then show that rationale supervision improves performance on complex multi‑constraint problems while potentially degrading it on simpler tasks.

## Key Takeaways
- MUSE curates expert‑annotated full‑text paragraphs to produce a high‑quality knowledge base of 37 K P‑S‑R triplets.  
- The annotation schema includes spans for problem, solution, rationale, solves and rationale_of links as well as conceptual coreference.  
- Training a rationale‑supervised LLM yields better performance on complex problems but can harm results on simpler ones.

## Context
The work addresses the need for structured scientific knowledge that captures not only what is solved but also why certain methods are chosen. By grounding explanations in the original text, MUSE supports AI models that require explicit reasoning about problem constraints and solution choices.

## Implications
For researchers building explainable AI systems, MUSE provides a scalable dataset to train models that understand scientific rationale. Industry practitioners can leverage these triplets to improve diagnostic tools and automated literature mining pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10974v1)
