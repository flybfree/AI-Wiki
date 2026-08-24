---
title: CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment
url: http://arxiv.org/abs/2608.21278v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_16-36-10Z_CLEAR_ContinuousLatentAdapterRoutingforUtility_Pre.md
generated_at: 2026-08-23 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CLEAR, a continuous latent adapter routing framework designed to improve LLM safety while preserving utility. It uses a lightweight hidden‑state gate to modulate the activation of a low‑rank safety adapter throughout inference rather than applying it globally. Experiments on HarmBench and GSM8K show that CLEAR cuts harmful completions dramatically without harming overall performance.

## Key Takeaways
- CLEAR reduces HarmBench ASR from 32.3 % to 0.5 %, demonstrating a near‑complete elimination of unsafe outputs.  
- The framework retains most of the base model’s utility, avoiding the degradation seen with globally applied safety tuning such as SFT or LoRA.  
- CLEAR achieves up to 7.1 percentage points higher GSM8K accuracy compared with standard SFT or LoRA methods.

## Context
In large language model alignment, improving safety often leads to a trade‑off where models become less useful on benign tasks. This tension is a central challenge for researchers and practitioners seeking robust yet functional systems. CLEAR addresses this by offering a continuous adaptation mechanism that can be integrated without retraining the entire model.

## Implications
The results suggest that lightweight, continuously gated adapters can deliver strong safety improvements while maintaining high utility, which could become a standard approach in industry deployments. Practitioners may adopt CLEAR to fine‑tune models for specific safety requirements without sacrificing performance on downstream tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21278v1)
