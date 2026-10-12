---
title: MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents
url: http://arxiv.org/abs/2610.13829v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_16-37-39Z_MC_EvoBench_AuditingExperience_DrivenSelf_Improvem.md
generated_at: 2026-10-11 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MC-EvoBench introduces a rigorously controlled Minecraft benchmark designed to audit whether embodied agents genuinely acquire durable, transferable capabilities from prior experience rather than merely carrying over resources or benefiting from unequal exposure. The benchmark constructs 19 registered evolution chains with graph-aligned probe families and evaluates agents under matched step budgets across multiple seeds, revealing that related experience does not produce stable capability transfer and that early-stage execution bottlenecks often mask whether later capabilities were truly learned.

## Key Takeaways
- The benchmark enforces strict separation between capability change and confounding factors: the target world is fully reset, only a declared agent artifact is permitted to cross the source-target boundary, and matched environment-step budgets with five seeds are enforced across no-prior, related, unrelated, and shuffled source conditions. This design prevents inflated transfer claims that could arise from carried-over inventory, unequal source-task exposure, or early execution failures that never reach later stages.
- Empirical results show a consistent direct-capability gap between controller-backed and planner-backed agent variants, but related experience yields no stable transfer improvement. The only observed gain in a wood-species probe hinges on a single seed, and all reported confidence intervals include zero, indicating that the apparent benefit is statistically indistinguishable from noise.
- Stage-level audits reveal that early bottlenecks in wood collection and crafting frequently prevent agents from ever reaching later capability stages, meaning that apparent failures to demonstrate transfer may actually reflect unobserved capability rather than genuine absence of learning. This highlights a critical evaluation blind spot in current self-improvement benchmarks.

## Context
Recursive self-improvement in embodied agents is a frontier problem in AI research, with applications spanning robotics, game-playing agents, and autonomous systems that must learn from accumulated interaction history. Prior benchmarks often conflate resource carryover, task familiarity, and genuine skill acquisition, making it difficult to determine whether an agent has truly improved its underlying capabilities. MC-EvoBench addresses this gap by formalizing tasks as state graphs with stage-level verifiers and enforcing experimental controls that isolate capability transfer from environmental confounds, providing a methodological template applicable beyond Minecraft to any embodied learning setting.

## Implications
For researchers building self-improving agents, MC-EvoBench demonstrates that naive transfer evaluation can produce misleadingly positive results driven by seed variance or early-stage resource advantages, and that rigorous stage-level auditing is essential before claiming durable capability gains. For practitioners deploying autonomous agents in production environments, the findings caution against assuming that accumulated experience automatically translates into improved performance on new tasks, underscoring the need for controlled evaluation pipelines before scaling agent systems. The open-source code and benchmark data provide a reusable testbed for validating future agent architectures against these stricter transfer criteria.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13829v1)
