---
title: STRATA: Self-Learning Through Role-Aligned Tiered Agents for Real-Time Strategy Games
published: 2026-09-30T03:31:06Z
authors: Xinhe Tian, Xiaoyue Zhang, Ziyou Zhang, Jiacheng Li, Xiaoqiang Jin, Qianchuan Zhao, Gaochen Cui
url: http://arxiv.org/abs/2609.38881v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STRATA: Self-Learning Through Role-Aligned Tiered Agents for Real-Time Strategy Games

## Abstract
Real-time strategy (RTS) games require agents to coordinate economic development, production and construction, base defense, unit organization, and attack timing over long matches. Existing studies have applied large language models to command decision-making in RTS games, enabling agents to read textual game states and generate high-level plans. However, long inference latency can cause them to miss critical tactical events. The complexity and tactical diversity of full RTS matches also leave existing systems heavily dependent on manually written experience-based prompts, with limited ability to learn continuously from past games. We present STRATA, a role-aligned hierarchical system with cross-game self-learning for Red Alert. STRATA assigns in-game strategic, logistical, and tactical decisions to a Strategic Agent (SA), Logistics Agent (LA), and Tactical Agent (TA), respectively. The SA generates high-level directives based on the global game state and relevant experience cards, while the LA and TA handle logistics and tactical execution. After each match, a Review Agent (RA) derives candidate experience from game traces, validates and revises it using evidence from subsequent matches, and compresses strategic experience supported across multiple games into concise experience cards for SA retrieval. We evaluate STRATA through the formation of experience cards, full-match comparisons before and after learning, and experience learning against AI opponents with different play styles. Under a fixed scenario, using the learned experience cards increases the observed win rate from 30% to 100%. Sequential learning against AI opponents with different play styles also produces distinct long-term strategic experience.

## Metadata
- **Published**: 2026-09-30T03:31:06Z
- **Authors**: Xinhe Tian, Xiaoyue Zhang, Ziyou Zhang, Jiacheng Li, Xiaoqiang Jin, Qianchuan Zhao, Gaochen Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38881v1)