---
title: Discovering Cross-Language Reasoning Invariance in LLMs with Geometry-Invariant Sparse Autoencoders
url: http://arxiv.org/abs/2608.23809v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_20-17-55Z_DiscoveringCross_LanguageReasoningInvarianceinLLMs.md
generated_at: 2026-08-25 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether multilingual language models rely on shared reasoning features across languages or on language‑specific computations that happen to produce similar answers. By analyzing six math problems in English, German, French, Spanish, Russian and Chinese, the authors train a Geometry‑Invariant Sparse Autoencoder (GI‑SAE) that forces cross‑language activations to be similar regardless of token order. They find that while GI‑SAE creates stronger geometric alignment, functional interchangeability is not guaranteed.

## Key Takeaways
- CKA and Jaccard similarity increase at nearly every layer after training the GI‑SAE, indicating more aligned representations across languages.
- The strength of cross‑language feature sharing varies by model: it is pronounced in Qwen, absent in Gemma, and mixed in Llama and Phi.
- Higher geometric similarity does not always translate into greater functional interchangeability when activations are swapped between languages.

## Context
Understanding whether multilingual models share a common reasoning space or generate parallel outputs is crucial for evaluating true cross‑lingual generalization. This study bridges representation learning and language modeling by using geometry‑invariant contrastive training to probe alignment at specific layers.

## Implications
For practitioners, the findings suggest that simply improving geometric similarity may not improve multilingual performance, highlighting the need for functional testing of shared features. Researchers should consider model architecture effects when designing cross‑language evaluation protocols.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23809v1)
