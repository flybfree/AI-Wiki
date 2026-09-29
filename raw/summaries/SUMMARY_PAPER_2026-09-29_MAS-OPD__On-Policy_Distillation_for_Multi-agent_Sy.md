---
title: MAS-OPD: On-Policy Distillation for Multi-agent Systems
url: http://arxiv.org/abs/2609.34234v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_03-39-32Z_MAS_OPD_On_PolicyDistillationforMulti_agentSystems.md
generated_at: 2026-09-29 02:14
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces MAS-OPD, a novel post-training framework designed to jointly optimize multi-agent systems through on-policy distillation. By addressing the challenges of role specialization and cross-agent coordination, the method enables student models to learn complementary expertise while maintaining shared foundational knowledge without relying on task-specific reward engineering or costly inference-time orchestration.

## Key Takeaways
- Traditional reinforcement learning approaches for multi-agent systems struggle with credit assignment due to team-level rewards or require extensive per-task redesign of local rewards, whereas MAS-OPD leverages token-level teacher supervision through on-policy distillation to provide denser training signals without reward engineering.
- The framework introduces Role-Advantage Specialization, which calculates the performance gap between target and non-target role conditions to foster complementary expertise while preserving universally needed knowledge across agents.
- To handle interdependent agent interactions, Privileged Attribution for Coordination identifies the source of collaborative conflicts and feeds this information exclusively to the

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34234v1)
