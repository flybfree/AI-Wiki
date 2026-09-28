---
title: The Hard Part Comes After Search: Benchmarking Web Agents on Synthesizing, Organizing, and Displaying Knowledge
url: http://arxiv.org/abs/2609.30604v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-24_22-36-10Z_TheHardPartComesAfterSearch_BenchmarkingWebAgentso.md
generated_at: 2026-09-27 21:27
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces KNOWS, a benchmark designed to evaluate web agents on complex, multi-step workflows that require synthesizing information across diverse sources and producing coherent artifacts like documents or spreadsheets. Evaluation of frontier models reveals that while agents achieve moderate partial success rates, the best-performing agent fully completes fewer than 3% of these long-horizon tasks. The study highlights that failures in visual understanding often render final outputs unusable, exposing significant gaps in current capabilities for acting as end-to-end assistants.

## Key Takeaways
- The authors present KNOWS, a benchmark comprising open-ended, browser-based tasks that demand agents to retrieve information, synthesize it into specific artifacts, and navigate program interfaces, with each task assessed by a hybrid evaluator combining deterministic checks and LLM judgments to balance reliability and richness.
- Benchmarking frontier computer-use agents shows that even the top performer fully succeeds in less than 3% of complex tasks, with visual step failures being particularly detrimental; these errors frequently make resulting artifacts unusable despite agents successfully completing over half of other evaluation steps.
- The results underscore fundamental limitations in current agent architectures regarding tool use, spatial and visual comprehension, and long-horizon reasoning, indicating that significant advancements are required before agents can reliably function as autonomous assistants capable of delivering high-quality end-to-end workflows.

## Context
As AI agents move beyond simple query-response paradigms toward autonomous assistance roles,

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30604v1)
