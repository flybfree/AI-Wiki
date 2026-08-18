---
title: Amortised Post-Hoc Explanation with Exact Preservation for Dynamic Graph Anomaly Detectors
published: 2026-08-16T06:10:40Z
authors: Iyad Assaad Nekka, Hamida Seba, Walid Khaled Hidouci, Karima Amrouche
url: http://arxiv.org/abs/2608.15559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Amortised Post-Hoc Explanation with Exact Preservation for Dynamic Graph Anomaly Detectors

## Abstract
Anomaly detection in dynamic graphs underpins financial fraud analysis, intrusion detection, and platform integrity, where automated decisions require human-interpretable justifications. StrGNN, the strongest performer in recent benchmarks, produces no explanation: when an edge is flagged, the analyst receives only a score. Explanation metrics are undefined for StrGNN because no attribution vector exists. This paper closes that gap. We present X-StrGNN, a post-hoc explanation layer that wraps a trained, frozen StrGNN and emits, for every flagged edge, dual attributions: a structural attribution identifying which contextual interactions in the enclosing subgraph drove the decision, and a temporal attribution identifying which historical snapshot carried the signal. Both attributions are multiplicative masks identically one in the unexplained pass, so the layer is an exact pass-through: detection is preserved to machine precision, verified rather than asserted (Delta AUC = 0.0000, Delta AP = 0.0000, Delta P@100 = 0.0000). Attribution costs 0.66 ms per edge, making explanation of an entire alarm list feasible. We conduct the first controlled design study of attribution strategies for this architecture, comparing gradient attribution, per-instance mask optimisation, and amortised parameterisation under one protocol, one budget, and three seeds. X-StrGNN attains the highest stability (0.913) at 268x lower cost than per-instance optimisation, and its temporal attribution (1.601 against a measured random floor of 0.973) is separably better than its ablated control, while per-instance optimisation - the most expensive strategy - falls below that floor. Code, protocol, and per-seed measurements are released.

## Metadata
- **Published**: 2026-08-16T06:10:40Z
- **Authors**: Iyad Assaad Nekka, Hamida Seba, Walid Khaled Hidouci, Karima Amrouche
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15559v1)