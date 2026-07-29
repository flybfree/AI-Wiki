---
title: Memory Layer: Train the In-Model Cache for Recommendation Models
published: 2026-07-27T22:15:13Z
authors: Liangyuan Na, Gufan Yin, Yixin Bao, Xianjie Chen, Justin Lin, Ziheng huang, Xinyuan Zhang, Wen Zhang, Hao Lin, Xiaoheng Mao, Shuo Tang, Min Yu, Lei Chen, Chao yang, Ziliang Zhao, Mengjiao Zhou, Zheng Qi, Dmitry Barablin, Chuo-Yun Yang, Kaustubh Vartak, Tingting Zhang, Arun Kumar Singh
url: http://arxiv.org/abs/2607.25110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory Layer: Train the In-Model Cache for Recommendation Models

## Abstract
Early ranking stages in recommendation systems precompute item embeddings and cache them in-model for scoring within strict latency constraints. Because this cache exists only at serving time, outside the training loop, training and serving use different item representations, a structural discrepancy that limits quality and adds operational fragility. We show that co-designing the training and serving paths removes this representation discrepancy at its source. We introduce the memory layer, an in-model key-value embedding cache co-trained with the model: the item tower writes embeddings during training and the model reads them at serving, one source of truth for item representations by construction. Always-on embeddings cover items not yet cached, so every item receives a prediction, and the design consolidates three separate trainer-to-predictor update paths into a single self-contained pipeline. Deployed in production on Instagram Reels, the memory layer raises prediction coverage from 96% to 100%, improves embedding freshness from $O(5\text{ min})$ to $O(20\text{ s})$, and narrows the training-serving Normalized Entropy (NE) gap by up to 86%, yielding over $2\times$ recall for the freshest content and a 5-6% cold start engagement lift. Because embeddings are produced during training, the system needs no separate bulk-evaluation or publish-time recomputation, cutting training-and-publish computational cost by 30% at neutral serving computational cost.

## Metadata
- **Published**: 2026-07-27T22:15:13Z
- **Authors**: Liangyuan Na, Gufan Yin, Yixin Bao, Xianjie Chen, Justin Lin, Ziheng huang, Xinyuan Zhang, Wen Zhang, Hao Lin, Xiaoheng Mao, Shuo Tang, Min Yu, Lei Chen, Chao yang, Ziliang Zhao, Mengjiao Zhou, Zheng Qi, Dmitry Barablin, Chuo-Yun Yang, Kaustubh Vartak, Tingting Zhang, Arun Kumar Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25110v1)