---
title: HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution
published: 2026-09-01T07:31:18Z
authors: Wen Jiang, Mingmin Chu, Yimeng Tian, Qianxin Zhang, Haofei Yang, Rui Yang, Yang Liu, Tao Lv, Fangming Li
url: http://arxiv.org/abs/2609.00829v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution

## Abstract
Self-evolving agents advance toward autonomy by optimizing their harness---prompts, skills, tools, and execution logic---based on environmental feedback. This paradigm, however, is hampered by three challenges: \textit{credit assignment failure}, where terminal success/failure feedback makes it ambiguous which step caused the error; \textit{shortcut learning}, where agents memorize task-specific patterns rather than acquire generalizable capabilities; and \textit{catastrophic forgetting}, where unguarded updates degrade previously acquired competence. In this paper, we introduce HarnessEvolve, a self-evolving framework that learns from reference trajectories to achieve reliable agent self-evolution. HarnessEvolve decouples the execution agent from the evolutionary pipeline, assigning execution, evaluation, optimization, and gating to independent agent modules, enabling generalizable and stable harness improvements. Specifically, HarnessEvolve overcomes credit assignment failure by generating reference trajectories (execution paths produced when given the ground-truth answers) and aligning failed executions against them to extract error signals, which are clustered to reveal systematic failure patterns. To prevent shortcut learning and catastrophic forgetting, candidate harness updates must pass two gates: a quality gate that filters data leakage and prompt bloat, and a performance gate that accepts each update if it improves on the current batch without degrading recent batches, with epoch-end validation on a held-out set selecting the best-performing accepted agent snapshot. We conduct extensive experiments on several benchmarks spanning open-domain and enterprise scenarios, using different models and agent frameworks. Results demonstrate that HarnessEvolve consistently outperforms state-of-the-art baselines across all benchmarks and settings, confirming reliability across task domains.

## Metadata
- **Published**: 2026-09-01T07:31:18Z
- **Authors**: Wen Jiang, Mingmin Chu, Yimeng Tian, Qianxin Zhang, Haofei Yang, Rui Yang, Yang Liu, Tao Lv, Fangming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00829v1)