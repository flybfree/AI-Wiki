---
title: Local Updates, Global Learning (LUGL): Playing Games with non-incremental Learners
published: 2026-09-03T10:58:09Z
authors: David Milec, Spyridon Samothrakis, Michael Fairbank, Dennis J. N. J. Soemers
url: http://arxiv.org/abs/2609.03660v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Local Updates, Global Learning (LUGL): Playing Games with non-incremental Learners

## Abstract
The dominance of Neural Networks (NNs) in RL is partially due to their incremental learning capability, which naturally suits the online, non-stationary nature of self-play training. However, gradient-boosted trees like LightGBM are widely recognised as the state of the art for tabular data in supervised learning, often outperforming NNs in accuracy and efficiency. Game states are inherently tabular---discrete actions, categorical card identities, structured board positions---which makes them an ideal candidate for tree-based methods. We introduce LUGL (Local Updates, Global Learning), a framework that decouples data collection from model fitting, enabling non-incremental learners such as GBTs to operate in RL settings where they would otherwise fail due to distributional shift. LUGL alternates between a local updates phase, where the agent plays self-play games and accumulates tabular updates (Q-values, V-values, policies, or regret values) in a finite table, and a global learning phase, where the table is used to train a function approximator that generalises to unseen states before the table is reset. We test our approach in four standard perfect-information games (Tic-tac-toe, Connect-4, Othello, and Hex) and five imperfect-information games (Kuhn's poker, Leduc Hold'em, Liar's Dice, Goofspiel, and Flop5 Hold'em), and show that our results are competitive with or superior to DQN and DeepCFR. Our experiments demonstrate that the community's strong bias towards NNs in game-playing may be unwarranted, since LightGBM-based agents achieve competitive or superior performance across all tested benchmarks.

## Metadata
- **Published**: 2026-09-03T10:58:09Z
- **Authors**: David Milec, Spyridon Samothrakis, Michael Fairbank, Dennis J. N. J. Soemers
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03660v1)