---
title: Q-Steer: Action-Value Guidance for Molecular Policy Optimization
published: 2026-07-29T01:53:14Z
authors: Xinyu Wang, Jinbo Bi, Minghu Song
url: http://arxiv.org/abs/2607.26391v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Q-Steer: Action-Value Guidance for Molecular Policy Optimization

## Abstract
Oracle-limited molecular optimization gives reward only after a complete molecule is generated, while each rollout requires many local next-token decisions. This delayed-feedback interface makes molecular policy optimization myopic: an optimizer can learn that a molecule was good without knowing which intermediate actions made it good. We introduce Q-Steer, a rollout-time action-value steering primitive for molecular language models. Q-Steer uses an offline-trained and frozen prefix-action value scorer, PAVS-Q, that estimates the downstream reward of taking a candidate next token under a partial SMILES prefix, then adds a normalized value bonus to sampling logits. The optimizer update rule and online oracle budget are unchanged; the claim is fixed-online-oracle performance, not equal total compute. On PMO23 with a fixed 10,000-call online budget, complete factorial studies across two molecular language-model backbones and four optimizers show that Q-Steer improves mean valid-unique score in all eight backbone-optimizer cells, with positive macro mean-score gains between +0.033 and +0.049 and 18-20 task wins per cell. Mechanism controls show that action identity matters: prefix-broadcast values are nearly neutral, while shuffled action values harm performance. These results support Q-Steer as a reusable rollout-time action-value wrapper that improves average molecular optimization reward across optimizer families and policy backbones without changing the online oracle budget.

## Metadata
- **Published**: 2026-07-29T01:53:14Z
- **Authors**: Xinyu Wang, Jinbo Bi, Minghu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26391v1)