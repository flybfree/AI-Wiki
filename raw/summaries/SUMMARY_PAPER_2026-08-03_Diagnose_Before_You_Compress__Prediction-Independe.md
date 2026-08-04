---
title: Diagnose Before You Compress: Prediction-Independent Bottleneck Witness Refinement for LLM Serving Traces
url: http://arxiv.org/abs/2608.00423v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_03-43-55Z_DiagnoseBeforeYouCompress_Prediction_IndependentBo.md
generated_at: 2026-08-03 20:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Bottleneck-Preserving Witnessing (BPW), a framework that creates compact, diagnostically reliable LLM serving replay suites by preserving evidence for every bottleneck component rather than relying on workload representativeness. Experiments show BPW achieves 2.3% and 16.3% relative improvements in Mean prefix Macro-F1 and WBRC-AUC over 16 policies using a verified gate with minimal workloads.

## Key Takeaways
- Workload Candidate Nomination identifies potential scheduler, prefill, decode, or KV-cache bottlenecks using response-blind features and closed-source measurements.
- Coverage-Priority Sequence Construction organizes multi-component proposals as reusable hyperedges, prioritizing weak and uncovered dimensions to build a compact set.
- Bottleneck Truth Verification derives prediction-independent labels from direct system measurements, ensuring the earliest prefix satisfying two-witness requirements for each component.

## Context
LLM serving generates millions of requests, making full trace replay costly; existing methods often miss rare bottlenecks. This work addresses that gap by focusing on preserving evidence per bottleneck rather than workload distribution.

## Implications
The compact, verified suite enables more efficient debugging and optimization without sacrificing diagnostic reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00423v1)
