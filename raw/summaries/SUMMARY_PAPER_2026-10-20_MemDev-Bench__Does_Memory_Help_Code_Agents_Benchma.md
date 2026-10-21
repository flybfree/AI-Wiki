---
title: MemDev-Bench: Does Memory Help Code Agents?Benchmarking Memory Systems over Real Repository Histories
url: http://arxiv.org/abs/2610.27524v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_02-39-26Z_MemDev_Bench_DoesMemoryHelpCodeAgents_Benchmarking.md
generated_at: 2026-10-20 22:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MemDev-Bench introduces a benchmark designed to evaluate how memory systems affect code agents operating over real, evolving repository histories. The benchmark pairs each task with relevance-annotated earlier tasks from the same repository, enabling controlled evaluation of memory's impact on code agent performance. The study finds that while memory improves fine-grained code localization and editing, it also introduces new failure modes when agents reuse stored experience without reassessing its applicability to the current task.

## Key Takeaways
- Memory systems primarily improve fine-grained localization and editing capabilities in code agents, leading to increased functional correctness on tasks where relevant prior experience exists. However, this benefit is conditional on the relevance of stored history to the current task.
- Memory systems introduce a novel failure mode: agents fail on tasks they could otherwise solve when given related history, and unrelated history exacerbates these failures. The root cause is agents blindly reusing stored memory without reassessing whether it applies to the current context, suggesting a critical gap in memory retrieval and application logic.
- Directly providing agents with raw historical trajectories substantially reduces the number of steps agents take compared to using compressed memory systems. Agents save steps by reusing process information—such as reasoning chains and intermediate decisions—that compressed memory representations tend to omit, highlighting a fundamental design flaw in current memory compression strategies.

## Context
This paper addresses a growing concern in the AI agent research community: as code agents like SWE-agent and Devin increasingly operate on real software repositories with complex histories, memory systems have been proposed as a way to help agents reuse prior experience. However, existing benchmarks lack temporally valid histories and control over prior-task relevance, making it impossible to rigorously assess whether memory genuinely helps or harms agent performance. MemDev-Bench fills this gap by constructing 4,869 historical tasks across 555 base tasks with controlled relevance annotations, providing the first systematic evaluation framework for memory-augmented code agents.

## Implications
For practitioners building code agents and memory-augmented AI systems, this research signals that current memory architectures may be actively harmful in certain scenarios, particularly when agents fail to validate stored experience against new task contexts. The finding that raw process information outperforms compressed memory suggests that future memory systems should preserve reasoning traces and decision sequences rather than summarizing them, and should incorporate applicability reassessment mechanisms before injecting retrieved memories into agent reasoning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27524v1)
