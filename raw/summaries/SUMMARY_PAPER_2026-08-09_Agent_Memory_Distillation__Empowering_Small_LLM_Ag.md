---
title: Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory
url: http://arxiv.org/abs/2608.07169v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_12-43-00Z_AgentMemoryDistillation_EmpoweringSmallLLMAgentswi.md
generated_at: 2026-08-09 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Agent Memory Distillation (AMD), a training‑free framework that transfers structured knowledge from a large teacher agent to a small student through hierarchical memory. It creates three complementary memory types — workflow, subtask, and function — and demonstrates average accuracy gains of 27.2 %, 11.2 % and 3.4 % on AppWorld, BFCL V3 and ToolSandbox benchmarks.

## Key Takeaways
- AMD constructs Workflow memory that encodes task‑level strategies and Subtask memory that provides concrete behavioral examples at an intermediate granularity, both injected proactively at the start of each task.
- Function memory is retrieved reactively when tool‑calling errors occur, capturing per‑function calling conventions and common pitfalls.
- The 4B‑sized student models benefit most from AMD, achieving the largest gains across all evaluated benchmarks.

## Context
Memory systems are increasingly explored to augment language model reasoning by storing past experiences. This work shows that even very small LLMs can improve performance when given structured memory transfer without retraining large teacher models.

## Implications
For practitioners, AMD provides a practical way to boost agent accuracy without the cost of full retraining. The findings suggest hierarchical memory could be integrated into future agent architectures and deployed across diverse tool‑use scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07169v1)
