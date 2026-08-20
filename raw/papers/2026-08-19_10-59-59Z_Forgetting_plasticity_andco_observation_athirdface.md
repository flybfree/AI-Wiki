---
title: Forgetting, plasticity, and co-observation: a third facet of continual learning
published: 2026-08-19T10:59:59Z
authors: Timm Hess, Abhishek Jha, Gido M. van de Ven, Tinne Tuytelaars
url: http://arxiv.org/abs/2608.18803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forgetting, plasticity, and co-observation: a third facet of continual learning

## Abstract
Efficient continual learning remains a fundamental challenge for deep neural networks. While catastrophic forgetting and loss of plasticity are widely considered the primary obstacles to overcome, we show that these two issues cannot fully explain the performance gap between naive sequential training and offline joint training. In this paper, we highlight data co-observation as a distinct factor influencing continual learning performance. By decoupling the constraints of separate data access from stability and plasticity, we systematically investigate the representational benefits gained by observing training data together. Empirically, we demonstrate a consistent performance difference between joint and separate training across both supervised and self-supervised paradigms in generic data-incremental "chunking" scenarios, whilst mitigating forgetting and controlling for plasticity. Our findings indicate that simultaneous observation of training data (co-observation) yields benefits to the learner's generalization that extend well beyond mere knowledge retention, and that this effect does not require a specific continual distribution shift. Furthermore, we contextualize prominent continual learning mechanisms through this lens: while distillation-based approaches act only as effective knowledge retention mechanisms, our results suggest that the empirical success of memory replay goes beyond the mitigation of forgetting, actively reintroducing the benefits of data co-observation into the learning process.

## Metadata
- **Published**: 2026-08-19T10:59:59Z
- **Authors**: Timm Hess, Abhishek Jha, Gido M. van de Ven, Tinne Tuytelaars
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18803v1)