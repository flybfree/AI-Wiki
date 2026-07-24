---
title: Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects
url: http://arxiv.org/abs/2607.20596v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_17-33-16Z_AreSingle_TokenSparseAutoencoderFeaturesCausallyNe.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether single‑token sparse autoencoder features have a stable causal role across different SAE families and layer depths in large language models. It finds that these features cluster tightly in decoder space, concentrate early, and their ablation causes significant logit reductions under most conditions.

## Key Takeaways
- Single‑token features are 4.7 times tighter in decoder space than multi‑token ones and appear mainly in the earliest layers of models such as GPT2‑Small (Layer 0) or Gemma (L0‑L4).  
- Ablating these features yields Benjamini‑Hochberg‑significant logit reductions in 178 out of 208 full‑layer conditions, showing that their removal has a measurable impact on model output.  
- Cross‑family causal differences are larger than within‑family scale effects: GemmaScope and BatchTopK features remain causally anchored while LlamaScope features become locally redundant, indicating that training methodology matters more than activation function or scale.

## Context
Understanding the causal contribution of interpretability features is essential for building trustworthy AI systems. This study provides empirical evidence on how feature behavior varies with model architecture and training practices, a gap previously left unexamined in SAE literature.

## Implications
For practitioners developing large language models, this research suggests that relying solely on activation‑function or scale differences to explain feature causality is insufficient; systematic ablation studies are needed. It also highlights the importance of layer depth in shaping interpretability outcomes across different model families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20596v1)
