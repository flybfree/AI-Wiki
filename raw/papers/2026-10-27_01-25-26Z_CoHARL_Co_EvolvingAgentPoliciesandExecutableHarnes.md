---
title: CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning
published: 2026-10-27T01:25:26Z
authors: Jianwen Chen, Peng Xia, Kaide Zeng, Siwei Han, Zhen-Yu Zhang, Charles Fleming, Xinyu Ye, Huaxiu Yao
url: http://arxiv.org/abs/2610.36469v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning

## Abstract
Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the interface that generates its training experience unchanged. This motivates adapting the harness throughout policy training. We introduce CoHARL, a population-based reinforcement learning framework that co-evolves a shared policy and a population of executable harnesses. The policy learns from rollouts across the population, and a proposer uses its execution traces to revise harness code during training. CoHARL achieves a 27.6% mean resolved rate on SWE-rebench, improving over harness-only search by 6.4 percentage points. Experiments on SWE-bench Verified and Terminal-Bench 2.0 show gains in software engineering and terminal-based tasks. Under matched training budgets, CoHARL also outperforms searching for a harness once before RL and alternating policy updates with revisions to a single active harness.

## Metadata
- **Published**: 2026-10-27T01:25:26Z
- **Authors**: Jianwen Chen, Peng Xia, Kaide Zeng, Siwei Han, Zhen-Yu Zhang, Charles Fleming, Xinyu Ye, Huaxiu Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36469v1)