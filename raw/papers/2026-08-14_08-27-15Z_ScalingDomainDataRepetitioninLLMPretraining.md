---
title: Scaling Domain Data Repetition in LLM Pretraining
published: 2026-08-14T08:27:15Z
authors: Jingwei Li, Xinran Gu, Rui Dai, Xintong Hao, Chengyin Xu, Yan Wu, Shuran Zheng, Jingzhao Zhang
url: http://arxiv.org/abs/2608.14071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Domain Data Repetition in LLM Pretraining

## Abstract
As large language models scale, their training-token budgets must also increase to maintain an appropriate tokens-per-parameter ratio (\(\mathrm{TPP}\)). However, high-quality domain data is much harder to scale than general web data. As model size and the training-token budget increase, its fraction in the training mixture tends to decrease. Repeating the available high-quality data provides an effective way to counteract this dilution, but excessive repetition may lead to overfitting. We study this trade-off under practical LLM scaling, where the training-token budget grows proportionally with model size. For a fixed domain, we first find that, surprisingly at a fixed \(\mathrm{TPP}\), the optimal repetition count mildly increases with model size. Across different domains, we find that the optimal repetition count is strongly negatively correlated with the final validation loss of a domain: domains with lower loss can generally benefit from more repetitions. In contrast, the amount of unique domain data is only weakly related to the optimal repetition count. These findings suggest that repetition counts tuned on smaller proxy models with the same \(\mathrm{TPP}\) can provide a practical estimate for larger models.

## Metadata
- **Published**: 2026-08-14T08:27:15Z
- **Authors**: Jingwei Li, Xinran Gu, Rui Dai, Xintong Hao, Chengyin Xu, Yan Wu, Shuran Zheng, Jingzhao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14071v1)