---
title: The Kinetics of Training: A Driven-Nucleation Rate Law for Emergence, Plasticity Loss, and Circuit Control in Language Models
url: http://arxiv.org/abs/2607.27281v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_13-46-52Z_TheKineticsofTraining_ADriven_NucleationRateLawfor.md
generated_at: 2026-07-30 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the emergence of capabilities in large language models by identifying a stochastic joint‑alignment event that is the rate‑limiting step for capability formation. It demonstrates that partial credit predicts capability better than random non‑part heads and shows that reinitializing only query‑key slices restores learnability while value slices do not.

## Key Takeaways
- No‑partial‑credit joint alignment is the rate‑limiting step of capability formation; missing parts delay emergence regardless of circuit size.
- Ablating one part reduces capability to 17 % in discriminating cells, whereas random non‑part heads give 100 %, showing partial credit matters.
- Reinitializing only query‑key slices restores learnability (6/6) whereas value slices fail (0/6), indicating the mechanism is localized.

## Context
The work provides a mechanistic explanation for emergent capabilities in large language models, moving beyond empirical scaling laws to a stochastic alignment process that can be targeted. This insight helps researchers understand why certain configurations succeed while others do not.

## Implications
For practitioners, focusing on query‑key slice reinitialization and minimizing missing parts may improve model performance. The findings also suggest training schedules where noise is annealed could better align circuits with the required stochastic event.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27281v1)
