---
title: A GHOST in Long-Horizon Agents: Governance Hazard from Overlooked Safety Constraints across Turns
url: http://arxiv.org/abs/2610.02664v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_01-33-04Z_AGHOSTinLong_HorizonAgents_GovernanceHazardfromOve.md
generated_at: 2026-10-04 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies and formalizes a previously underexplored safety failure mode in long-horizon AI agents, termed GHOST (Governance Hazard from Overlooked Safety Constraints across Turns), where an agent violates a safety constraint that was specified many interaction turns earlier, even under benign conditions. The authors demonstrate that this failure occurs at an 11.5% rate on GPT-5.5, provide a theoretical proof that such hazards accumulate almost surely under certain conditions, and propose STAR-Guard, a two-layer defense mechanism that eliminates all observed GHOST events in their experiments.

## Key Takeaways
- GHOST events are not rare edge cases but a systematic failure mode: under benign interaction conditions, GPT-5.5 exhibits an 11.5% occurrence rate of violating safety constraints specified many turns earlier, indicating that extended interaction history itself introduces a structural execution-safety vulnerability that can cause irreversible damage to the environment or user.
- The authors provide a theoretical guarantee showing that if the residual conditional violation hazard along each safe prefix is bounded below by a non-summable sequence, the agent's execution enters the hazard region almost surely, meaning that without intervention, repeated interactions make safety violations statistically inevitable rather than merely possible.
- STAR-Guard addresses this through a two-layer architecture: the first layer restores applicable historical semantic safety constraints to reduce unsafe action proposals, while the second layer performs a deterministic pre-execution audit that prevents any residual violations from reaching the environment. Under the GPT-5.5 setup, this combined approach yielded zero GHOST events in experiments.

## Context
As long-horizon agents increasingly handle complex, multi-turn problem-solving tasks such as code generation, planning, and tool use, their extended interaction histories create a growing surface area for safety constraint drift. Prior safety research has largely focused on single-turn alignment or prompt-level guardrails, leaving the cross-turn governance of constraints as a significant gap. This paper fills that gap by naming the failure mode, quantifying its prevalence, and grounding it in formal probability theory, thereby elevating it from anecdotal observation to a rigorously characterized risk class.

## Implications
For practitioners deploying long-horizon agents in production, this work signals that safety constraints specified early in a conversation cannot be assumed to persist through dozens or hundreds of turns without active enforcement mechanisms. The STAR-Guard framework offers a concrete, implementable defense pattern—combining constraint restoration with deterministic auditing—that agent developers and safety teams can integrate into orchestration pipelines. More broadly, the theoretical result that hazards accumulate almost surely under mild conditions suggests that passive safety monitoring is insufficient for long-horizon deployments, and that proactive, turn-aware governance layers will become a necessary component of safe agent architectures across industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02664v1)
