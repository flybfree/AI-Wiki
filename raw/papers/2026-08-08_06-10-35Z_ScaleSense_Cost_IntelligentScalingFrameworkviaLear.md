---
title: ScaleSense: Cost-Intelligent Scaling Framework via Learned Resource Estimation in Alibaba AnalyticDB
published: 2026-08-08T06:10:35Z
authors: Yifan Wu, Yuhan Li, Zhenhua Wang, Ke Chen, Lidan Shou, Zonghao Chen, Liang Lin, Huan Li, Gang Chen
url: http://arxiv.org/abs/2608.07945v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ScaleSense: Cost-Intelligent Scaling Framework via Learned Resource Estimation in Alibaba AnalyticDB

## Abstract
Cloud-native serverless data warehouses achieve fine-grained elasticity by decoupling storage from compute, yet determining the optimal resource allocation for highly heterogeneous ad-hoc queries remains a formidable industrial challenge. Our analysis of production workloads in Alibaba AnalyticDB exposes a costly ``provisioning trap'': the fear of catastrophic resource depletion drives users to blindly over-provision resources, wasting immense monetary budgets without alleviating non-CPU bottlenecks (e.g., I/O saturation). To break this impasse, we propose ScaleSense, a proactive, query-level resource scaling framework. Specifically, it features a multi-faceted query encoder that jointly models plan topologies and hardware specifications. Crucially, a quantile-based resource predictor estimates multi-dimensional physical footprints, acting as a reliable safety net for optimal resource scaling. An auto-scaling controller then navigates the performance-cost Pareto frontier, dynamically tailoring allocations to specific business priorities without requiring model retraining. Evaluations on over 1.36 million production queries show that ScaleSense achieves state-of-the-art prediction accuracy with good prediction interval coverage. By achieving a 76.7% relative improvement in optimal resource configuration selection over the best baseline, this approach addresses the critical performance-cost trade-off while maintaining low-overhead inference latency, confirming its practical performance in production deployments. Under the performance-optimization policy, ScaleSense satisfies user-defined performance requirements while reducing monetary cost by up to 5.22x.

## Metadata
- **Published**: 2026-08-08T06:10:35Z
- **Authors**: Yifan Wu, Yuhan Li, Zhenhua Wang, Ke Chen, Lidan Shou, Zonghao Chen, Liang Lin, Huan Li, Gang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07945v1)