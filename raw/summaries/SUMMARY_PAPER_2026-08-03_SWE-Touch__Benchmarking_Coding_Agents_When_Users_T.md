---
title: SWE-Touch: Benchmarking Coding Agents When Users Touch the Code
url: http://arxiv.org/abs/2608.02499v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
generated_at: 2026-08-03 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SWE-Touch, a framework that tests coding agents on shared workspaces where users make counter‑edits to code, revealing a 7.7 percentage‑point drop in resolve rate compared with SWE‑bench Verified. It shows that agents often retain conflicting versions of the same region and fail to re‑inspect after edits.

## Key Takeaways
- The average resolve rate drops by 7.7 percentage points on SWE-bench Verified due to agents' limited awareness of evolving workspace changes.
- Agents may keep both original and new code, leading to conflicts that hinder task completion.
- Successful resolution requires re‑inspection and validation of revised code with targeted tests.

## Context
This work addresses the gap between autonomous coding performance and real‑world collaborative development where users interact directly with code. Existing benchmarks ignore such dynamic edits, limiting understanding of agent adaptability in shared environments.

## Implications
For developers and AI practitioners, this highlights the need for agents that can detect workspace modifications, reconcile conflicting edits, and verify behavior after changes. Future systems must incorporate robust state awareness to support true collaborative coding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02499v1)
