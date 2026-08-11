---
title: Fair on the Surface? Benchmarking Hidden-Output Fairness Gaps in LLM Recommenders
url: http://arxiv.org/abs/2608.08284v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_18-32-34Z_FairontheSurface_BenchmarkingHidden_OutputFairness.md
generated_at: 2026-08-10 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FairGap, a benchmark that jointly evaluates fairness at two levels: observable output shift (OBS) and hidden representation shift (IBS). It shows that the alignment between these shifts is weak, with Representation-Output Alignment rarely exceeding 0.22, indicating that internal changes often do not translate to visible differences in recommendations.

## Key Takeaways
- ROA values are typically low, meaning most users experience stable outputs despite substantial hidden shifts, which output‑only audits cannot detect.
- Activation steering can reduce IBS by up to eightfold but simultaneously worsens OBS, revealing a tension between internal and output‑level fairness.
- The benchmark uncovers user‑level mismatches where internal representations change while observable recommendations remain unchanged.

## Context
Current fairness assessments for LLM recommenders focus on surface outputs, assuming that stable recommendations reflect stable processing. This assumption overlooks the possibility of hidden representation drift, which can affect model behavior without altering user perception. FairGap addresses this gap by probing both levels simultaneously.

## Implications
For practitioners, FairGap highlights the need to monitor internal representations alongside visible outputs when auditing fairness. Industry adoption of such benchmarks could lead to more robust and equitable recommendation systems that account for hidden biases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08284v1)
