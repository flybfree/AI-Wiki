---
title: Clustering and Token Denoising for Faster and More Robust VLMs
url: http://arxiv.org/abs/2608.19285v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-19_11-20-26Z_ClusteringandTokenDenoisingforFasterandMoreRobustV.md
generated_at: 2026-08-20 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes ClustRS, a training‑free two‑stage algorithm that prunes visual tokens in Visual‑Language Models to reduce computational load while preserving performance. By clustering attention‑weighted tokens and applying residual denoising, the method can shrink token counts from 576 down to as few as 16 without retraining, achieving up to a 20 % improvement on noisy data.

## Key Takeaways
- ClustRS selects representative tokens per semantic cluster using attention weights, enabling robust pruning that adapts to image‑noise variations.  
- The residual denoising step is applied in a single pass over the selected tokens, preserving their meaning despite token reduction.  
- Experiments on ScienceQA‑IMG and MM‑VET show that ClustRS outperforms attention‑only and diversity‑only pruning methods under extreme noise conditions.

## Context
The rapid integration of vision tokens into large language models like LLaVA has driven demand for efficient deployment, especially on edge devices where token count directly impacts latency and power usage. Existing pruning strategies often require retraining or limit the amount of visual information retained, hindering real‑world applicability.

## Implications
ClustRS offers a lightweight, training‑free solution that can be applied to any VLM architecture without architectural changes, making it suitable for industry‑scale deployments where compute constraints are tight. This approach not only reduces latency but also enhances robustness, allowing models to operate reliably on noisy visual inputs with minimal token overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19285v1)
