---
title: Can Released LLM Vocabularies Support Token-Level Estimation of Hidden Corpora?
published: 2026-08-11T09:14:25Z
authors: Qingjie Zhang, Xingzhang Ren, Zixuan Chen, Jinfeng Li, YueFeng Chen, Yitong Yang, Hui Xue, Dayiheng Liu, Han Qiu
url: http://arxiv.org/abs/2608.10690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Released LLM Vocabularies Support Token-Level Estimation of Hidden Corpora?

## Abstract
Pretraining corpus composition shapes LLM capabilities, but it often remains hidden even when model weights are released. Prior work has inferred corpus mixtures or traced specific token groups from released tokenizer vocabularies; in contrast, we estimate corpus ratios for arbitrary target tokens. We first show that BPE tokenizers trained on different corpora share stable token ID--ratio distributions, motivating distribution transfer from known corpora to a target tokenizer trained on hidden corpora. We then propose Quantile-Guided Density Estimation (QGDE), which approximates this distribution with multiple quantile trends and uses local density weighting to produce token-level estimates. In controlled settings and a realistic setting using the released SmolLM tokenizer, QGDE achieves mean relative errors as low as 3.00% for token-level estimation and 3.08% after aggregation into category-level mixtures. These results suggest that released tokenizer vocabularies provide a useful signal for fine-grained corpus estimation beyond coarse composition inference.

## Metadata
- **Published**: 2026-08-11T09:14:25Z
- **Authors**: Qingjie Zhang, Xingzhang Ren, Zixuan Chen, Jinfeng Li, YueFeng Chen, Yitong Yang, Hui Xue, Dayiheng Liu, Han Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10690v1)