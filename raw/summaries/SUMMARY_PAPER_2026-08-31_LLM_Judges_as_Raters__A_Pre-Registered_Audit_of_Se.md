---
title: LLM Judges as Raters: A Pre-Registered Audit of Severity, Halo, Reliability, and Version Instability in LLM Essay Scoring on Public Corpora
url: http://arxiv.org/abs/2608.29517v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_02-45-46Z_LLMJudgesasRaters_APre_RegisteredAuditofSeverity_H.md
generated_at: 2026-08-31 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models behave when used as essay graders, treating them as raters and applying a pre‑registered battery of psychometric tests to detect severity, halo effects, reliability, and version instability. It analyses 2 377 essays across two language corpora with twelve judges and five model versions, finding that LLM performance is far from human‑level accuracy while showing systematic shifts.

## Key Takeaways
- Severity varies widely on ENEM’s 0‑1000 scale (219 points) and ASAP panels span only 15‑33 % of the score range, indicating large inter‑judge spread. - Judge‑human correlations are low (.47‑.56), showing limited alignment with human grading standards. - Version contrasts shift severity by up to 133 points, exceeding a permutation null and revealing version instability.

## Context
This study addresses a growing concern that AI‑driven assessment tools may inherit or amplify biases from their training data and design choices. By quantifying rater effects on public corpora, the work provides empirical evidence for the limitations of relying solely on agreement statistics in educational analytics.

## Implications
For educators and developers, the findings warn against deploying LLMs as final grading instruments without rigorous validation. The results suggest that continuous monitoring of model behavior across versions is essential to maintain fairness and reliability in automated assessment systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29517v1)
