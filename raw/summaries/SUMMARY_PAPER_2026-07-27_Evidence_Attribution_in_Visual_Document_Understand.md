---
title: Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels
url: http://arxiv.org/abs/2607.24651v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_16-49-36Z_EvidenceAttributioninVisualDocumentUnderstandingwi.md
generated_at: 2026-07-27 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the failure of visual document understanding models to correctly attribute answers to evidence regions stems from limitations in expressing coordinates, and it compares a coordinate interface with a language‑only interface that relies on text quoting and a layout parser. On a bilingual CiteVQA subset, the new approach improves recall dramatically, reduces hallucination roughly in half, while preserving answer quality. The authors also train an 8B model using a gradient‑policy optimization to quote better evidence without any region labels.

## Key Takeaways
- Evidence recall jumps from at most 8 points to between 26 and 47 by replacing coordinates with text quotes linked to page regions.
- Hallucination rates roughly halve, indicating fewer incorrect or fabricated evidence citations.
- The model’s answer quality remains unchanged despite the shift in attribution method.

## Context
Current vision‑language systems often rely on bounding‑box outputs that are brittle for long documents and require costly manual annotation. This study shows a viable alternative using only textual cues and existing layout parsers, reducing reliance on expensive region‑level supervision.

## Implications
Practitioners can implement this quote‑and‑retrieve pipeline to build more robust document QA systems without extensive labeled data. The approach lowers development costs and improves reliability for enterprise applications that need accurate evidence attribution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24651v1)
