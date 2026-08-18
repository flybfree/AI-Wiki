---
title: CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills
url: http://arxiv.org/abs/2608.16246v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_08-20-44Z_CompoSkill_CompositionalSkillChainAttacksfromIndiv.md
generated_at: 2026-08-17 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CompoSkill, a framework that demonstrates how autonomous AI agents can be vulnerable to skill composition attacks even when individual skills pass safety scanners. It shows high risk chain formation rates in both white‑box and black‑box settings, up to 83.3% and 80.6%, respectively.

## Key Takeaways
- A skill may individually pass scanner checks yet create risky compositions that are path‑level hazards.
- The attacker constructs a Skill Composition Graph from top marketplace skills for a role profile, finding high‑risk chains without explicit skill IDs.
- Bridge‑skill benefits increase attack success but ASR drops after three hops due to decay.

## Context
Autonomous AI agents rely on certified marketplace skills for long‑horizon tasks, assuming each skill is safe in isolation. This paper reveals that this assumption breaks down when skills interact, exposing a gap in current safety verification methods.

## Implications
For developers and regulators, single‑skill certification is insufficient; new approaches must evaluate compositional risk. The findings urge industry to adopt holistic skill chain analysis before deploying autonomous agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16246v1)
