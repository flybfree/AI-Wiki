---
title: TLA$^{+}$-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation
url: http://arxiv.org/abs/2607.23425v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_02-49-56Z_TLA_______Bench_AnExecution_GroundedBenchmarkandDa.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TLA+‑Bench, a dataset and benchmark that evaluates natural‑language to TLA$^+$ generation by running model checkers on the full reachable state space rather than relying on parsing or similarity. It shows that correctness is not binary but varies within an envelope, and that providing configuration names improves scores dramatically.

## Key Takeaways
- The dataset contains 403 gold specifications with execution‑based grading and 897 parse‑only silver ones from public repositories.
- An exact oracle yields a range of correct rates; without interface information the rate is as low as 1.7 % while it rises to 26 % when configuration names are supplied.
- Correctness drops sharply with difficulty, indicating that model output quality scales poorly under complexity.

## Context
This work addresses a long‑standing gap in measuring LLM performance on formal verification tasks where traditional metrics are misleading. By grounding evaluation in execution, TLA+‑Bench provides a more reliable benchmark for future research and tooling.

## Implications
For practitioners, the envelope of correctness suggests that interface design is crucial; without it models remain far from useful. The field must adopt execution‑grounded benchmarks to guide model improvement and avoid overestimating performance based on parsing alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23425v1)
