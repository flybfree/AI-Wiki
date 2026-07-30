---
title: HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models
url: http://arxiv.org/abs/2607.26515v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_06-28-26Z_HiFloat4FormatforEnd_To_EndReinforcementLearningPo.md
generated_at: 2026-07-29 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HiFloat4, a three‑level hierarchical scaling format that enables end‑to‑end reinforcement learning post‑training of large language models using only 4‑bit precision. The authors demonstrate that the primary degradation in FP4 RL stems from rollout activation quantization, where outlier values underflow to zero, and that fixing this by raising training precision actually harms performance. Their solution, Rollout Residual Quantization (Rollout‑ResQ), adds a lightweight correction to the rollout matmul, restoring most of the lost precision without increasing computational cost.

## Key Takeaways
- The dominant source of accuracy loss in FP4 RL is not quantization error from the training policy but underflow caused by outlier activations during rollout.  
- Restoring the training policy to higher precision while keeping rollout at FP4 reduces model accuracy, indicating a mismatch between rollout and training that standard pretraining fixes cannot resolve.  
- Rollout Residual Quantization (Rollout‑ResQ) corrects the underflow by applying a sparsely structured residual term only to the rollout matmul, preserving compute efficiency while recovering most precision.

## Context
Current research on quantization for large language models focuses on minimizing training‑side errors, yet real‑world RL pipelines suffer from hidden activation underflows that degrade performance. HiFloat4 and Rollout Residual Quantization together address this gap by providing a format‑aware correction mechanism specific to the rollout phase.

## Implications
For practitioners deploying quantized LLMs in reinforcement learning, choosing an appropriate 4‑bit format can dramatically affect achievable accuracy. The work shows that HiF4 combined with Rollout‑ResQ brings fully quantized RL within striking distance of full‑precision baselines, offering a practical path to high‑quality models at minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26515v1)
