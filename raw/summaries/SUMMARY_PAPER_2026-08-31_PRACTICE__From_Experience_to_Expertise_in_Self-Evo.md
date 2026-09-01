---
title: PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents
url: http://arxiv.org/abs/2608.30760v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_13-26-16Z_PRACTICE_FromExperiencetoExpertiseinSelf_EvolvingE.md
generated_at: 2026-08-31 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PRACTICE, a framework that trains a skill learner to continuously discover and maintain a persistent library of skills from interaction trajectories while the task executor remains frozen. Experiments on EB‑ALFRED and EB‑Habitat show that the compact skill learner delivers consistent performance improvements across successive library‑update rounds, outperforming existing experience‑based baselines.

## Key Takeaways
- The learner first generates basic skills directly from oracle trajectories, establishing a reliable foundation for skill discovery.
- It then contrasts successful and failed trajectories to identify invalid action patterns and develop recovery strategies that guide future updates.
- Finally, it employs online skill‑edit distillation aligned with a stronger teacher to refine the current edit distribution and boost policy performance.

## Context
Multimodal large language models are increasingly used as embodied agents that translate language instructions into actions. While experience‑based methods aim to let agents improve from past interactions, they often depend on manually designed prompting workflows that cannot adapt quickly to new or diverse experiences, limiting their scalability and robustness in dynamic environments.

## Implications
PRACTICE demonstrates a path toward self‑evolving agents that can autonomously maintain and refine their skill sets without human intervention. This reduces reliance on static prompting pipelines and enables scalable, continuous improvement across multiple frozen executors, offering practical benefits for industry applications requiring persistent performance gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30760v1)
