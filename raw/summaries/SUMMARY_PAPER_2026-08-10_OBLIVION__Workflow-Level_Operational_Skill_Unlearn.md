---
title: OBLIVION: Workflow-Level Operational Skill Unlearning for Deployed Agents
url: http://arxiv.org/abs/2608.08264v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_17-51-51Z_OBLIVION_Workflow_LevelOperationalSkillUnlearningf.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper OBLIVION addresses the problem of operational skill unlearning in deployed language model agents, where revoked skills can be reconstructed from residual carriers. It introduces a benchmark and defense harness that models skill attacks as source-to-sink workflows and applies cross-surface erasure to reduce resurrection chances. Experiments show defenses lower attack success rates dramatically while preserving utility.

## Key Takeaways
- The no-defense arm achieves a formal attack success rate of 1.0, indicating that without intervention agents can fully reconstruct revoked skills.
- OBLIVION reduces the attack success rate to 0.114 and impact-weighted exposure to 0.115 while maintaining locked utility at 1.0 and benign block rate at 0.
- In a separate sandbox, OBLIVION cuts attack success from 1.0 to 0.2 and impact-weighted exposure from 1.0 to 0.213 without affecting any utility controls.

## Context
This work matters because as AI agents interact with external systems they inherit skills that can be revoked, yet traditional parameter-level forgetting does not stop skill resurrection through primitive tools. The study highlights a gap between registry management and operational resilience.

## Implications
For practitioners, OBLIVION demonstrates the need for workflow-level evaluation beyond checking explicit skill entries to ensure deployed agents cannot rebuild revoked capabilities. It suggests that defenses should target residual carriers in real-world workflows rather than just model parameters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08264v1)
