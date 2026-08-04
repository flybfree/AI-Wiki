---
title: Pretrain on Small Synthetic Data, Scale Large for Free: Symmetry-Aware Foundation Model for Logic Rule Induction
published: 2026-08-01T01:49:25Z
authors: Yin Jun Phua
url: http://arxiv.org/abs/2608.00383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pretrain on Small Synthetic Data, Scale Large for Free: Symmetry-Aware Foundation Model for Logic Rule Induction

## Abstract
Logical rule induction seeks interpretable rules that transfer across propositional schemas. This requires respecting symmetries: atom naming, example order, polarity flips, and label swap. Enforcing exact symmetry by construction lets one trained inducer scale beyond its training schemas. Our central contribution is a canonical export that decodes a discrete rule from literal scores. It needs no retraining and is exactly equivariant whenever those scores respect the symmetries. We instantiate it on the Neural Rule Inducer, a disjunctive-normal-form (DNF) foundation model that natively respects only example order. We restore the remaining symmetries through architecture, inference, and training. On synthetic stress tests, accuracy on the support labels stays stable at much larger schemas, and rule fidelity on fresh inputs remains above the unmodified model. On real data, accuracy improves most on larger schemas. The exported rule is exact on synthetic full-group tests and on schema-valid real-data tests. This is a mathematical property of the export rather than of a specific model, and we validate it empirically only on the NRI. Enforcing symmetry by construction turns this small-data pretrained model into a reusable, interpretable inducer that transfers to larger schemas.

## Metadata
- **Published**: 2026-08-01T01:49:25Z
- **Authors**: Yin Jun Phua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00383v1)