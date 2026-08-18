---
title: PERO: Efficient Robust Post-Training Foundation Models for Encrypted Traffic Classification
published: 2026-08-16T03:10:09Z
authors: Wumei Du, Jiarong Wen, Kaiyu Zhang, Zi Yang, Yiqin Lv, Longfei Zhang, Dong Liang, Zheng Xie
url: http://arxiv.org/abs/2608.15504v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PERO: Efficient Robust Post-Training Foundation Models for Encrypted Traffic Classification

## Abstract
Encrypted traffic classification is vital for network security, yet real-world deployments are inherently sensitive to rare but high-loss errors such as misclassification of malicious traffic. The encrypted traffic foundation model, as a promising general-purpose technique, can achieve impressive overall performance. However, employing standard objectives such as empirical risk minimization often overlooks high-risk tail events, and commonly used performance metrics hardly reflect robustness limitations in risk-sensitive scenarios. Directly applying robust optimization objectives, such as conditional value-at-risk, to post-training is computationally prohibitive for large models, as identifying high-loss samples exhausts substantial computation. To this end, we propose Pre-Evaluation Robust Optimization (PERO), an efficient robust post-training framework for encrypted traffic foundation models. PERO employs a lightweight proxy to estimate sample-wise risk and selects a subset of high-risk samples to update the foundation model, decoupling risk estimation from expensive large-model optimization. Extensive experiments on typical encrypted traffic datasets show that PERO achieves competitive or superior robustness and average performance compared to outstanding robust post-training methods, while significantly reducing computational and memory costs.

## Metadata
- **Published**: 2026-08-16T03:10:09Z
- **Authors**: Wumei Du, Jiarong Wen, Kaiyu Zhang, Zi Yang, Yiqin Lv, Longfei Zhang, Dong Liang, Zheng Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15504v1)