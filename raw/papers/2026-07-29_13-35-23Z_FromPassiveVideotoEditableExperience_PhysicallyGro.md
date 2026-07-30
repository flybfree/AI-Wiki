---
title: From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence
published: 2026-07-29T13:35:23Z
authors: Jia Luo
url: http://arxiv.org/abs/2607.26903v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence

## Abstract
The key bottleneck in embodied AI is not model architecture but data. Although billions of human manipulation videos exist online, robots cannot directly learn from them due to the embodiment gap between human morphology and robot hardware. We introduce Pegasus, a low-resource framework that bridges this gap by translating human demonstrations into robot-learnable data through structured knowledge transfer. Instead of relying on raw video prompts, Pegasus constructs a graph-based intermediate representation: a Task Graph extracted from human videos is transformed through Affordance and Constraint Graphs into a Robot Planning Graph for robot-conditioned video generation. A hierarchical affordance latent space models the relationship between object states, affordances, and tasks, enabling generalization beyond object identities. A closed-loop physics verifier further filters invalid generations using kinematic feasibility, collision constraints, and joint limits. We evaluate Pegasus across a range of egocentric manipulation benchmarks, including GTEA Gaze+ and EPIC-KITCHENS-100, and diverse robot embodiments, assessing Task Correctness, Executability, State Consistency, and Learnability. Results demonstrate reliable cross-embodiment translation and show that robot data generation can be reframed from a hardware collection problem into a scalable, low-resource knowledge transfer problem.

## Metadata
- **Published**: 2026-07-29T13:35:23Z
- **Authors**: Jia Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26903v1)