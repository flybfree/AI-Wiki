---
title: A^2Agent: Action-Aware Reinforcement Learning for Repository-Level Code Localization Agents
url: http://arxiv.org/abs/2608.29831v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_14-53-35Z_A_2Agent_Action_AwareReinforcementLearningforRepos.md
generated_at: 2026-08-31 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces A^2Agent, an action-aware reinforcement learning framework that improves code region localization by rewarding both discovery and commitment of gold regions. Experiments on SWE-Bench Verified and Pro show gains of 1.58% and 8.55% in average F1 over state-of-the-art methods, with the model outperforming larger baselines up to eightfold.

## Key Takeaways
- The method rewards both discovering gold code regions and committing them, unlike prior approaches that only reward discovery.
- It uses an action-level advantage estimation scheme that groups turns sharing the same exploration context to isolate each action's credit.
- On SWE-Bench Verified the F1 improves by 1.58% and on Pro it improves by 8.55%, while the 4B model beats larger baselines up to eight times.

## Context
Code localization is a core challenge in automated software engineering, where agents must pinpoint relevant lines within large repositories. Existing reinforcement learning approaches often fail because they rely on sparse trajectory signals and cannot commit discovered regions, limiting practical deployment.

## Implications
This work demonstrates that action-aware RL can significantly boost performance without requiring massive model sizes, offering a scalable solution for real-world codebase analysis. Practitioners can adopt A^2Agent to achieve higher accuracy in issue detection while maintaining efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29831v1)
