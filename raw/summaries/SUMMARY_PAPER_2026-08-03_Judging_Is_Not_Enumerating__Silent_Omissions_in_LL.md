---
title: Judging Is Not Enumerating: Silent Omissions in LLM-Authored Acceptable Sets
url: http://arxiv.org/abs/2608.01000v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_05-00-44Z_JudgingIsNotEnumerating_SilentOmissionsinLLM_Autho.md
generated_at: 2026-08-03 20:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why large language models (LLMs) that generate acceptable sets for algorithmic tasks perform poorly in judging those same sets compared with their own creation. The authors show a consistent gap between model‑authored and model‑judged F1 scores across four reference constructions, especially on executable code where judges accept far fewer correct solutions than the author produces.

## Key Takeaways
- Models judge candidate solutions at F1 0.74–0.90 while they only author suites containing 19–42% of oracle‑correct programs, indicating a severe omission bias in their acceptance criteria.  
- The failure is not due to missing knowledge but an inability to materialise the logical region that a specification defines; over‑inclusions are flagged six to seven times more often than omitted members.  
- In a production deployment of 43 227 items, omission errors dominate at a ratio of ten to one, costing models 1.9 points of accuracy versus an exact oracle and 18.5 WordNet‑relative points.

## Context
The rise of LLMs as automated test authors creates a dependency on their correctness for downstream systems that rely on these reference sets. Existing research often assumes that the same model can both generate and evaluate solutions, yet this study reveals a systematic disconnect between generation quality and evaluation fidelity across diverse problem types.

## Implications
For practitioners deploying LLM‑generated test suites, the risk of missing valid solutions is high, potentially leading to false negatives in automated grading pipelines. The findings suggest that current approaches must incorporate repair mechanisms or alternative validation methods rather than relying solely on model‑authored reference sets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01000v1)
