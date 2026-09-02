---
title: Predicting Program Exit Code with LLMs and Programming Language Semantics
url: http://arxiv.org/abs/2609.00579v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_02-18-20Z_PredictingProgramExitCodewithLLMsandProgrammingLan.md
generated_at: 2026-09-01 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Program Executability Prediction (PrEx), a task that asks large language models to determine whether a program is semantically valid or invalid and, if invalid, which formal rule it breaks. The authors evaluate open‑source coding LLMs on the PrEx benchmark using two semantic formalisms and three program splits. Their results reveal that LLMs rely heavily on pre‑training priors rather than applying the explicit rules given in the task, especially when semantics are altered or programs become more complex.

## Key Takeaways
- LLMs perform poorly on modified semantics because they do not systematically follow the provided formal rules.
- The degradation of performance increases with program complexity, indicating a breakdown in handling intricate control flows and data structures.
- PrEx demonstrates that current LLMs lack reliable grounding in programming‑language semantics beyond what was learned during pre‑training.

## Context
The study fits within the growing effort to assess whether large language models can be trusted for tasks requiring precise logical reasoning. By focusing on executable correctness, it highlights a gap between model capability and the need for exact compliance with program specifications, a concern that resonates across AI safety, software engineering, and automated testing.

## Implications
For developers relying on LLMs for code generation or debugging, this paper warns against assuming semantic fidelity without rigorous validation. It also suggests that future research should incorporate more systematic rule‑following mechanisms to align model behavior with formal program semantics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00579v1)
