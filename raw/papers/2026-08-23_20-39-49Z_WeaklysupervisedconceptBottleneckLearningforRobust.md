---
title: Weakly supervised concept Bottleneck Learning for Robust Two stage Object centric visual reasoning
published: 2026-08-23T20:39:49Z
authors: Sparsh Tiwari, Gesina Schwalbe, Bettina Finzel
url: http://arxiv.org/abs/2608.22584v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Weakly supervised concept Bottleneck Learning for Robust Two stage Object centric visual reasoning

## Abstract
Two-stage neuro-symbolic architectures provide an elegant paradigm for visual problem solving by cleanly separating connectionist perception of predefined symbols from possibly later defined relational reasoning thereon. However, anchoring high-level predicates into visual frames typically necessitates annotations that are expensive to acquire. In this work, we introduce the Dynamic Orthogonal Concept Bottleneck (D-OCB), an object-centric slot- VAE framework designed to extract human-aligned symbolic predicates under extremely weak supervision. D-OCB eliminates the arduous manual tuning of loss-balancing coef- ficients by dynamically learning optimal hyperparameter allocations during training. To infuse prior knowledge on independence of concept categories, in addition to standard re- construction self-supervision we penalize correlation across concept subspaces. Crucially, to combat the instability of very low supervision regimes, D-OCB incorporates a dynamic di- mensionality allocation mechanism; this adaptive formulation allows well-represented con- cepts to yield latent dimensions to underperforming concepts that are lagging behind, effectively preventing representation collapse and significantly improving overall concept accuracy. Through an extensive empirical evaluation, we demonstrate that our framework achieves high concept alignment and downstream visual reasoning accuracy using minimal label budgets, matching or outperforming end-to-end paradigms.

## Metadata
- **Published**: 2026-08-23T20:39:49Z
- **Authors**: Sparsh Tiwari, Gesina Schwalbe, Bettina Finzel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22584v1)