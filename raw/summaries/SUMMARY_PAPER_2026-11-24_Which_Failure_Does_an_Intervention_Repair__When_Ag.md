---
title: Which Failure Does an Intervention Repair? When Agent Interventions Help, and Where Self-Evolving Skills Stall
url: http://arxiv.org/abs/2611.29290v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-22_07-25-04Z_WhichFailureDoesanInterventionRepair_WhenAgentInte.md
generated_at: 2026-11-24 22:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the common practice of evaluating agent interventions—such as skills, harnesses, and inference budgets—as if they produce a single average improvement across all settings. Through a large-scale matched factorial study spanning nine benchmarks, four models, four skill conditions, four harness levels, and three inference budgets (nearly 0.9 million trajectories), the authors demonstrate that interventions interact rather than simply add, that no configuration is universally best, and that the specific failure mode of the current system determines which intervention actually repairs it. They further show that self-evolving skills derived from an agent's own experience hit a fundamental bottleneck and cannot substitute for externally supplied knowledge.

## Key Takeaways
- Interventions interact rather than compose additively: a harness can absorb a skill's gain, rescue a failure the skill introduces, or leave the gain intact, meaning stacking stronger components does not guarantee cumulative improvement. The failure left by the current system points to the fix—missing knowledge requires a stronger model, while execution errors require a richer harness—making diagnosis of the specific failure mode a prerequisite for choosing an intervention.
- Self-evolving skills that agents generate from their own experience hit a hard ceiling: they rarely outperform a short human-written skill, tend to learn dataset-specific shortcuts rather than generalizable procedures, break when transferred to a different model, and fundamentally cannot supply missing factual knowledge that only external information can provide. Feedback loops alone are not recovery; a matched recovery mechanism repairs mainly failures that leave a visible error signal.
- A benchmark-level model-selection switch guided by a small 20-task labeled pilot achieves both higher performance and lower cost than uniformly deploying the strongest model, suggesting that targeted, task-aware routing outperforms blanket upgrades and that intervention evaluation must be configuration-specific rather than averaged.

## Context
The broader AI-agent research landscape has increasingly treated interventions like tool-use harnesses, prompt skills, and extended reasoning budgets as universally beneficial add-ons, reporting a single aggregate score improvement. This paper directly confronts that assumption by showing that the interaction structure between models, skills, and harnesses is highly configuration-dependent, and that the popular paradigm of self-improving or self-evolving agent skills has structural limits that no amount of internal feedback can overcome. It matters because it reframes how the community should design, evaluate, and deploy agent systems in practice.

## Implications
For practitioners building agentic systems, the findings argue against one-size-fits-all upgrades and in favor of failure-diagnosis-driven intervention selection: identify what the current system actually gets wrong before choosing whether to add a skill, a harness, a stronger model, or more compute. For the industry, the 20-task pilot routing result offers a concrete, low-cost strategy for model selection that outperforms always using the largest model, which has direct cost and deployment consequences. For researchers, the paper sets a methodological standard—matched factorial designs with hundreds of thousands of trajectories—that future agent-evaluation work should adopt to avoid misleading average-gain claims.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.29290v1)
