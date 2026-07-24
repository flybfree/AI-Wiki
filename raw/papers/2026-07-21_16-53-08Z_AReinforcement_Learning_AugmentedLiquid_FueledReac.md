---
title: A Reinforcement-Learning-Augmented Liquid-Fueled Reactor Network Model for Predicting Lean Blowout in Gas Turbine Combustors
published: 2026-07-21T16:53:08Z
authors: Philip John, Eloghosa Ikponmwoba, Pinaki Pal, Opeoluwa Owoyele
url: http://arxiv.org/abs/2607.19281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Reinforcement-Learning-Augmented Liquid-Fueled Reactor Network Model for Predicting Lean Blowout in Gas Turbine Combustors

## Abstract
This study introduces a reinforcement learning (RL) framework for generating optimal liquid-fueled reactors to improve lean blowout (LBO) predictions in gas turbine combustors. Existing approaches for determining cluster boundaries rely on manual heuristics or distance-based metrics in the input space. In contrast, the proposed method is goal-oriented, explicitly accounting for the target metric (e.g., LBO prediction accuracy) during cluster formation. The framework employs a multi-stage clustering--classification strategy: an initial clustering step (e.g., $k$-means clustering) generates a large set of homogeneous micro-clusters, followed by an actor-critic RL agent that merges them into optimal reactor zones. The validation study, performed using a Jet-A mechanism (119 species, 841 reactions), shows the RL framework offers improved predictive fidelity compared to $k$-means and captures the correct LBO trends, while achieving substantial speedups relative to the high-fidelity computational model. Overall, the RL-driven approach demonstrates strong potential as a computationally efficient reduced-order modeling technique that can complement high-fidelity simulations for rapid design-space exploration.

## Metadata
- **Published**: 2026-07-21T16:53:08Z
- **Authors**: Philip John, Eloghosa Ikponmwoba, Pinaki Pal, Opeoluwa Owoyele
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19281v1)