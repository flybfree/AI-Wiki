---
title: MemDuet: Learning Dual-Process Memory for Long-Context Reasoning
url: http://arxiv.org/abs/2610.19928v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_10-16-13Z_MemDuet_LearningDual_ProcessMemoryforLong_ContextR.md
generated_at: 2026-10-14 21:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MemDuet introduces a dual-process memory framework inspired by Kahneman's System 1 and System 2 thinking model to address the accuracy-efficiency trade-off in long-context reasoning with recurrent memory agents. The system pairs a small language model for fast, parallel evidence selection from raw context chunks with a large language model for memory-update verification and sequential memory rewriting, trained through a three-stage pipeline. Experiments across three long-context benchmarks demonstrate a 9.74x end-to-end inference speedup and a 73.91% reduction in output tokens compared to the prior RL-MemAgent baseline, while maintaining competitive reasoning accuracy as context length grows.

## Key Takeaways
- MemDuet decomposes long-context reasoning into two coordinated subsystems: a lightweight System 1 model performs fast, parallel evidence selection across raw context chunks, while a heavier System 2 model handles memory-update verification and sequential memory rewriting in document order. This architectural split directly targets the core bottleneck of recurrent memory agents, where increasing context length forces a trade-off between reasoning quality and inference cost.
- The training pipeline is structured in three progressive stages: supervised fine-tuning of System 1 for evidence selection, Group Relative Policy Optimization (GRPO) of System 2 for verification and memory rewriting, and a final joint optimization stage that coordinates selection and updating policies together. This staged approach allows each subsystem to specialize before being harmonized for end-to-end long-context reasoning.
- On RULER-HQA, LongBench v2, and 2WikiMultiHopQA, MemDuet achieves an averaged 9.74x inference speedup and a 73.91% output-token reduction relative to RL-MemAgent, demonstrating that the dual-process design scales favorably with increasing context length rather than degrading, which is a critical property for practical deployment on very long documents.

## Context
Recurrent memory agents have emerged as a promising approach for reasoning over documents that exceed the context window of any single model call, but they suffer from compounding inference costs as documents grow longer. Prior systems such as RL-MemAgent treat memory selection and memory updating as a monolithic process, leading to redundant token generation and slow sequential processing. MemDuet draws on cognitive science, specifically Kahneman's dual-process theory, to restructure this pipeline into a fast heuristic layer and a slower deliberative layer, aligning the computational architecture with how humans actually process long texts. This positions the work at the intersection of efficient inference, reinforcement learning for language models, and scalable document understanding.

## Implications
For practitioners deploying long-context reasoning systems in production—such as legal document analysis, scientific literature review, or enterprise knowledge retrieval—MemDuet's near-tenfold speedup and substantial token reduction directly translate into lower latency, reduced API costs, and the ability to handle longer documents within existing hardware budgets. The three-stage training recipe, particularly the use of GRPO for the verification subsystem, offers a reproducible recipe that other teams can adapt to their own domain-specific long-document tasks. More broadly, the paper validates that architectural inspiration from cognitive dual-process theory can yield concrete engineering gains, suggesting that future memory-augmented systems should explicitly separate fast retrieval heuristics from slow deliberative verification rather than treating them as a single monolithic policy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19928v1)
