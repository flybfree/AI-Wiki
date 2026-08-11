---
title: Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts
published: 2026-08-09T18:31:16Z
authors: Zongfei Li
url: http://arxiv.org/abs/2608.08853v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts

## Abstract
Sparse Mixture-of-Experts (MoE) routers commonly use the same scores both to select experts and to weight their already-computed outputs. We study whether these two roles, dispatch and aggregation, should be coupled. On pretrained OLMoE-1B-7B, we keep selected Top-8 expert IDs, expert computation, and total selected router mass fixed and change only within-set aggregation. A structured oracle improves full-horizon cross-entropy by 0.0160 +/- 0.0039 across three seeds; the router's top-scored expert is the counterfactual-best vertex only 17.2% of the time, with router-utility Spearman 0.030. We therefore train Fixed-Dispatch Adaptive Aggregation (FDAA), a 301K-parameter post-compute head optimized directly with the language-modeling objective while freezing the backbone, router, and experts. On OLMoE, FDAA improves fresh WikiText-103 test by Delta CE = -0.1523 +/- 0.0031 across three seeds, and mixed-domain training gives robust gains on WikiText-103, C4, and held-out Penn Treebank under frozen confirmatory evaluation. We also replicate the fixed-dispatch audit on DeepSeek-V2-Lite, which uses Top-6 routed experts plus shared experts. Best-vertex headroom remains significant on WikiText and C4, while router Top1 identifies the best selected expert in only 12.5% and 16.7% of audited examples. In a one-seed mixed-domain replication, FDAA improves locked WikiText and PTB, while C4 is statistically neutral. These results support a cross-architecture distinction between expert selection and expert commitment.

## Metadata
- **Published**: 2026-08-09T18:31:16Z
- **Authors**: Zongfei Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08853v1)