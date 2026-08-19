---
title: Authorization Before Context: A Model-Neutral Audience Boundary Against Cross-Audience Memory Leakage in Agentic Systems
published: 2026-08-17T21:31:10Z
authors: Sibo Liu
url: http://arxiv.org/abs/2608.17148v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Authorization Before Context: A Model-Neutral Audience Boundary Against Cross-Audience Memory Leakage in Agentic Systems

## Abstract
A personal language agent learns a fact from one audience and may later place it in the prompt it assembles for another. This memory-to-context step is an attack surface: ambiguous or inconsistent channels, cross-audience prying, and poisoned memory can each cause the system to assemble context containing a fact relevant to the query yet unauthorized for the current viewers. We introduce authorization before context: a single, anti-monotone audience-membership rule applied at the memory-to-context transition. Each item carries the audience present when it was recorded; the current viewer set is read from channel metadata and falls back to public when ambiguous; and the item is admitted only when every current viewer already belonged to its audience. We prove that this rule gives every participant cross-channel recall while ensuring, by exclusion rather than by model behavior, that nothing recorded for a narrower audience reaches a broader one and that poisoned memory cannot widen its own audience. The boundary is a model-neutral invariant on the exact assembled context: a forbidden fact must be absent before the model is called. On a synthetic Contextual-Integrity suite, no forbidden fact entered the context our boundary assembled, whereas unscoped baselines included such facts by construction; we further audit that every read path fails closed. The evidence is preliminary and synthetic.

## Metadata
- **Published**: 2026-08-17T21:31:10Z
- **Authors**: Sibo Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17148v1)