---
title: TransHands: Repurposing Human Pose Encoders as Hand Pose Encoders
published: 2026-08-23T10:17:09Z
authors: Milo Piccioli, Gianluca Amprimo, Claudia Ferraris, Gabriella Olmo
url: http://arxiv.org/abs/2608.22341v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TransHands: Repurposing Human Pose Encoders as Hand Pose Encoders

## Abstract
Lifting 3D hand poses from 2D monocular representations remains challenging due to the limited availability of large-scale, diverse 3D-annotated hand datasets, in contrast to the abundance of human body motion data. We address this limitation by transferring motion representations learned from large body pose corpora to the hand domain. We introduce TransHands, a backbone-agnostic transfer learning framework that enables pre-trained human motion encoders to be effectively adapted for 3D hand pose estimation from 2D pose inputs. Rather than training hand-specific biomechanical models from scratch, TransHands combines a two-stage training and fine-tuning strategy with a lightweight hand-specific input adaptation module that aligns hand kinematics with the representation space learned for full-body motion. We evaluate TransHands across four state-of-the-art motion modeling architectures, including transformer-based, graph-based, and frequency- domain models. Results demonstrate that motion priors learned from body pose data transfer consistently across architectures, yielding consistent accuracy gains, strong cross-domain generalization, particularly in challenging egocentric settings, and applicability for downstream tasks in real-world contexts.

## Metadata
- **Published**: 2026-08-23T10:17:09Z
- **Authors**: Milo Piccioli, Gianluca Amprimo, Claudia Ferraris, Gabriella Olmo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22341v1)