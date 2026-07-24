---
title: Dual Attention Residuals
published: 2026-07-21T05:42:55Z
authors: Xingda Yu, Yining Li, Xinzhang Liu, Zhihao Yang, Haowei He, Chao Wang, Yongxiang Li, Shuangyong Song
url: http://arxiv.org/abs/2607.18730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual Attention Residuals

## Abstract
Recent work extends Transformer residual pathways along two complementary axes: historical retrieval selects information from earlier depths, whereas multi-stream methods maintain multiple residual trajectories. These capabilities have largely been studied in isolation, and assigning an independent retriever to each stream still prevents one trajectory from influencing depth selection in another. We propose Dual Attention Residuals (DAR), which brings multi-stream interaction into historical retrieval through reciprocal cross-stream addressing. For each target stream, DAR computes depth weights from normalized states in the opposite stream and applies them to values from the target stream's own history. The retrieved states are combined for an unchanged Transformer branch and updated through constrained gated writes; a block-form variant operates on block-level histories to control overhead. Across dense models from 0.1B to 1B parameters and a 7B sparse-MoE model, DAR consistently improves validation loss over standard residual Transformers and Attention Residuals. Routing ablations show that the gain cannot be explained by an additional stream or value projection alone. Representation and intervention analyses further show that reciprocal cross-stream selection preserves depth-wise diversity and avoids the redundancy or functional imbalance observed in alternative two-stream designs.

## Metadata
- **Published**: 2026-07-21T05:42:55Z
- **Authors**: Xingda Yu, Yining Li, Xinzhang Liu, Zhihao Yang, Haowei He, Chao Wang, Yongxiang Li, Shuangyong Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18730v1)