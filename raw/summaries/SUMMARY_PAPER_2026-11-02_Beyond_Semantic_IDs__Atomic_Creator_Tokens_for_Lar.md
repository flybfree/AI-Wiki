---
title: Beyond Semantic IDs: Atomic Creator Tokens for Large-Scale Generative Recommendation
url: http://arxiv.org/abs/2611.00323v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-30_19-43-04Z_BeyondSemanticIDs_AtomicCreatorTokensforLarge_Scal.md
generated_at: 2026-11-02 21:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies the Semantic ID (SID) tokenization layer as the fundamental bottleneck in generative recommendation systems for creator discovery, rather than the language model itself. The authors propose Atomic Creator Token (ACT), a bijective tokenization scheme that assigns each creator a unique vocabulary token trained end-to-end, eliminating the many-to-one collisions inherent in SID-based approaches. In controlled experiments on production data, ACT achieves a 19.8-point improvement in creator-level Recall@15 over a matched SID baseline while simultaneously reducing per-user inference latency by approximately 2.7x.

## Key Takeaways
- The prevailing SID approach quantizes frozen embeddings into shared tokens, creating a many-to-one creator-to-SID mapping. Colliding creators must be resolved through popularity tie-breaking, which structurally caps creator-level recall and systematically biases the system toward already-popular creators, undermining the cold-start discovery objective. Additionally, the frozen quantizer blocks training gradients from reaching the creator representation, preventing the model from learning better creator embeddings.
- ACT replaces the quantizer with a one-to-one vocabulary token per creator, making collisions impossible and enabling inference as a direct top-k selection over creator logits. In a controlled comparison where the token layer is the sole variable, ACT outperforms the SID baseline by 19.8 points in Recall@15 (a 1.84x improvement), maintains its advantage even when the SID codebook is enlarged 64-fold, and operates at roughly 2.7x lower per-user latency.
- The ACT advantage generalizes beyond the proprietary production setting: on the public KuaiRand dataset, ACT is the only method that surpasses a global-popularity baseline, contingent on each creator token receiving sufficient training examples. A live A/B test further confirms directionally positive results across all reported metrics against both SID-enhanced and classic production ranking systems.

## Context
Generative recommendation systems have increasingly adopted language-model architectures that generate item identifiers as token sequences, with Semantic IDs serving as the standard interface between continuous embeddings and discrete token generation. This paper challenges a widely accepted assumption in the field by demonstrating that the tokenization layer, not the generative model, is the performance-limiting component for creator discovery tasks. The finding reframes how researchers should allocate engineering effort in generative recommender pipelines, shifting attention from model scaling to representation design.

## Implications
For practitioners building large-scale creator or content discovery platforms, ACT offers a simpler and faster alternative to SID pipelines that eliminates a class of structural failures tied to quantization collisions and frozen embeddings. The bijective design also simplifies deployment by removing the need for popularity-based tie-breaking heuristics that inadvertently reinforce existing popularity biases. For the broader research community, the controlled ablation methodology—holding the language model fixed while varying only the token layer—provides a template for isolating architectural bottlenecks in generative recommendation systems and may inform future work on item tokenization across other recommendation domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00323v1)
