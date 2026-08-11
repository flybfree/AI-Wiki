---
title: Opportunity Is Not Realizability: Selection-Valid Diagnostics for Multi-LLM Routing
published: 2026-08-08T17:53:43Z
authors: Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb
url: http://arxiv.org/abs/2608.08265v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Opportunity Is Not Realizability: Selection-Valid Diagnostics for Multi-LLM Routing

## Abstract
Oracle routing measures how much a pool of language models could gain from per-query selection, but the diagnostic has two flaws: testing against a best fixed model selected on the same examples invalidates paired inference, and a full-information oracle sees outcomes no deployable router observes. We separate three estimands (outcome-oracle opportunity, the Bayes-optimal gain from a declared pre-answer signal, and the held-out gain of a learned router) and prove selection-valid confidence intervals that survive choosing the best fixed model or the best member of a router family, a signal-information sandwich, and a $(1-1/e)$ greedy guarantee for building compact pools from submodular complementary coverage. On eight checkpoints from six families over four benchmarks, selection-valid intervals certify a population oracle gap of $9.7$--$30.7$ points on every task, yet the strongest deployable prompt router recovers only $7.5$--$14.4\%$ of it, and the simultaneous interval for the best of eleven tested policies has lower limit zero throughout. The realizable share of oracle opportunity is small and certifiable: strong routers beat the best fixed model, and most of the gap remains.

## Metadata
- **Published**: 2026-08-08T17:53:43Z
- **Authors**: Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08265v1)