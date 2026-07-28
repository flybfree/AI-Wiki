---
title: SLA-Constrained Carbon-Aware Routing in Geo-Distributed Serverless Clouds
url: http://arxiv.org/abs/2607.22806v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_16-13-28Z_SLA_ConstrainedCarbon_AwareRoutinginGeo_Distribute.md
generated_at: 2026-07-27 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an SLA-constrained carbon-aware routing model for serverless cloud services that balances latency requirements with real-time carbon intensity data across geographic regions. The proposed policy minimizes emissions within feasible Service Level Agreements and achieves up to 46.8% reduction in carbon output while guaranteeing zero SLA violations.

## Key Takeaways
- The model integrates live carbon intensity measurements from five AWS deployments, allowing routing decisions that prioritize low-carbon zones without exceeding latency budgets.
- Experimental results demonstrate a 27.4% average carbon reduction under mixed workloads and up to 46.8% peak savings when routing flexibility is maximized.
- Routing overhead remains negligible at less than 0.02% of total request latency, indicating minimal performance impact.

## Context
Serverless architectures rely on dynamic placement across multiple regions, where traditional latency‑only policies can inadvertently increase carbon emissions by favoring distant data centers. This work addresses the gap between user experience and environmental responsibility in cloud computing.

## Implications
Practitioners can adopt this routing framework to align cloud operations with sustainability goals such as SDG 13 and SDG 7, reducing operational carbon footprints without sacrificing service quality. The approach sets a benchmark for integrating AI‑driven optimization into large‑scale distributed systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22806v1)
