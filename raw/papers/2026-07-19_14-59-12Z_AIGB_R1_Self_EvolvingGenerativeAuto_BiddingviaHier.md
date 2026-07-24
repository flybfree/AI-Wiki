---
title: AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization
published: 2026-07-19T14:59:12Z
authors: Yuejia Dou, Hesong Wang, Xinyu Zhang, Tianyu Wang, Zhilin Zhang, Chuan Yu, Jian Xu, Bo Zheng, Qi Qi
url: http://arxiv.org/abs/2607.17281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization

## Abstract
Auto-bidding plays an essential role in online advertising, automatically adjusting bids for advertisers to optimize their commercial goals. The emerging AI-Generated Bidding (AIGB) paradigm widely adopts generative modeling to optimize bidding strategies, yet suffers from the limited mode coverage of offline datasets and inadequate task-state understanding, hindering effective exploration of optimal strategies. Large Language Models (LLMs), with prior world knowledge and reasoning capabilities, offer a promising approach to overcome these limitations. However, directly applying LLMs to auto-bidding tasks faces inherent challenges in limited numerical precision, hallucinations, and inference latency. To address these limitations, we propose AIGB-R1, a hierarchical self-evolving auto-bidding framework aiming to enhance AI-Generated Bidding via LLMs' Reasoning capabilities, comprising a high-level Planner module for macro-level strategy planning and a low-level Executor module for fine-grained decision-making. Building upon this, we design an experience-driven self-evolving loop, enabling autonomous strategy exploration and optimization from accumulated experience. We adopt a two-stage pipeline of offline pre-training and post-training alignment, and build an interactive bidding simulation environment for strategy rollout. Furthermore, we propose Decoupled Group Relative Policy Optimization (D-GRPO) to achieve end-to-end optimization via advantage decoupling. Experimental results on a large-scale public dataset demonstrate the effectiveness of AIGB-R1.

## Metadata
- **Published**: 2026-07-19T14:59:12Z
- **Authors**: Yuejia Dou, Hesong Wang, Xinyu Zhang, Tianyu Wang, Zhilin Zhang, Chuan Yu, Jian Xu, Bo Zheng, Qi Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17281v1)