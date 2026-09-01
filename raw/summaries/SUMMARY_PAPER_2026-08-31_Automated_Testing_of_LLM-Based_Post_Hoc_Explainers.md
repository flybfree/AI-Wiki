---
title: Automated Testing of LLM-Based Post Hoc Explainers Using Model Checking as an Oracle
url: http://arxiv.org/abs/2608.30581v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_10-54-37Z_AutomatedTestingofLLM_BasedPostHocExplainersUsingM.md
generated_at: 2026-08-31 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a method to automatically test large language model explanations of sequential decision-making policies using probabilistic model checking as an oracle. It generates structured natural‑language queries from a taxonomy that maps them to environment facts and scores their diagnostic difficulty. Across seven MDPs the approach shows three LLMs differ markedly in reliability, with only one passing most tests.

## Key Takeaways
- Probabilistic model checking provides an exact reference for comparing LLM explanations to ground truth actions.
- A taxonomy of query categories structures input space around factual policy behavior enabling systematic test case generation.
- Prioritization by diagnostic difficulty surfaces harder cases, revealing that a 1B model performs below random chance while smaller models achieve moderate accuracy.

## Context
LLM explainers are increasingly deployed as post‑hoc justifications for autonomous agents but lack reliable verification mechanisms. Existing methods treat explanations as black boxes without systematic validation against underlying policies. This work bridges the gap by introducing an automated testing framework that couples model checking with natural‑language query generation.

## Implications
The results highlight trustworthiness gaps in LLM‑generated policy rationales, urging developers to adopt rigorous testing before deployment. For industry practitioners, the approach offers a scalable way to evaluate explanation quality and prioritize risky queries, improving safety in autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30581v1)
