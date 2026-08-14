---
title: Statistical Properties of Robust Learning under Distributional Shifts
published: 2026-08-13T12:06:48Z
authors: Zhiyi Li, Xiaojie Mao, Yunbei Xu, Ruohan Zhan
url: http://arxiv.org/abs/2608.13133v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Statistical Properties of Robust Learning under Distributional Shifts

## Abstract
Distributional shifts arise when the target deployment environment differs from the source environment that generated the training data. Robust learning frameworks such as Distributionally Robust Optimization (DRO) and Robust Satisficing (RS) aim to address this challenge, yet their finite-sample guarantees under such shifts, and their systematic comparison, remain underexplored: existing analyses typically establish guarantees either in the source environment or for adversarial worst-case performance over an ambiguity set. This paper instead studies generalization error in the target environment---the excess loss under the shifted target distribution. Our contributions are threefold. First, we derive finite-sample generalization error bounds in the shifted target environment for both DRO and RS. These bounds explicitly characterize the trade-off between reduced sensitivity to shift and the regularization penalty induced by each method's robustness hyperparameter, and they avoid the curse of dimensionality associated with Wasserstein empirical concentration. Second, when partial shift information such as shift magnitude or direction is available, we propose information-directed hyperparameter calibrations and compare the two methods given the same information. Under these calibrations, and in the partial-information regimes we study, DRO and RS exhibit complementary theoretical and empirical behavior. Finally, we apply the framework to a network lot-sizing problem, using it to interpret how robust policies respond to positive shifts in the demand distribution. Together, these results fill a gap in understanding the statistical properties of robust learning methods under distributional shifts and provide a principled basis for comparing DRO and RS.

## Metadata
- **Published**: 2026-08-13T12:06:48Z
- **Authors**: Zhiyi Li, Xiaojie Mao, Yunbei Xu, Ruohan Zhan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13133v1)