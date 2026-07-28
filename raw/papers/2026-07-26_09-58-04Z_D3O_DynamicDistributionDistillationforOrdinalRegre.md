---
title: D3O: Dynamic Distribution Distillation for Ordinal Regression
published: 2026-07-26T09:58:04Z
authors: Chunlai Dong, Yaojun Hu, Yuyang Xu, Haochao Ying, Jian Wu
url: http://arxiv.org/abs/2607.23575v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D3O: Dynamic Distribution Distillation for Ordinal Regression

## Abstract
Ordinal regression is widely used in scenarios where labels are discrete yet inherently ordered. In practice, however, ordinal labels are often obtained by discretizing underlying continuous semantics through subjective human judgment, resulting in ambiguous boundaries and annotation noise. Such uncertainty challenges existing methods that rely on fixed supervision targets, which may reinforce biased ordering under subjective annotations. To address this limitation, we propose D3O, a dynamic distribution distillation framework that replaces static supervision with training-driven evolution of ordinal label distributions via self-distillation. Specifically, we introduce a contrastive ordinal-aware label enhancement module that leverages vision-language alignment to recover refined label distributions capturing both inter-class ambiguity and instance-level uncertainty. Furthermore, we design a CDF-based cross-layer interaction distillation mechanism to propagate cumulative ordinal structure across network hierarchy, ensuring consistent ordinal geometry in intermediate representations. Extensive experiments on four general ordinal regression tasks demonstrate that our proposed D3O consistently outperforms existing approaches, particularly under severe class imbalance and noisy supervision. These results highlight the effectiveness of dynamic supervision in learning robust ordinal representations beyond fixed targets. The code will be publicly available.

## Metadata
- **Published**: 2026-07-26T09:58:04Z
- **Authors**: Chunlai Dong, Yaojun Hu, Yuyang Xu, Haochao Ying, Jian Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23575v1)