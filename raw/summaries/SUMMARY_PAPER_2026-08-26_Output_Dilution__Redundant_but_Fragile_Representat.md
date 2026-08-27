---
title: Output Dilution: Redundant but Fragile Representations in MoE Models
url: http://arxiv.org/abs/2608.25231v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_23-41-07Z_OutputDilution_RedundantbutFragileRepresentationsi.md
generated_at: 2026-08-26 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper examines how MoE architectures encode moral content and identifies a vulnerability that dense models lack. It demonstrates that linear probes can recover moral valence from almost every expert layer with high accuracy, but this representation collapses under activation noise that a comparable dense model tolerates easily. The authors attribute the fragility to output dilution caused by averaging across active experts before residual propagation.

## Key Takeaways
- Linear probes achieve mean peak-layer accuracy above 90% for moral valence in OLMoE-1B-7B, showing robust encoding despite MoE sparsity.
- Output dilution reduces feedforward signal magnitude by roughly two orders of magnitude compared to dense MLPs, making the aggregate signal easily overwhelmed by noise.
- Checkpoint trajectories reveal that expert specialization occurs within a few thousand steps and accuracy saturates early, indicating an architectural limitation rather than learned behavior.

## Context
MoE models aim to combine efficiency with performance, but this study reveals that their sparse aggregation can degrade signal integrity. The findings highlight a gap between theoretical robustness claims and empirical stability under real-world perturbations. This work contributes to understanding the trade-offs inherent in routing-based architectures.

## Implications
For practitioners, the fragility of MoE moral representations suggests caution when deploying these models in safety-critical applications where noise is inevitable. It also prompts research into alternative aggregation strategies that preserve signal fidelity without sacrificing sparsity benefits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25231v1)
