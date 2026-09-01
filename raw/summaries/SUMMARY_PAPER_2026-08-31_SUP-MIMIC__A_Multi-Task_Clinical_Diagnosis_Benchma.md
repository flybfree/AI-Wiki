---
title: SUP-MIMIC: A Multi-Task Clinical Diagnosis Benchmark for Evaluating LLMs' Robustness to Contradictory Evidence
url: http://arxiv.org/abs/2608.29582v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_05-59-47Z_SUP_MIMIC_AMulti_TaskClinicalDiagnosisBenchmarkfor.md
generated_at: 2026-08-31 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SUP-MIMIC, a multi‑task benchmark that evaluates large language models’ ability to reason about contradictory clinical evidence. Using the MIMIC‑IV‑v3.1 dataset it creates three tasks: Basic Assessment, Diagnostic Divergence Task, and Diagnostic Convergence Task. The study finds that state‑of‑the‑art LLMs degrade sharply on the divergence and convergence tasks, revealing a reliance on shortcuts rather than genuine causal reasoning.

## Key Takeaways
- The DDT task shows substantial performance loss when models must disambiguate multiple possible diagnoses from similar clinical presentations, indicating limited one‑to‑many reasoning.  
- The DCT task reveals that models often fail to recognize that diverse symptoms can converge on a single disease, highlighting poor many‑to‑one diagnostic pattern detection.  
- A consistent bias toward “healthy” predictions emerges across tasks, suggesting non‑trivial risk of missed diagnoses in real clinical settings.

## Context
Current LLM assessments focus mainly on factual retrieval and ignore the nuanced reasoning required for medical diagnosis where evidence is often contradictory or ambiguous. This work addresses that gap by constructing a benchmark that directly tests diagnostic ambiguity and convergence, offering a more realistic measure of model robustness.

## Implications
For clinicians relying on AI assistance, this research underscores the danger of models that default to safe but incorrect predictions, potentially leading to misdiagnosis. For developers, SUP‑MIMIC provides a concrete framework to improve causal reasoning and reduce bias in diagnostic outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29582v1)
