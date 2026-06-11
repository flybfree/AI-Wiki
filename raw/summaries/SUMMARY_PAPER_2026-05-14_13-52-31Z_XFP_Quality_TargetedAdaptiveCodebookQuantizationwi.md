---
title: XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation for LLM Inference
url: http://arxiv.org/abs/2605.14844v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-14_13-52-31Z_XFP_Quality_TargetedAdaptiveCodebookQuantizationwi.md
generated_at: 2026-06-11 10:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
XFP is a dynamic weight quantizer designed to improve LLM inference by automatically selecting codebook parameters such as size and outlier budget without manual calibration. The paper demonstrates that XFP reaches 138 tokens per second on the Qwen3.5-122B-A10B model at 94.49% GSM8K strict-match, outperforming Marlin INT4 in both speed and accuracy.

## Key Takeaways
- XFP automatically determines codebook size and outlier budget per layer without Hessian calculations or calibration data.
- It splits each weight matrix into a sparse fp16 outlier residual and a dense sub-byte index tensor encoded by a per-group learned codebook using two storage modes V2 (per-channel Lloyd) and V2a (shared library of L=32 codebooks).
- The H‑Process iteratively adjusts cosine similarity thresholds to find the memory‑fit operating point, allowing full deployment of large models like Qwen3.5-397B-A17B with 100.9 tok/s long‑output decode.

## Context
Dynamic quantization is essential for reducing memory usage in LLM inference where hardware constraints limit model size and throughput. XFP’s approach addresses the trade‑off between accuracy and efficiency by decoupling reconstruction quality from manual bit‑width selection, enabling more flexible deployment across diverse systems.

## Implications
For practitioners, XFP offers a plug‑and‑play solution that can be integrated into existing inference pipelines without extensive tuning. This lowers barriers to deploying high‑quality LLMs on workstation hardware, accelerating research and commercial adoption while maintaining competitive performance against traditional INT4 methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.14844v1)
