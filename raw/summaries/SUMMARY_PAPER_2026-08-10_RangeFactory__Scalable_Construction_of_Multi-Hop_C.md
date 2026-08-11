---
title: RangeFactory: Scalable Construction of Multi-Hop Cyber Ranges
url: http://arxiv.org/abs/2608.09526v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_12-25-49Z_RangeFactory_ScalableConstructionofMulti_HopCyberR.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RangeFactory, an automated framework that builds multi-hop cyber ranges by treating range construction as dependency resolution from real vulnerability attacks. It creates a large validated dataset of 1,148 attack chains and shows many compromised entry points still fail to complete further hops, highlighting a sustained-compromise gap.

## Key Takeaways
- RangeFactory automatically composes multi-hop ranges using dependency extraction from actual attacks and template-guided orchestration.
- Validation via end-to-end execution reveals that 24.5‑47.0% of compromised entry points do not lead to successful completion of the remaining attack path, exposing a persistent gap in sustaining compromise.
- The system generates 5,541 outcome‑annotated trajectories for analysis and training.

## Context
Multi-hop cyber ranges are needed because real attacks progress across multiple hosts and network segments, yet existing tools only scale isolated tasks or manually curated scenarios. This paper addresses the need for scalable, automated orchestration that can handle growing vulnerability supplies without human specification.

## Implications
For AI researchers, RangeFactory provides a benchmark to evaluate agents on realistic attack depth and network scale. For industry practitioners, it offers execution data to improve detection and response strategies against sustained cyber threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09526v1)
