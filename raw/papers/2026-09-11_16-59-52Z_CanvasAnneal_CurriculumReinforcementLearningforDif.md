---
title: CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models
published: 2026-09-11T16:59:52Z
authors: Blake Olson, Yuhang Song, Emmett McQuinn, Yuan Shangguan
url: http://arxiv.org/abs/2609.13060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models

## Abstract
Diffusion Language Models (DLMs) offer promising parallel generation capabilities but lag behind autoregressive models in complex reasoning and tool-use tasks. While Reinforcement Learning (RL) has recently been applied to enhance DLMs, standard RL approaches suffer from an exploration bottleneck. To address this, we inject reasoning priors from a stronger teacher model to guide RL exploration. In this paper, we introduce CanvasAnneal, a curriculum-guided diffusion RL framework. During the initial RL phase, we warm-start exploration by injecting teacher-generated reasoning traces into the initial diffusion canvas. As training progresses, we gradually remove this guidance and require the model to generate more of the reasoning trajectory independently. Across mathematical reasoning and tool-use benchmarks, CanvasAnneal improves over standard diffu-GRPO on MATH500, Countdown, and Tau2 and substantially accelerates reward improvement on several tasks, while gains are task-dependent. Our results suggest that structured training-time guidance can alleviate exploration bottlenecks in diffusion RL and speed up convergence on harder tasks.

## Metadata
- **Published**: 2026-09-11T16:59:52Z
- **Authors**: Blake Olson, Yuhang Song, Emmett McQuinn, Yuan Shangguan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13060v1)