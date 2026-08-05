---
title: CARE-Bench: Benchmarking Patient-Facing LLM Triage
url: http://arxiv.org/abs/2608.03731v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-26-45Z_CARE_Bench_BenchmarkingPatient_FacingLLMTriage.md
generated_at: 2026-08-05 01:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CARE‑Bench, a benchmark for evaluating patient‑facing medical LLMs that triage symptoms into four actions per turn. It tests 11 models on 500 cases and finds unprompted macro‑F1 low (31–50) while prompting improves to 47–63 but errors persist.

## Key Takeaways
- Unprompted macro‑F1 remains low, ranging from 31.2 to 50.4, indicating poor performance without prompts.
- Prompting raises macro‑F1 to 46.9–63.4 for ten models, yet many still recommend care before obtaining needed clarification.
- The persistent threshold errors show that prompting does not fully solve the timing problem in patient triage.

## Context
Patient‑facing medical LLMs are being deployed to guide users toward appropriate next steps, but their safety hinges on correct action sequencing. This benchmark provides a systematic way to measure how well models handle multi‑step dialogue without clinician input, addressing a gap in existing evaluation tools that focus only on accuracy rather than temporal correctness.

## Implications
Clinicians and developers must consider not just response quality but also when actions are taken relative to information gaps. The findings warn against blind reliance on prompting fixes and suggest explicit timing evaluation before real‑world deployment of triage systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03731v1)
