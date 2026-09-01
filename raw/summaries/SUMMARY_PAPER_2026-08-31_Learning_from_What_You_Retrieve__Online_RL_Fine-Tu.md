---
title: Learning from What You Retrieve: Online RL Fine-Tuning for Semantic Retrieval
url: http://arxiv.org/abs/2608.30753v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_13-21-47Z_LearningfromWhatYouRetrieve_OnlineRLFine_Tuningfor.md
generated_at: 2026-08-31 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PAO (Positive‑Advantage‑Only), a selective reinforcement learning method that adapts dual‑encoder retrievers using reward‑model feedback without altering the frozen document index. Experiments on industrial and public datasets show that PAO improves retrieval quality compared with standard RL and distillation baselines.

## Key Takeaways
- The proposed PAO only updates retrieved items whose advantages are positive, thereby pulling query embeddings toward high‑reward regions while leaving negative samples untouched to preserve the global semantic manifold.  
- Standard policy‑gradient approaches degrade embedding geometry because they push both positive and negative samples away from each other in a frozen space, which harms pre‑trained similarity structures.  
- PAO’s selective optimization yields significant performance gains on both massive industrial datasets and public benchmarks, outperforming conventional RL and distillation methods.

## Context
In large‑scale e‑commerce retrieval, dual‑encoder models are optimized for contrastive learning while rerankers handle fine‑grained relevance, creating a mismatch that limits end‑to‑end quality. Reinforcement learning offers a way to incorporate reward feedback but often requires costly updates to the document index. PAO addresses this by providing an efficient, geometry‑preserving adaptation strategy.

## Implications
PAO enables practitioners to improve retrieval systems without breaking industrial constraints on frozen indices, reducing retraining costs and preserving model stability. The method’s success suggests that selective RL can be a viable alternative to full‑scale fine‑tuning for real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30753v1)
