---
title: TRCA: Transition-wise Rubric Credit Assignment for Long-horizon LLM Agents
published: 2026-08-17T06:19:12Z
authors: Huan Zhang, Mingju Chen, Dongxu Zhou, Can Lv, Heng Chang, Sen Cui, Faguo Wu, Shiji Zhou
url: http://arxiv.org/abs/2608.16156v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRCA: Transition-wise Rubric Credit Assignment for Long-horizon LLM Agents

## Abstract
Long-horizon large language model (LLM) agents are typically optimized with sparse terminal outcomes, making fine-grained credit assignment across multi-step interactions difficult. Existing approaches either rely on process evaluators, which incur annotation and inference costs, or derive step-level credit from successful trajectories. However, successful trajectories are extremely scarce during early-stage reinforcement learning, substantially weakening anchor-based methods. We propose Transition-wise Rubric Credit Assignment (TRCA), which derives step-level supervision directly from action-induced transitions without learned evaluators or successful anchors. TRCA evaluates each transition using Evidence, Execution, and Invalidity rubrics to capture task-relevant information acquisition, valid task execution, and invalid or regressive behavior. From these judgments, Foundational Rubric Reward measures local transition quality, while Breakthrough Rubric Reward tracks newly covered Evidence and Execution conditions to reward incremental task progress. Combined with terminal outcomes, these signals produce fine-grained step-level advantages for policy optimization. Experiments on ALFWorld, WebShop, and seven search-augmented question-answering benchmarks show consistent improvements over the evaluated baselines. With Qwen2.5-7B-Instruct, TRCA improves the WebShop score by 6.0%-12.6%; with Qwen2.5-3B-Instruct, it improves the average SearchQA score by 1.9%-18.3%. These results demonstrate the effectiveness of transition-wise rubric credit assignment for long-horizon tasks with sparse successful anchors.

## Metadata
- **Published**: 2026-08-17T06:19:12Z
- **Authors**: Huan Zhang, Mingju Chen, Dongxu Zhou, Can Lv, Heng Chang, Sen Cui, Faguo Wu, Shiji Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16156v1)