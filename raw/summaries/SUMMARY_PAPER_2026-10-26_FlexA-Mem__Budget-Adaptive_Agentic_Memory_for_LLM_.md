---
title: FlexA-Mem: Budget-Adaptive Agentic Memory for LLM Agents
url: http://arxiv.org/abs/2610.33274v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-23_20-34-09Z_FlexA_Mem_Budget_AdaptiveAgenticMemoryforLLMAgents.md
generated_at: 2026-10-26 20:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FlexA-Mem proposes a unified, budget-adaptive memory architecture for LLM agents that handles both fact-retrieval scenarios (requiring exact named strings) and multi-step task scenarios (requiring procedural traces and unnamed contextual details). By writing each unit of history once into an immutable store and rendering a fresh, compact memory per call using a fixed rule-based budget allocation without any additional LLM inference, FlexA-Mem outperforms specialized single-purpose memory systems by 11.5% to 12.2% on AppWorld benchmarks while matching dedicated keyword retrievers on LongMemEval and LoCoMo.

## Key Takeaways
- Existing memory systems for LLM agents are siloed by scenario type: retrieval memories like A-Mem miss steps the current query does not explicitly express, while summarization-based memories drop exact strings needed for factual recall. Pairing both approaches fixes the budget split in advance, limiting adaptability. FlexA-Mem eliminates this split by rendering a single unified memory per call.
- The core mechanism writes each history unit once into an immutable store, then constructs a per-call rendered memory consisting of a compact timeline of records plus detail (either relevant raw-text units, excerpts, or verbatim query-matching pieces). A fixed rule fits this into the remaining token budget without invoking an LLM, making the rendering step deterministic and fast.
- Ablation experiments reveal a clear division of labor: the timeline component is responsible for task completion on AppWorld multi-step tasks, while the recovery/detail component primarily saves redundant steps and determines accuracy on exact-fact retrieval. This confirms that neither component alone suffices for general-purpose agentic memory.

## Context
LLM agents increasingly operate across heterogeneous workloads—from conversational assistants recalling specific past facts to autonomous agents executing long-horizon multi-step plans—yet the memory subsystems supporting them remain purpose-built and brittle. This paper sits at the intersection of retrieval-augmented generation, agent planning, and token-budget management, addressing a practical deployment bottleneck: practitioners cannot afford to maintain separate memory pipelines for different task types, and fixed budget splits degrade performance when workloads shift. FlexA-Mem's immutable-store-plus-render-on-demand design offers a principled path toward a single memory substrate that adapts to query semantics at inference time.

## Implications
For practitioners building agentic systems, FlexA-Mem demonstrates that a single memory store with deterministic, rule-based rendering can match or exceed specialized systems across both factual-retrieval and procedural-task benchmarks, reducing engineering complexity and eliminating the need to pre-allocate budget splits. For the broader field, the finding that LLM-written summaries fall far behind keyword-based retrieval at tight budgets challenges the prevailing assumption that generative summarization is the right compression strategy for agent memory, suggesting that verbatim preservation with query-aware rendering may be more robust under resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33274v1)
