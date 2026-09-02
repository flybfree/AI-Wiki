---
title: Bandits in Prod: Hyperparameter Optimization at Inference Time
url: http://arxiv.org/abs/2609.01335v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-48-08Z_BanditsinProd_HyperparameterOptimizationatInferenc.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses Online Hyperparameter Optimization where configurations are chosen at inference time and validated only on live data. It formalizes the problem as an infinitely many‑armed bandit over mixed search spaces and introduces IMABO, a framework that couples any bandit policy with any oracle for proposing new settings. The authors prove a cumulative quantile‑regret bound of O(p_ρ^{-1/β}+T^{(1+β)/2}) and show three oracles improve performance.

## Key Takeaways
- The framework IMABO combines an anytime active set policy IMOSS with oracles such as Tree‑structured Parzen Estimator, incumbent‑mutation, and a pretrained tabular foundation model to outperform uniform random selection. 
- The regret bound depends on the growth exponent β of the active set and the probability p_ρ that a proposed configuration is among the top ρ fraction of possible settings. 
- Experimental results demonstrate lower cumulative regret across tasks ranging from classical ML models to LLM‑based agents.

## Context
In production AI systems, hyperparameter choices are often made dynamically without offline validation data, creating a challenge for reliable optimization. This work formalizes that scenario as a bandit problem, highlighting the gap between theoretical guarantees and real‑world deployment constraints.

## Implications
The results provide concrete guidance for practitioners seeking to balance exploration and exploitation in live inference pipelines. By leveraging active set policies and domain‑specific oracles, teams can reduce regret and improve model performance without sacrificing latency. This approach could become a standard toolkit for hyperparameter tuning in edge AI environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01335v1)
