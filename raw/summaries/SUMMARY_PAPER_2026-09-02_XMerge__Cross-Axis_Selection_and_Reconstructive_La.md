---
title: XMerge: Cross-Axis Selection and Reconstructive Layer Merging for LLM Depth Compression
url: http://arxiv.org/abs/2609.02083v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_04-12-44Z_XMerge_Cross_AxisSelectionandReconstructiveLayerMe.md
generated_at: 2026-09-02 20:52
model: nvidia/nemotron-3-nano-4b
---

## Summary
XMerge proposes a post‑training depth‑compression technique that selects transformer blocks with minimal hidden‑state change and reconstructs the output of adjacent surviving layers to preserve performance. Experiments on Llama and Qwen models show XMerge outperforms five baselines across seven architectures, especially at aggressive layer removal, without adding architectural changes or inference parameters.

## Key Takeaways
- Cross‑axis selection targets blocks with low relative magnitude and angular hidden‑state change, enabling efficient pruning while preserving output quality.  
- Local boundary reconstruction re‑fits the surviving block to match the original two‑block output, providing most of the compression gain.  
- The method achieves top performance on both CORE and MMLU tasks across multiple regimes without perplexity spikes or collapse.

## Context
Depth‑compression methods aim to reduce model size and inference cost while maintaining language understanding capabilities. Existing approaches often require fine‑tuning or introduce extra parameters, which can hinder deployment in resource‑constrained settings. XMerge’s label‑free, parameter‑free design addresses these practical constraints.

## Implications
For practitioners seeking scalable AI models, XMerge demonstrates that significant compression is possible without sacrificing quality or requiring costly retraining. This approach could enable smaller, faster models for edge devices and real‑time applications where latency and memory are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02083v1)
