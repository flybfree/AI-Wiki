---
title: Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization
published: 2026-08-11T09:17:22Z
authors: Tal Oved, Roi Pony, Oshri Naparstek, Udi barzelay
url: http://arxiv.org/abs/2608.10694v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization

## Abstract
Evolutionary optimization of LLM prompts and agentic programs (e.g., GEPA) is dominated by fitness evaluation: scoring each candidate runs an answering LLM over a validation set, so the evaluator's price tier dictates total search cost. We restructure that search by decoupling the three roles an LLM plays, running the high-volume answering role on the cheapest tier, reserving a strong model for the rare reflection/variation operator, then exploiting upward cross-tier transfer to deploy the cheaply evolved prompt on a stronger target. We contribute a cost-controlled characterization of when cheap-tier search substitutes for target-tier search, and where it fails. Across four tasks (HotpotQA, IFBench, LiveBench-Math, HoVer) and eleven models in four model families, the resulting prompt matches or exceeds same-tier optimization while placing over 96% of search tokens on the cheapest tier, at 5.6-14x lower search cost, rising to 25-54x where reasoning tiers emit long chains of thought on every fitness call.

## Metadata
- **Published**: 2026-08-11T09:17:22Z
- **Authors**: Tal Oved, Roi Pony, Oshri Naparstek, Udi barzelay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10694v1)