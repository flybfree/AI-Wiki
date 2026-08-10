---
title: StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection
url: http://arxiv.org/abs/2608.06477v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_18-14-30Z_StepJack_BenchmarkingComputer_UseAgentSafetyAgains.md
generated_at: 2026-08-09 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces StepJack, a benchmark for evaluating safety of computer-use agents against multi-step indirect prompt injection attacks. It shows that decomposing adversarial goals into innocuous sub-steps can significantly increase attack success rates on several state-of-the-art CUAs, reaching up to 31.2 points higher at three-step depth compared with single-step.

## Key Takeaways
- Multi-step indirect prompt injection degrades CUA safety by breaking a malicious goal into seemingly harmless navigation steps that collectively achieve the original objective.
- The benchmark demonstrates that attack success rates can rise from around 30% to over 70% across three-step attacks, highlighting vulnerability at deeper decomposition depths.
- Only five of six tested CUAs are affected, indicating that some models resist such indirect injection while others remain highly susceptible.

## Context
Computer-use agents increasingly rely on external web resources for tasks, making them vulnerable to attacks that exploit the environment rather than direct prompts. This research underscores a shift from prompt‑level defenses to environment‑aware security in AI systems that interact with dynamic content.

## Implications
For developers and researchers, StepJack calls for robust evaluation protocols that consider multi-step attack vectors when deploying CUAs in real‑world settings. Industry practitioners must prioritize safeguards that prevent adversarial manipulation across linked pages to maintain trustworthy automated agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06477v1)
