---
title: Excess Separability: Nuisance-Controlled Residual-Stream Probing for Benchmark Contamination Detection
published: 2026-08-12T23:27:20Z
authors: Florian Braun
url: http://arxiv.org/abs/2608.12652v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Excess Separability: Nuisance-Controlled Residual-Stream Probing for Benchmark Contamination Detection

## Abstract
Benchmark contamination is diagnosed today with n-gram overlap, with likelihood-based membership inference, or with canary strings, and each needs something usually unavailable: the training corpus, a well-chosen test statistic, or foresight at dataset release. A recent alternative reads contamination off a linear probe on internal activations. We show that the natural way to do this does not work, and specify one that survives measurement.   The protocol reports a zero-sum contrast on the depth profile of probe accuracy, recentred on a level-matched placebo baseline, tested against a label-permutation null, with the reference set twice the size of the suspect set. Each choice replaces a simpler alternative we measured and rejected. Reporting the level of excess separability rather than its shape makes the false positive rate track the size of the analyst's own control set, from 0.03 to 0.99 under a true null. Contrasting against a flat depth profile fails in both directions, rejecting a true null 0.72 of the time when surface decodability rises with depth and losing all power when it falls. An item bootstrap holds the fitted probe fixed and rejects up to 0.09 of the time where a permutation null that refits it holds 0.02. A half-size baseline triples the error rate.   On real transformers, baseline depth profiles are measurably not flat, spanning up to 29.1 accuracy points on a temporal split, and their non-flatness tracks the surface difference between the item sets (correlation 0.87 over 6 audits), so the correction is largest exactly where it is needed. All 4 well-matched Pile arms return null, and the protocol refuses a verdict on the temporal split rather than reporting one. What this does not establish is whether transformers carry a familiarity direction at all: the only positive sits on the split where exchangeability fails. Implementation, tests and audits are released.

## Metadata
- **Published**: 2026-08-12T23:27:20Z
- **Authors**: Florian Braun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12652v1)