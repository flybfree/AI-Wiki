---
title: LatentMT: Machine Translation with Latent Reasoning
published: 2026-07-21T01:38:23Z
authors: Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang, Wenhui Zhu, Zhipeng Wang, Muhammad Abdul-Mageed
url: http://arxiv.org/abs/2607.18618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LatentMT: Machine Translation with Latent Reasoning

## Abstract
Latent-reasoning looped language models (LoopLMs) offer a different scaling path for machine translation (MT): instead of increasing parameter count or emitting explicit chain-of-thought tokens, they spend additional recurrent computation inside hidden states. We introduce LatentMT, the first systematic study of latent-reasoning LoopLMs for machine translation. LatentMT adapts a small 2.6B-parameter backbone model with lightweight training. Across 32 translation directions spanning high-, mid-, and low-resource languages, LatentMT achieves performance comparable to models three to five times larger. It is competitive in a high-resource language and achieves state-of-the-art performance on both mid-resource and low-resource languages. Studying the behavior of scaling the number of recurrent reasoning steps, we find that recurrent computation consistently improves translation quality in early steps, then saturates quickly afterwards. Our mechanistic analysis shows that hidden-representation differences shrink along the recurrent reasoning-step axis, supporting the observed saturation in performance. Finally, our efficiency analysis shows that LatentMT requires lower training and inference compute than much larger non-latent-reasoning models with similar performance, making latent recurrent computation a promising path toward compact, efficient, and strong machine translation.

## Metadata
- **Published**: 2026-07-21T01:38:23Z
- **Authors**: Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang, Wenhui Zhu, Zhipeng Wang, Muhammad Abdul-Mageed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18618v1)