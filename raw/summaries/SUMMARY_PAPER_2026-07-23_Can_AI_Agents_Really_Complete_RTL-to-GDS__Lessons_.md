---
title: Can AI Agents Really Complete RTL-to-GDS? Lessons from Benchmarking Tool-Interactive EDA Workflows
url: http://arxiv.org/abs/2607.17528v3
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_04-08-06Z_CanAIAgentsReallyCompleteRTL_to_GDS_LessonsfromBen.md
generated_at: 2026-07-23 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether AI agents can reliably perform an end‑to‑end RTL‑to‑GDS flow using commercial EDA tools under two timing targets. The study compares three agent architectures and four foundation models, measuring design quality, stage completion, and Token ROI as cost‑efficiency metrics.

## Key Takeaways
- Domain‑specific skills enhance individual subtask understanding but do not guarantee reliable execution of a long‑horizon EDA flow.
- Agents achieving similar progress can differ by up to 141 times in Token ROI, highlighting large variations in runtime and cost efficiency.
- Low‑level tool‑interface mismatches cause physical design failures, especially when Tcl commands depend on tool version or execution mode.

## Context
The work addresses the growing expectation that generative AI will automate complex engineering pipelines. By benchmarking agents against traditional EDA tools, it reveals gaps between model capability and practical deployment constraints in semiconductor manufacturing.

## Implications
For practitioners, the findings stress the need for structured tool interfaces and persistent design context to avoid costly failures. Industry adoption of agentic EDA must incorporate process‑level evaluation and controlled execution to ensure robust performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17528v3)
