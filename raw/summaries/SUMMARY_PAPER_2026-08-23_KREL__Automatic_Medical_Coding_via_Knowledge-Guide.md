---
title: KREL: Automatic Medical Coding via Knowledge-Guided Reasoning over Clinical Evidence with LLMs
url: http://arxiv.org/abs/2608.20887v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_09-05-15Z_KREL_AutomaticMedicalCodingviaKnowledge_GuidedReas.md
generated_at: 2026-08-23 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KREL, a framework that uses large language models to understand clinical notes and apply ICD coding guidelines through structured reasoning. Experiments on benchmark datasets show KREL outperforms existing PLM and LLM approaches by reducing hallucinations and improving code accuracy. The authors demonstrate that integrating external knowledge into LLMs yields better performance.

## Key Takeaways
- KREL couples domain-specific ICD coding rules with LLM reasoning, enabling tighter alignment between clinical evidence and standardized codes.
- By treating AMC as a generation task guided by structured knowledge rather than pure classification, the model reduces hallucinations common in extreme multi-label problems.
- The framework achieves consistent gains over strong baselines across multiple datasets, highlighting the value of knowledge-guided prompting.

## Context
Current AI research on medical coding often relies on pre-trained language models that lack explicit handling of complex coding rules. This paper addresses a gap by showing how external structured knowledge can be embedded to guide LLMs, offering a more reliable alternative to classification-based methods.

## Implications
For healthcare providers and coders, KREL suggests that AI tools incorporating clinical guidelines may reduce errors in reimbursement claims and research data quality. Practitioners can trust the system's outputs as they align with established coding standards, potentially streamlining workflows and improving compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20887v1)
