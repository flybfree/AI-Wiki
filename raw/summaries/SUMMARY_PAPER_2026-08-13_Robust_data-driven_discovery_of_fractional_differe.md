---
title: Robust data-driven discovery of fractional differential equations via weak formulations and Pareto-based subset selection
url: http://arxiv.org/abs/2608.12879v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_06-44-25Z_Robustdata_drivendiscoveryoffractionaldifferential.md
generated_at: 2026-08-13 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Weak‑Pareto, a data‑driven framework for discovering fractional partial differential equations from noisy measurements. By combining an adjoint‑consistent weak formulation with Pareto‑based subset selection over term types and continuous orders, the method mitigates noise amplification that plagues pointwise differentiation. Experiments across advection‑diffusion, reaction‑diffusion, and Burgers benchmarks show that Weak‑Pareto recovers parsimonious structures from both clean and noisy data while outperforming a strong‑form counterpart.

## Key Takeaways
- The weak formulation replaces noisy pointwise fractional differentiation with smoothing integration, causing the variance of linear right‑hand‑side features to vanish as grid refinement improves.  
- Continuous‑order Pareto search avoids support‑selection failure seen in dense fixed dictionaries by adaptively choosing term types and orders based on validation error.  
- Weak‑Pareto recovers parsimonious structures from clean and noisy measurements across benchmarks, maintaining correct support at every tested multiplicative‑noise level.

## Context
Fractional PDEs capture nonlocal dynamics that are hard to model with conventional derivatives because the derivative orders are unknown and high‑frequency noise is amplified. Current AI approaches often rely on strong forms or neural networks, which struggle with noisy data and computational cost. This work bridges that gap by providing a principled, low‑complexity discovery method.

## Implications
For practitioners in engineering and scientific computing, Weak‑Pareto offers a reliable way to detect fractional dynamics without requiring prior knowledge of the order, reducing both error and runtime compared to neural baselines. The method’s robustness under multiplicative noise makes it suitable for real‑world sensor data where high‑frequency artifacts are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12879v1)
