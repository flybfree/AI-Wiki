---
title: PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments
published: 2026-08-14T16:25:43Z
authors: Yuhao Zhan, Bingxiang He, Zecong Tang, Chaojun Xiao
url: http://arxiv.org/abs/2608.14441v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments

## Abstract
Self-evolving agents improve future behavior from interaction experience, yet existing evaluations typically optimize under fixed execution conditions and do not test recovery after those conditions change. To address this gap, we introduce PACE-Bench (Physics Adaptation via Code Evolution), a simulator-grounded benchmark of 144 source-to-target adaptation pairs across six physics domains. Each pair links a source environment to a mutated target environment with the same goal and interface. A code-driven design that succeeds in the source fails in the target, where agents must iteratively adapt it into a working target design using diagnostic sandbox feedback within a limited attempt budget. We compare ten self-evolving methods from four paradigms. The benchmark remains far from saturated: Reflexion + Qwen3-14B succeeds on only 35.9\% of full-benchmark pairs, while GPT-5.5 solves 66.7\% of the Statics subset under the full budget. Together, these results show that simulator-grounded reflection is more reliable than unverified self-revision, while memory anchors agents to early designs and broad tree search explores without converging. Even revealing exact physical changes does not raise the performance ceiling, pointing to mechanism redesign rather than parameter inference as the central bottleneck. Data and code are available at https://github.com/thunlp/PACE-Bench.

## Metadata
- **Published**: 2026-08-14T16:25:43Z
- **Authors**: Yuhao Zhan, Bingxiang He, Zecong Tang, Chaojun Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14441v1)