---
title: Rethinking Personalized Reward Modeling for LLMs under Preference Heterogeneity via Group-Debiased Federated Learning
published: 2026-08-03T00:25:52Z
authors: Seongyoon Kim, Boryeong Cho, Jihwan Oh, Seokhyun Chung, Se-Young Yun
url: http://arxiv.org/abs/2608.01556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Personalized Reward Modeling for LLMs under Preference Heterogeneity via Group-Debiased Federated Learning

## Abstract
Large language models are increasingly aligned to human preferences via reward modeling, but user preference data are sensitive and often cannot be centralized. Federated learning keeps such data local while learning a shared initial reward model, which is later personalized for each client through local fine-tuning. Because users often assign opposite labels to the same pair of responses, existing federated methods address preference heterogeneity by clustering similar clients and training one reward model per group, assuming that each group requires its own initialization. We show that this assumption is unnecessary. Under balanced preference groups, a single FedAvg model, despite starting at nearly random accuracy, surpasses reward models trained separately for each ground-truth group after only a few local optimization steps. We attribute this phenomenon to the flatness of the shared initialization: averaging across all clients learns richer shared representations that distinguish responses while canceling conflicting preference directions, leaving the model near a decision boundary that can be rapidly adapted. Group imbalance breaks this effect as the cancellation becomes asymmetric and leaves minority clients too far from the boundary to recover. Motivated by this observation, we propose FedGD (Federated Learning with Group Debiasing), which discovers latent preference groups during federated training and learns a single reward model using group-debiased client sampling. By counteracting the effect of group imbalance, FedGD learns an initialization that remains highly adaptable, enabling effective personalization without prior knowledge of the underlying groups.

## Metadata
- **Published**: 2026-08-03T00:25:52Z
- **Authors**: Seongyoon Kim, Boryeong Cho, Jihwan Oh, Seokhyun Chung, Se-Young Yun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01556v1)