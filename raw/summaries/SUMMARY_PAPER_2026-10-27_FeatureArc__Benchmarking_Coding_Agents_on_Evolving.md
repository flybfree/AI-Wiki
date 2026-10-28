---
title: FeatureArc: Benchmarking Coding Agents on Evolving Features
url: http://arxiv.org/abs/2610.37434v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_15-45-50Z_FeatureArc_BenchmarkingCodingAgentsonEvolvingFeatu.md
generated_at: 2026-10-27 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FeatureArc introduces a benchmark that evaluates coding agents on evolving software features rather than single fixed requests, requiring agents to build successive extensions on their own earlier code across 2 to 10 stages. The study of 10 coding agents on 73 tasks reveals a dramatic performance degradation from 62.7% success at the first stage to 28.5% when the full feature is tested on final code, with inherited defects from earlier stages present in 72.9% of failed later stages.

## Key Takeaways
- FeatureArc constructs tasks from real repository histories and validates them using fail-to-pass (F2P) tests for new behavior and pass-to-pass (P2P) tests for existing behavior across four programming languages, ensuring that each stage's correctness is verified against both new requirements and previously established interface contracts.
- The evaluation exposes a critical failure mechanism: agents inherit defects from earlier stages and fail to detect them, leaving earlier errors unnoticed approximately 95% of the time in subsequent stages, while their self-tests rarely revisit prior stages, meaning compounding errors propagate silently through the feature's evolution.
- Agents operate in a single persistent session and workspace without external test feedback or rollback capability, simulating realistic autonomous development conditions, and the benchmark spans 73 manually reviewed tasks with 2 to 10 stages to capture the full complexity of feature evolution rather than isolated code generation.

## Context
Most existing coding agent benchmarks evaluate a single code generation request against a fixed codebase, which fails to capture how real software features are incrementally extended as new use cases and requirements arrive. FeatureArc addresses this gap by modeling the sequential dependency structure of feature evolution, where each stage builds upon code the agent itself wrote earlier, reflecting the actual workflow developers follow in production software engineering. This shift from static single-shot evaluation to multi-stage autonomous evolution represents a more ecologically valid assessment of coding agent capabilities.

## Implications
For practitioners deploying coding agents in production software development, the findings indicate that current agents cannot yet reliably evolve features autonomously without human verification between stages, as inherited defects compound and remain undetected. The pipeline and evaluation methodology developed for FeatureArc are already being applied at Tencent to extend internal evaluations and guide the development of the Hunyuan family of large language models, signaling that industry leaders recognize multi-stage feature evolution as a critical capability gap that must be addressed before coding agents can be trusted for sustained autonomous software development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37434v1)
