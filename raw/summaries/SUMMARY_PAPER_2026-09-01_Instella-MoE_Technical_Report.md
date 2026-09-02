---
title: Instella-MoE Technical Report
url: http://arxiv.org/abs/2609.00791v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_06-38-17Z_Instella_MoETechnicalReport.md
generated_at: 2026-09-01 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Instella-MoE, a fully open Mixture-of-Experts language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely on AMD Instinct MI300X and MI325X GPUs. It achieves high performance scores across standard benchmarks, outperforming many prior fully open models while remaining efficient.

## Key Takeaways  
- Instella-MoE reaches an average pre‑training score of 76.7, surpassing OLMo‑3‑7B and SmolLM3‑3B.  
- The model uses Gated Multi-head Latent Attention and FarSkip‑Collective connectivity to keep active parameters low while maintaining capacity.  
- After fine‑tuning the Think checkpoint scores 73.2 on instruction‑following, reasoning, math, coding, and chat tasks.

## Context  
MoE models promise scaling efficiency but often require proprietary hardware or closed weights; Instella-MoE demonstrates that open, efficient training is feasible on commodity AMD GPUs, reducing cost and barrier to entry.

## Implications  
Researchers can now build large language systems without expensive GPU clusters, fostering democratization of AI research. Practitioners benefit from a ready‑to‑use foundation model that balances openness with performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00791v1)
