---
title: Analysis of Federated Aggregation under Model Poisoning and Backdoor Attacks: A Reconstructed Cross-Dataset and Cross-Architecture Benchmark
url: http://arxiv.org/abs/2608.11423v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_20-42-56Z_AnalysisofFederatedAggregationunderModelPoisoninga.md
generated_at: 2026-08-12 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper reconstructs a comprehensive evaluation matrix to compare federated aggregation methods across diverse datasets, architectures, and attack scenarios, highlighting that Trimmed Mean excels in clean conditions while Krum shows resilience under sign‑flipping and Gaussian attacks. It also reveals that the BadNets metric is actually Triggered Target-Label Rate rather than a conventional success rate, and notes potential discrepancies between local model summaries and corrupted aggregation weights.

## Key Takeaways
- The benchmark demonstrates Trimmed Mean achieving 76.02% macro‑mean accuracy in clean settings, giving it the best overall performance when no attacks are present.
- Krum maintains high accuracy even under sign‑flipping and Gaussian perturbations, indicating strong robustness to common data‑corruption attacks.
- The BadNets metric is audited as Triggered Target‑Label Rate, meaning test inputs trigger label counting before exclusion, which changes the interpretation of attack success compared with traditional definitions.

## Context
Federated learning systems must balance predictive performance with security against adversarial and poisoning threats. This work provides a unified framework that evaluates multiple aggregation strategies under realistic conditions, offering a reference point for future research on robustness. The cross‑dataset and cross‑architecture design helps isolate the impact of each factor, which is essential as datasets and hardware evolve rapidly.

## Implications
For practitioners, the findings suggest prioritizing Trimmed Mean when data integrity is guaranteed but expecting Krum for environments with active attacks. Understanding that BadNets measures Triggered Target‑Label Rate guides correct metric selection to avoid misreporting attack success. The benchmark’s reproducibility issues remind researchers to document exact configurations, reinforcing the need for transparent audit trails in federated learning research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11423v1)
