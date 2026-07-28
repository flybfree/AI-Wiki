---
title: Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning
url: http://arxiv.org/abs/2607.23605v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_11-16-59Z_HybridAdvantageEstimationwithUnifiedCriticforVLMAg.md
generated_at: 2026-07-27 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HyGAE, a hybrid advantage estimator that combines token‑wise and turn‑wise optimization for VLM agents. It derives a unified critic capable of estimating values at both levels and achieves 91% success across five environments, outperforming prior methods by about 10%. The hybrid framework also reduces variance by aligning discount factors across levels.

## Key Takeaways
- The hybrid advantage quantifies returns separately per token and per turn, enabling fine‑grained credit assignment that improves multi‑turn reasoning.  
- A unified critic model can compute values for both optimization levels using a single network architecture, simplifying training.  
- Choosing the discount factor appropriately allows the same loss to serve both token‑wise and turn‑wise objectives simultaneously.

## Context
Vision‑language agents must plan across multiple turns where decisions depend on accumulated observations; current methods struggle with aligning credit across granularity. This work addresses that gap by providing a principled, unified framework for multi‑scale reward estimation in agentic VLM systems.

## Implications
The approach offers practitioners a scalable solution to improve long‑term performance of multimodal agents without sacrificing computational efficiency. By standardizing how value functions are computed, it can be integrated into existing RL pipelines and research on embodied AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23605v1)
