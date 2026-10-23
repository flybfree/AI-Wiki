---
title: Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences
url: http://arxiv.org/abs/2610.30485v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_22-08-49Z_WhyBotherMeAgain_BenchmarkingPersonalAgentMemoryfo.md
generated_at: 2026-10-22 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MemPABench, an interactive benchmark designed to evaluate how personal AI agents learn, retain, and act upon user interaction preferences—such as when to clarify, confirm, or act autonomously—rather than merely recalling factual information. The authors evaluate four memory systems (including Mem0, MemOS, simple RAG, and File-based memory) across four LLM backbones and find that current memory architectures deliver limited gains in preference-aware behavior, with retrieval-based systems failing to outperform a no-memory baseline and File-based memory over-applying preferences outside relevant contexts.

## Key Takeaways
- MemPABench is a novel on-policy evaluation environment featuring four grounded simulated users who hold 14 interaction preferences spanning work and personal contexts, with feedback collected across 99 sessions over four months and five event-driven preference changes per user to stress-test memory update capabilities. This design shifts benchmarking from static factual recall to dynamic, long-horizon decision-making about when an agent should ask, confirm, or act independently.
- Retrieval-based memory systems such as Mem0, MemOS, and simple RAG do not outperform a No Memory baseline in preference selection, indicating that current retrieval architectures struggle to identify and surface interaction preferences from conversational history. File-based memory improves preference accuracy but introduces a new failure mode: it applies stored preferences beyond the contexts where they are relevant, leading to inappropriate or over-generalized agent behavior.
- Even when the correct preference is available in memory, agents consistently fail to override their default interaction habits, revealing a fundamental gap between storing a preference and behaviorally adapting to it. This suggests that preference retrieval and preference application are distinct challenges, and current systems address neither adequately.

## Context
The broader AI landscape is rapidly moving toward personal agents that manage everyday tasks—scheduling, communication, reminders—across extended interactions. Existing memory benchmarks like LoCoMo or LongMemEval focus on factual recall and personalized Q&A, leaving a critical gap: no standard evaluation tests whether agents can learn and respect how users want to be assisted. MemPABench fills this gap by grounding evaluation in realistic, multi-session interaction patterns with preference drift, making it a necessary complement to the current benchmarking ecosystem for agent memory research.

## Implications
For practitioners building personal assistants, this work signals that simply adding a memory module to an LLM agent is insufficient; developers must design systems that can distinguish contextually appropriate preferences from over-generalized rules and that can update behavior when user preferences shift. For the research community, the finding that retrieval-based memory underperforms even a no-memory baseline challenges prevailing assumptions about RAG-based agent architectures and motivates new approaches to preference-aware memory design. Industry teams deploying personal agents should treat interaction preference management as a first-class engineering problem rather than an afterthought, since unaddressed preference mismatches directly translate into user frustration and perceived agent unreliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30485v1)
