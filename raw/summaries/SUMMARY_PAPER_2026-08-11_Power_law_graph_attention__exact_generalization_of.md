---
title: Power law graph attention: exact generalization of scaled dot-product attention, empirical collapse at inference
url: http://arxiv.org/abs/2608.10288v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_22-45-22Z_Powerlawgraphattention_exactgeneralizationofscaled.md
generated_at: 2026-08-11 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Power Law Graph Attention (PLGA) as an exact generalization of scaled dot‑product attention that uses a learned bilinear operator derived from elementwise power laws. The authors prove several theorems about the structure and behavior of PLGA, showing that inference collapses to generalized SDPA with a constant operator under certain conditions.

## Key Takeaways
- Exact input invariance of deductive outputs collapses inference to generalized SDPA with a constant operator, as shown by an inference‑collapse theorem.  
- Measured relative fluctuations are on the order of 10⁻⁶ and below, yet perturbation bounds do not certify cached inference because the assembled proxy misses the decoding margin.  
- A conditional three‑stage mechanism involving rotary twirl, concentration, and row‑map contraction is measured on a released checkpoint to explain observed behavior.

## Context
PLGA builds on the PLDR‑LLM framework that replaces fixed attention with learned bilinear forms, aligning with recent efforts to make attention more flexible. The work contributes to understanding how power‑law structures can preserve relative position information while enabling exact generalization.

## Implications
For practitioners, PLGA offers a provably equivalent alternative to SDPA that may reduce computational cost without sacrificing performance. For the field, it provides a rigorous framework for analyzing attention mechanisms and highlights the importance of formal verification in AI research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10288v1)
