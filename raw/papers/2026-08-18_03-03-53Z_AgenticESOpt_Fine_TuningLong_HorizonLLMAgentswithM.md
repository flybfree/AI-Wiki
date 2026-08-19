---
title: Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements
published: 2026-08-18T03:03:53Z
authors: Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
url: http://arxiv.org/abs/2608.17310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements

## Abstract
Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger LLMs, and longer-horizon trajectories make credit assignment in RL substantially harder. This paper argues that evolution strategies (ES) can be a better choice for fine-tuning long-horizon LLM agents. Compared with agentic RL, ES offers three key advantages: 1) Model Scalability: ES enables full-parameter optimization with only minimal, inference-level GPU memory, making it possible to fine-tune large LLMs. 2) Flexibility: its lightweight, black-box feedback interface makes ES fine-tuning easy to compose with prompt-space evolution (e.g., skill optimization & test-time compute); and 3) Long-Horizon Scalability: ES performs trajectory-level parameter attribution without decomposing rewards across horizons, yielding better scalability than Agentic RL as the horizon length grows. Based on this insight, we propose Agentic ESOpt, a full-parameter agentic fine-tuning framework tailored to flexible parameter--context co-evolution. At each step, Agentic ESOpt samples perturbations around the current LLM parameters, evaluates the resulting agents with rewards, and applies an online reward-weighted update. To improve the exploration--adaptation trade-off, Agentic ESOpt further introduces a cosine decay schedule of the perturbation scale $σ$. On WebArena-Lite, full-parameter optimization of Qwen-3.5-27B improves the No Skill baseline by 6.69%. In test-time automatic heuristic design, Agentic ESOpt performs online prompt--parameter co-evolution, improving its matched baseline in 28 of 36 settings.

## Metadata
- **Published**: 2026-08-18T03:03:53Z
- **Authors**: Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17310v1)