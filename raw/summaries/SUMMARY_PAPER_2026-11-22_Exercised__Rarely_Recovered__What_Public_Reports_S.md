---
title: Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes
url: http://arxiv.org/abs/2611.27090v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-20_04-05-35Z_Exercised_RarelyRecovered_WhatPublicReportsSayAbou.md
generated_at: 2026-11-22 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper systematically evaluates whether recovery mechanisms in AI coding agents and runtimes actually work in practice, grading 50 systems (12 persistent agent runtimes, 26 coding-agent harnesses, and 12 research runtimes) across eight recovery mechanisms using a pre-frozen protocol with blind coding passes and re-verification. The central finding is a stark gap between the near-universal presence of recovery features and their actual effectiveness: while 36 of 38 practical systems report at least one real-use recovery attempt, only 19 out of 128 documented reports describe a run fully recovering, with the majority being partial or outright failures.

## Key Takeaways
- Recovery mechanisms are almost universally present in practical agent systems—11 of 12 persistent runtimes and 25 of 26 coding-agent harnesses have at least one real-use recovery report—yet full recovery is rare: only 19 of 128 reports describe complete recovery, 54 are partial, and 45 represent outright failures, indicating that the existence of a mechanism does not guarantee its effectiveness under real conditions.
- Specific mechanisms perform poorly in practice: checkpoint/resume recovered successfully in only 1 out of 27 reported cases, and transactional rollback succeeded in only 1 out of 15 cases, suggesting that these commonly relied-upon strategies are unreliable when applied to actual agent workloads involving file deletions, long-running processes, and external side effects.
- Research runtimes exhibit an inverted profile compared to practical harnesses: their formal guarantees such as saga-style compensation and transactional rollback are evaluated exclusively on benchmarks with zero reports of operation in real use, and critically, the compensation of external effects—the central guarantee these systems promise—is offered by none of the 26 coding-agent harnesses, revealing a fundamental disconnect between research promises and deployed capabilities.

## Context
As AI coding agents like autonomous software engineering assistants become embedded in production workflows, failures such as incorrect file deletions, mid-run crashes, and unintended side effects are inevitable. The field has responded by building recovery infrastructure—checkpoints, undo systems, approval gates, logs, and transactional rollback—into both open-source harnesses and academic runtimes. This paper is significant because it is the first systematic, protocol-frozen audit of whether these mechanisms actually function when agents encounter real failures, moving beyond feature checklists to evidence-based grading across 128 documented recovery events.

## Implications
For practitioners deploying AI coding agents, the findings suggest that current recovery safety nets are largely cosmetic: users should not assume that checkpoint/resume or rollback will restore a failed run, and external side effects from agent actions remain essentially uncompensated across all practical harnesses. For the research community, the gap between benchmark-validated guarantees and zero operational evidence demands that future runtime designs be evaluated under realistic failure scenarios rather than synthetic benchmarks, and that harness developers prioritize compensating external effects as a first-class requirement rather than an afterthought.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27090v1)
