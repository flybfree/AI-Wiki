---
title: Defending Against Backdoor Attacks via Alignment Checking in Model-Contrastive Federated Learning
published: 2026-07-29T13:59:37Z
authors: Hongliang Zhang, Zhongyuan Yu, Guijuan Wang, Tianqing He, Wenshuo Ma, Xiaosong Zhang, Jiguo Yu
url: http://arxiv.org/abs/2607.26933v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Defending Against Backdoor Attacks via Alignment Checking in Model-Contrastive Federated Learning

## Abstract
Federated Learning (FL) is vulnerable to backdoor attacks because of its distributed nature in edge computing scenarios. Existing defense methods show limited efficacy as they overlook the deviations among benign local updates caused by statistical heterogeneity and the stealthiness of backdoor attacks. To tackle these issues, we propose FedDAB, a two-phase method that combines local contrastive regularization with alignment checking, to defend against backdoor attacks. In the first phase, FedDAB introduces a novel model-contrastive term into the local objective to enhance direction and magnitude consistency among benign updates. In the second phase, FedDAB employs an alignment checking strategy to evaluate each local update in terms of overall-direction alignment and parameter-level alignment with historical information, excluding updates that exhibit abnormal alignment patterns from global aggregation. We theoretically prove FedDAB's robustness with a convergence rate of $\mathcal{O}(1/T)$.   Extensive experiments show that FedDAB outperforms existing defense methods against backdoor attacks.

## Metadata
- **Published**: 2026-07-29T13:59:37Z
- **Authors**: Hongliang Zhang, Zhongyuan Yu, Guijuan Wang, Tianqing He, Wenshuo Ma, Xiaosong Zhang, Jiguo Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26933v1)