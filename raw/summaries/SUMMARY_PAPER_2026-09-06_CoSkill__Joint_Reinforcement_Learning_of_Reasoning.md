---
title: CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution
url: http://arxiv.org/abs/2609.04865v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_08-25-30Z_CoSkill_JointReinforcementLearningofReasoningandMe.md
generated_at: 2026-09-06 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoSkill, a joint reinforcement learning framework that unifies reasoning and meta‑skill agents within a hierarchical skill library. By treating the static meta‑skill workflow as a learnable agent, CoSkill enables end‑to‑end co‑adaptation between the reasoning agent and its child step skills, achieving significantly higher success rates than prior methods.

## Key Takeaways
- The framework decouples skill evolution from policy optimization by jointly training a Reasoning Agent that selects task and step skills with a Meta‑Skill Agent that refines them.  
- Experiments on ALFWorld and WebShop demonstrate superior early‑stage sample efficiency, asymptotic performance, and wall‑clock efficiency compared to baseline RL and skill‑based approaches.  
- The unified model allows the Reasoning Agent’s actions to condition on retrieved skills while simultaneously guiding the Meta‑Skill Agent’s updates.

## Context
Current skill libraries in reinforcement learning often treat skills as static resources that are managed separately from policy learning, limiting flexibility and sample efficiency. This paper addresses those limitations by integrating skill selection and adaptation into a single joint training objective.

## Implications
For practitioners, CoSkill offers a practical path to more efficient AI agents that can evolve their capabilities autonomously. In industry, the approach could reduce development time for complex tasks requiring multiple procedural steps, leading to faster deployment and lower computational costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04865v1)
