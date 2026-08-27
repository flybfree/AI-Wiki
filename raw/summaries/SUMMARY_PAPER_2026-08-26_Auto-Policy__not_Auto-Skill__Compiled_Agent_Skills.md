---
title: Auto-Policy, not Auto-Skill: Compiled Agent Skills for the Physical World
url: http://arxiv.org/abs/2608.25091v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_19-40-50Z_Auto_Policy_notAuto_Skill_CompiledAgentSkillsforth.md
generated_at: 2026-08-26 20:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Edge Skillguard, a typed authority layer that resides within high‑risk skill artifacts to prevent malicious or misused skills from causing physical harm. Experiments on a live edge control plane show the guards reject 60 out of 60 borrowed‑authority requests across five attack variants while leaving benign actions untouched, and these results scale to 5× size and multiple hosts in a Tailscale mesh.

## Key Takeaways
- Skills describe how an agent should behave, but the policy decides which behavior becomes an action; the skill format provides no typed mechanism for rejecting permission claims.  
- Borrowed authority enables malicious skills to drive physical actuation by attaching unchecked permissions between agents.  
- Edge Skillguard adds a machine‑checkable guard over world state and sensor evidence inside each skill, achieving 60/60 rejection across attacks without blocking legitimate use.

## Context
Self‑evolving agent systems such as AutoSkills and Hermes Agent generate advisory orchestration automatically, yet their reported benefits focus on efficiency rather than safety. This gap is critical because a single unsafe skill invocation can unlock doors or move money, raising real‑world risk. The paper situates this issue within the broader AI field where formal verification of high‑risk actions remains underdeveloped.

## Implications
For industry and practitioners, embedding typed policy checks directly into skills makes physical actuation depend on verifiable evidence rather than peer‑agent claims, reducing reliance on ad‑hoc workflow engines. This approach encourages safer design of autonomous robots and other high‑impact agents, fostering trust in AI systems that interact with the physical world.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25091v1)
