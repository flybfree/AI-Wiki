---
title: The Announcement Carries the Cue: Markup, Boundaries, and the Notation of Pre-Training Corpora
url: http://arxiv.org/abs/2608.09093v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_03-43-30Z_TheAnnouncementCarriestheCue_Markup_Boundaries_and.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the arrangement and notation of document boundaries affect pre‑training model behavior. It introduces a deterministic metric called clean‑window survival to quantify unmarked text that still requires boundary inference. The study finds that converters preserve structure only when an explicit announcement precedes it, while deleting the annotation has negligible impact on prediction difficulty.

## Key Takeaways
- Clean‑window survival drops from 0.889 in C4 to 0.153 for vision‑converted PDF slices, showing that long unmarked text is a scarce resource and that institutional corpora retain more structural cues than consumer data.
- Deleting an announcement makes subsequent prose measurably harder to predict, indicating the annotation itself is the operative cue rather than its visual signature.
- Base models do not automatically add back deleted announcements when processing zero‑annotation texts, revealing a bounded null that limits the reliability of such preprocessing.

## Context
The paper addresses a gap in dataset documentation where text extraction choices are treated as neutral but they subtly shape model training. By measuring notation and survival rates across diverse corpora, it highlights how annotation practices influence downstream AI performance without being captured by standard data cards.

## Implications
Practitioners must record extractor identity and survival metrics on data cards to ensure reproducibility of pre‑training pipelines. Choosing format operators based on their training capability rather than fidelity will improve model robustness across varied document structures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09093v1)
