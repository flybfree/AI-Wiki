---
title: State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents
published: 2026-10-09T08:54:07Z
authors: Zhentao Zhang, Yanzhao Zheng, Yanlin Liu, Yuanqiang Yu, Tianze Xu, Chao Ma, Jihuai Zhu, Lelun Wu, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu
url: http://arxiv.org/abs/2610.13238v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents

## Abstract
On-Policy Distillation (OPD) has emerged as a powerful paradigm for transferring reasoning capabilities from frontier models to smaller models, while extending its success to multi-turn agentic environments remains challenging. We study agentic OPD through interaction states, distinguishing the objective task and executed action-observation record from the internal semantic trajectory of student reasoning. Through this lens, we identify two roles of student reasoning in multi-turn OPD: prior reasoning distorts teacher supervision, while current reasoning shapes the action alternatives sampled at the same state. Specifically, at matched interaction states, removing prior student reasoning improves teacher continuation success and changes the teacher's token-level targets, with larger continuation gains at later turns. Meanwhile, resampling complete reasoning-action responses yields greater action diversity at the same state than resampling actions under a fixed reasoning trace. We introduce State-Grounded On-Policy Distillation, a framework that grounds teacher supervision in interaction states and reallocates the sampling budget to generate multiple complete reasoning-action responses at states with high response entropy, while retaining full-history student generation. Comprehensive evaluations across ALFWorld, ScienceWorld and WebShop demonstrate that State-OPD achieves the highest macro-average success rate among the evaluated methods for both Qwen3-1.7B and Qwen3-4B students. Notably, for Qwen3-4B, State-OPD raises macro-average success from 26.07\% with the strongest baseline to 31.74\% and surpasses its Qwen3-32B teacher on ALFWorld Seen. Further analyses reveal that State-OPD achieves higher task success with fewer supervised turn responses and substantially reduces persistent failed-action repetition; qualitative traces illustrate decision revision based on interaction feedback.

## Metadata
- **Published**: 2026-10-09T08:54:07Z
- **Authors**: Zhentao Zhang, Yanzhao Zheng, Yanlin Liu, Yuanqiang Yu, Tianze Xu, Chao Ma, Jihuai Zhu, Lelun Wu, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13238v1)