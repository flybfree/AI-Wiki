---
title: "Summary: 2026-05-11_17-49-43Z_WildClawBench_ABenchmarkforReal_World_Long_Horizon.md"
date: 2026-05-11
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-11_17-49-43Z_WildClawBench_ABenchmarkforReal_World_Long_Horizon.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.10912v1)
Saved: 2026-05-12 03:00
Source: 2026-05-11_17-49-43Z_WildClawBench_ABenchmarkforReal_World_Long_Horizon.md
Model: None

---


## Summary  
WildClawBench is a benchmark designed to evaluate large‑language and vision‑language agents on realistic long‑horizon tasks that run in native command‑line interfaces with genuine tools rather than synthetic sandboxes. The authors introduce 60 human‑authored, bilingual, multimodal tasks across six thematic categories, each lasting roughly eight minutes and involving over twenty tool calls. Grading combines deterministic rule‑based checks, environment‑state auditing of side effects, and an LLM/VLM judge for semantic verification, producing a single overall score per model.

## Semantic links
- [[concepts/papers/2026-06-11_17-58-35Z_Agents_K1_TowardsAgent_nativeKnowledgeOrche_summary.md|Summary: 2026-06-11_17-58-35Z_Agents_K1_TowardsAgent_nativeKnowledgeOrchestratio.md]] — 3 title terms overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-11_17-59-36Z_SpatialClaw_RethinkingActionInterfaceforAge_summary.md|Summary: 2026-06-11_17-59-36Z_SpatialClaw_RethinkingActionInterfaceforAgenticSpa.md]] — 2 title terms overlap; shared tags: ai, paper, research; 10 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The best frontier model, Claude Opus 4.7, attains only 62.2 % overall on WildClawBench under the OpenClaw harness, far below expectations for long‑horizon performance.  
- [Finding 2] Switching from one CLI harness to another can shift a single model’s score by up to 18 points, demonstrating that harness choice is a major source of variance.  
- [Finding 3] The benchmark reveals that current frontier models still struggle with long‑horizon, native‑runtime agent evaluation; the task remains far from resolved.

## Methodology  
The authors assembled tasks that mimic real user workflows and placed them inside reproducible Docker containers hosting an OpenClaw CLI harness. Each container runs one of four front‑end agents—Claude Code, Codex, or Hermes Agent—granting the model access to actual tools such as file system operations, web search APIs, and database queries. Grading is hybrid: deterministic rule‑based checks verify final outputs, environment‑state auditing records all side effects, and an LLM/VLM judge assesses semantic correctness. The entire pipeline is fully reproducible with public code and container images.

## Results  
Across 19 frontier models evaluated on WildClawBench, Claude Opus 4.7 achieved the highest score of 62.2 % under OpenClaw, while every other model scored below 60 %. The authors also measured harness‑induced variance: moving a model from OpenClaw to Claude Code can increase its score by up to 18 points, underscoring how much performance depends on the specific CLI environment rather than the model alone.

## Significance  
WildClawBench demonstrates that long‑horizon, native‑runtime agent evaluation is still an open problem for state‑of‑the‑art models. By providing a set of realistic, multimodal tasks with a transparent grading scheme and fully containerized tooling, the benchmark enables fair comparison across different harnesses and offers a community resource to advance research in long‑term agency.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/alignment-safety/alignment-hub.md|Alignment Hub]]
