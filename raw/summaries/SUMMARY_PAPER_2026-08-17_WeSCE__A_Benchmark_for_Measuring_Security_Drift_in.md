---
title: WeSCE: A Benchmark for Measuring Security Drift in LLM-Driven Code Editing
url: http://arxiv.org/abs/2608.15092v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_07-24-13Z_WeSCE_ABenchmarkforMeasuringSecurityDriftinLLM_Dri.md
generated_at: 2026-08-17 21:39
model: nvidia/nemotron-3-nano-4b
---

## Summary
WeSCE introduces a benchmark to measure security drift in large language model‑driven code editing under weak‑security constraints, where tasks focus solely on functional outcomes without explicit security specifications. The study evaluates 400 real‑world executable programs that undergo feature addition, removal, bug fixing, and refactoring. Continuous risk representation and multi‑scale drift measures reveal how overall risk, worst‑case severity, and vulnerability distribution evolve during code transformations.

## Key Takeaways
- WeSCE quantifies security drift by aggregating heterogeneous vulnerability signals into a unified continuous risk representation, allowing precise tracking of changes across code edits.
- The benchmark defines three distinct drift measures: overall risk change, maximum severity impact, and the shift in vulnerability distribution, providing both average‑case and worst‑case perspectives.
- Results show that even minor functional modifications can cause significant security degradation, highlighting the need for continuous monitoring in LLM‑assisted development.

## Context
The rapid adoption of large language models for code generation raises concerns about hidden security risks that may not be captured by traditional static analysis. WeSCE addresses this gap by providing a systematic way to evaluate how such models affect program safety under realistic, low‑security workflows.

## Implications
For developers and AI tool providers, WeSCE underscores the importance of embedding security checks into LLM‑driven editing pipelines. Industry adoption will likely drive more robust safeguards, reducing the risk of vulnerabilities introduced by automated code changes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15092v1)
