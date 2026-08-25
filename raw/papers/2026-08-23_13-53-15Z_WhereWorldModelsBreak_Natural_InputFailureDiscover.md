---
title: Where World Models Break: Natural-Input Failure Discovery
published: 2026-08-23T13:53:15Z
authors: Zhanpeng Shi, Zi Liang, Rong Feng, Shiqin Tang, Xuyang Chen, Hongzong Li
url: http://arxiv.org/abs/2608.22421v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where World Models Break: Natural-Input Failure Discovery

## Abstract
World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from general queries, they fail to stress-test the model against catastrophic collapses under rare or unobserved condition-action combinations. To bridge this gap, we formalize the natural-input failure discovery problem: under a finite query budget, finding environment-valid conditions and action prefixes that induce severe prediction risk, verifying whether these failures reproduce on fresh seeds, and testing their persistence under nearby valid edits. Discovering such critical failures is computationally challenging, as valid condition-action combinations explode exponentially, rendering exhaustive search or standard sampling infeasible given the high cost of noisy rollouts. To tackle this, we propose BasinLens, which exploits the underlying structure of valid inputs, where each coordinate possesses environment-defined semantic types and admissible domains, by pairing uncertainty-guided global search with typed local replacements. Across diverse benchmarks and world-model families, BasinLens exposes reproducible and locally persistent failure modes that conventional evaluations fail to reveal, showing that average-case benchmarks can mask important vulnerabilities in world-model-driven control.

## Metadata
- **Published**: 2026-08-23T13:53:15Z
- **Authors**: Zhanpeng Shi, Zi Liang, Rong Feng, Shiqin Tang, Xuyang Chen, Hongzong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22421v1)