---
title: Why Static Probes Fail: Context Determines Deception Feature Composition
published: 2026-10-20T03:42:51Z
authors: Yao Huang, Siyuan Chen, Zhenghan Zhou, Yinpeng Dong
url: http://arxiv.org/abs/2610.27577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Static Probes Fail: Context Determines Deception Feature Composition

## Abstract
With increasing autonomy, Large Language Models (LLMs) may engage in deceptive behaviors, such as scheming to pursue misaligned goals or sandbagging to escape oversight. Monitoring outputs alone is insufficient, as models can produce seemingly benign responses while harboring misaligned internal objectives. While mechanistic approaches like linear probing are promising, they rely on the assumption that deception corresponds to a single direction in representation space. We demonstrate that such single-direction probes fail to generalize across diverse deception scenarios. To bridge this gap, we propose representing deception as a multi-dimensional subspace rather than a single direction. Our method utilizes iterative orthogonal decomposition to identify complementary directions that capture distinct facets of deceptive intent. To effectively leverage these directions for detection, we find that static combinations prove brittle due to strong domain dependence across different scenarios. We therefore introduce a domain-adaptive gating mechanism that dynamically composes the extracted directions through few-shot adaptation at test time. With only 10 examples, our approach achieves an average AUROC of 0.97 and 94% recall at 5% FPR across all evaluated datasets, substantially outperforming existing methods.

## Metadata
- **Published**: 2026-10-20T03:42:51Z
- **Authors**: Yao Huang, Siyuan Chen, Zhenghan Zhou, Yinpeng Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27577v1)