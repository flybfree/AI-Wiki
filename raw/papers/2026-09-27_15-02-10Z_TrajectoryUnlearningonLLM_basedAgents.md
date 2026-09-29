---
title: Trajectory Unlearning on LLM-based Agents
published: 2026-09-27T15:02:10Z
authors: Yingdan Shi, Ren Wang
url: http://arxiv.org/abs/2609.33639v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory Unlearning on LLM-based Agents

## Abstract
Existing large language model (LLM) unlearning has focused primarily on removing specific knowledge, such as harmful facts, private data, or copyrighted content. However, as LLMs are increasingly deployed as autonomous agents, a fundamental yet overlooked problem emerges: beyond suppressing what an agent knows, an agent should not reproduce undesired behaviors through its action trajectories. In this work, we introduce trajectory-level unlearning, a new problem formulation that targets the removal of specific action trajectories in long-horizon agentic tasks, rather than factual knowledge. We identify two fundamental challenges that distinguish trajectory unlearning from knowledge unlearning: (1) our unlearning target is what the agent \emph{does}, not what it \emph{says}; and (2) trajectories are sequentially dependent action sequences that cannot be decomposed into isolated prompt-response pairs without losing inter-step structure. To address these challenges, we propose Group-injected Relative Policy Optimization (GiRPO), which injects forget trajectories into the policy rollout group with penalized rewards and isolates the normalization statistics, yielding a stable and bounded unlearning signal that does not corrupt gradient updates for normal task trajectories. We construct trajectory unlearning benchmarks from two application scenarios, household tasks (ALFWorld) and online shopping (WebShop), and design three complementary metrics for evaluating forgetting quality and model utility. Experiments on ALFWorld and WebShop demonstrate that GiRPO effectively unlearns target trajectories while preserving task success rates, outperforming existing knowledge-unlearning baselines on both forgetting quality and task utility.

## Metadata
- **Published**: 2026-09-27T15:02:10Z
- **Authors**: Yingdan Shi, Ren Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33639v1)