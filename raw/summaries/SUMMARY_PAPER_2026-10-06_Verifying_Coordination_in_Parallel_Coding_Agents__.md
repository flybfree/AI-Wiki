---
title: Verifying Coordination in Parallel Coding Agents: NP-Bench and a Scheduling Planner
url: http://arxiv.org/abs/2610.07261v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_19-02-27Z_VerifyingCoordinationinParallelCodingAgents_NP_Ben.md
generated_at: 2026-10-06 21:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper addresses coordination failures in parallel coding-agent teams by reframing integration conflicts as a scheduling problem rather than a post-hoc warning problem. It introduces Nerveplane, a proactive planner that partitions declared work scopes and orders merges along producer-consumer dependencies, and evaluates it with NP-Bench, a three-arm benchmark that tests no coordination, reactive detection, and proactive planning against real git merges. The planner substantially improves clean integration and eliminates merge conflicts, while a cross-session memory reduces repeated mistakes.

## Key Takeaways
- Parallel coding agents can individually pass tests yet break the merged codebase because they collide on shared functions, contracts, or integration points; single-agent evaluation misses these team-level failures, so coordination must be evaluated at the level of merged outcomes.
- Reactive coordination tools often warn after agents have already made wasted edits, whereas proactive scheduling can prevent conflicts by taking each work item’s declared scope, partitioning work into disjoint scopes, and ordering merges along the producer-to-consumer graph before execution begins.
- NP-Bench shows measurable gains: clean integration rises from 1/9 to 9/9 scenarios, merge conflicts fall from 13 to 0, and on a live breaking contract change the planner rescues outcomes that both no-coordination and reactive baselines miss, with scope leakage at 0/5 and cross-session memory reducing repeated mistakes from 1.00 to 0.00.

## Context
This work matters because multi-agent coding systems are increasingly used to parallelize software development, but current evaluation often focuses on isolated agent competence rather than team integration. It connects agent orchestration, software engineering, and scheduling theory by treating coordination as an upfront allocation problem rather than a runtime monitoring problem.

## Implications
For practitioners, the results suggest that better planning, scope partitioning, and dependency-aware merge ordering can make parallel coding agents more reliable without relying solely on stronger models. For the field, the negative finding that routing facts does not rescue long-context accuracy at window-fitting scales shifts attention toward architectural coordination, cost, and capacity as the main sources of benefit.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07261v1)
