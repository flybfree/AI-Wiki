---
title: Omni-Prune: Query-Aware Unified Token Pruning for Efficient Omnimodal Large Language Models
url: http://arxiv.org/abs/2607.23445v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_03-51-39Z_Omni_Prune_Query_AwareUnifiedTokenPruningforEffici.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
Omni-Prune is a training-free method that prunes audio-visual tokens in large language models to reduce latency and memory usage while preserving query-relevant evidence. It achieves up to 3.25x speedup and 1.3x memory reduction with minimal performance loss.

## Key Takeaways
- Omni-Prune splits token sequences into adaptive windows at audio saliency peaks, enabling fine-grained pruning aligned with user queries.
- It scores both modalities on a unified scale that combines encoder attention and text-query relevance to keep important cross-modal links.
- A K-medoids step within each window selects representative tokens, capturing diverse cues beyond score-based selection.

## Context
Current OmniLLMs face long token sequences from synchronized audio-video inputs, causing high GPU demand. Existing pruning techniques ignore query-driven relevance and modality coupling, limiting efficiency gains.

## Implications
This approach enables faster inference for real-time multimodal applications such as video assistants and smart home devices. Practitioners can adopt training-free pruning to deploy large models on edge hardware without retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23445v1)
