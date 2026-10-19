---
title: Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them
url: http://arxiv.org/abs/2610.22984v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_06-10-01Z_Self_EvolvingAgentsCanRepairFailuresbutStruggletoG.md
generated_at: 2026-10-18 20:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether LLM-based agents can self-evolve using only failed interactions, a setting the authors term Cold-Start Failure-Only Evolution (CFOE). Through experiments spanning three self-evolving paradigms, multiple LLM backbones, and four interactive environments, the authors identify a consistent "repair-generalization gap": agents can repair tasks they previously failed but cannot build transferable capabilities from those failures. The study demonstrates that failure-derived experience is fundamentally insufficient for generalizable learning without additional signals such as verifier feedback or successful trajectories.

## Key Takeaways
- Agents can repair previously failed tasks using failure-derived experience, but this repair capability does not translate into sustained improvements on unseen tasks. The authors term this the "repair-generalization gap," showing it holds consistently across multiple paradigms, model backbones, and interactive environments, suggesting it is a structural limitation rather than a method-specific artifact.
- Agents frequently misinterpret the causes of their own failures, which undermines the quality of the experience they extract. Even when failures are correctly diagnosed, the resulting experience remains difficult to transfer to new task contexts, indicating that failure signals are inherently noisy and context-bound for learning purposes.
- Relaxing the strict CFOE constraint reveals that verifier feedback and additional interaction attempts provide only limited gains, whereas incorporating successful trajectories substantially improves transfer performance. This suggests that positive anchors—successful examples or external evaluation signals—are critical for building generalizable capabilities, and that failure-only learning is a fundamentally weaker learning signal.

## Context
Self-evolving agents represent a major frontier in LLM research, promising continual improvement through interaction without human supervision. Most existing self-evolution methods implicitly depend on successful trajectories or external evaluation signals as learning anchors. This paper addresses a foundational gap in the literature by isolating what happens when those positive anchors are entirely removed, testing whether agents can bootstrap improvement purely from their own mistakes. The findings challenge optimistic assumptions about autonomous agent learning and clarify the boundary between repair and generalization in experience-driven evolution.

## Implications
For practitioners building autonomous agents in production, this work signals that purely failure-driven learning loops will not yield robust generalization and should be supplemented with curated successful examples, verifier feedback, or structured evaluation. For the research community, the repair-generalization gap highlights a critical open problem: designing self-evolution mechanisms that extract transferable knowledge from failures rather than merely patching specific task instances. Industry deployments of self-improving agents in robotics, software engineering, and customer service should treat failure-only learning as a repair mechanism, not a general capability-building strategy, and invest in hybrid pipelines that combine failure analysis with successful-trajectory distillation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22984v1)
