---
title: Parallel Thinking for Large Language Model with Path Diversity
published: 2026-10-21T09:51:42Z
authors: Jiaru Qian, Yihong Dong, Xue Jiang, Chun-Wah Hsu, Zhi Jin, Ge Li
url: http://arxiv.org/abs/2610.29501v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Parallel Thinking for Large Language Model with Path Diversity

## Abstract
Parallel thinking has emerged as a promising paradigm for enhancing the reasoning capabilities of Large Language Models (LLMs) by exploring multiple reasoning paths simultaneously. However, we identify that parallel thinking via Reinforcement Learning (RL) typically suffers from the mode collapse of reasoning paths, where parallel thinking trajectories degenerate into similar ones. This homogeneity undermines the fundamental motivation of parallel thinking, that is, maintaining multiple hypotheses concurrently to prevent premature loss into a suboptimal solution. In this paper, we propose Diverse Parallel Thinking (DPT), a simple yet effective RL approach for parallel thinking designed to encourage path diversity. DPT rewards the model to develop distinct reasoning strategies by penalizing the prefix similarity of parallel thinking paths, thereby enhancing a more comprehensive exploration of the reasoning space. We conduct various experiments and analyses across multiple reasoning benchmarks to demonstrate the effectiveness of DPT. Results show that DPT successfully outperforms previous parallel thinking methods, achieving state-of-the-art performance over baselines. We validate path diversity as a key element to improve parallel thinking. Our code is available at https://github.com/JiaruQian/DPT.

## Metadata
- **Published**: 2026-10-21T09:51:42Z
- **Authors**: Jiaru Qian, Yihong Dong, Xue Jiang, Chun-Wah Hsu, Zhi Jin, Ge Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29501v1)