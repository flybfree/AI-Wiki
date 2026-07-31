---
title: PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball
published: 2026-07-30T17:59:35Z
authors: Lizhi Yang, Junheng Li, Aaron D. Ames
url: http://arxiv.org/abs/2607.28623v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball

## Abstract
We present PAC-MAN, a perception-aware CBF-RL framework that couples control-barrier safety with deployment-realistic onboard sensing for whole-body humanoid dodgeball. The deployed policy sees the ball only as segmentation-masked depth from a head-mounted camera, while training-time CBF guidance represents clearance to every body link, and an adversarial motion prior regularizes the resulting evasive reflexes. We evaluate on a controlled any-link contact benchmark with seeded throws in two regimes: single throws and a deployment loop in which the robot walks back to its station and recovers between throws. On this benchmark, the policy comes within a few points of a privileged state oracle: a fixed onboard camera alone is adequate for evasion. We find that usable barrier structure depends on perceptual observability: Joint-CBF gives the best performance with accurate ball states, degrades under fixed-camera observations when used only as training guidance, and recovers with a ball-tracking gimbal or privileged runtime filter. We therefore deploy a lightweight Link-CBF policy zero-shot on the Unitree G1 in the real world, where it tolerates imperfect perception, succeeds on 95% of throws, and uses semantic segmentation to dodge different balls.

## Metadata
- **Published**: 2026-07-30T17:59:35Z
- **Authors**: Lizhi Yang, Junheng Li, Aaron D. Ames
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28623v1)