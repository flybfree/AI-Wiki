---
title: Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm
published: 2026-08-09T12:44:47Z
authors: Hirofumi Suzuki
url: http://arxiv.org/abs/2608.08674v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm

## Abstract
In the operation of machine learning models, model update is a fundamental process that requires careful consideration of its impact on downstream decision-making. Particularly when operating explainable models, changes in explanations resulting from model updates can lead to detrimental outcomes for users. Decision trees, due to their high transparency, are frequently employed in risk-sensitive decision-making and serve as a prominent example in which the aforementioned issue is evident. However, existing research addressing similar issues has focused on explanations based on feature contributions, and thus cannot handle explanations derived from tree structures. Therefore, this paper proposes the Backward Compatibility Loss in Tree-based eXplanations (BCLTX), a loss metric that suppresses changes in decision tree explanations before and after updates. Furthermore, we design CART with Backward Compatibility in Tree-based eXplanations (CART-BCTX), a lightweight algorithm that improves upon CART for the decision tree update problem under BCLTX. Experimental results using 10 real-world datasets, including both classification and regression tasks, show that CART-BCTX achieves favorable trade-offs between prediction performances and BCLTX values, with comparable computation times to CART, regardless of the task.

## Metadata
- **Published**: 2026-08-09T12:44:47Z
- **Authors**: Hirofumi Suzuki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08674v1)