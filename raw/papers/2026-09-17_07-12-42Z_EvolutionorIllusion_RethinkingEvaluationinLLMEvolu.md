---
title: Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search
published: 2026-09-17T07:12:42Z
authors: Tal Oved, Roi Pony, Oshri Naparstek, Udi Barzelay
url: http://arxiv.org/abs/2609.19799v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search

## Abstract
LLM-driven evolutionary search finds programs by launching seeds and iterating each one. Papers report a single budget setting, usually one seed run for a fixed number of iterations, and rank methods from that one point. We show this is not enough. We evaluate three evolutionary search strategies on five optimization tasks, commonly used by papers in the genre to report results. We run the analysis over a full grid of seeds and iterations. Our findings suggest that the best way to split a fixed budget between more seeds (width) and more iterations (depth) changes with the strategy, the task, and the total budget. Furthermore, we observe that the ranking of strategies also changes with the budget. On one task the strategy that looks worst at one seed is best at forty seeds. On another the best number of iterations is well below the value common in practice, so extra depth wastes budget that more seeds would turn into score. We provide a measurement protocol that reports the seeds-by-iterations frontier and practical guidance for using it.

## Metadata
- **Published**: 2026-09-17T07:12:42Z
- **Authors**: Tal Oved, Roi Pony, Oshri Naparstek, Udi Barzelay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19799v1)