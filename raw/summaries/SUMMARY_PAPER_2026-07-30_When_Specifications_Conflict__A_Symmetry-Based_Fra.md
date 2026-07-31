---
title: When Specifications Conflict: A Symmetry-Based Framework for Measuring LLM Preferences
url: http://arxiv.org/abs/2607.28384v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_15-42-32Z_WhenSpecificationsConflict_ASymmetry_BasedFramewor.md
generated_at: 2026-07-30 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a symmetry‑based framework for measuring how large language models choose between conflicting specifications. Experiments on an executable mathematical benchmark reveal systematic preference patterns across four representation types. The results show formal representations outrank natural language and input‑output examples, supporting the framework’s reliability.

## Key Takeaways
- The framework constructs explicit conflict instances to directly observe model choices rather than inferring from noisy outputs.
- Systematic ordering Formal ≈ Naturalized Formal > Pure Natural Language > Input--Output Examples emerges across 550 conflict cases.
- Effect sizes depend on model capability and function family, indicating nuanced performance differences.

## Context
Current LLMs often face contradictory instructions or data sources, yet existing evaluation methods lack control over representation type. This work fills that gap by providing a reproducible setup for comparing how models weigh competing specifications across different input formats.

## Implications
Practitioners can use the framework to diagnose why certain model outputs are preferred and to design better specification engineering. The approach also offers a benchmark for fairness testing, helping developers align model behavior with intended specifications in safety‑critical domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28384v1)
