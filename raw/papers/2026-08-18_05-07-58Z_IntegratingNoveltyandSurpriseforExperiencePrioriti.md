---
title: Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning
published: 2026-08-18T05:07:58Z
authors: Hoda Yamani, Henry Williams, Bruce A. MacDonald
url: http://arxiv.org/abs/2608.17373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning

## Abstract
Sample efficiency is a central challenge in reinforcement learning (RL), particularly in image-based domains where agents must learn from high-dimensional visual inputs. Traditional sampling often relies on random or suboptimal experience selection, leading to redundant updates and slow learning. Improving efficiency requires mechanisms that prioritize informative experiences while also encouraging effective exploration. Prioritized Experience Replay (PER) addresses part of this challenge by reusing high-value transitions, while intrinsic rewards promote the exploration of novel or uncertain states. However, their integration has not been extensively studied. This paper introduces Novelty and Surprise Prioritized Experience Replay (NSPER), which uses novelty to capture underrepresented states and surprise to expose gaps in the agent's understanding of the environment. We further extend this with NSPER+R, integrating these signals as intrinsic rewards to jointly improve replay quality and exploration. Experiments on DeepMind Control Suite tasks show that NSPER and NSPER+R improve training efficiency and convergence speed compared to existing methods in image-based RL.

## Metadata
- **Published**: 2026-08-18T05:07:58Z
- **Authors**: Hoda Yamani, Henry Williams, Bruce A. MacDonald
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17373v1)