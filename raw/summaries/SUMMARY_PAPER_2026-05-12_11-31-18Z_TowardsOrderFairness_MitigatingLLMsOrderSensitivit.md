---
title: Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Advantage Optimization
url: http://arxiv.org/abs/2605.11974v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-12_11-31-18Z_TowardsOrderFairness_MitigatingLLMsOrderSensitivit.md
generated_at: 2026-06-11 10:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Dual Group Advantage Optimization (DGAO) to reduce order bias in large language models by balancing accuracy and stability through reinforcement learning. Experiments show DGAO improves performance on RAG, math reasoning, and classification while achieving superior order fairness compared with prior methods.

## Key Takeaways
- DGAO calculates both intra‑group relative accuracy advantage and inter‑group relative stability advantage to reward correct and order‑stable outputs.  
- The method uses reinforcement learning to directly penalize order‑sensitive or incorrect responses, addressing the bias at its source.  
- New metrics Consistency Rate and Overconfidence Rate expose pseudo‑stability of earlier approaches and guide evaluation.

## Context
Order sensitivity in LLMs hampers reliable in‑context learning and retrieval‑augmented generation, limiting practical deployment. Existing solutions either add heavy computation or produce consistent but wrong answers, highlighting a need for bias mitigation that preserves accuracy.

## Implications
DGAO offers a scalable framework that can be integrated into existing training pipelines without sacrificing performance, encouraging developers to adopt order‑fair models in production systems and fostering more equitable AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.11974v1)
