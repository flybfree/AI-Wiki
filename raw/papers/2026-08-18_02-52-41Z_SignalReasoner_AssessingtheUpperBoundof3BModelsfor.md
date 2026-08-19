---
title: SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning
published: 2026-08-18T02:52:41Z
authors: Guozheng Sun
url: http://arxiv.org/abs/2608.17301v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning

## Abstract
Post-training with supervised chain-of-thought fine-tuning and reinforcement learning from verifiable rewards has substantially improved the mathematical reasoning capabilities of large language models (LLMs). However, their application to signal processing problems remains relatively under-explored. This report investigates reinforcement fine-tuning strategies for adapting Qwen2.5-3B-Base to graduate-level signal mathematical problems from WirelessMATHBench-XL, a comprehensive benchmark for mathematical reasoning in this domain. We examine two training paradigms: (i) direct reinforcement learning (RL) on WirelessMATHBench-XL with verifiable rewards; and (ii) supervised fine-tuning (SFT) on a distilled wireless-domain chain-of-thought corpus, followed by the same domain-specific RL stage. Across both paradigms, we benchmark Group Relative Policy Optimization (GRPO), Group Sequence Policy Optimization (GSPO), and Geometric-Mean Policy Optimization (GMPO). We aim to assess whether domain-aware CoT SFT serves as an effective initialization for subsequent RL, and whether GSPO or GMPO offer advantages in stability or accuracy over GRPO for signal reasoning tasks. Our best model achieves an overall accuracy of 39.12\%, representing a more than threefold improvement over the untrained Base model (12.37\%).

## Metadata
- **Published**: 2026-08-18T02:52:41Z
- **Authors**: Guozheng Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17301v1)