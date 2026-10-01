---
title: When a Kindergartener Solves Calculus: Measuring Capability Leakage in Role-Prompted Reasoning Models
url: http://arxiv.org/abs/2609.39846v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_14-39-41Z_WhenaKindergartenerSolvesCalculus_MeasuringCapabil.md
generated_at: 2026-09-30 22:05
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates role-capability leakage (RCL), a phenomenon where reasoning models maintain expert-level performance on benchmarks despite being prompted to adopt roles with significantly lower capability levels, such as a kindergarten student solving calculus problems. The authors introduce RoleCapBench, a curriculum-grounded benchmark assessing RCL across six educational roles and four assessment levels, revealing that while models produce stylistically convincing in-role text, they consistently fail to suppress underlying capabilities even when explicitly instructed to do so. To address this misalignment, the study proposes "Injection," an inference-time intervention combining role-specific capability guidelines with a guiding prefilled response prefix, which significantly reduces above-role accuracy while preserving the quality of role-aligned responses.

## Key Takeaways
- Role-capability leakage is pervasive and robust; models exhibit

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39846v1)
