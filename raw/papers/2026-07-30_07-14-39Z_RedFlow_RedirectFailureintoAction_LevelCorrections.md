---
title: RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy
published: 2026-07-30T07:14:39Z
authors: Zhengyang Yan, Junhao Li, Fangqi Zhu, Zijun Wang, Quanxin Shou, Yikun Miao, Xiaoyi Pang, Zicong Hong, Song Guo
url: http://arxiv.org/abs/2607.27782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy

## Abstract
Flow-matching Vision-Language-Action (VLA) policies have shown strong potential for robotic manipulation but often suffer from compounding errors caused by distribution shifts during deployment. While offline reinforcement learning (RL) provides a practical way to improve deployed policies using rollout data, existing methods either ignore failure data or exploit it only at the trajectory level, resulting in low learning efficiency and persistent errors. We propose **RedFlow**, a fine-grained offline RL framework that redirects failure experiences into action-level corrective supervision for flow-matching VLA policies. RedFlow consists of two key components: (1) a **Context-Aware Corrective Matching** mechanism that identifies failure-inducing actions and retrieves successful alternatives from similar contexts as corrective targets, and (2) an **Adaptive Redirection Objective** that jointly reinforces successful actions, suppresses undesirable ones, and redirects recoverable failures toward corrective targets. By converting both successful and failed experiences into dense supervision, RedFlow enables robust recovery learning from mixed-quality data. Experiments on the LIBERO benchmark and three real-world manipulation tasks show that RedFlow consistently outperforms state-of-the-art offline RL baselines, improving the real-world success rate from 56.7% to 74.7%. It also matches strong on-policy methods (PPO, GRPO, and DDPO) while requiring roughly an order of magnitude fewer training samples.

## Metadata
- **Published**: 2026-07-30T07:14:39Z
- **Authors**: Zhengyang Yan, Junhao Li, Fangqi Zhu, Zijun Wang, Quanxin Shou, Yikun Miao, Xiaoyi Pang, Zicong Hong, Song Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27782v1)