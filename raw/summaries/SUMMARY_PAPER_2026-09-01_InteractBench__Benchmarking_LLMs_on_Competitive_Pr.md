---
title: InteractBench: Benchmarking LLMs on Competitive Programming under Unrevealed Information
url: http://arxiv.org/abs/2608.29632v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-30_07-50-53Z_InteractBench_BenchmarkingLLMsonCompetitiveProgram.md
generated_at: 2026-09-01 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces InteractBench, a benchmark that evaluates large language models on competitive programming problems where information is revealed only through interactive queries rather than being given upfront. The authors find that even state‑of‑the‑art reasoning models perform poorly on these tasks, and they propose a detailed failure taxonomy to explain why.  

## Key Takeaways
- Interactive problems require dynamic information acquisition and protocol compliance, which most LLMs struggle with despite strong static reasoning abilities.  
- The benchmark shows that query‑budget overruns and protocol violations are common failure modes beyond simple logic errors.  
- A fine‑grained taxonomy of failures provides a roadmap for diagnosing model weaknesses in interactive settings.  

## Context
Competitive programming benchmarks have traditionally focused on full‑information tasks, overlooking the interactive component that tests real‑time reasoning and protocol adherence. This paper highlights a gap between static algorithmic competence and the ability to adapt under dynamic constraints, a challenge relevant to any system that must interact with external agents.  

## Implications
For AI researchers, InteractBench underscores the need for models capable of iterative information gathering and strict rule following in real‑world applications such as automated coding assistants. Industry practitioners should consider these limitations when deploying LLMs for interactive problem solving or similar constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29632v1)
