---
title: When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems
url: http://arxiv.org/abs/2608.05563v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_03-32-43Z_WhenExperienceBecomesInstruction_TrajectoryPoisoni.md
generated_at: 2026-08-06 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PoisonedEvolution, a trajectory‑poisoning attack that manipulates self‑evolving skill systems by feeding bounded evidence to embed attacker‑defined behaviors into trusted skills. Experiments show the attack succeeds in 91 % of trials on six mainstream LLM evolvers and 62 % on Trace2Skill, highlighting how skill promotion can be compromised even with limited support.

## Key Takeaways
- The attack relies on three stages—Inclusion, Evolution Attribution, and Realization—where attribution is the bottleneck that must be satisfied for a behavior to become a permanent skill.  
- At 10 % attacker support, PoisonedEvolution embeds target behaviors in 546 out of 600 trials across six evolvers, achieving a SER of 91 %.  
- Three consistent attacker records can influence a 30‑record batch, while a single record is much weaker, indicating the importance of repeated evidence.

## Context
Self‑evolving skill systems aim to turn untrusted agent experiences into reliable instruction, but they depend on opaque promotion mechanisms that are vulnerable to subtle attacks. This work demonstrates that even when attackers cannot edit private pools or evolution logic, they can still influence outcomes by shaping visible evidence.

## Implications
The findings reveal that security boundaries must be examined beyond code integrity, focusing instead on the trustworthiness of skill promotion processes. Practitioners should design robust attribution checks and limit reliance on single‑record evidence to mitigate exploitation in self‑evolving AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05563v1)
