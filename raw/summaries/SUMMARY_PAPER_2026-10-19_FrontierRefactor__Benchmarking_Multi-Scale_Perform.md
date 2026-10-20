---
title: FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring
url: http://arxiv.org/abs/2610.25834v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_05-47-51Z_FrontierRefactor_BenchmarkingMulti_ScalePerformanc.md
generated_at: 2026-10-19 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FrontierRefactor introduces a benchmark of 60 engineering tasks spanning four scales—from computational kernels to full repositories—to evaluate whether autonomous coding agents can refactor code while preserving behavioral contracts and improving execution performance. The study reveals a critical decoupling between functional correctness and speedup: 41.2% of agent submissions pass functional equivalence checks yet fail to deliver verified performance gains, exposing a fundamental gap in current coding agent capabilities.

## Key Takeaways
- Correctness and performance are largely decoupled in agent-driven refactoring: 41.2% of submissions satisfy functional equivalence but fail to deliver verified speedups, with 19.3% suffering outright performance regressions and 21.9% trapped in measurement noise, meaning passing a correctness test does not guarantee a useful optimization outcome.
- Refactoring scale dramatically impacts success rates: cross-language rewrites gain speedups from native compilation after passing functional checks, but agents struggle with contract fidelity, with pass rates dropping from 65.0% on modules to 32.6% at package scale, while in-place optimization reliably preserves behavioral contracts at 86.5% but rarely achieves acceleration without physical performance profiling.
- Multi-turn execution-timing feedback directly resolves the "uncalibrated micro-benchmarking illusions" that trap agents in ineffective optimization loops, raising strict success rates from 16.0% to 40.0%, demonstrating that iterative runtime measurement feedback is essential for agents to distinguish genuine speedups from noise.

## Context
This paper addresses a critical gap in AI-assisted software engineering evaluation. Existing benchmarks either test refactoring correctness without measuring runtime regressions, or benchmark isolated micro-kernels without capturing codebase-scale complexity. By defining refactoring scale through the scope of the caller-visible interface, FrontierRefactor provides a principled framework for measuring whether coding agents can handle real-world engineering tasks where behavioral invariants must be preserved while private implementations are optimized. The cascaded, reference-free evaluation protocol across 1,080 execution runs sets a new standard for rigor in agent evaluation.

## Implications
For practitioners deploying coding agents in production software engineering, these findings warn that current agents cannot be trusted to deliver performance improvements even when they produce functionally correct code, making human oversight of runtime behavior essential. For the AI research community, the demonstrated effectiveness of multi-turn execution-timing feedback suggests that future agent architectures should incorporate physical performance profiling loops rather than relying on static analysis or micro-benchmark heuristics. Industry teams adopting autonomous refactoring tools should expect significant performance regressions at package and repository scales and should prioritize agents trained with calibrated runtime feedback to avoid silent degradation in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25834v1)
