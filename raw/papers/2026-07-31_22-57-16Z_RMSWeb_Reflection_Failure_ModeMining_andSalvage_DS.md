---
title: RMSWeb: Reflection, Failure-Mode Mining, and Salvage-DS for Web Agent Reinforcement Learning
published: 2026-07-31T22:57:16Z
authors: Chengbo Liu, Lifang Zhou, Ruijie Yan, Pei Tan, Ao Sun, Haojun Huang, Guichun Hua, Sining Wei, Yining Chen, Yingying He, Yutao Xie
url: http://arxiv.org/abs/2608.00335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RMSWeb: Reflection, Failure-Mode Mining, and Salvage-DS for Web Agent Reinforcement Learning

## Abstract
Compact web agents can reduce deployment cost, but training them poses challenges in both data collection and post-SFT reinforcement learning (RL). Successful trajectories are expensive to collect and often contain inefficient detours. After supervised fine-tuning (SFT), full trajectory corpora are dominated by routine states; moreover, when group-relative RL is applied to web actions, inadequately designed action-level rewards can yield weak or misleading relative updates, while groups rejected as unsuitable for such updates receive no fallback learning signal. We present RMSWeb, a three-part recipe for Qwen3-VL-Instruct at 8B and 32B. Reflection-conditioned retries increase collection yield and shorten successful trajectories; failure-mode mining concentrates offline RL on critical states exposed by the SFT policy; and Salvage-DS combines an action-semantic polarized reward, contrast-and-competence-gated dynamic sampling, and an action-only anchor for rejected groups. Policies trained with reflection-collected data use up to 19.7% fewer action steps on solved tasks. On WebVoyager, Online-Mind2Web, and WebTailBench, RMSWeb improves over SFT by 2.4-7.0 points at 8B and 1.2-7.7 points at 32B. Our 8B model also achieves the strongest reported Online-Mind2Web result among similarly sized open-weight models in our comparison and a leading reported accuracy-cost trade-off on WebVoyager and WebTailBench, with the caveat that external evaluation protocols differ.

## Metadata
- **Published**: 2026-07-31T22:57:16Z
- **Authors**: Chengbo Liu, Lifang Zhou, Ruijie Yan, Pei Tan, Ao Sun, Haojun Huang, Guichun Hua, Sining Wei, Yining Chen, Yingying He, Yutao Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00335v1)