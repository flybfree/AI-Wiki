---
title: TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions
published: 2026-08-15T19:44:59Z
authors: Md Fazley Rafy
url: http://arxiv.org/abs/2608.15391v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions

## Abstract
Large language model (LLM)-assisted energy-management tools can translate natural-language context into structured grid commands, but syntactic validity does not imply physical admissibility. This paper presents TwinGridShield, a model-independent runtime authorization layer that evaluates each proposed action in a deterministic network twin before release. The prototype checks connectivity, branch-flow, generator, and load-shedding invariants and records each decision in a hash-chained log. A controlled IEEE 14-bus study evaluates single-step switching, redispatch, and load-shedding actions using DC power flow and experimentally assigned branch ratings. In the matched-model experiment, a stochastic proposal source configured to select an unsafe action with probability p=0.84 produced 421 unsafe proposals in 500 attacked-condition trials, a realized rate of 84.2%. This value characterizes the configured surrogate and is not an empirical measurement of LLM prompt-injection susceptibility. TwinGridShield produced 0 unsafe releases in those 500 trials. Because action labeling and authorization used the same DC model, system state, branch ratings, and encoded constraints, this result verifies conformance of the implementation to its encoded authorization predicate rather than safety under model error. The principal robustness evaluation therefore introduces model mismatch. Unsafe acceptance reached 5.63% under bounded +20% and -20% per-bus load-measurement error and 30.09% when actual branch ratings were 20% below modeled ratings.

## Metadata
- **Published**: 2026-08-15T19:44:59Z
- **Authors**: Md Fazley Rafy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15391v1)