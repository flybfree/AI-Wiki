---
title: From Sweep to Seam: Interleaved Cross-Block Post-Training Quantization
url: http://arxiv.org/abs/2608.09595v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_13-28-23Z_FromSweeptoSeam_InterleavedCross_BlockPost_Trainin.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Interleaved Cross‑Block Quantization (ICBQ), a scheduling tweak for block‑wise post‑training quantization that revisits each seam pair between consecutive Transformer blocks. By refining the boundary twice — once at the end of one chunk and again at the start of the next — ICBQ mitigates early error propagation, unlike the matched sequential baseline which moves the window only once. Experiments show lower ternary‑quantization perplexity, finite perplexity where the baseline degrades severely, and compatibility with 3‑bit and 2‑bit GPTQ.

## Key Takeaways
- ICBQ revisits every seam pair twice, allowing errors to be corrected both forward and backward across block boundaries.  
- The method preserves the local two‑block objective while reusing existing calibration inputs from standard PTQ pipelines.  
- Under assumptions of local contraction and smoothness, depth‑wise analysis shows that repeated seam refinement multiplies only a bounded propagated term, leaving residual error independent of network depth.

## Context
Block‑wise post‑training quantization is essential for compressing large language models to two bits or fewer, enabling deployment on edge devices. The challenge lies in handling cross‑block interactions without sacrificing accuracy, especially when the moving window cannot revisit earlier errors. This work advances that challenge by providing a simple yet effective scheduling mechanism.

## Implications
ICBQ offers practitioners a practical way to improve quantization quality without redesigning calibration pipelines. For industry, it reduces model size and improves inference latency on low‑power hardware while maintaining high perplexity, supporting broader adoption of ultra‑compressed LLMs in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09595v1)
