---
title: Not All Correct Fixes Run Alike: An Empirical Study of Patch Performance in Repository-Level Issue Resolution
url: http://arxiv.org/abs/2610.13563v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_13-17-53Z_NotAllCorrectFixesRunAlike_AnEmpiricalStudyofPatch.md
generated_at: 2026-10-11 22:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the built-in FAIL_TO_PASS (F2P) tests from repository-level benchmarks like SWE-bench can be repurposed to evaluate the runtime performance of patches that already pass correctness tests. By generating multiple correct solutions using four frontier LLMs paired with SWE-agent across 262 benchmark instances, the authors demonstrate that test-passing patches exhibit significant runtime performance differences, and that these performance rankings are nearly reversed relative to the models' issue resolution rates.

## Key Takeaways
- The authors propose using the native F2P tests already provided in SWE-bench as a natural, zero-cost performance workload to measure patch runtime efficiency in instruction count and wall-clock time, eliminating the need to design custom performance benchmarks for each instance. They employ Welch ANOVA as a more robust statistical discrimination criterion compared to the relative standard deviation (RSD) used in prior work, achieving notable discrimination capability that identifies meaningful performance differences among patches in nearly half of the evaluated instances.
- A critical finding is that runtime performance of generated patches is independent of the issue resolution rate of LLMs, with model rankings nearly reversed between correctness and performance metrics. This means a model that resolves more issues correctly does not necessarily produce faster or more efficient patches, challenging the assumption that higher resolution rates correlate with higher-quality code generation across all dimensions.
- The case study reveals that performance analysis uncovers architectural regressions in some patches that correctness-based evaluation completely overlooks. Patches that pass all tests may introduce hidden inefficiencies or structural regressions in the codebase, suggesting that correctness tests alone are insufficient to characterize the true quality of a generated fix.

## Context
Repository-level issue-resolution benchmarks such as SWE-bench have become the dominant evaluation framework for assessing LLMs' ability to fix real-world software bugs, yet they evaluate patches almost exclusively on binary correctness—whether tests pass or fail. This paper addresses a significant gap in the evaluation methodology by demonstrating that correctness is only one dimension of patch quality and that runtime performance can vary dramatically among patches that are all deemed "correct." The work sits at the intersection of software engineering, LLM evaluation, and performance analysis, pushing the field toward more holistic assessment of code-generation capabilities.

## Implications
For practitioners and benchmark designers, these findings suggest that resolution rate alone does not adequately characterize an LLM's capability for repository-level issue resolution, and future evaluations should incorporate patch performance metrics alongside correctness to provide a more complete picture of model quality. For industry teams deploying AI-assisted code generation, the discovery that performance rankings can be nearly reversed relative to correctness rankings means that selecting models based solely on benchmark pass rates may inadvertently introduce runtime regressions into production codebases, motivating the integration of performance-aware evaluation pipelines into CI/CD workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13563v1)
