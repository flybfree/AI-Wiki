---
title: ORCA-bench: How Ready Are Language Model Agents for Oncall?
url: http://arxiv.org/abs/2607.28545v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-14-07Z_ORCA_bench_HowReadyAreLanguageModelAgentsforOncall.md
generated_at: 2026-07-30 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ORCA-bench, a benchmark that tests large language model agents on realistic root cause analysis tasks in production. Across five frontier agents, the best accuracy is 25.3% on medium‑difficulty RCA tasks and 10.0% on hard tasks, indicating limited reliability. The results show that even advanced models like Claude Fable 5 fall short of human performance.

## Key Takeaways
- The benchmark demonstrates that current frontier coding agents achieve only modest accuracy in RCA, with hallucinations occurring in up to 40% of incidents when source code is unavailable.
- Ground‑truth symptoms are expert‑verified and re‑scored by humans, yielding a high Cohen’s κ_w=0.90 reliability for the evaluation.
- The gap between model performance and human experts suggests that deploying these agents on production systems would require substantial engineering effort to mitigate errors.

## Context
Root cause analysis is critical for incident response but often involves noisy logs, traces, and ambiguous reports. Existing AI research focuses on code generation or debugging in isolation, not on the holistic, real‑time reasoning required by SREs. This work bridges that gap by placing models directly into a production‑fidelity environment.

## Implications
The findings warn that entrusting frontier agents to live systems is premature; they cannot yet reliably identify root causes without extensive safeguards and larger datasets. Industry adoption will likely need incremental improvements in model robustness, access to source code, and human oversight before oncall reliability can be assured.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28545v1)
