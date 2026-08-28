---
title: Relational Over-Regularization: Graph-Based AI-Generated Text Detection via Sentence Transition Deviation
published: 2026-08-27T06:51:40Z
authors: Hyeonchu Park, Bugeun Kim
url: http://arxiv.org/abs/2608.26694v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Relational Over-Regularization: Graph-Based AI-Generated Text Detection via Sentence Transition Deviation

## Abstract
Detecting AI-generated text (AIGT) remains challenging because existing approaches rely on token-level statistical signals or independent stylometric features, causing them to overfit to specific generators and fail under distribution shift. We identify a structural signal at the sentence-pair level: LLMs produce inter-sentence transition variance that deviates from human writing through inflated variance driven by recurring similarity bursts at paragraph boundaries and templated transitions. We formalize this as Relational Over-Regularization (ROR) and validate it across four benchmarks (p < 0.001). The central contribution is this relational problem formulation, not a novel GNN architecture; CSFG is one concrete instantiation for operationalizing ROR. To exploit this signal, we propose the Cross-Source Stylometric Fingerprint Graph (CSFG), a graph-based framework that encodes positional, sequential, semantic, and transition deviation signals as learnable GNN edge features. The per-edge signed deviation δ_ij operationalizes ROR without hand-crafted thresholds and acts as a false-positive calibrator. CSFG achieves 97.14% accuracy under binary detection, outperforming the strongest graph-based baseline by 11.14 pp, with a false-positive rate of 1.57% and robust generalization to unseen LLMs in the inflated-variance regime; detection degrades for generators whose transition variance falls at or below the human baseline.

## Metadata
- **Published**: 2026-08-27T06:51:40Z
- **Authors**: Hyeonchu Park, Bugeun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26694v1)