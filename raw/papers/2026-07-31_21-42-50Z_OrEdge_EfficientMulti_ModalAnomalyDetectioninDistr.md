---
title: OrEdge: Efficient Multi-Modal Anomaly Detection in Distributed Software Systems via Orthogonal-Domain Learning
published: 2026-07-31T21:42:50Z
authors: Amr M. Zaki, Farhoud Jafari Kaleibar, Honggeun Ji, Komal Sarda, Marin Litoiu
url: http://arxiv.org/abs/2608.00309v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OrEdge: Efficient Multi-Modal Anomaly Detection in Distributed Software Systems via Orthogonal-Domain Learning

## Abstract
We introduce Orthogonal-Edge (OrEdge), a lightweight framework for real-time anomaly detection in multi-modal distributed software systems. Unlike existing approaches that rely on computationally expensive attention- and graph-based architectures, OrEdge leverages orthogonal-domain temporal representations to achieve accurate anomaly detection with substantially lower computational complexity and model size. It jointly analyzes heterogeneous monitoring data, including logs, metrics, and traces, to identify abnormal software behavior, capture temporal dependencies, and reduce redundancy across observability signals. At its core, OrEdge incorporates OrEdgeCore, a lightweight orthogonal-domain reconstruction module that captures recurring temporal patterns while suppressing transient variations. Evaluated on three real-world microservice datasets (MSDS, SN, and TT), OrEdge achieves competitive detection performance while reducing the reconstruction model size to at most 9.6K parameters, compared with 20K--143K parameters in existing methods. This compact design enables efficient deployment on resource-constrained edge devices: on Raspberry Pi platforms, OrEdge achieves sub-second inference and reduces inference latency by over an order of magnitude compared with existing approaches. Extensive ablation studies, sensitivity analyses, orthogonal basis evaluations, and qualitative case studies further validate the effectiveness of each design component. Overall, OrEdge demonstrates that orthogonal-domain temporal modeling provides an effective alternative to computationally intensive attention- and graph-based architectures, achieving a favorable balance between detection accuracy and computational efficiency for real-time multi-modal anomaly detection in edge environments. The code is available at https://github.com/theamrzaki/MicroService_Twin_Original.

## Metadata
- **Published**: 2026-07-31T21:42:50Z
- **Authors**: Amr M. Zaki, Farhoud Jafari Kaleibar, Honggeun Ji, Komal Sarda, Marin Litoiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00309v1)