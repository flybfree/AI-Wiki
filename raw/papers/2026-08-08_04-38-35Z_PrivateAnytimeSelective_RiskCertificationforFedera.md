---
title: Private Anytime Selective-Risk Certification for Federated Retrieval-Augmented Generation: Guarantees and Empirical Limits
published: 2026-08-08T04:38:35Z
authors: Sanjeda Akter, Ibne Farabi Shihab, Anuj Sharma
url: http://arxiv.org/abs/2608.07913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Private Anytime Selective-Risk Certification for Federated Retrieval-Augmented Generation: Guarantees and Empirical Limits

## Abstract
Selective-risk certificates promise that accepted outputs meet a declared error target. We develop Fed-SRC, a score-agnostic certificate for federated, differentially private, adaptively monitored retrieval-augmented generation. Clients release only Gaussian-perturbed score and loss histograms. Record-indexed and noise-variance-indexed martingales jointly bound target-risk contrast and accepted mass over all registered thresholds and rounds, permitting predictable recruitment, dropout, threshold selection, and optional stopping. A range-one total-variation term transfers the calibration mixture to a declared deployment mixture. The contribution is this private, federated, anytime combination, rather than the contrast statistic or acceptance floor individually. Empirically, no simultaneous-bound violation occurs in any evaluated cell, privacy level, or policy. Operational power depends on the score and population: the primary target r*=0.10 never certifies, and on RAGTruth the secondary target r*=0.20 never certifies either, whereas on HaluEval question answering it certifies in all 200 non-private trials, with held-out risk below the target. Naively privatized non-private certificates violate their bounds in 146 to 198 of 200 trials. As an exploratory comparison, we also evaluate a private betting-capital heuristic for which we do not establish e-process validity. This heuristic stops certifying at epsilon <= 4, where Fed-SRC still certifies. Certification nevertheless consumes roughly 30 times more stream events than unique calibration items.

## Metadata
- **Published**: 2026-08-08T04:38:35Z
- **Authors**: Sanjeda Akter, Ibne Farabi Shihab, Anuj Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07913v1)