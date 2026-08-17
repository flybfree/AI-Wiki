---
title: AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning
url: http://arxiv.org/abs/2608.14135v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_09-41-16Z_AgilePE_AutonomousUAVPursuit_EvasionviaSelf_PlayRe.md
generated_at: 2026-08-16 21:59
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AgilePE, a self-play reinforcement learning framework for autonomous UAV pursuit-evasion that directly maps onboard state to collective thrust and body rates commands. It achieves end-to-end agile maneuvering without intermediate planners. Real-world deployment is demonstrated with zero-shot transfer to quadrotors.

## Key Takeaways
- The policy learns CTBR commands directly from state observations enabling rapid, coordinated maneuvers.
- Competitive self-play with PFSP stabilizes optimization and reduces policy oscillation while improving strategies against diverse opponents.
- Hardware-aligned simulation enables zero-shot transfer to real quadrotors without task-specific tuning.

## Context
Autonomous aerial combat remains a challenge due to high-dimensional dynamics and rapid opponent changes. Traditional methods often require complex planners that cannot adapt quickly enough. This work demonstrates how reinforcement learning can replace such planners with lightweight, reactive policies.

## Implications
The approach offers a scalable solution for swarm coordination where each agent must act autonomously yet collaboratively. Practitioners can deploy UAVs in real combat scenarios without extensive offline tuning. The method also highlights the importance of simulation fidelity for safe transfer to physical systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14135v1)
