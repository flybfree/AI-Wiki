---
title: AgentSLABench: Evaluating and Benchmarking Agentic Systems Under Resource Constraints
published: 2026-08-01T18:17:47Z
authors: Meher Bhaskar Madiraju, Meher Sai Preetam Madiraju
url: http://arxiv.org/abs/2608.00805v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentSLABench: Evaluating and Benchmarking Agentic Systems Under Resource Constraints

## Abstract
We present AgentSLABench, a resource-aware evaluation framework for autonomous AI agents that measures correctness alongside latency, cost, compute, memory, and network usage under declared resource budgets. Unlike standard benchmarks that report only accuracy, AgentSLABench produces a multi-dimensional profile per agent per task - the same way systems profilers (perf, pprof, cProfile) measure resource consumption of code, but extended with task correctness as a first-class dimension. AgentSLABench provides 16 task environments across 6 categories (5 core: multi-hop QA, retail substitution, code generation, web shopping, travel planning; 11 extended) with isolated Docker containers, declared CPU/memory/time/network budgets, sealed test sets with SHA256 hashes, and a standardized profiling protocol. We profile 5 general-purpose baseline agents (ReAct, PlanAndSolve, Reflexion, CoT, Random) plus 4 task-specialized agents, finding that specialized agents achieve 100% success on 3/5 core tasks (fact_qa, web_shopping, travel_planning) and 66.7-83.3% on retail and code_gen, while general baselines fail entirely on 4/5 domain tasks. Crucially, we report the Efficiency-Adjusted Success Rate (EASR) - success weighted by resource consumption relative to declared budgets - revealing that high accuracy at unbounded cost is not production-viable. We release the full infrastructure, sealed test sets, and profiling results to enable reproducible, resource-aware agent evaluation.

## Metadata
- **Published**: 2026-08-01T18:17:47Z
- **Authors**: Meher Bhaskar Madiraju, Meher Sai Preetam Madiraju
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00805v1)