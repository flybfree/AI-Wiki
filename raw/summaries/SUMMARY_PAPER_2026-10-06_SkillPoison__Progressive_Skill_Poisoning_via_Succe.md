---
title: SkillPoison: Progressive Skill Poisoning via Successful Experiences
url: http://arxiv.org/abs/2610.07645v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_02-38-36Z_SkillPoison_ProgressiveSkillPoisoningviaSuccessful.md
generated_at: 2026-10-06 21:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillPoison investigates a subtle poisoning threat in self-improving LLM agents that learn reusable skills from successful experiences. Instead of injecting obviously malicious trajectories or false facts, the authors show that verified task-correct experiences can be shaped to make a skill extractor generalize a useful behavior too broadly. Across three benchmarks, this progressive poisoning reaches a 95.71 percent attack success rate while the injected experiences remain correct and pass verification and lexical inspection.

## Key Takeaways
- Existing skill attacks often corrupt individual experiences or extracted skills by adding malicious triggers, behaviors, or false facts, but these methods are easier to detect and may not persist as reusable skills. SkillPoison changes the threat model by poisoning the generalization process rather than the visible content of a trajectory.
- The framework first constructs successful experiences that reinforce a target behavior and then removes contextual conditions that normally constrain when that behavior should apply. This causes the skill extractor to learn a broad rule that appears beneficial in verified examples but becomes harmful when misapplied in new contexts.
- The attack is stealthy because every injected experience remains task-correct and can pass verification and lexical inspection. The resulting high attack success rate, 95.71 percent across three benchmarks, shows that successful-experience pipelines can be compromised without any individual trajectory being malicious.

## Context
Self-improving agents increasingly rely on experience distillation, where successful interactions are converted into persistent skills for future tasks. This creates a new attack surface because even if each experience is verified as correct, the extraction and generalization stage can turn benign examples into unsafe reusable procedures. The paper matters because it exposes a gap between task-level verification and skill-level safety in agentic systems.

## Implications
For practitioners, SkillPoison suggests that defenses focused only on detecting malicious trajectories, false facts, or lexical anomalies are insufficient for skill-learning pipelines. Industry deployments of autonomous agents need safeguards that monitor how extracted skills generalize, including constraints on applicability, provenance, and context-dependent activation. The work also motivates benchmarking and auditing of skill extraction itself, not just the raw experiences fed into it.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07645v1)
