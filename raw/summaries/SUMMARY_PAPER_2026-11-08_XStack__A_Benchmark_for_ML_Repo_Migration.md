---
title: XStack: A Benchmark for ML Repo Migration
url: http://arxiv.org/abs/2611.08472v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-05_18-55-54Z_XStack_ABenchmarkforMLRepoMigration.md
generated_at: 2026-11-08 21:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
XStack is a benchmark designed to evaluate AI agents on their ability to migrate entire machine learning repositories from PyTorch (on NVIDIA GPUs) to JAX (on Google TPUs). The paper finds that current agents remain unreliable at this task, with Claude Opus 5 achieving only a 75% pass rate, GPT-5.6-sol at 45%, and all other agents at most 40%. The benchmark grades outputs against the source repository's published results, authenticated and calibrated by the authors.

## Key Takeaways
- ML code is currently locked into two dominant ecosystems—PyTorch on NVIDIA GPUs and JAX on Google TPUs—and migrating between them requires handling differences in frameworks, hardware, and entire repository structures, making it a long-horizon and genuinely challenging task for any agent.
- The benchmark's grading criteria are grounded in the source repository's published results, which the authors authenticate and calibrate, ensuring that a "pass" means the migrated JAX code reproduces the original research findings rather than merely compiling or running without errors.
- Even the strongest current agent (Claude Opus 5) fails to reliably complete full repository migrations, with a 25% failure rate, while most agents fail more than 60% of the time, indicating that framework-and-hardware-aware code translation remains an open and unsolved problem in AI-assisted software engineering.

## Context
This paper sits at the intersection of AI agents for software engineering and the practical infrastructure concerns of the ML research community. As model training increasingly depends on specific hardware ecosystems, the ability to port code across frameworks and accelerators becomes a bottleneck for reproducibility, accessibility, and hardware flexibility. XStack formalizes this real-world pain point into a measurable benchmark, filling a gap where existing coding-agent evaluations focus on single-file or single-function tasks rather than whole-repository, cross-framework migration.

## Implications
For ML researchers and practitioners, a reliable migration agent would unlock access to alternative hardware (TPUs, AMD GPUs, etc.) without rewriting training pipelines from scratch, lowering barriers to experimentation and reducing vendor lock-in. For the AI-agent development community, XStack provides a rigorous, long-horizon evaluation target that exposes current limitations in tool-use, framework reasoning, and multi-file code transformation. For industry, it signals that fully autonomous code porting across major ML stacks is not yet achievable, guiding investment toward more capable agentic systems and better cross-framework tooling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.08472v1)
