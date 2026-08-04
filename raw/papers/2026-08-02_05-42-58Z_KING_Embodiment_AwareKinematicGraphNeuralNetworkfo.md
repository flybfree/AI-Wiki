---
title: KING: Embodiment-Aware Kinematic Graph Neural Network for Unified Motion Representation of Legged and Wheeled Robots
published: 2026-08-02T05:42:58Z
authors: Taku Okawara, Aoki Takanose, Kenji Koide, Shuji Oishi, Masashi Yokozuka
url: http://arxiv.org/abs/2608.01015v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KING: Embodiment-Aware Kinematic Graph Neural Network for Unified Motion Representation of Legged and Wheeled Robots

## Abstract
Kinematic models provide reliable motion constraints for odometry estimation in featureless environments, where exteroceptive sensing degrades and IMU integration drifts. Learning-based kinematic models can achieve more accurate odometry estimation than model-based methods by capturing nonlinear effects; however, most existing learning-based models are trained on a single embodiment and generalize poorly to new embodiments. This generalization is difficult because the meanings and structures of proprioceptive measurements vary across embodiments, including the number of joints and ground-contact elements (e.g., wheels, feet). To address this challenge, we propose KING, a Graph Neural Network (GNN)-based kinematic model that explicitly incorporates robot embodiments by representing them as a common graph. We show that wheel and leg kinematic models can be expressed by a unified representation, enabling a single model for both wheeled and legged robots. Trained on datasets spanning diverse embodiments, KING provides a unified representation of wheeled and legged kinematics and achieves high-accuracy odometry estimation in real environments. KING estimates accurate odometry using only an embodiment description (e.g., a URDF file) and on-board proprioception (encoders and an IMU) and can be adapted to new robot embodiments through few-shot learning with only one minute of data, avoiding retraining from scratch on a new dataset for each robot. The project page is available at: https://smrg-aist.github.io/king_project_page/

## Metadata
- **Published**: 2026-08-02T05:42:58Z
- **Authors**: Taku Okawara, Aoki Takanose, Kenji Koide, Shuji Oishi, Masashi Yokozuka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01015v1)