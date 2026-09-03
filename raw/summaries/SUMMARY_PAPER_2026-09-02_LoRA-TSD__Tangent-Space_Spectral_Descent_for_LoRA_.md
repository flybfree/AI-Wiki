---
title: LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates
url: http://arxiv.org/abs/2609.02734v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-41-45Z_LoRA_TSD_Tangent_SpaceSpectralDescentforLoRAviaMuo.md
generated_at: 2026-09-02 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LoRA‑TSD, an optimizer that treats every low‑rank adaptation step as a tangent vector of the fixed‑rank matrix manifold and performs a steepest‑descent move inside that space. It maps the result back to the factors with a cheap retraction native to LoRA’s parametrization. The method avoids full weight‑matrix operations and proves global convergence for both LoRA‑Pro and LoRA‑TSD under the Riemannian gradient measure.

## Key Takeaways
- It treats each LoRA step as a tangent vector of the fixed‑rank matrix manifold and performs a steepest‑descent step in that space.  
- The retraction is up to 2.8 times cheaper than truncated‑SVD used by earlier manifold methods, avoiding full weight‑matrix ops.  
- Global convergence guarantees are proven for both LoRA‑Pro and LoRA‑TSD under the Riemannian gradient measure.

## Context
LoRA fine‑tunes large language models by updating low‑rank matrices while leaving the main weights frozen, but existing optimizers ignore geometric constraints that limit update quality. This work fills that gap with a mathematically grounded approach that respects the manifold structure of LoRA’s parameter space.

## Implications
Practitioners can adopt LoRA‑TSD for efficient, robust fine‑tuning of massive models without heavy computational overhead, improving performance across benchmarks and maintaining robustness to adapter rank. Industry pipelines can integrate this optimizer to boost fine‑tuning speed or quality while keeping costs low.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02734v1)
