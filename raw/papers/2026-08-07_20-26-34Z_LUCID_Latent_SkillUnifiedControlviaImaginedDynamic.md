---
title: LUCID: Latent-Skill Unified Control via Imagined Dynamics for Long-Horizon Humanoid Loco-Manipulation
published: 2026-08-07T20:26:34Z
authors: Cheng Guo, Mingzhe Ni, Angelo Cangelosi, Arash Ajoudani
url: http://arxiv.org/abs/2608.07746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LUCID: Latent-Skill Unified Control via Imagined Dynamics for Long-Horizon Humanoid Loco-Manipulation

## Abstract
Long-horizon humanoid loco-manipulation requires composing versatile whole-body skills and reliable high-level decision making. Existing methods often coordinate pretrained skills with scripted planners, finite-state machines or task-specific model-free policies, restricting their ability to handle complex task sequences. To address this limitation, we propose \textbf{LUCID}, a hierarchical model-based reinforcement learning framework that plans over reusable skills through imagined rollouts of a learned dynamics model. LUCID first trains a structured latent-conditioned low-level policy via adversarial imitation and then freezes it while jointly learning a high-level policy and macro-dynamics world model. The world model predicts the temporally extended state transitions induced by latent decisions, enabling high-level policy optimization through imagined rollouts. We evaluate our framework across various simulated multi-object rearrangement scenarios. Experimental results show that LUCID improves the full-task success and partial-completion rates compared to prior baseline methods, demonstrating its effectiveness in complex sequential loco-manipulation tasks.

## Metadata
- **Published**: 2026-08-07T20:26:34Z
- **Authors**: Cheng Guo, Mingzhe Ni, Angelo Cangelosi, Arash Ajoudani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07746v1)