---
title: AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization
url: http://arxiv.org/abs/2607.17281v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_14-59-12Z_AIGB_R1_Self_EvolvingGenerativeAuto_BiddingviaHier.md
generated_at: 2026-07-23 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AIGB‑R1, a hierarchical self‑evolving auto‑bidding framework that leverages the reasoning abilities of large language models to improve online advertising strategies. By integrating a high‑level planner and a low‑level executor, the system learns from accumulated experience through an offline pre‑training and post‑training alignment pipeline, achieving end‑to‑end optimization via Decoupled Group Relative Policy Optimization (D‑GRPO). Experiments on a large public dataset show that AIGB‑R1 outperforms prior AI‑generated bidding methods.

## Key Takeaways
- The paper highlights the limitation of offline datasets in covering all bidding modes and the inadequate task‑state understanding that hampers strategy exploration.  
- It proposes an experience‑driven self‑evolving loop that enables autonomous strategy optimization from accumulated interaction data.  
- The framework employs Decoupled Group Relative Policy Optimization (D‑GRPO) to achieve end‑to‑end optimization by decoupling advantages, reducing inference latency and hallucinations.

## Context
The integration of large language models into automated bidding has gained traction as a way to bring domain knowledge and reasoning capabilities to online advertising. However, these models often struggle with numerical precision, generate inaccurate bids, and introduce latency in real‑time decision making. AIGB‑R1 addresses these challenges by combining hierarchical planning with experience‑based self‑evolution.

## Implications
For the advertising industry, AIGB‑R1 offers a scalable solution that can continuously refine bidding strategies without manual intervention, potentially increasing ROI for advertisers. Practitioners can adopt this framework to reduce reliance on static models and improve adaptability to changing market conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17281v1)
