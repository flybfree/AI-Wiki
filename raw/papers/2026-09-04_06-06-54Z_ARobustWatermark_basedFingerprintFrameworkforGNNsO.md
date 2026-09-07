---
title: A Robust Watermark-based Fingerprint Framework for GNNs Ownership Verification
published: 2026-09-04T06:06:54Z
authors: Han Zhang, Yan Wang, Guanfeng Liu, Pengfei Ding, Huaxiong Wang, Kwok-Yan Lam
url: http://arxiv.org/abs/2609.04772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Robust Watermark-based Fingerprint Framework for GNNs Ownership Verification

## Abstract
The high training cost of Graph Neural Networks (GNNs) has raised growing concerns regarding model ownership infringement, such as model stealing and unauthorized misuse. To verify model ownership and prevent significant economic losses, two groups of GNN Ownership Verification (OV) methods have been proposed: watermark-based methods and fingerprint-based methods. However, these methods typically face three limitations: (1) the performance degradation of protected models caused by out-of-distribution (OOD) watermark graphs with respect to the training set; (2) the unrealistic assumption that surrogate models have been trained on a watermark-containing training set; and (3) over-reliance on specific output levels for fingerprint extraction. In this paper, we propose a Robust watErMArk-based fingeRprint frameworK for GNNs, named REMARK. REMARK first generates carefully crafted in-distribution watermark graphs that maximize output differences between GNN models, thus mitigating OOD-induced performance degradation. REMARK then extracts robust fingerprints from these output differences to verify GNN ownership, thereby removing the assumptions that surrogate models must be trained on a watermark-containing dataset or expose specific output levels. Extensive experiments across widely used real-world datasets and GNN architectures demonstrate that REMARK achieves state-of-the-art OV accuracy and robustness while preserving the utility of protected models.

## Metadata
- **Published**: 2026-09-04T06:06:54Z
- **Authors**: Han Zhang, Yan Wang, Guanfeng Liu, Pengfei Ding, Huaxiong Wang, Kwok-Yan Lam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04772v1)