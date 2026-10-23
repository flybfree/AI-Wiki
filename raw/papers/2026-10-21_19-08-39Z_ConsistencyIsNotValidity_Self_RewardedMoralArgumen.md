---
title: Consistency Is Not Validity: Self-Rewarded Moral Argumentation Makes Language Models Decisive but Pliable
published: 2026-10-21T19:08:39Z
authors: Marius De Kuthy Meurers, Aaron Parisi, Bernd Bohnet
url: http://arxiv.org/abs/2610.30349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Consistency Is Not Validity: Self-Rewarded Moral Argumentation Makes Language Models Decisive but Pliable

## Abstract
LLMs are increasingly consulted for moral judgment. We aim to improve performance on such tasks by rewarding good arguments, on the premise that arguing well increases the likelihood of judging well. We train a reinforcement learning policy initialized from a state-of-the-art language model in a self-judged tournament with masked thinking: the generated arguments are judged pairwise on argument quality by the policy itself. As an empirical basis, we extract authentic dilemmas from classic novels, using a logic solver to verify that each constitutes a conflict. We show that our judge rates argument quality like human annotators, and the policy then adopts the language register that it rewards. Testing on the external benchmarks MoralChoice, ELEPHANT, and MORABLES, we find that the policy becomes more decisive and invariant to the order in which options are presented, but sycophancy and reframing remain a challenge to validity. Two ablation studies with synthetic dilemmas and unmasked thinking match the reordering gains, but show a weaker register shift and higher sycophancy. We conclude that consistency is not validity: consistency under reordering can be optimized without improving the moral judgment it is meant to signal.

## Metadata
- **Published**: 2026-10-21T19:08:39Z
- **Authors**: Marius De Kuthy Meurers, Aaron Parisi, Bernd Bohnet
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30349v1)