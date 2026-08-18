---
title: Who Leads Now? Token-Level Modality Arbitration for Chart-to-Code Generation
published: 2026-08-16T03:33:01Z
authors: Qinghao Fu, Yarong Wang, Shunlei Ning, Yilin Wang, Shunwen Bai, Xinda Wang, Jiaotuan Wang, Yinan Nie, Wei Zhou
url: http://arxiv.org/abs/2608.15510v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Leads Now? Token-Level Modality Arbitration for Chart-to-Code Generation

## Abstract
Chart-to-code generation requires a model to read the fine-grained visual details of a chart and write executable code that reproduces it. Existing chart-to-code methods either train visual and coding abilities separately, or fine-tune on chart-to-code data with the two abilities entangled. Neither strategy accounts for the distinct nature of the two abilities or the interference that arises when they are optimized together. We propose MoCA (Mixture of Cross-modal Arbitration), which separates the two abilities rather than blending them. MoCA is built on Cross-modal Arbitration Block (CAB), which maintains a visual branch and a code branch as two distinct pathways, and a lightweight arbiter that arbitrates their relative contributions at every layer and generated token. We train MoCA in two stages: a supervised warm-up on self-distilled reasoning trajectories that decomposes visual understanding into explicit steps, followed by reinforcement learning with rewards on both the reasoning process and the final code. Analysis shows that the arbiter learns structured rather than arbitrary allocations, with expert contributions varying systematically across tokens, layers, and instances. Across three benchmarks, MoCA delivers competitive performance against general-domain and chart-specialized models. Ablation results show that the gains cannot be attributed to a larger model size alone, but instead arise from the joint contributions of complementary visual and code branch initialization and input-conditioned arbitration through CAB.

## Metadata
- **Published**: 2026-08-16T03:33:01Z
- **Authors**: Qinghao Fu, Yarong Wang, Shunlei Ning, Yilin Wang, Shunwen Bai, Xinda Wang, Jiaotuan Wang, Yinan Nie, Wei Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15510v1)