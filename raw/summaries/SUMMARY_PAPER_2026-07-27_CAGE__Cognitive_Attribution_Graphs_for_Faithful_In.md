---
title: CAGE: Cognitive Attribution Graphs for Faithful Inline Citation Generation in Long-Form Question Answering
url: http://arxiv.org/abs/2607.24236v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_10-14-45Z_CAGE_CognitiveAttributionGraphsforFaithfulInlineCi.md
generated_at: 2026-07-27 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAGE, a two‑stage framework that tackles attribution ambiguity in long‑form question answering by generating cognitive attribution graphs before answer generation. Experiments on ASQA, ELI5, and ExpertQA demonstrate that CAGE attains state‑of‑the‑art performance, showing that explicit map‑aligned citation generation reduces evidence‑boundary overrun.

## Key Takeaways
- CAGE resolves combinatorial claim–document assignments by first constructing answer‑centered support subgraphs through a Cognitive Map Induction Model.  
- The Structured Citation Reasoning Model translates these semantic units into sentence‑level claims paired with map‑aligned citations, preventing overrun of evidence.  
- State‑of‑the‑art results on three benchmark datasets confirm that attention to attribution space contraction improves factual verification.

## Context
Long‑form QA systems increasingly rely on inline citations to make LLM answers verifiable, yet current methods often produce topically related but insufficient citations. This gap leads to ambiguous attributions and the risk of citing beyond document boundaries, undermining trust in generated content.

## Implications
For researchers, CAGE offers a principled way to embed citation generation within answer generation pipelines, reducing hallucinations and improving factual consistency. For industry practitioners, adopting such attribution‑aware models can enhance product reliability and user confidence in AI‑generated answers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24236v1)
