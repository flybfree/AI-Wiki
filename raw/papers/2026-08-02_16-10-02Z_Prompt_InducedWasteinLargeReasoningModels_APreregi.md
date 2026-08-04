---
title: Prompt-Induced Waste in Large Reasoning Models: A Preregistered Two-Harness Benchmark of Coding Agents
published: 2026-08-02T16:10:02Z
authors: Sarel Weinberger, Amir Hozez
url: http://arxiv.org/abs/2608.01347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompt-Induced Waste in Large Reasoning Models: A Preregistered Two-Harness Benchmark of Coding Agents

## Abstract
Large reasoning models used as coding agents incur costs from deliberation, tool calls, and repeated agent turns, yet the causal effect of prompt wording on this spend has not been measured systematically. We present a preregistered benchmark across six large reasoning models, two real agent harnesses, and 24 deterministic coding tasks with hidden evaluators. Across 4,643 valid runs, including screening, stress, holdout, replication, and cross-provider studies, we find that prompt formulation can multiply reasoning cost without improving correctness. Asking the model to develop and compare several approaches is the most consistently wasteful instruction, increasing reasoning tokens by 2.4-7.4x across all models. Generic "think deeply" cues also increase deliberation by 1.6-2.2x, while a bounded-efficiency template specifying scope, acceptance criteria, and a stop condition is cost-neutral and can halve reasoning. Harness choice matters even more: identical model-task-prompt triples cost 5-30x more per success under Claude Code than under pi, mainly because of larger static prefixes and more turns. Misleading architectural hints are far costlier than irrelevant prose, and provider-side caching reduces billed cost without changing behavior, so it must not be treated as efficiency. Replications on Kimi-K3 and Claude Sonnet 5 preserve the main effect directions while revealing model-specific sensitivity to thinking and certainty cues. Overall, prompt wording and harness design materially affect agent cost, often with no gain in task success.

## Metadata
- **Published**: 2026-08-02T16:10:02Z
- **Authors**: Sarel Weinberger, Amir Hozez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01347v1)