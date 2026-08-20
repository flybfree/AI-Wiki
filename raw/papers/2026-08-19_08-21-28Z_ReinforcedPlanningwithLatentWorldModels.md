---
title: Reinforced Planning with Latent World Models
published: 2026-08-19T08:21:28Z
authors: Armin Sommer, Jannik Schilling
url: http://arxiv.org/abs/2608.18669v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reinforced Planning with Latent World Models

## Abstract
Humans solve complex problems by constructing plans and mentally simulating their outcomes with an internal model of the world. Machine learning has produced world models that similarly predict the outcomes of action sequences, but the improvement of candidate plans still isn't fully learned. Current planners are either hand-designed, distilled from a hand-designed optimizer, or learned only to inform an amortized policy rather than to revise the plan itself. We introduce the Reinforced Planning, a method based on the idea that search can be learned by reinforcing good search rules into a neural planner. Our implementation RP1 learns both how to evaluate imagined outcomes through a critic, as well as how to improve multi-step plans through an optimizer trained fully offline from imagined world-model roll-outs. To our knowledge, RP1 is the first method to fully learn how to improve multi-step plans. Furthermore, it can be trained independently of and attached to any pretrained latent world model. Across visual navigation, arm reaching, and robotic manipulation on two world-model backbones, RP1 substantially outperforms hand-designed search algorithms, reaching near-perfect success in several settings while using $1,000 \times$ less world-model rollouts and being up to $67 \times$ faster than the strongest alternative under concurrent planner inference.

## Metadata
- **Published**: 2026-08-19T08:21:28Z
- **Authors**: Armin Sommer, Jannik Schilling
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18669v1)