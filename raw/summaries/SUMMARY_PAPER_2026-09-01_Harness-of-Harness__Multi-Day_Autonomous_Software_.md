---
title: Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement
url: http://arxiv.org/abs/2609.01481v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_16-17-18Z_Harness_of_Harness_Multi_DayAutonomousSoftwareDeve.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Harness-of-Harness (HoH), a framework that lets LLM‑based coding agents improve their autonomous software development over multiple iterations. By organizing existing harnesses into iterative planning‑coding‑testing loops, HoH balances repair work with new capability growth and delivers progressively better results. On benchmark suites it outperforms its standalone counterparts by an average of 52 percent after three iterations.

## Key Takeaways
- The framework continuously improves code quality by separating implementation‑time testing from independent evaluation and focusing on verifiable outputs rather than rigid workflows.
- It breaks development into small, incremental increments that expose deliverables, tools, and skills gradually, encouraging reuse of existing work instead of recreating it.
- Versioned project histories are maintained to track changes across multiple iterations, enabling a multi‑day autonomous creation of complex software such as a first‑person shooter.

## Context
Autonomous software development using large language models is rapidly advancing, but most systems treat each run as independent, limiting progress. This work addresses that limitation by introducing a structured iterative loop that enables learning and adaptation over time, aligning with trends toward self‑optimizing AI agents in engineering tasks.

## Implications
For researchers, HoH provides a practical template for evaluating and enhancing autonomous coding agents beyond single‑run benchmarks. For industry practitioners, the framework suggests that long‑term projects can benefit from continuous improvement loops, reducing manual oversight and accelerating delivery of complex applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01481v1)
