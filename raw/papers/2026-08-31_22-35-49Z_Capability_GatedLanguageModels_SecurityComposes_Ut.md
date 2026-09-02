---
title: Capability-Gated Language Models: Security Composes, Utility Does Not
published: 2026-08-31T22:35:49Z
authors: Patrikas Vanagas, Augustas Mačijauskas, Laurynas Lopata
url: http://arxiv.org/abs/2609.00445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Capability-Gated Language Models: Security Composes, Utility Does Not

## Abstract
Deployed language model safeguards (safety fine-tuning, filtering, unlearning) vary by principal only outside the model weights: filters are reconfigured, tiers are multiplied, and artefacts are reissued; inside one set of weights every request meets the same model configuration. This motivates us to define capability-gated deployment: per-principal access control inside one set of weights, whose configurations form a lattice - meets accumulate a principal's restrictions and joins pool a coalition's reach. We instantiate it by sparse rank gating over an existing nested-factorisation mechanism, guide profile search with one-pass attribution, and read every result once from a pre-registered held-out split. Security composes: provably at meets under a monotone-elicitation assumption we falsify pointwise. In two lineages the median held-out meet deepens suppression; the one effect surviving correction strengthens it. Utility does not: individually harmless profiles can compose to retention and fluency damage, and no compositional bound exists.

## Metadata
- **Published**: 2026-08-31T22:35:49Z
- **Authors**: Patrikas Vanagas, Augustas Mačijauskas, Laurynas Lopata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00445v1)