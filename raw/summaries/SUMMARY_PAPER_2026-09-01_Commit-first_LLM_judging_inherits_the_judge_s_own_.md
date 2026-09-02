---
title: Commit-first LLM judging inherits the judge's own errors
url: http://arxiv.org/abs/2609.00088v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_12-14-14Z_Commit_firstLLMjudginginheritsthejudge_sownerrors.md
generated_at: 2026-09-01 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates commit‑first LLM judging, a technique where the judge first solves a task and commits to an answer before evaluating candidates. The authors audit eight popular evaluation frameworks and find that none implement this approach; instead they use variants with known typographical errors. Experiments show that commit‑first judging does not eliminate gaming; it merely shifts the flaw from candidate responses to the judge’s own incorrect commitment, which can even be adopted by other judges.

## Key Takeaways
- Commit‑first judging removes the effect of gamed candidates but introduces a new vulnerability: the judge’s answer may itself be wrong.  
- The judged system can converge on the judge’s flawed answer, making evaluation less reliable.  
- The paper demonstrates that evaluating a judge’s competence is cheap and task‑specific rather than dependent on model scale.

## Context
LLM judges are widely used to assess code quality and other outputs, yet their performance often depends on hidden biases or errors in their own reasoning. This research highlights how standard evaluation pipelines may unintentionally propagate these flaws, affecting trust in automated assessment tools.

## Implications
For developers and researchers, the findings warn that relying solely on judge scores can lead to misleading conclusions about system quality. Organizations should verify judge competence independently before using them for critical evaluations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00088v1)
