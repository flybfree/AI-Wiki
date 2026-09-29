---
title: WebPageBench: Event-Level Verification and Controlled UI-Variant Generation for Web Agents
url: http://arxiv.org/abs/2609.35026v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_12-24-23Z_WebPageBench_Event_LevelVerificationandControlledU.md
generated_at: 2026-09-28 23:15
model: qwen3.6-35b-a3b
---

## Summary
WebPageBench introduces an open evaluation framework for web agents that verifies task completion through interface event logs rather than relying on judge models or rendered page scraping. The system enables controlled UI variation testing by re-rendering tasks via different control implementations while keeping prompts and success conditions constant, allowing precise measurement of agent sensitivity to interface changes. Evaluation results highlight a substantial reliability gap, where one configuration claimed all tasks finished but only satisfied actual log conditions for 59% of cases, demonstrating a discrepancy of up to 41 points between declared and verified success.

## Key Takeaways
- WebPageBench employs a rigorous event-level verification mechanism where instrumented mock sites emit typed events with parameters as actions occur; task success is determined strictly by matching declared required events against the log, completely removing dependency on external judge models or browser rendering analysis

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35026v1)
