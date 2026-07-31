---
title: How Benchmarks Mis-Score Computer-Use Agents
url: http://arxiv.org/abs/2607.28367v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_15-29-42Z_HowBenchmarksMis_ScoreComputer_UseAgents.md
generated_at: 2026-07-30 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why computer-use agents (CUA) receive inaccurate benchmark scores, showing that many failures are due to flawed evaluation pipelines rather than genuine inability. It audits 150 trajectories from five benchmarks and finds that 15.3% of failed verdicts are wrong, including evaluator false negatives and broken tasks.

## Key Takeaways
- 15.3% of FAIL verdicts are incorrect, with 10.7% caused by evaluators missing valid solutions and 4.7% due to malformed task definitions.
- Genuine failures are mainly verification/feedback problems or planning issues rather than execution errors, indicating a three-tier diagnostic taxonomy is needed.
- A single success rate cannot capture the complexity of CUA evaluation because different failure modes dominate at various stages.

## Context
Computer-use agents aim to perform real‑world tasks by interacting with browsers and desktop applications, but current benchmarks rely on brittle scripted oracles that do not reflect actual agent behavior. This misalignment leads to inflated confidence in scores and hampers trustworthy research.

## Implications
Researchers must redesign evaluation pipelines to include robust verification and feedback loops rather than relying solely on scalar success metrics. Practitioners should adopt stage‑specific design rules to improve reliability and reduce false failures in CUA deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28367v1)
