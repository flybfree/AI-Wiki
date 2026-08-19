---
title: ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback
published: 2026-08-18T03:30:12Z
authors: Muhammad A. Muttaqien, Tomohiro Motoda, Ryo Hanai, Yukiyasu Domae
url: http://arxiv.org/abs/2608.17323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback

## Abstract
Robotic manipulation policies trained via imitation learning, such as Action Chunking with Transformers (ACT), can achieve strong performance under ideal conditions but often remain sensitive to small execution errors and distribution shifts. Correcting these failures typically requires dataset aggregation and full-policy retraining, which is computationally expensive and unsuitable for real-time deployment. In this work, we propose Online Residual Policy Adaptation (ORPA), a framework that enables immediate, feedback-driven correction of robot actions without modifying the underlying policy parameters. ORPA augments a pretrained control policy with a lightweight, feedback-conditioned module that predicts residual adjustments directly in joint space, allowing the system to adapt its behavior at runtime. We evaluate ORPA on a set of precision-sensitive manipulation tasks using the ALOHA platform, demonstrating improvements in success rate and recovery from small perturbations compared to baseline control policies and rule-based inverse kinematics corrections.

## Metadata
- **Published**: 2026-08-18T03:30:12Z
- **Authors**: Muhammad A. Muttaqien, Tomohiro Motoda, Ryo Hanai, Yukiyasu Domae
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17323v1)