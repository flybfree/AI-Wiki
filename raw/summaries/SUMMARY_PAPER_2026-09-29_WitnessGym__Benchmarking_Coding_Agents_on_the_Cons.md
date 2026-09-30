---
title: WitnessGym: Benchmarking Coding Agents on the Construction of Bug Witnesses
url: http://arxiv.org/abs/2609.36635v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-29_03-43-13Z_WitnessGym_BenchmarkingCodingAgentsontheConstructi.md
generated_at: 2026-09-29 20:40
model: qwen3.6-35b-a3b
---

## Summary
WitnessGym introduces an automated framework for generating high-quality bug-validation benchmarks by injecting bugs into test-reached paths of real-world Java projects, addressing the challenges of manual construction and data leakage in existing evaluations. The system produces 1,300 benchmark cases with injected patches that closely mimic historical bug patterns, ensuring realistic difficulty while maintaining executable witnesses for auditability. Evaluation across four coding agent frameworks reveals that constructing these witnesses remains a significant challenge even when bug patterns are explicitly known, highlighting persistent gaps in current model capabilities.

## Key Takeaways
- WitnessGym automates benchmark creation by injecting bugs into test-reached paths of real projects, rebuilding the code, and retaining only cases where a witness can be constructed; it further employs bug-preserving transformations to vary surrounding structures without altering faulty behavior, enabling scalable generation of diverse

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36635v1)
