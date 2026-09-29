---
title: CodeSkill: Latent Skill Abstraction for Long-Horizon Code Agents
published: 2026-09-27T05:29:35Z
authors: Song-Li Wu, Jingyi Wang, Zhaocheng Du, Weinan Gan, Weiwen Liu
url: http://arxiv.org/abs/2609.33243v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CodeSkill: Latent Skill Abstraction for Long-Horizon Code Agents

## Abstract
Code agents require long-horizon decision-making over complex interaction trajectories. However, existing reinforcement learning (RL) approaches typically optimize behavior at the token level, creating a mismatch between low-level generation and high-level behavioral reasoning. This limitation leads to inefficient exploration and weak credit assignment under sparse rewards. Moreover, while large-scale agent trajectories often contain recurring multi-step behavioral patterns, their noisy token-level representations hinder effective experience reuse. To address these challenges, we propose CodeSkill, a framework that adapts hierarchical latent skill modeling to the code agent domain. CodeSkill first leverages a teacher model to distill both successful and failed trajectories into multi-level textual abstractions. It then integrates temporal variational inference with reinforcement learning to map these discrete semantics into continuous latent variables, while an adaptive boundary mechanism dynamically gates skill transitions based on execution feedback. The learned skills are injected into a frozen LLM policy as latent semantic prefixes, enabling optimization in a compact semantic space rather than over raw token sequences. By shifting RL from token-level exploration to experience-level reasoning, CodeSkill improves optimization efficiency and long-horizon behavioral coherence. Extensive experiments demonstrate that CodeSkill achieves highly competitive performance against strong open-weight baselines across diverse general and industrial coding benchmarks. Furthermore, the learned skills exhibit strong transferability and robust cross-domain generalization, highlighting the effectiveness of explicit behavioral abstraction for scalable agentic code generation.

## Metadata
- **Published**: 2026-09-27T05:29:35Z
- **Authors**: Song-Li Wu, Jingyi Wang, Zhaocheng Du, Weinan Gan, Weiwen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33243v1)