---
title: CoMemBench: Benchmarking Collaborative Memory Boundaries across Multi-Agent Workflow Topologies
url: http://arxiv.org/abs/2609.32192v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_03-33-15Z_CoMemBench_BenchmarkingCollaborativeMemoryBoundari.md
generated_at: 2026-09-28 20:40
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces CoMemBench, a benchmark designed to evaluate collaborative memory boundaries in multi-agent workflows, focusing on how workflow topologies dictate the sharing and isolation of information among agents. Unlike existing benchmarks that prioritize retention or end-to-end completion, this framework assesses task-conditioned scope by measuring verified handoffs, isolation robustness, and progress across 800 composite workflows spanning four domains. Experimental results highlight a critical trade-off where broader context enhances information availability but compromises isolation integrity, causing system rankings to fluctuate significantly based on topology and artifact violations.

## Key Takeaways
- CoMemBench constructs 800 composite workflows derived from source-grounded dependency graphs across four domains, featuring node-local specifications, verifiable artifact handoffs, native evaluators, and matched isolation challenges to rigorously test collaborative memory dynamics under structural constraints.
- The benchmark evaluates five distinct dimensions including workflow completion rates, verified node progress, required-handoff reliability, isolation robustness against irrelevant or stale information, and token cost, providing a holistic assessment of memory efficiency beyond simple retrieval accuracy.
- Experiments reveal a fundamental sharing-isolation trade-off where expanding context improves information availability for downstream workers but weakens isolation boundaries; additionally, system performance rankings shift dynamically across different workflow topologies and artifact violation scenarios rather than remaining consistent.

## Context
As multi-agent systems increasingly rely on complex workflows to solve intricate tasks, the ability to manage

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32192v1)
