---
title: SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents
url: http://arxiv.org/abs/2610.26995v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_08-46-15Z_SPEM_Structure_AwareProceduralMemoryforEfficientSk.md
generated_at: 2026-10-20 22:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SPEM, a structure-aware procedural memory framework designed to help LLM-based agents efficiently select and compose reusable skills without incurring the high token and runtime costs of loading an entire skill library or the inaccuracy of treating skills as flat, independent text entries. By combining Atomic Skill Memory with a Skill-DAG Memory that captures reusable compositions learned from successful executions, SPEM achieves the best effectiveness-to-efficiency trade-off among evaluated baselines, reaching 87.1% success on ALFWorld and 38.38% reward on SkillsBench while reducing computational overhead.

## Key Takeaways
- SPEM addresses two critical failure modes in current skill-use pipelines for LLM agents: full skill loading, which imposes prohibitive token and runtime overhead as libraries grow, and flat semantic retrieval, which treats every skill as an isolated text entry and therefore ignores inter-skill dependencies, required execution order, state transitions, and data-flow constraints that are essential for multi-step task completion.
- The framework is built around two complementary memory stores: Atomic Skill Memory, which stores individual skill descriptions and metadata, and Skill-DAG Memory, which captures directed acyclic graph templates of skill compositions that have previously led to successful task executions. When a new task arrives, SPEM first attempts to match it against high-confidence Skill-DAG templates; if none are available, it falls back to retrieving atomic skills and invoking a Skill-GNN module that performs state- and structure-aware selection, ensuring that prerequisite skills and data dependencies are respected.
- SPEM incorporates a continual learning loop: every successful execution is written back as a new Skill-DAG, allowing the procedural memory to accumulate and improve over time. This means the agent does not merely retrieve static skill descriptions but progressively builds a richer, validated library of executable skill compositions, reducing the need for costly exploration on future tasks.

## Context
As LLM agents are increasingly deployed in interactive environments such as embodied task-solving (ALFWorld) and tool-use benchmarks (SkillsBench), the ability to reuse previously learned skills becomes a central scaling bottleneck. Existing approaches either load the entire skill library into the context window or rely on flat embedding-based retrieval, both of which fail to model the structured, sequential nature of multi-step skill execution. SPEM sits at the intersection of procedural memory research, graph-based retrieval, and agent planning, offering a lightweight alternative that respects the compositional structure of skills while remaining computationally tractable.

## Implications
For practitioners building agentic systems, SPEM demonstrates that structure-aware retrieval and learned composition templates can dramatically reduce token consumption and inference latency without sacrificing task success, making large skill libraries viable in production settings where cost and speed are hard constraints. For the broader research community, the Skill-DAG write-back mechanism suggests a path toward agents that genuinely accumulate procedural knowledge over time rather than starting from scratch on every task, pointing toward more autonomous, self-improving agent architectures that could be adapted to software engineering, robotics, and multi-tool orchestration pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26995v1)
