---
title: PerturbMap: Cross-Context Transfer of Single-Cell Perturbation Responses
published: 2026-07-30T11:58:52Z
authors: Panpan Cui, Yiqi Liu, Wenhao Sun
url: http://arxiv.org/abs/2607.28090v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PerturbMap: Cross-Context Transfer of Single-Cell Perturbation Responses

## Abstract
Single-cell perturbation atlases rarely measure every intervention in every cellular context: a query perturbation is often observed in one or more source contexts but missing in the recipient context where its effect is needed. Ignoring those measured responses discards query-specific experimental evidence, whereas copying or weakly calibrating them across contexts risks transferring the wrong signal. We propose PerturbMap, which predicts a missing recipient-context effect by combining a recipient-local low-rank base with accepted proposals that transport the same perturbation's measured source responses through source-to-recipient ridge experts fit on paired training perturbations, with proposal weights determined by route reliability estimated on validation anchors. On the Perturb-CITE-seq melanoma cohort, PerturbMap improves full-effect MSE by 4.1\% over a recipient-local low-rank base and achieves lower MSE than FedAvg, zero-response, raw-copy, calibrated-copy, and identity-shuffled affine controls. It remains within $2.82\times10^{-6}$ MSE of our centralized token-matched pooled reference, which uses a stronger training interface. A condition-mean specificity diagnostic shows the same direction: same-recipient top-10 counterpart retrieval by cosine increases from 74.5\% for the low-rank base to 80.5\% for PerturbMap.

## Metadata
- **Published**: 2026-07-30T11:58:52Z
- **Authors**: Panpan Cui, Yiqi Liu, Wenhao Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28090v1)