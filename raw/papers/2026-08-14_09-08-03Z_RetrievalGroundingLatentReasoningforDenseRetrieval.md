---
title: Retrieval Grounding Latent Reasoning for Dense Retrieval
published: 2026-08-14T09:08:03Z
authors: Gang Zhou, Xiongxi Yu, Hu Tian, Yang Wei, Lu Pan, Ke Zeng, Shibiao Xu, Xiaolong Zheng
url: http://arxiv.org/abs/2608.14107v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval Grounding Latent Reasoning for Dense Retrieval

## Abstract
Reasoning-intensive retrieval requires text representations to capture not only semantic similarity, but also the reasoning needed to determine relevance under a given retrieval instruction. Existing reasoning-enhanced embedding models improve retrieval by incorporating reasoning information into dense representations, yet their supervision is typically dominated by the final retrieval objective. As a result, latent reasoning trajectories may learn shortcut reasoning patterns that preserve retrieval performance without producing meaningful incremental retrieval gains. We propose Retrieval Grounding Latent Reasoning (RGLT), a latent reasoning framework for dense retrieval that explicitly connects intermediate latent transitions with retrieval improvements. RGLT performs non-autoregressive reasoning in hidden space through an instruction-conditioned latent reasoning trajectory constructed from silent tokens. It combines process-supervised explicit-to-implicit distillation with retrieval-grounded supervision, using stage-wise CoT reconstruction to shape intermediate latent states and retrieval-effect credit to optimize incremental retrieval gains across the latent reasoning trajectories. Experiments on reasoning-intensive retrieval benchmarks show that RGLT consistently outperforms strong baselines while preserving efficient embedding inference.

## Metadata
- **Published**: 2026-08-14T09:08:03Z
- **Authors**: Gang Zhou, Xiongxi Yu, Hu Tian, Yang Wei, Lu Pan, Ke Zeng, Shibiao Xu, Xiaolong Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14107v1)