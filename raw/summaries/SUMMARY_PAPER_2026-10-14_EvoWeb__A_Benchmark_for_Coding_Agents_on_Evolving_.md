---
title: EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications
url: http://arxiv.org/abs/2610.16402v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_08-42-42Z_EvoWeb_ABenchmarkforCodingAgentsonEvolvingWebAppli.md
generated_at: 2026-10-14 00:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EvoWeb introduces a benchmark of 320 cumulative requests across 32 web applications designed to evaluate coding agents on iterative, multi-request web development rather than single-shot generation from fixed specifications. The benchmark uses functional dependency graphs and a multimodal web agent that tests each intermediate application in a live browser, revealing that cross-request integration and deep dependency chains are the primary failure modes for frontier models, with performance degrading as requests accumulate.

## Key Takeaways
- EvoWeb structures 320 requests over 32 web applications using functional dependency graphs grounded in real-world product features, forcing agents to iteratively modify a persistent codebase rather than generate from scratch, which more faithfully mirrors how software teams actually build and extend web products over time.
- A multimodal web agent tests each intermediate application in a live browser, evaluating three dimensions simultaneously: newly requested functionality, cross-request integration (ensuring new features do not break previously implemented ones), and previously requested functionality, providing a holistic reliability signal rather than a single pass/fail check.
- Experiments across open- and closed-source frontier models show that cross-request integration is the dominant challenge, with later requests that have deeper or more numerous dependency links solved less accurately, and runtime errors becoming increasingly frequent as successive requests accumulate, demonstrating a compounding degradation effect that fixed-specification benchmarks fail to capture.

## Context
Most existing code-generation benchmarks, such as SWE-bench or WebArena, evaluate agents against static, isolated specifications, which does not reflect the incremental, dependency-heavy nature of real software development where each new feature must coexist with all prior ones. EvoWeb fills this gap by modeling development as a trajectory of cumulative requests with explicit dependency structure, shifting evaluation from single-task accuracy to long-horizon reliability. This aligns with a broader industry push toward agentic coding systems that operate over extended sessions, making benchmarks that stress sustained correctness increasingly critical for measuring genuine progress.

## Implications
For practitioners building coding agents for production use, EvoWeb highlights that a model's ability to handle a single well-specified task is a poor predictor of its reliability across a multi-feature development cycle, and that integration failures compound over time in ways that static benchmarks cannot detect. For the research community, the benchmark provides a concrete testbed for developing techniques—such as dependency-aware planning, regression testing loops, or context management strategies—that specifically target cross-request integration and long-horizon stability, areas where current frontier models show the largest performance gaps.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16402v1)
