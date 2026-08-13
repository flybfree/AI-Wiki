---
title: Benchmarking LLM Judges for Mobile Agent Evaluation
published: 2026-08-11T21:00:46Z
authors: Ziqiang Wan, Li Gu, Zhixiang Chi, Zhi Liu, Seyed Mehdi Ayyoubzadeh, Yuanhao Yu, Yang Wang
url: http://arxiv.org/abs/2608.11434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking LLM Judges for Mobile Agent Evaluation

## Abstract
Mobile agent benchmarks increasingly rely on LLM-based judges to evaluate task completion, yet the reliability of these judges on mobile agent trajectories remains largely unexamined. We introduce MobileJudgeBench, a benchmark for systematically evaluating LLM-as-judge methods on mobile agent trajectories. Our benchmark comprises 931 human-annotated trajectories spanning 6 mobile agent benchmarks, 4 agent models, and 68 apps. We evaluate 6 judge methods (five adapted from SPA-Bench, A3 with two modes, AndroidArena, and AgentRewardBench, plus a simple baseline we design) across multiple LLM backends. Our experiments reveal three key findings. First, a simple baseline judge with sampled screenshots is competitive with, and often exceeds, purpose-built methods, indicating that more elaborate judge pipelines do not consistently improve judge quality; among competitive methods, the LLM backbone is the primary driver. Second, benchmark quality metrics reliably predict real-world judge utility: they correlate with both agent ranking fidelity for evaluation and downstream performance when judges serve as reward signals for on-policy reinforcement learning. Third, failure analysis across two LLM backends uncovers qualitatively opposite failure profiles, one conservative and the other permissive, linked to the backbone's precision-recall characteristics.

## Metadata
- **Published**: 2026-08-11T21:00:46Z
- **Authors**: Ziqiang Wan, Li Gu, Zhixiang Chi, Zhi Liu, Seyed Mehdi Ayyoubzadeh, Yuanhao Yu, Yang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11434v1)