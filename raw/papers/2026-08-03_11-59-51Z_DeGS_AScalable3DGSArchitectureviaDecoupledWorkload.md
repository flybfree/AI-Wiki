---
title: DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization
published: 2026-08-03T11:59:51Z
authors: Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng
url: http://arxiv.org/abs/2608.02099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization

## Abstract
3D Gaussian Splatting (3DGS) has emerged as a leading technique for real-time novel view synthesis, yet existing 3DGS accelerators suffer from poor architectural scalability: increasing the number of PEs leads to marginal performance improvement during rendering. We identify that the root cause is the tightly coupled ``checking-while-blending'' dataflow, which exacerbates PE underutilization caused by spatial redundancy from irregular Gaussian coverage and temporal redundancy from asynchronous pixel-wise termination under parallel execution.   To address this issue, we propose DeGS, a scalable architecture for efficient 3DGS inference. To systematically eliminate the redundancies inherent in rendering, DeGS exploits a decoupled dataflow, restructuring the coupled $α$-checking, transmittance checking, and $α$-blending of the standard rendering process into consecutive workload parsing, reorganization, and blending stages. This allows the fragmented, length-variable, and temporal-dependent workloads to be reorganized into compact, conflict-free, and dense workloads prior to blending, thereby significantly improving PE utilization during parallel blending. Implemented in 28 nm technology, DeGS achieves 2.36$\times$--7.25$\times$ throughput, 1.82$\times$--6.02$\times$ end-to-end speedup, and 1.59$\times$--4.42$\times$ energy efficiency over state-of-the-art 3DGS accelerators (GSCore, GBU, GCC) across diverse scenes and resolutions (720p to 8K). Moreover, scaling from 16 to 1024 PEs, DeGS maintains over 80\% PE utilization at high resolutions, significantly outperforming existing accelerators.

## Metadata
- **Published**: 2026-08-03T11:59:51Z
- **Authors**: Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02099v1)