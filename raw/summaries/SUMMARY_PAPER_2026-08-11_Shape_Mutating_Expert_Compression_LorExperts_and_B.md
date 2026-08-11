---
title: Shape Mutating Expert Compression:LorExperts and BTExperts
url: http://arxiv.org/abs/2608.07814v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-07_23-23-40Z_ShapeMutatingExpertCompression_LorExpertsandBTExpe.md
generated_at: 2026-08-11 12:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LorExperts and BTExperts as compression techniques for Mixture-of-Experts language models that retain the original router without retraining, achieving significant weight savings while preserving accuracy. Experiments on Qwen3‑30B‑A3B and Gemma‑4‑26B‑A4B show LorExperts reduces expert count by about 50% with minimal loss in downstream performance compared to prior delta‑decomposition baselines.

## Key Takeaways
- LorExperts clusters experts into functional communities, keeping one full‑precision dominant per cluster and representing others as low‑rank corrections, which enables compression without altering the router.  
- The method preserves all expert weights and the original routing logic, unlike prior approaches that require retraining or suffer from accuracy drops when expert count grows.  
- Reconstruction fine‑tuning further improves performance, and BTExperts adds a tree structure to amortize shared computation during inference.

## Context
Mixture-of-Experts models are central to scaling language AI efficiently, but their large weight matrices pose storage and compute challenges. Existing compression strategies either sacrifice accuracy or demand costly router updates, limiting practical deployment.

## Implications
These methods open the door for deploying massive MoE systems on resource‑constrained hardware while maintaining high quality, encouraging broader adoption of scalable generative models in industry and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07814v1)
