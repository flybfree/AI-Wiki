---
title: SAGE: Surrogate-gradient Adaptation via Attention-Guided Entropy for Spiking Transformers
url: http://arxiv.org/abs/2608.13702v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_18-51-04Z_SAGE_Surrogate_gradientAdaptationviaAttention_Guid.md
generated_at: 2026-08-16 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes SAGE, a surrogate‑gradient adaptation method that uses attention‑derived entropy to adjust training parameters in Transformer‑based spiking neural networks. Experiments on CIFAR‑10/100 show that SAGE improves accuracy by up to 2 % compared with fixed‑surrogate baselines while keeping the inference model unchanged.

## Key Takeaways
- SAGE estimates block‑level uncertainty from normalized self‑attention entropy and uses it to adapt surrogate‑gradient slopes during training.  
- The method modifies only the training‑time surrogate parameter, leaving the deployment architecture untouched.  
- Across multiple simulation time steps, SAGE yields consistent accuracy gains of 1–2 % over fixed‑surrogate approaches.

## Context
Transformer‑based spiking networks face a core challenge: their non‑differentiable spike function requires surrogate gradients that are often suboptimal and static across layers. Traditional solutions replace the entire model with differentiable approximations, increasing computational cost. SAGE addresses this by introducing a lightweight, attention‑guided uncertainty signal that modulates only the gradient slope.

## Implications
For researchers, SAGE offers a practical way to enhance SNN training without sacrificing inference efficiency, encouraging more accurate and energy‑efficient models. For industry practitioners, it enables deployment of transformer‑based spiking systems with improved performance while preserving low‑power hardware requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13702v1)
