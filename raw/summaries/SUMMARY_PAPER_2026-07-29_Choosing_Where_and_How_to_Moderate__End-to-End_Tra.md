---
title: Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting
url: http://arxiv.org/abs/2607.26200v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_19-05-24Z_ChoosingWhereandHowtoModerate_End_to_EndTrade_offs.md
generated_at: 2026-07-29 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how to place content‑moderation filters and what actions follow a flag, using two end‑to‑end customer‑outcome metrics: usefulness (the fraction of turns that receive a non‑harmful, relevant response) and harmful exposure (the fraction that receive a harmful response). Experiments on human‑labelled product data and the public ToxicChat benchmark compare three placement strategies—input only, response only, and input + response hard blocking—and find that response‑only filtering maximizes usefulness while input + response achieves lower harmful exposure. Adding a rewrite step recovers most blocked traffic without increasing harmful exposure.

## Key Takeaways
- Response only achieves the highest filter‑only usefulness in both evaluation settings.
- Input plus response hard blocking reduces harmful exposure but blocks more traffic than response only alone.
- Replacing response only with response plus rewrite restores most lost interactions while keeping observed harmful exposure counts unchanged, though this is not a formal equivalence.

## Context
The study addresses a gap where component‑level accuracy metrics are insufficient for real‑world deployment; moderation must balance safety, user experience, and latency. By focusing on end‑to‑end outcomes rather than isolated classifier scores, the work aligns with broader AI research that emphasizes holistic system design over individual model evaluation.

## Implications
Practitioners should adopt configuration choices based on specific deployment constraints rather than applying a one‑size‑fits‑all moderation rule. The findings suggest that lightweight probing routing can improve response times without sacrificing safety, offering a practical path for integrating moderation into large language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26200v1)
