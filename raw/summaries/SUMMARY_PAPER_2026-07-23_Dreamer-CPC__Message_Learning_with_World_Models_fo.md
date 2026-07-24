---
title: Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning
url: http://arxiv.org/abs/2607.19809v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_06-42-03Z_Dreamer_CPC_MessageLearningwithWorldModelsforDecen.md
generated_at: 2026-07-23 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Dreamer-CPC, a decentralized model‑based multi‑agent reinforcement learning method that learns messages from the latent dynamics of each agent’s world model. It integrates Collective Predictive Coding to generate and exchange history‑aware messages. In two test environments it outperforms IPPO‑CPC and communication baselines.

## Key Takeaways
- Dreamer-CPC uses a world model per agent to infer latent states that encode past observations and actions, enabling message learning beyond current inputs.
- The method integrates Collective Predictive Coding to produce messages grounded in these latent dynamics rather than only on present observations.
- In CatchApple, Dreamer-CPC achieves 4‑5 times higher episode returns than IPPO-CPC, showing strong coordination when observations are missing.

## Context
Message‑learning frameworks aim to reduce communication overhead while preserving information. Dreamer-CPC extends this by embedding message generation within a model that predicts future states, offering a principled way to handle partial observability in decentralized settings.

## Implications
This work provides a template for integrating predictive coding into model‑based MARL, potentially improving performance on tasks with intermittent or noisy observations. Practitioners can adopt similar latent‑state communication modules to enhance coordination without central control.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19809v1)
