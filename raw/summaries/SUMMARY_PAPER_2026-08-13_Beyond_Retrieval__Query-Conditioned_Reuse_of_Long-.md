---
title: Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories
url: http://arxiv.org/abs/2608.12847v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_05-39-49Z_BeyondRetrieval_Query_ConditionedReuseofLong_Horiz.md
generated_at: 2026-08-13 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles the bottleneck of converting retrieved long‑horizon agent trajectories into usable support for new tasks. By fixing retrieval, target state, model, decoding and tool budget while varying the support delivered to the agent, it introduces a query‑conditioned reuse (QCR) framework that demonstrates 62.3 % success on 2,391 instances—outperforming full trajectory use by 10.7 points with fewer online tokens.

## Key Takeaways
- Retrieval alone does not guarantee effective post‑retrieval reuse because the agent must adapt to changed users, entities, constraints or environment states.  
- QCR provides a reusable procedure that records bindings, applicability conditions and verification requirements, allowing the agent to apply stored experience safely in new contexts.  
- Direct injection of long trajectories loses much utility as traces grow longer or source‑specific values shift, whereas target‑bound support retains most of the measured gain.

## Context
Long‑horizon memory is essential for agents that must remember and reuse past experiences across tasks, yet existing approaches treat retrieval and post‑retrieval conversion as a single step. This paper highlights the need for a principled evaluation framework that isolates these stages, enabling researchers to assess how well retrieved experience translates into task support.

## Implications
Efficient memory reuse reduces token consumption and improves agent performance in real‑world applications where online resources are limited. Practitioners can adopt target‑bound support strategies to preserve gains from long‑term retrieval while minimizing the risk of unsafe or irrelevant execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12847v1)
