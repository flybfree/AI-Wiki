---
title: V-Simba: Unleashing the Architectural Potential of RL in Visual Continuous Control
published: 2026-08-08T02:44:43Z
authors: Donghu Kim, Youngdo Lee, Hojoon Lee, Johan Obando-Ceron, Byungkun Lee, Aaron Courville, Pablo Samuel Castro, Jaegul Choo, Clare Lyle
url: http://arxiv.org/abs/2608.07870v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# V-Simba: Unleashing the Architectural Potential of RL in Visual Continuous Control

## Abstract
Improving sample efficiency remains a core challenge in reinforcement learning (RL), especially in real-world settings like robotics, where data collection is costly. This challenge is pronounced in visual RL, where high-dimensional inputs often obscure learning signals. While prior work in visual RL has focused on algorithmic solutions, such as better dynamics models or exploration strategies, recent advances in state-based RL show that architectural design alone can lead to significant gains in sample efficiency. This raises an important question: Can these architectural principles transfer to visual RL? In response, we introduce V-Simba, a simple yet effective visual RL architecture inspired by the Simba architecture from state-based RL. Built on top of Soft Actor-Critic (SAC) with data augmentation, V-Simba modifies the architecture by adding normalization layers to stabilize training and using pointwise convolutions to reduce computation. Despite its simplicity, V-Simba matches or outperforms the state-of-the-art methods across the DMC, Adroit, and Meta-World benchmarks, while being more computationally efficient than DrQ-v2. We make our code publicly available at https://github.com/DAVIAN-Robotics/V-Simba.

## Metadata
- **Published**: 2026-08-08T02:44:43Z
- **Authors**: Donghu Kim, Youngdo Lee, Hojoon Lee, Johan Obando-Ceron, Byungkun Lee, Aaron Courville, Pablo Samuel Castro, Jaegul Choo, Clare Lyle
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07870v1)