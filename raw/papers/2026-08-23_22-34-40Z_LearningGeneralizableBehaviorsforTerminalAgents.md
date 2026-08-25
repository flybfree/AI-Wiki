---
title: Learning Generalizable Behaviors for Terminal Agents
published: 2026-08-23T22:34:40Z
authors: Yihang Yao, Bo Pang, Xuan Phi Nguyen, Ding Zhao, Shafiq Joty, Semih Yavuz
url: http://arxiv.org/abs/2608.22631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Generalizable Behaviors for Terminal Agents

## Abstract
Terminal agents are a compelling application of large language models (LLMs), with the potential to integrate deeply into users' daily workflows. Reinforcement learning (RL) is a key technique for improving their capabilities, making scalable training environments a central challenge. Since public real-user interaction data are scarce, synthetic environments provide a practical alternative, but often suffer from domain gaps and limited fidelity, leading to poor generalization. Existing work mainly scales the quantity and diversity of synthetic environments, while reward-signal quality and the mechanisms governing generalization remain under-explored. We study how RL improves terminal agents and propose the Agentic Compositional Generalization hypothesis: rather than teaching new domain-specific skills from scratch, RL primarily shapes high-level decision-making behaviors that compose and route low-level skills acquired during pre-training and supervised fine-tuning (SFT). This account is consistent with our empirical results and suggests that verifier quality, which determines which behaviors are reinforced, is more important than simply increasing environment quantity or diversity. Motivated by this insight, we propose River, a simple training recipe that improves reward quality by filtering low-quality environments and augmenting outcome rewards with process-level behavior regularization. Using this recipe, our RL-trained agent achieves the best performance among evaluated open-source RL-trained 8B models across four terminal-agent benchmarks. River also generalizes across model families, scales, agent harnesses, and RL objectives. Using fewer than 30% of the TMax training environments, River improves RL gains by 106% and 30% on average for models ranging from 2B to 27B on Terminal-Bench-Lite and Terminal-Bench-v2.1, respectively.

## Metadata
- **Published**: 2026-08-23T22:34:40Z
- **Authors**: Yihang Yao, Bo Pang, Xuan Phi Nguyen, Ding Zhao, Shafiq Joty, Semih Yavuz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22631v1)