---
title: Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail
url: http://arxiv.org/abs/2609.39086v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_06-26-07Z_TrustworthyRuntimeErrorHealinginReal_WorldReposito.md
generated_at: 2026-09-30 20:49
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the gap between theoretical LLM-based runtime error healing and practical application in real-world software repositories by introducing HealBench, a benchmark of 265 errors from 18 repositories, and HealGuard, a safety mechanism for healing code. The study demonstrates that while existing agents can resume execution in over 38% of cases and pass tests nearly 29% of the time, significant safety risks remain, as HealGuard identifies unsafe state propagation in a notable fraction of successful healings, though it currently suffers from a high false positive rate.

## Key Takeaways
- The authors introduce HealBench, a comprehensive benchmark comprising 265 runtime errors sourced from 18 real-world repositories, each paired with reference executions on patched versions, alongside a unified framework enabling LLM agents to perform healing using cross-file context and live runtime state information.
- HealGuard is designed to enforce safety by restricting healing code to an analyzable subset of Python called HealCore, utilizing static and dynamic taint analysis to detect whether modifications made by the healing process propagate to operations protected by developers.
- Evaluations show that top-performing configurations achieve a 38.11% execution resumption rate and a 28.68% test pass rate, proving agents can handle real-world crashes; however, HealGuard flags 17.4% of passing executions as potentially unsafe regarding protected operations, and while it detects all 684 controlled unsafe cases, it incurs a substantial 68.42% false positive rate.

## Context
As large language models increasingly demonstrate capabilities in code generation and debugging, the field is shifting from synthetic benchmarks to evaluating agents on complex, real-world software maintenance tasks where live execution and state manipulation are required. This work bridges a critical gap by moving runtime error healing beyond controlled competition environments into messy, production-like repositories, highlighting the urgent need for safety guardrails when allowing AI models to modify live process states.

## Implications
For practitioners and industry adopters, this research underscores that while LLMs can effectively recover from runtime errors

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39086v1)
