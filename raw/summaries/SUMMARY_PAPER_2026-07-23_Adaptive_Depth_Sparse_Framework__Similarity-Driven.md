---
title: Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs
url: http://arxiv.org/abs/2607.21291v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
generated_at: 2026-07-23 22:59
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces the Adaptive Depth Sparse Framework (AdaDSF), a method that reduces inference cost of large language models by sparsely activating only those layers whose input‑output similarity is high. Experiments on GPT‑NeoX and Qwen2.5 show that AdaDSF cuts FLOPs dramatically while keeping generation quality close to the dense baseline, outperforming strong sparsity baselines such as MoD, D‑LLM, and DLO.

## Key Takeaways
- Layer selection is driven by cosine similarity between input and output hidden states, enabling a lightweight router that retains only informative tokens.  
- AdaDSF uses a feature‑preserving alignment objective to align sparse and dense representations, minimizing performance loss.  
- The framework achieves up to 40 % fewer inference FLOPs on language modeling tasks while maintaining accuracy within 1–2 percentage points of the full model.

## Context
Efficient deployment of LLMs is a pressing challenge as larger models demand massive compute resources. Existing sparsity techniques often require extensive fine‑tuning or retraining, which limits their practical use across diverse tasks and scales.

## Implications
AdaDSF demonstrates that depth‑sparse adaptation can be applied to existing pre‑trained models without costly re‑training, offering a scalable path to lower latency in real‑time applications. This approach could reduce cloud costs for inference services and enable broader adoption of LLMs in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21291v1)
