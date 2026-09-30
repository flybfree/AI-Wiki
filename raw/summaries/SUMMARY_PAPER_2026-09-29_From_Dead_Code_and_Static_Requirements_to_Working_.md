---
title: From Dead Code and Static Requirements to Working Engines: Software Revival with Coding Agents
url: http://arxiv.org/abs/2609.36161v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_19-30-12Z_FromDeadCodeandStaticRequirementstoWorkingEngines_.md
generated_at: 2026-09-29 20:47
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces ReviveBench, a benchmark designed to evaluate coding agents' ability to restore non-functional software and reconstruct engines from open specifications using executable verification calibrated against native environments or reference implementations. The study demonstrates that while state-of-the-art models can successfully revive legacy codebases and reconstruct complex systems like CAD and CRM tools, the evaluation process itself is prone to significant measurement errors due to verifier defects, including numerous false negatives and positives.

## Key Takeaways
- The revival family of tasks, encompassing dependency incompatibilities and deleted core modules, reveals that the strongest evaluated model passes all ten tasks; contamination-control experiments using identifier obfuscation reduce line similarity to original implementations significantly without lowering pass rates, confirming robustness against training data leakage.
- In the reconstruction family spanning numerical, geometric, hardware, and transactional systems, two models meet the benchmark's pass criteria on all thirteen tasks, yet auditing exposes limitations where certain tasks, such as a CFD simulation, fail to establish genuine numerical-solver capability despite passing verification.
- Benchmark construction uncovered 28 verifier defects, including 24 false negatives and two false positives, highlighting that executable verification can introduce substantial measurement error; the authors recommend practical checks like verifying method reachability to grading thresholds and recomputing diagnostics from submitted artifacts to mitigate these risks.

## Context
As large language models increasingly automate software engineering tasks, rigorous evaluation frameworks are essential to distinguish genuine capability from memorization or superficial code generation. This work addresses the critical need for dynamic, execution-based assessment methods that go beyond static analysis to validate whether agents can handle real-world maintenance and creation challenges in industrial settings.

## Implications
Practitioners must recognize that high benchmark scores may mask underlying verifier flaws, necessitating multi-faceted validation approaches when deploying coding agents for legacy system modernization or automated development pipelines. The findings urge the community to prioritize robust verification auditing and diverse task design to build trust in AI-driven software revival and reconstruction workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36161v1)
