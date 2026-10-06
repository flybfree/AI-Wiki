---
title: Sibyl: An Efficient Small-large Model Collaboration Framework for Long-horizon Tasks
published: 2026-10-04T17:14:41Z
authors: Zhewei Fang, Yuxin Zhang, Zhenwei Shao, Mengze Li, Zheng Lin, Long Chen, Zhou Yu, Zhe Chen, Zhiwen Chen, Zhaode Wang, chengfei lv
url: http://arxiv.org/abs/2610.05383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sibyl: An Efficient Small-large Model Collaboration Framework for Long-horizon Tasks

## Abstract
Small language models (SLMs) offer a promising foundation for on-device agents through low-latency, resource-efficient inference, yet limited reasoning and planning capabilities constrain their performance on long-horizon tasks requiring multi-step interaction with the environment. Step-level collaboration between SLMs and larger cloud-hosted models can bridge this gap, but identifying states that warrant cloud assistance remains challenging: the contribution of each cloud call is entangled with subsequent actions and can be assessed only from the final task outcome. Compounding this challenge, the SLM must balance two competing objectives: maximizing task success and minimizing cloud calls. To address this, we propose Sibyl, an algorithm that trains SLM agents to selectively consult cloud models at the step level and internalize their guidance for subsequent decisions, achieving strong task performance with minimal cloud reliance. Sibyl follows a three-stage training pipeline that (1) builds a robust base policy through consultation-free self-evolving reinforcement learning (RL); (2) cold-starts consultation behavior via decisive-disagreement state mining; and (3) jointly optimizes consultation decisions and guidance internalization through consultation-aware RL. Experiments on ALFWorld and WebShop demonstrate that Sibyl, using only a 0.6B-parameter model, outperforms state-of-the-art baselines, including agent training and routing methods, by 95.2% and 80.4% in success rate while averaging only 0.8 and 3.9 cloud calls per trajectory, respectively.

## Metadata
- **Published**: 2026-10-04T17:14:41Z
- **Authors**: Zhewei Fang, Yuxin Zhang, Zhenwei Shao, Mengze Li, Zheng Lin, Long Chen, Zhou Yu, Zhe Chen, Zhiwen Chen, Zhaode Wang, chengfei lv
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05383v1)