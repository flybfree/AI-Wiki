---
title: How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering
url: http://arxiv.org/abs/2611.07286v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-05_01-08-43Z_HowShouldAgentsSeeCode_RethinkingCodeRepresentatio.md
generated_at: 2026-11-08 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

This paper investigates how different code-representation workflows—abstract syntax trees, call graphs, module dependencies, documentation-enriched search, and a hybrid combination—affect LLM agents' performance on repository-level software engineering tasks. The authors evaluate Claude Code with Haiku 4.5 against a raw-tool baseline across four benchmarks and find that map-based workflows primarily serve as token-saving tools when localization is the bottleneck, while their success gains narrow when the decisive step involves patch or test authoring, making their benefits task-dependent rather than universal.

## Key Takeaways

- On fault localization (LinuxFLBench), all five representation workflows improve recall@10 over the raw-tool baseline, achieving scores between 0.757 and 0.829 compared to 0.717, while simultaneously reducing token usage by 25-39%. This demonstrates that structured repository maps help agents identify relevant code regions more efficiently than lexical search and shell commands alone.

- On repository-level code generation and repair (SWE-bench Pro), resolution rates remain close to the baseline (44.3-50.6% versus 49.0%), but token usage drops by 17-26%. This indicates that while structured views help agents navigate large repositories, they do not fundamentally improve the agent's ability to author correct patches, suggesting the bottleneck shifts from retrieval to generation quality.

- On security patching (SecBench) and test generation (SWT-bench), results are mixed: Callgraph achieves the highest patch-resolution rate (34.3% vs. 28.9%), and Hybrid and Docs achieve the highest reproducing-test rates (47.8% and 47.2% vs. 44.7%), but all workflows increase latency and, in the test-generation case, increase token usage. This reveals that the utility of a given representation depends heavily on the specific task structure and where the agent's reasoning bottleneck lies.

## Context

As LLM agents become central to automated software engineering pipelines, the question of how agents perceive and navigate codebases has become a critical design decision that directly impacts cost, speed, and reliability. Most current agentic systems treat repositories as flat text accessed through grep, file reading, and shell commands, which scales poorly for large codebases and wastes tokens on irrelevant context. This paper positions code representation as a first-class architectural variable rather than an implementation detail, contributing to the growing research effort around retrieval-augmented generation for code and structured program analysis integrated with language models.

## Implications

For practitioners building agentic coding tools, this work provides empirical guidance on when to invest in structured code representations: they are most valuable for localization-heavy tasks and token-constrained deployments, but offer diminishing returns when the core challenge is generating correct code or tests. For the broader field, these findings suggest that future agent architectures should dynamically select or combine representation strategies based on task type rather than adopting a single universal view, and that benchmarking must account for token cost and latency alongside accuracy to reflect real-world deployment constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07286v1)
