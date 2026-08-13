---
title: Analysis of Federated Aggregation under Model Poisoning and Backdoor Attacks: A Reconstructed Cross-Dataset and Cross-Architecture Benchmark
published: 2026-08-11T20:42:56Z
authors: Soumya Mazumdar, Vineet Kumar Rakesh, Tapas Samanta
url: http://arxiv.org/abs/2608.11423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Analysis of Federated Aggregation under Model Poisoning and Backdoor Attacks: A Reconstructed Cross-Dataset and Cross-Architecture Benchmark

## Abstract
Robust comparisons of federated aggregation methods require joint consideration of predictive performance, threat definitions, metric semantics, and execution provenance. A 500-cell seed-1 evaluation matrix was reconstructed across five aggregation methods, five datasets, five architectures, and four recorded conditions: clean, sign-flipping, Gaussian, and BadNets. Successful execution logs were identified for 454 original runs and 36 repaired or rerun executions, whereas 10 clean SVHN cells were supported by summary-only provenance. Trimmed Mean achieved the highest clean macro-mean accuracy (76.02%) and the lowest mean within-task rank (1.70). Krum attained the highest recorded accuracy under both sign-flipping and Gaussian configurations. These relative rankings remained unchanged when analysis was restricted to 21 task pairs for which original successful logs were available for every method-condition combination. Audit of the supplied BadNets metric implementation established that every test input is triggered prior to target-label counting; consequently, the retained metric represents Triggered Target-Label Rate (TTLR) rather than a conventional target-excluding attack success rate. An audit of the supplied FedPARETO scaffold further identified a pathway in which predictive summaries may characterize an uncorrupted local model while the aggregation weight is applied to a separately corrupted update, introducing a potential discrepancy between reported predictive outcomes and the updates used for aggregation. The canonical matrix contains a single identified seed for each cell, and exact attack and configuration lineage is incomplete. Accordingly, the findings should be interpreted as descriptive comparisons within the recorded configurations and not as statistical estimates or universal claims regarding robustness.

## Metadata
- **Published**: 2026-08-11T20:42:56Z
- **Authors**: Soumya Mazumdar, Vineet Kumar Rakesh, Tapas Samanta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11423v1)