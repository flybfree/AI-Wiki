---
title: Cross-Benchmark Generalization in Long-Horizon Agents
published: 2026-07-31T18:05:36Z
authors: Sushant Mehta, Logan Ritchie, Liudas Panavas, Edwin Chen
url: http://arxiv.org/abs/2608.00181v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Benchmark Generalization in Long-Horizon Agents

## Abstract
For reinforcement learning (RL) in self-contained environments, a policy can get rewards by exploiting environment-specific regularities (tool schemas, grader parsing, task templates) rather than by acquiring transferable skill, and an in-distribution holdout shares those regularities. We argue that the discriminating question is behavioral, namely how a trained agent acts, and that cross-benchmark transfer is the right place to look for it. We post-train an open-weight mixture-of-experts model (Qwen3.5-122B-A10B) on 363 long-horizon Model Context Protocol (MCP) tasks across 27 categories, using a two-stage SFT-then-RL pipeline. Toolathlon performance informed the initial base-family and SFT-teacher choices, but no external-benchmark task or grader entered training and no external score informed the reward, training hyperparameters, trained-checkpoint selection, or stopping. At greedy pass@1, the trained model improves over the base on five reported external evaluations: Toolathlon (+9.6 pp), $τ^2$-Bench (+5.3 pp), BFCL-V4 (+3.5 pp), SWE-Bench Pro (+5.8 pp), and Terminal-Bench 2 (+2.8 pp). Both software-engineering benchmarks improve despite the training collection containing no software-engineering tasks. An exploratory paired-trajectory analysis identifies four recurring behavioral differences (more careful local-goal formation, building goal-relevant working state, keeping parent goals stable through local repairs, and verifying completion) that appear in analogous forms across office workflows and code. These results provide descriptive evidence that long-horizon multi-tool post-training can change ways of working that transfer beyond its training domain.

## Metadata
- **Published**: 2026-07-31T18:05:36Z
- **Authors**: Sushant Mehta, Logan Ritchie, Liudas Panavas, Edwin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00181v1)