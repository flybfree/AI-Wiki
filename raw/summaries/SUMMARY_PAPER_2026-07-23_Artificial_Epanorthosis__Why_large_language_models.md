---
title: Artificial Epanorthosis: Why large language models overuse a classical rhetorical figure, and how to mitigate it
url: http://arxiv.org/abs/2607.21498v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_16-47-39Z_ArtificialEpanorthosis_Whylargelanguagemodelsoveru.md
generated_at: 2026-07-23 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why large language models frequently employ epanorthosis, a rhetorical figure of self‑correction, and proposes an Epanorthosis Index to measure its overuse. It finds that the phenomenon is driven by training data rich in promotional prose and RLHF preferences for confident phrasing rather than left‑to‑right generation. The study shows mis‑calibration across genres, with overshoot in oratory and undershoot in informal Q&A.

## Key Takeaways
- Models overuse epanorthosis about twofold in oratory and up to threefold in Italian, while underusing it in casual Q&A writing.
- A lightweight LoRA adapter can cut the figure by half to three‑quarters with a single instruction line, and supervised fine‑tuning removes it almost entirely, scaling back to human rates.
- The goal is calibration to human rates per genre rather than complete elimination.

## Context
This research addresses a subtle stylistic bias in AI text generation that reflects broader concerns about model alignment with human communication norms. By quantifying epanorthosis, the work contributes to understanding how training distribution and reinforcement learning shape linguistic style.

## Implications
Practitioners can use lightweight adapters to fine‑tune tone without large compute costs, improving user trust in AI outputs. The paper underscores that mitigating overuse is less about removing the figure than aligning it with human expectations across contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21498v1)
