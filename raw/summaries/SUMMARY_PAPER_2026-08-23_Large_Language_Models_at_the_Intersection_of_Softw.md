---
title: Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda
url: http://arxiv.org/abs/2608.21107v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_13-54-38Z_LargeLanguageModelsattheIntersectionofSoftwareEngi.md
generated_at: 2026-08-23 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents an evidence‑centered structured survey of Large Language Model research up to May 2026 that bridges software engineering and security assessments. It identifies gaps between functional task completion and security validation, proposes a dual assurance framework, and outlines recurring validity threats such as weak test oracles and duplicated data.

## Key Takeaways
- Execution feedback and repository access boost engineering task success but do not guarantee security because they lack explicit vulnerability checks.  
- Static‑analysis labels or vulnerability scores rarely provide evidence of deployable correctness, highlighting a misalignment between measured risk and functional safety.  
- Common validity threats include weak test oracles, duplicated temporally leaked data, changing agent harnesses, proxy‑only security checks, under‑reported budgets, and insufficient human intervention.

## Context
The rapid shift from code completion to repository‑scale AI agents creates a need for assessments that consider both functional reliability and security. Existing surveys often treat these domains separately, leading to fragmented evidence and inconsistent benchmarking practices.

## Implications
Practitioners must adopt joint assurance cases that combine task‑appropriate evidence with calibrated human oversight to trust model outputs in production environments. This work sets a roadmap for developing benchmarks that evaluate both correctness and security together.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21107v1)
