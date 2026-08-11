---
title: SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning
published: 2026-08-08T06:48:08Z
authors: Keyang Zhong, Kuo Wang, Peng Liu, Quanlong Zheng, Junlin Xie, Zhijia Liang, Yanhao Zhang, Guanbin Li
url: http://arxiv.org/abs/2608.07959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning

## Abstract
Ultra-long egocentric video understanding requires reasoning over temporally sparse evidence distributed across hours or days, challenging current multimodal models with limited context and the grounding of key video segments. While Chain-of-Tool-Thought (CoTT) agent systems enable iterative retrieval and inspection, they suffer from error propagation due to rigid zoom-in strategies that lack recovery mechanisms. In this work, we address these challenges through SCOUT (Self-Checking Chain-Of-Tool-thought), a recovery-aware agentic framework introducing an adaptive policy that evaluates intermediate tool observations and dynamically trades off exploitation (zoom-in) and exploration (region switching), enabling robust multi-hop reasoning over extremely long horizons. However, training such multi-turn tool-using agents remains challenging, as existing RL methods rely on sparse outcome-level rewards and lack supervision over extended decision trajectories, resulting in suboptimal credit assignment for long-horizon reasoning. To address this, we develop UPS-GRPO, an uncertainty-prioritized policy optimization method that concentrates exploration on high-uncertainty post-tool states while preserving sample efficiency. We further introduce a turn-level advantage decomposition that integrates outcome rewards with tool-grounded temporal alignment rewards for improved credit assignment. Experiments show that SCOUT achieves state-of-the-art results on ultra-long egocentric benchmarks, while remaining competitive on shorter-horizon long-video settings.

## Metadata
- **Published**: 2026-08-08T06:48:08Z
- **Authors**: Keyang Zhong, Kuo Wang, Peng Liu, Quanlong Zheng, Junlin Xie, Zhijia Liang, Yanhao Zhang, Guanbin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07959v1)