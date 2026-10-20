---
title: OpenSaC: A Python Library for Search as Code in Deep Research Agents
url: http://arxiv.org/abs/2610.25779v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_04-46-35Z_OpenSaC_APythonLibraryforSearchasCodeinDeepResearc.md
generated_at: 2026-10-19 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
OpenSaC is an open-source Python library that enables deep research agents to adopt the "Search as Code" paradigm, where agents write executable programs that compose search queries, source reading, reranking, model calls, and local processing into unified workflows rather than alternating reasoning with individual search actions. The library provides configurable capability interfaces that allow agents to combine these operations while retaining evidence for inspection and reuse. Benchmark evaluations on BrowseComp and WideSearch demonstrate that OpenSaC configurations achieve lower execution time and fewer model tokens compared to standard Codex with built-in web search, while delivering higher accuracy on BrowseComp.

## Key Takeaways
- Search as Code fundamentally restructures how deep research agents operate: instead of iteratively alternating between reasoning steps and individual search or reading actions, agents author programs that orchestrate search, source examination, reranking, model invocations, and local data processing as composable code blocks, returning selected observations for subsequent reasoning. This shifts the agent from a sequential action loop to a programmatic pipeline.
- OpenSaC provides a practical open-source implementation through a Python library paired with a companion Search as Code skill, designed to integrate into existing coding agent frameworks. Its configurable capability interfaces allow developers to mix and match operations such as web search, document reading, reranking, and local computation, while preserving intermediate evidence artifacts for transparency, inspection, and downstream reuse.
- Empirical results on BrowseComp and WideSearch benchmarks show that OpenSaC configurations consume less execution time and fewer model tokens than standard Codex relying on its built-in web search tool. OpenSaC achieves higher accuracy on BrowseComp, though it records slightly lower row F1 on WideSearch, indicating that the paradigm's benefits may vary depending on the structure of the evaluation task.

## Context
Deep research agents have emerged as a critical capability in modern AI systems, enabling autonomous investigation of complex, multi-hop questions that require iterative information gathering and evidence synthesis. The dominant paradigm treats search and reading as discrete tool calls interleaved with reasoning, which limits composability, reproducibility, and efficiency. OpenSaC addresses a growing demand for structured, programmable research workflows that treat information retrieval as a first-class composable operation rather than an opaque tool invocation, positioning itself at the intersection of agentic AI, information retrieval, and software engineering.

## Implications
For practitioners building research agents, OpenSaC lowers the barrier to adopting Search as Code by providing an open, extensible foundation that can be integrated into existing coding agent stacks without proprietary lock-in. The demonstrated reductions in token usage and execution time suggest that programmatic composition of search operations can yield meaningful cost savings in production deployments. For the broader research community, the library and its transparent benchmarking methodology provide a shared platform for developing, comparing, and auditing deep research agent architectures, fostering more reproducible and accountable progress in agentic information retrieval.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25779v1)
