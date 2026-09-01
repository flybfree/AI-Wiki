---
title: HANIA: Planner-Guided Multimodal Graph Evidence Selection for Grounded Question Answering
url: http://arxiv.org/abs/2608.29088v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_06-38-21Z_HANIA_Planner_GuidedMultimodalGraphEvidenceSelecti.md
generated_at: 2026-08-31 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HANIA, a planner‑guided multimodal graph framework that selects concise visual and textual evidence for grounded question answering without fine‑tuning. It demonstrates competitive performance on ScienceQA by using structured evidence planning and compact graph retrieval.

## Key Takeaways
- HANIA extracts only question‑relevant visual statements from images while allowing abstention, producing a minimal evidence set that improves grounding quality.
- The two‑group finite‑state planner coordinates descriptive and relational triples into an input‑grounded multimodal graph to support multi‑step reasoning.
- Coverage‑aware pruning balances relevance, graph confidence, concept coverage, and modality diversity to keep the evidence compact.

## Context
Multimodal QA systems often suffer from noisy or redundant evidence when processing long unstructured contexts. Flat retrieval methods ignore relational links needed for complex questions, limiting answer accuracy. This work addresses these challenges by integrating a planner that explicitly models dependencies between visual and textual statements.

## Implications
Practitioners can deploy HANIA with frozen models to achieve high‑quality answers without dataset‑specific fine‑tuning, reducing development cost. The approach also offers a transparent evidence budget that can be adapted for resource‑constrained applications such as mobile or edge AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29088v1)
