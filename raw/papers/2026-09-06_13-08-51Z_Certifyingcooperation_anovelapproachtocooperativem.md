---
title: Certifying cooperation: a novel approach to cooperative multi-agent task generation
published: 2026-09-06T13:08:51Z
authors: Yannick Molinghen, Hugo Charels, Tom Lenaerts
url: http://arxiv.org/abs/2609.06586v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Certifying cooperation: a novel approach to cooperative multi-agent task generation

## Abstract
A shared reward gives agents a common objective, but leaves open when, how and even whether they must cooperate to succeed. We address these questions in the Laser Learning Environment, a multi-agent path-finding environment where cooperation materializes as one agent blocking a laser to let a teammate pass safely. We represent these interactions through temporal cooperation graphs whose timed edges connect helpers to beneficiaries, define six cooperation profiles as overlapping graph predicates, and prove that every cooperative trajectory satisfies at least one. By encoding the environment dynamics and profile predicates as propositional formulae, we distinguish tasks that admit}a profile in some winning trajectory from those that require it in every winning trajectory within a specified horizon. Used as filters, these queries turn a random layout sampler into a generator of tasks with certified cooperation requirements. Experiments with five multi-agent reinforcement learning algorithms show that training diversity improves joint success on unseen tasks when cooperation-free solutions exist. When cooperation is required, greater diversity improves individual-agent exits, but joint success remains near zero. Across five profile-certified pools, final exit rates averaged over algorithms separate the pools into four statistically distinguishable levels but this ordering primarily reflects partial completion: policies collect rewards for individual exits but rarely exhibit the profile required for joint success. Our framework exposes this gap between rewarded partial completion and realized cooperation by certifying what cooperation successful completion requires and using temporal cooperation graphs to reveal what policies exhibit.

## Metadata
- **Published**: 2026-09-06T13:08:51Z
- **Authors**: Yannick Molinghen, Hugo Charels, Tom Lenaerts
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06586v1)