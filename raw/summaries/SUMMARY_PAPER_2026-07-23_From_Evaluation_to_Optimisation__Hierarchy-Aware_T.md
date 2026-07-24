---
title: From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python
url: http://arxiv.org/abs/2607.21069v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the hierarchical penalty introduced in the ALPHA benchmark can be used as a training signal to improve CWE prediction models in Python. By comparing supervised fine‑tuning, dual‑head classification loss, and reinforcement learning with a dense reward derived from the normalised penalty, the authors show that only the reinforcement‑learning approach successfully reduces cumulative penalties on held‑out data.

## Key Takeaways
- The hierarchical penalty can be turned into a training signal when delivered directly via reinforcement learning, unlike supervised fine‑tuning which regresses below zero‑shot performance.  
- Using GRPO with a dense reward derived from the normalised penalty yields a 27.9 % reduction in cumulative ALPHA penalty under greedy decoding and 25.5 % under sampled decoding (p = 0.005, Welch’s t‑test).  
- The best policy reaches statistical parity with a zero‑shot teacher that is four point five times larger in model capacity.

## Context
Current CWE prediction systems often rely on static supervised benchmarks that do not adapt to distribution shifts, leading to degraded performance when new code patterns appear. This work demonstrates how reward‑shaping techniques can close the gap between zero‑shot and fine‑tuned models, offering a more robust evaluation framework for AI safety tools.

## Implications
Practitioners can integrate hierarchical penalties into their training pipelines to improve model resilience without retraining from scratch. The findings suggest that direct reinforcement learning of evaluation metrics may be a viable path toward safer code generation in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21069v1)
