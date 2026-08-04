---
title: CallScreenBench: Benchmarking On-Device Models as Phone Secretaries
url: http://arxiv.org/abs/2608.01033v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_06-31-25Z_CallScreenBench_BenchmarkingOn_DeviceModelsasPhone.md
generated_at: 2026-08-03 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CallScreenBench, a benchmark that evaluates on‑device language models as phone secretaries by measuring how users would judge their handling of an unknown call. The study finds that model quality scales with capability but triage performance does not, and that some agents achieve perfect scores simply by hanging up or echoing the caller.

## Key Takeaways
- CallScreenBench scores agents on five quality dimensions rather than a single averaged metric, highlighting that certain failures are tolerated while others are not.  
- The apparent gap in triage performance is explained by degenerate agents that hang up or repeat the caller’s message, which inflate scores and obscure true differences between models.  
- After correcting for these artifacts, no model pair shows a measurable improvement in triage, suggesting the metric may be misleading.

## Context
The rapid rise of quantized language models on mobile devices enables real‑time task automation without cloud reliance. However, existing benchmarks often assume cooperative users and complete task success, which does not reflect realistic user expectations for privacy‑preserving assistants.

## Implications
For practitioners, CallScreenBench underscores the need to design metrics that separate genuine capability from superficial artifacts in on‑device agents. The field must move beyond single‑number rankings toward nuanced evaluations that respect user judgment and privacy constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01033v1)
