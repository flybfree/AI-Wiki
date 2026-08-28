---
title: Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification
published: 2026-08-27T16:12:23Z
authors: Jinghan Xu, Yikai Zhang, Aili Chen, Weiyuan Li, Jiaqing Liang, Deqing Yang
url: http://arxiv.org/abs/2608.27311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification

## Abstract
Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typically score every candidate on a fixed task set, wasting rollouts on unrelated behaviors and allowing aggregate scores to obscure specific regressions. We introduce HarnessLens, a budget-aware framework for automated harness evolution. HarnessLens jointly explores the task space and user-configurable components, derives candidate modifications from execution trajectories, and selectively verifies each candidate on behavior-relevant tasks using an attributable-evidence gate. Across three agent harnesses and four benchmarks, HarnessLens improves average held-out performance by 7.6-13.6% while consuming substantially less evaluation budget than competing baselines. These results demonstrate that behavior-aware verification with explicit attribution enables more reliable and sample-efficient harness evolution under constrained interaction budgets. Our code is available at https://github.com/jhxu5214/HarnessLens.

## Metadata
- **Published**: 2026-08-27T16:12:23Z
- **Authors**: Jinghan Xu, Yikai Zhang, Aili Chen, Weiyuan Li, Jiaqing Liang, Deqing Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27311v1)