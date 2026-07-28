---
title: Exploring Budgeted Image Classification with Content-Sensitive Resource Allocation
published: 2026-07-27T04:49:14Z
authors: Athanasios G. Papadopoulos
url: http://arxiv.org/abs/2607.23997v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exploring Budgeted Image Classification with Content-Sensitive Resource Allocation

## Abstract
The ever-growing adoption of Artificial Intelligence (AI) creates the need to deploy Deep Neural Networks in a variety of computational environments. We consider dynamic environments, where computational requirements are subject to change, and we pose the following question: How do we adjust the complexity of an AI classification system, in order to maximize its accuracy, while meeting changing computational constraints? We call this problem Budgeted Image Classification, and we formally formulate it as a resource allocation integer program. Given a computational budget, a batch of images, and a classification system that can make decisions with varying complexity (it has multiple decision points), we explore strategies to allocate images to decision points, in order to maximize accuracy within the available budget. The original integer program is NP-Hard, so, we propose a continuous relaxation, leading to a content-agnostic allocation strategy which assigns images to decision points without considering their particular content. We address this issue by proposing a content-sensitive strategy, that we experimentally show it leads to superior performance. We theoretically study the behavior of our strategies, deriving conditions that must be satisfied by decision points to be suitable for budgeted classification. We analyze fails cases, offering insights for future research directions.

## Metadata
- **Published**: 2026-07-27T04:49:14Z
- **Authors**: Athanasios G. Papadopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23997v1)