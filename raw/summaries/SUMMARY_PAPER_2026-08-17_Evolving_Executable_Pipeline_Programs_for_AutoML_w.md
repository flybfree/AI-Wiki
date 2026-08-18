---
title: Evolving Executable Pipeline Programs for AutoML with Language Models
url: http://arxiv.org/abs/2608.16416v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_11-15-25Z_EvolvingExecutablePipelineProgramsforAutoMLwithLan.md
generated_at: 2026-08-17 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LACE, an AutoML framework that searches over executable Python pipeline programs instead of predefined components. Evaluated on 68 OpenML classification tasks with a leakage‑controlled protocol, LACE using GPT‑5.4‑mini outperforms several state‑of‑the‑art search systems while delivering fully editable pipelines.

## Key Takeaways
- LACE generates complete scikit‑learn compatible Python classes as candidate pipelines rather than tuning only hyper‑parameters within fixed operators and learners.  
- The large language model acts solely as a variation operator, producing diverse program structures that are not constrained by the original AutoML search space.  
- All resulting pipelines can be inspected and edited directly in code, unlike frameworks that return opaque model objects.

## Context
AutoML traditionally limits itself to known preprocessing operators, learners, and hyper‑parameter ranges, missing novel pipeline designs. This work expands the search space to full executable programs, aligning with the trend toward generative AI‑driven tooling for machine learning pipelines.

## Implications
Practitioners can reuse and modify generated pipelines without relying on proprietary frameworks, fostering transparency and adaptability in automated model development. The approach may inspire future AutoML systems that combine code generation with robust search mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16416v1)
