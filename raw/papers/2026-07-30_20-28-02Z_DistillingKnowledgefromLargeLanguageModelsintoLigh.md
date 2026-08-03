---
title: Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations
published: 2026-07-30T20:28:02Z
authors: Konur Tholl, François Rivest, Mariam El Mezouar, Adrian Taylor, Ranwa Al Mallah
url: http://arxiv.org/abs/2607.28826v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations

## Abstract
Autonomous Cyber Operations (ACO) are increasingly important for defending enterprise networks as cyber threats continue to evolve in sophistication. ACO applications commonly employ Reinforcement Learning (RL) agents to learn defensive behaviors through interaction with environments. However, RL agents typically require extensive exploration during training, often resulting in unstable behavior and poor initial decision-making before converging toward effective defense strategies.   In this work, we investigate the use of a Large Language Model (LLM) to improve autonomous defensive decision-making within an ACO environment. Through prompt engineering rather than fine-tuning, we demonstrate that an 8-billion parameter LLM pretrained on cybersecurity data can outperform a baseline RL agent in a modified CybORG CAGE Challenge 2 environment. We then propose an online policy distillation framework that transfers the LLM's defensive policy into a lightweight RL agent containing only 64,910 parameters, reducing model size by several orders of magnitude while maintaining effective defensive capabilities. This provides a pathway toward operationalizing frontier cybersecurity models within lightweight, deployable agents.   To evaluate transferability, we construct CybORG scenarios ranging from 4 to 12 hosts and assess the approach across varying network configurations. We also evaluate teacher-guided RL stabilization strategies and observe that none consistently surpass the optimized teacher policy, suggesting policy-alignment limitations between reward-driven RL optimization and teacher-guided defense strategies.   Our results demonstrate the potential of cybersecurity-focused LLMs as sources of expertise for autonomous cyber defense, while policy distillation provides a practical path toward operationalizing frontier cybersecurity models within efficient, scalable agents.

## Metadata
- **Published**: 2026-07-30T20:28:02Z
- **Authors**: Konur Tholl, François Rivest, Mariam El Mezouar, Adrian Taylor, Ranwa Al Mallah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28826v1)