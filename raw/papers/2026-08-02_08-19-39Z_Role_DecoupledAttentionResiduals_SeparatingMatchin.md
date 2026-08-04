---
title: Role-Decoupled Attention Residuals: Separating Matching and Content Retrieval Across Depth
published: 2026-08-02T08:19:39Z
authors: Kehan Wang
url: http://arxiv.org/abs/2608.01075v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Role-Decoupled Attention Residuals: Separating Matching and Content Retrieval Across Depth

## Abstract
Depth-routing residual architectures allow Transformer layers to retrieve earlier representations instead of inheriting only the immediately preceding state. Existing Block Attention Residuals, however, use a single content-dependent depth mixture to construct the inputs to queries, keys, and values. This design couples two functionally different decisions: queries and keys determine where attention matches, whereas values determine what content is retrieved. We therefore ask whether matching and content retrieval should be forced to read from the same depth. We introduce Role-Decoupled Attention Residuals (RD-AttnRes), a minimal extension that shares one depth route between queries and keys while learning an independent value route over the same residual sources. Tying the two routing queries exactly recovers the parent architecture, while decoupling them adds only one model-width vector per layer and introduces no additional token-to-token attention operation. We evaluate RD-AttnRes using a frozen, paired pretraining protocol on FineWeb-Edu with five matched seeds for both 120M- and 343M-parameter models and a 2.0B-token training budget. RD-AttnRes improves validation negative log-likelihood in all 10 matched comparisons. The mean reductions are 0.0301 and 0.0247, corresponding to perplexity reductions of 2.97 percent and 2.43 percent at 120M and 343M parameters, respectively. Early-budget controls indicate that neither the additional parameter count, duplicated routing execution, nor a fixed value route reproduces the improvement. Routing diagnostics further reveal persistent divergence between the query-key and value depth distributions. These results suggest that, within the evaluated training regime, attention matching and content retrieval benefit from distinct reads over the residual hierarchy.

## Metadata
- **Published**: 2026-08-02T08:19:39Z
- **Authors**: Kehan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01075v1)