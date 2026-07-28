---
title: SLA-Constrained Carbon-Aware Routing in Geo-Distributed Serverless Clouds
published: 2026-07-24T16:13:28Z
authors: Anmol Chaudhary, Rahul Mishra
url: http://arxiv.org/abs/2607.22806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SLA-Constrained Carbon-Aware Routing in Geo-Distributed Serverless Clouds

## Abstract
Modern cloud deployments distribute applications across multiple geographic regions, yet standard routing mechanisms prioritize latency while ignoring the fluctuating carbon intensity of local power grids. Latency-driven routing incurs avoidable carbon emissions, particularly when cleaner regions are within acceptable latency bounds. The proposed model formulates the carbon-aware serverless routing problem as a constrained optimization over geo-distributed cloud regions and introduces an SLA-constrained carbon-aware routing policy that achieves optimal carbon reduction within the SLA-feasible region, evaluated using real carbon intensity measurements across 5 primary AWS deployments. Experimental results show that the proposed policy achieves up to 46.8% carbon reduction while maintaining zero SLA violations across all evaluated thresholds. The system reduces carbon by an average of 27.4% under mixed workloads, and the routing overhead is very low (less than 0.02% of total request latency). A scalability study across 12 AWS regions spanning 6 continents demonstrates that average carbon savings increase from 27.4% to 47.5% as routing flexibility expands under mixed workloads. The proposed work contributes to SDG 13 (Climate Action) and SDG 7 (Affordable and Clean Energy) by enabling low-carbon routing decisions. These results indicate that cloud systems can achieve significant carbon savings without compromising user experience.

## Metadata
- **Published**: 2026-07-24T16:13:28Z
- **Authors**: Anmol Chaudhary, Rahul Mishra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22806v1)