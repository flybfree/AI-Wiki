---
title: RLPF: Reinforcement Learning from Performance Feedback for Code Generation
url: http://arxiv.org/abs/2607.27271v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_11-39-55Z_RLPF_ReinforcementLearningfromPerformanceFeedbackf.md
generated_at: 2026-07-30 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes RLPF, a reinforcement learning framework that trains code generation models to optimize both correctness and runtime by using performance feedback as a staged reward. Fine‑tuning Qwen3-32B on PerfCodeBench raises correct‑and‑runnable solutions from 11.1 % to 54.6 % and improves relative efficiency from 8.1 % to 38.6 %, showing the model can compete with strong open‑weight systems.

## Key Takeaways
- Failed programs are ordered by execution progress, giving useful feedback before they succeed.
- Correct programs receive rewards based on their improvement from a baseline toward an expert reference, linking performance gains directly to learning.
- The composite reward outperforms both correctness‑only and runtime‑only baselines, yielding higher correct‑and‑runnable rates and efficiency improvements.

## Context
Most code generation models rely solely on test pass/fail signals, which ignore execution characteristics such as speed. This limitation hampers the production of efficient software in real applications where performance matters. RLPF addresses this gap by integrating runtime as a meaningful reward that is only meaningful after correctness is achieved.

## Implications
By enabling agents to balance correctness and speed, RLPF can lead to more practical AI‑generated code for industry use. The findings also suggest that composite supervisory signals are more reliable than single metrics, guiding future research toward richer feedback mechanisms in code optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27271v1)
