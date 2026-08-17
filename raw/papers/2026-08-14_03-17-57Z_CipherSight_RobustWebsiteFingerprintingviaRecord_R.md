---
title: CipherSight: Robust Website Fingerprinting via Record-Resource Semantic Supervision under Distribution Shifts
published: 2026-08-14T03:17:57Z
authors: Runhan Song, Qiqi Liu, Chuanzhou Pan, Zhenquan Ding, Youquan Xian, Chongru Fan, Lei Cui, Wei Wang, Zhiyu Hao
url: http://arxiv.org/abs/2608.13905v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CipherSight: Robust Website Fingerprinting via Record-Resource Semantic Supervision under Distribution Shifts

## Abstract
HTTPS website fingerprinting (WF) aims to identify visited websites from metadata observable in encrypted traffic. However, real-world deployments introduce a significant out-of-distribution (OOD) problem caused by temporal and geographic changes, while previously unseen websites are common in open-world scenarios. Existing methods primarily learn from raw TCP packet sequences and struggle to capture stable and generalizable website representations, resulting in performance degradation under practical conditions.   We propose CipherSight, a TLS-record-based hierarchical framework for robust HTTPS WF. Unlike existing approaches that rely on TCP packet sequences and are sensitive to transport-layer artifacts, CipherSight learns website representations from TLS records by jointly encoding multiple record-level attributes. It introduces a hierarchical architecture that captures both intra-flow dependencies among TLS records and inter-flow interactions across concurrent flows, enabling the model to exploit structural patterns in HTTPS traffic. Besides, to learn robust representations, CipherSight employs a masked record modeling (MRM) task to capture contextual traffic semantics and leverages fine-grained record-resource annotations as privileged supervision through structure-aware objectives and semantic distillation. Experiments show that CipherSight achieves 95.41% accuracy across more than 2,000 website classes in the closed-world setting and maintains over 90% accuracy under both temporal and geographic drift, consistently outperforming all evaluated baselines.

## Metadata
- **Published**: 2026-08-14T03:17:57Z
- **Authors**: Runhan Song, Qiqi Liu, Chuanzhou Pan, Zhenquan Ding, Youquan Xian, Chongru Fan, Lei Cui, Wei Wang, Zhiyu Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13905v1)