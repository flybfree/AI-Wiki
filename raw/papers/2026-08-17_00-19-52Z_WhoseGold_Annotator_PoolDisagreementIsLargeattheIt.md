---
title: Whose Gold? Annotator-Pool Disagreement Is Large at the Item Level, and Hidden by Small Leaderboards
published: 2026-08-17T00:19:52Z
authors: Anik Jha
url: http://arxiv.org/abs/2608.15980v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Whose Gold? Annotator-Pool Disagreement Is Large at the Item Level, and Hidden by Small Leaderboards

## Abstract
Preference benchmarks are built by hiring annotators, and the identity of those annotators is treated as an implementation detail. We measure what that detail buys. On the 2,885 MultiPref items where both pools are internally unanimous, so no tie-breaking convention is consulted at all, expert and crowd annotators assign a different majority label to 23.6% and name the opposite winner on 9.2%; on the 246 comparably unanimous MT-Bench cells, benchmark authors and recruited experts differ on 30.5% and reverse on 8.5%. Yet on both corpora the resulting model leaderboards are bit-identical: Kendall tau = 1.00 with zero of six models displaced.   That invariance is far weaker evidence than it looks, and we quantify how weak. Switching pools moves a model's win rate by 1.9pp (SD), one adjacent pair in our own leaderboard sits 0.8pp apart and had a 38% chance of swapping, and an item-level bootstrap displaces at least one model in 28% of resamples. The observed zero is the common outcome, not a property of aggregation: on the same measured perturbation, a ten-model leaderboard is displaced with probability 0.86 and a twenty-model leaderboard with probability 0.9997. Reporting a six-model leaderboard is safe; the safety does not generalise, and everything that consumes labels per item is not safe at any size. We make the distinction precise, show that a widely used dataset's stated assumption of no intra-group annotator variability is false, and show that an LLM judge tracks the crowd pool over the expert pool on all three models we test, including one from a different vendor. All code, per-call outputs, and pre-registered decision rules will be released upon acceptance.

## Metadata
- **Published**: 2026-08-17T00:19:52Z
- **Authors**: Anik Jha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15980v1)