---
title: Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction
url: http://arxiv.org/abs/2608.23296v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_14-21-43Z_SigmoidAttentionasaBetterSubstrateforLearnedKVCach.md
generated_at: 2026-08-24 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the choice of attention mechanism influences learned key-value cache eviction, a technique that removes less useful tokens to save memory during inference. The authors compare sigmoid and softmax attention combined with learned gating on GPT‑2‑scale models trained on OpenWebText, showing that sigmoid‑gated models achieve clean hard deletions without noticeable perplexity loss relative to their no‑eviction baselines.

## Key Takeaways
- Sigmoid attention yields a softer gate during training, but when combined with learned eviction it can still produce hard KV deletions that leave little PPL impact compared to the model’s own reference.  
- Under a matched live‑cache protocol on dense backbones, sigmoid‑gated models obtain lower perplexity than H₂O and KeyDiff implementations, indicating that attention normalization benefits hard deletion decisions.  
- Softmax gates do not consistently outperform these post‑hoc methods, suggesting that the substrate of attention matters more than the gating function alone.

## Context
Cache eviction is a key challenge for scaling transformer inference to massive datasets where memory constraints limit token retention. Recent work has explored differentiable gating and hard deletion strategies, yet their effectiveness often depends on subtle interactions between model architecture and training dynamics. This study highlights that attention normalization can act as a bridge between soft training signals and hard inference decisions.

## Implications
For practitioners, the findings suggest that selecting sigmoid attention may enable more efficient memory usage without sacrificing quality, especially when paired with learned eviction mechanisms. Researchers should consider how attention type influences the transferability of soft gating to hard deletions in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23296v1)
