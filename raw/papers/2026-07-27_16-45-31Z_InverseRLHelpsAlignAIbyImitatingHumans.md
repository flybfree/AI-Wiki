---
title: Inverse RL Helps Align AI by Imitating Humans
published: 2026-07-27T16:45:31Z
authors: Michał Wiliński, Liu Leqi, Chirag Nagpal
url: http://arxiv.org/abs/2607.24900v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inverse RL Helps Align AI by Imitating Humans

## Abstract
Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following. Current approaches typically use supervised fine-tuning on demonstrations or reinforcement learning with rewards derived from verifiers or human feedback. These paradigms leave an important question underexplored: can demonstrations alone yield an implicit reward that can be inspected, reused, and optimized on-policy to align AI? Motivated by inverse reinforcement learning, we introduce Projected Alignment Reward Estimated from Demonstrations (PARED). PARED recovers the implicit reward underlying expert demonstrations as an explicit function over a small set of response-level features, learned by a lightweight discriminator that separates demonstrations from the policy's own samples in this feature space. Unlike a standard reward model, PARED requires no task-specific preference annotations: demonstrations provide the task-specific supervision, which can be augmented with AI feedback as additional dimensions of supervision. Through experiments involving inference-time reranking and adversarial on-policy RL, we show that the recovered reward improves a base policy without a supervised loss and yields further gains when optimized after standard supervised fine-tuning. Additionally, we demonstrate that PARED can be used for contextual alignment, in which a single policy can be tailored to the preferences of different audiences.

## Metadata
- **Published**: 2026-07-27T16:45:31Z
- **Authors**: Michał Wiliński, Liu Leqi, Chirag Nagpal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24900v1)