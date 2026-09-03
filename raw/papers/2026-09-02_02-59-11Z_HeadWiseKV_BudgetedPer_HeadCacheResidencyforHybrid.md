---
title: HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models
published: 2026-09-02T02:59:11Z
authors: Renjie Xie, Juncheng Yang, Aoting Hu, Mingxi Zhang, Liyao Wu, Zheheng Hong, Wei Xu
url: http://arxiv.org/abs/2609.02029v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models

## Abstract
Long-context inference retains a growing key--value (KV) cache during decoding, which consumes substantial GPU memory and can reduce generation throughput. This bottleneck remains in hybrid language models because their residual global-attention layers can dominate context-dependent cache demand. We study how to allocate this state under an aggregate KV-residency budget. We introduce HeadWiseKV, a training-free framework that compresses the residual global KV caches of hybrid language models while preserving their native local, recurrent, and linear paths. It assigns each physical KV head a static, multilevel history window, making cache demand predictable before serving. We formulate this allocation as a restricted operational rate--distortion problem and propose SeqCalib as the core policy-generation algorithm in HeadWiseKV. SeqCalib processes layers in execution order and conditions each decision on the lower-layer policy used at deployment, thereby accounting for interactions across depth. A grouped-cache runtime materializes the selected policy as actual per-head KV residency rather than a mask over a full cache. We evaluate downstream quality across four hybrid long-context models and study physical residency and serving behavior on Qwen3.6-27B. HeadWiseKV retains near-Full-KV RULER and LoCoMo quality across the evaluated models. In the fixed-model systems study, it reduces sampled peak device memory by 8.59\% at a 112K context length and extends the largest verified successful context from 114K to 161K.

## Metadata
- **Published**: 2026-09-02T02:59:11Z
- **Authors**: Renjie Xie, Juncheng Yang, Aoting Hu, Mingxi Zhang, Liyao Wu, Zheheng Hong, Wei Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02029v1)