---
title: PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention
url: http://arxiv.org/abs/2607.25157v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_00-05-43Z_PreDiff_LM_PretrainedDiscreteMaskedDiffusionLangua.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PreDiff-LM, a hybrid attention approach that keeps causal attention on the observed prompt while allowing full bidirectional attention for masked tokens in diffusion language models. It improves unconditional perplexity from 34.1 to 28.7 and MAUVE from 0.71 to 0.78 compared with uniform bidirectional attention using the same autoregressive initialization.

## Key Takeaways
- Hybrid mask preserves causal attention within the prompt but enables bidirectional attention for masked targets, improving unconditional perplexity from 34.1 to 28.7.
- Pretrained initialization reduces steps needed to reach perplexity below 50 from about 350K to 8K, though a fine‑tuned AR model remains stronger at equal compute (18.9 vs 28.7).
- Attention adaptation combined with a DiffuGPT‑style objective yields 26.9 perplexity and better repetition, distributional quality, zero‑shot task performance, and human preference.

## Context
This work tackles the tension between causal autoregressive training and bidirectional denoising in diffusion models, offering a way to reuse large language model backbones without full retraining. It demonstrates that hybrid attention can complement existing AR models effectively.

## Implications
Practitioners can adopt this hybrid attention mechanism to quickly adapt existing AR models, lowering fine‑tuning cost while maintaining strong performance, which is valuable for resource‑constrained deployment and rapid prototyping in industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25157v1)
