---
title: Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants
url: http://arxiv.org/abs/2610.20022v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_11-33-40Z_MemorizingWho_KnowingHow_BenchmarkingPersonalandPr.md
generated_at: 2026-10-14 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PraxisMemBench, a benchmark designed to evaluate how persistent personal assistants handle the intertwined demands of personal memory (knowing who the user is) and procedural memory (knowing how to act on their behalf). The authors demonstrate that treating these two memory types as independent systems leads to significant performance degradation, and they propose PraxisMem, a memory management framework that jointly supervises both memory content and its organizational structure, achieving a 40.78% Session Success Rate compared to 20.60% for Claude Code's native memory system.

## Key Takeaways
- Separating personal and procedural memory maintenance is insufficient for persistent assistants. The benchmark shows task completion drops from 84.6% under single-type dependencies to 77.9% when tasks require interdependent personal and procedural knowledge, revealing that real-world assistance tasks inherently couple "who" information with "how" procedures in ways that isolated memory systems cannot capture.
- Relation-related failures grow as interaction history accumulates, increasing from 59.8% in early sessions to 72.9% in later sessions. This exposes a continual-maintenance challenge: even if a memory system writes correct memories initially, it fails to preserve evolving content and organizational structure needed for later retrieval, meaning static memory writing strategies degrade over extended use.
- PraxisMem addresses these failures through privileged joint-state supervision that trains the memory manager to internalize both content maintenance and organizational upkeep, combined with location-aware GRPO and dynamic residual-routed OPSD techniques. This approach nearly doubles the Session Success Rate over Claude Code's native memory, suggesting that joint-state training is critical for handling the co-evolution of personal and procedural knowledge.

## Context
Persistent personal assistants, such as those embedded in coding harnesses or daily-life task managers, are increasingly expected to remember user preferences, habits, and workflows over extended interactions. Most existing memory benchmarks evaluate either factual recall about a user or procedural skill retrieval in isolation, leaving the interaction between these two memory types largely unexplored. PraxisMemBench fills this gap by constructing daily-life and work trajectories where later tasks depend on both personal context and procedural procedures evolving together, reflecting the realistic coupling found in harness-based assistance settings.

## Implications
For practitioners building long-running assistant systems, this work signals that memory architectures must treat personal and procedural knowledge as a jointly evolving state rather than as separate retrieval targets. The finding that failures compound over sessions warns that current memory systems may appear adequate in short interactions yet degrade substantially in production deployments with growing history. For the broader AI research community, the joint-state supervision approach and the benchmark itself provide a concrete evaluation framework and training methodology that could guide the next generation of memory-augmented agents toward genuinely persistent, user-conditioned assistance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20022v1)
