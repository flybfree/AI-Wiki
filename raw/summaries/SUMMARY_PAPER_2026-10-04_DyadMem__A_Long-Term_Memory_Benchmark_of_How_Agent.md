---
title: DyadMem: A Long-Term Memory Benchmark of How Agents Work with Users
url: http://arxiv.org/abs/2610.03020v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_08-57-43Z_DyadMem_ALong_TermMemoryBenchmarkofHowAgentsWorkwi.md
generated_at: 2026-10-04 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DyadMem introduces a novel benchmark called User-conditioned Relational Agent Memory (URAM) that evaluates not just what an agent knows about a user, but how the agent should behave within a specific user-agent relationship as shared history evolves. The benchmark spans 3,065 episodes, 50,961 sessions, and 61,210 QA instances across 6 memory categories, testing 20 models (16 open-weight and 4 proprietary). The central finding is that while models perform well when given gold memory annotations, their performance drops sharply in full-pipeline evaluation, revealing critical failures in memory capture, recall completeness, and safe deletion even among frontier LLMs.

## Key Takeaways
- DyadMem defines URAM as a new evaluation target distinct from user-fact or preference memory, focusing on relationship-specific agent behaviors that evolve across multi-session interactions. This fills a gap where existing benchmarks supervise only user-side facts or cross-user reusable experiences, leaving agent-side relational memory unmeasured.
- The benchmark provides dual-domain annotations including session-level Capture and Update gold labels, query-level Recall support, and two QA settings (Gold-Memory and Full-Pipeline). The consistent performance gap between these settings across all 20 tested models demonstrates that current agents fail at the operational pipeline of capturing, updating, and recalling relational memory even when they can reason well over provided context.
- Quantitative results expose three specific failure modes in frontier LLMs: low Capture recall (failing to store new relational information), incomplete Recall (failing to retrieve stored relational knowledge), and unsafe-deletion (incorrectly removing relationship-relevant memory). The URAM validation experiment confirmed positive effects across all 20 models, suggesting the benchmark design itself is effective at surfacing these gaps.

## Context
Long-term conversational agents and AI assistants increasingly operate over extended user interactions spanning days or weeks, making persistent memory a core capability rather than a peripheral feature. Prior benchmarks such as those measuring user preference recall or cross-user experience reuse have advanced the field but left a critical blind spot: the agent's own behavioral adaptation to a specific user's evolving relationship. DyadMem addresses this by formalizing URAM and providing the first large-scale, dual-domain annotation effort that jointly tracks user-side memory and agent-side relational memory along identical multi-session trajectories, enabling fine-grained pipeline evaluation rather than final-answer-only scoring.

## Implications
For practitioners building personalized AI assistants, customer-service bots, or collaborative agents, DyadMem reveals that current frontier models are not yet reliable at maintaining relationship-specific operational memory across long interactions, meaning deployment in production settings carries real risks of unsafe memory deletion or missed relational context. For the research community, the benchmark's full-pipeline evaluation design and its demonstration that Gold-Memory performance does not predict Full-Pipeline performance argue strongly against evaluating memory systems with final-answer QA alone, pushing the field toward granular, stage-by-stage memory assessment as a prerequisite for building trustworthy long-term agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03020v1)
