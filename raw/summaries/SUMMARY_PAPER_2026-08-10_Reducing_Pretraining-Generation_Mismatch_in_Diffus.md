---
title: Reducing Pretraining-Generation Mismatch in Diffusion Language Models
url: http://arxiv.org/abs/2608.09424v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_10-52-20Z_ReducingPretraining_GenerationMismatchinDiffusionL.md
generated_at: 2026-08-10 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles the mismatch between how diffusion language models are trained and how they generate text, noting that native dLLM pretraining can corrupt both prompt and continuation tokens together. By introducing PCD (Prefix-Conditioned Diffusion), it aligns the pretraining context with generation conditions, achieving a 4.2% relative gain on benchmark evaluations.

## Key Takeaways
- PCD combines autoregressive prefix supervision with no‑shift suffix denoising to preserve the clean prompt while applying diffusion only to unknown continuation tokens.  
- The method modifies attention masks, corruption masks, and label construction for continued pretraining without requiring a new decoder or inference mode.  
- Experiments on LLaDA2‑Mini and Qwen‑1.7B show consistent improvements over stable native dLLM baselines.

## Context
Diffusion language models enable parallel denoising but their native training often mixes prompt and continuation tokens, weakening the clean‑prefix interface needed for conditional generation. Aligning pretraining with inference is a known challenge that can degrade performance without architectural changes.

## Implications
This work demonstrates that pretraining objectives can be tuned to match prompt‑conditioned generation, potentially closing the continuation gap in existing diffusion LLMs without modifying their inference pipeline. Practitioners may adopt PCD to improve downstream tasks while keeping current model architectures intact.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09424v1)
