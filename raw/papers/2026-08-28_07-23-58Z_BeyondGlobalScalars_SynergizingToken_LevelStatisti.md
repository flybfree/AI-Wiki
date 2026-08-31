---
title: Beyond Global Scalars: Synergizing Token-Level Statistics and Deep Semantics for Adversarial AIGC Text Detection
published: 2026-08-28T07:23:58Z
authors: Peiming Li, Yifan Wang, Zhiyuan Hu, Shiyu Li, Zheng Wei, Yang Tang
url: http://arxiv.org/abs/2608.28009v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Global Scalars: Synergizing Token-Level Statistics and Deep Semantics for Adversarial AIGC Text Detection

## Abstract
The rapid evolution of large language models necessitates robust machine-generated text detection. Existing paradigms typically follow two isolated tracks. Training-free methods rely on global statistical scalars such as perplexity, while training-based methods utilize semantic hidden states. Both approaches exhibit fundamental vulnerabilities in adversarial scenarios. Global scalars act as lossy compressions that obscure local probabilistic burstiness in interleaved texts, whereas pure semantic models overfit to specific fingerprints and remain susceptible to spoofing. To expose these flaws, we introduce MOSAIC, a comprehensive adversarial benchmark comprising 16000 samples across a full-granularity attack spectrum. To address these challenges, we propose NeuroStat, an end-to-end framework bridging the statistical and semantic gap. NeuroStat captures uncompressed token-level probabilistic logits alongside deep semantic hidden states from a single causal language model backbone. We fuse these heterogeneous signals through Macro-State Residual Modulation, which adaptively calibrates local convolutional features using global uncertainty indicators. Orthogonal and contrastive losses further ensure the learning of complementary representations. Extensive experiments demonstrate that NeuroStat maintains exceptional robustness on MOSAIC compared to the severe degradation of state-of-the-art methods, establishing a new standard for adversarial text detection. Code and the MOSAIC benchmark are available at https://github.com/TencentBAC/NeuroStat.

## Metadata
- **Published**: 2026-08-28T07:23:58Z
- **Authors**: Peiming Li, Yifan Wang, Zhiyuan Hu, Shiyu Li, Zheng Wei, Yang Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28009v1)