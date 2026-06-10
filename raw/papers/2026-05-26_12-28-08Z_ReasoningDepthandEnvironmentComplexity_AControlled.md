---
title: 'Reasoning Depth and Environment Complexity: A Controlled Study of RLVR Data Allocation across Logical Reasoning Tasks'
published: 2026-05-26T12:28:08Z
authors: Yihua Zhu, Qianying Liu, Fei Cheng, Jiaxin Wang, Akiko Aizawa, Sadao Kurohashi, Hidetoshi Shimodaira
url: http://arxiv.org/abs/2605.26934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning Depth and Environment Complexity: A Controlled Study of RLVR Data Allocation across Logical Reasoning Tasks

## Abstract
Reinforcement learning with verifiable rewards (RLVR) has become central to post-training reasoning models, yet a key limitation of existing studies is their narrow view of the reasoning space: difficulty is treated as reasoning depth alone, and reward is concentrated on forward deductive state tracking. We instead characterize the reasoning space along two dimensions. Difficulty. Beyond reasoning depth, we study environment complexity, where models must identify the correct path amid distractors and interacting structures. Rewarded reasoning form. We consider four abilities core to real-world reasoning: deductive state tracking, abductive recovery of hidden events or facts, inductive rule induction, and analogical transfer. To disentangle these factors, we construct a synthetic knowledge-graph environment with controlled pre- and post-training distributions, where each instance varies along depth, complexity, and task family. Three findings emerge: joint depth-complexity coverage outperforms single-axis recipes; reasoning families respond non-uniformly, with abductive reasoning degrading outside the RL-covered region and task correlations clustering into deductive-abductive and inductive-analogy pairs; and uniform mixing outperforms staged curricula under a fixed budget. We also find that recent off-the-shelf models exhibit the same deductive-over-abductive asymmetry, suggesting that this gap is not merely an artifact of our controlled setup.

## Metadata
- **Published**: 2026-05-26T12:28:08Z
- **Authors**: Yihua Zhu, Qianying Liu, Fei Cheng, Jiaxin Wang, Akiko Aizawa, Sadao Kurohashi, Hidetoshi Shimodaira
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.26934v1)