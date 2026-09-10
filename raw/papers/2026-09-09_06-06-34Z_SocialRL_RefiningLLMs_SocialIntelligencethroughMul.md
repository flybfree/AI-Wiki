---
title: SocialRL: Refining LLMs' Social Intelligence through Multi-turn Reinforcement Learning and Reward Design
published: 2026-09-09T06:06:34Z
authors: Jianing Wang, Xintao Wang, Aili Chen, Jie Shi, Hongcheng Guo, Jun Gao, Wenxuan Zhao, Chengkun Lang, Yuanli Guo, Yanghua Xiao
url: http://arxiv.org/abs/2609.09764v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SocialRL: Refining LLMs' Social Intelligence through Multi-turn Reinforcement Learning and Reward Design

## Abstract
Social intelligence enables agents to read social context, infer intent, and adapt over sustained dialogue. As language models become autonomous collaborators, it is central to building effective and trustworthy human-AI interaction. Existing reinforcement learning methods optimize single-turn utterances and sparse outcome rewards, producing short-sighted policies that struggle to manage goal-relationship tensions across multi-turn interactions. We propose SocialRL, a multi-turn reinforcement learning framework addressing both challenges. First, we apply multi-turn reinforcement learning using PPO that propagates delayed outcome rewards back to each turn, enabling long-horizon planning. Second, we design six process reward dimensions capturing the goal-relationship trade-off, including goal advancement, relational attunement, contextual coherence, etc. A reward model dynamically generates fine-grained scoring criteria for each dimension, while a stage-aware weight schedule prioritizes relationship-building in early turns, goal advancement mid-way, and balanced closure late. Across multiple social-dialogue benchmarks, SocialRL improves Goal Achievement by an average of 9.2 percentage points over the corresponding Base models. These results demonstrate the effectiveness of SocialRL across synthetic and real social scenes, as well as standard and challenging social scenarios.

## Metadata
- **Published**: 2026-09-09T06:06:34Z
- **Authors**: Jianing Wang, Xintao Wang, Aili Chen, Jie Shi, Hongcheng Guo, Jun Gao, Wenxuan Zhao, Chengkun Lang, Yuanli Guo, Yanghua Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09764v1)