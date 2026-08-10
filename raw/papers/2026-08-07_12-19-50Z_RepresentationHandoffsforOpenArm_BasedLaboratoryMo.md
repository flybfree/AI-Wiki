---
title: Representation Handoffs for OpenArm-Based Laboratory Mobile Manipulation
published: 2026-08-07T12:19:50Z
authors: Yang Shen, Chonghao Cheng, Ziyi Zhao, Jialuo Zhu, Zhenyi Yi, Qi Zhao, Jian Yang, Yuhui Shi, Chin-Teng Lin
url: http://arxiv.org/abs/2608.07154v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Representation Handoffs for OpenArm-Based Laboratory Mobile Manipulation

## Abstract
Open-source robotics and foundation models have lowered the barrier to embodied AI, yet language-guided laboratory automation still requires reliable alignment from instructions and observations to safe actions. This field report presents an OpenArm-based mobile manipulation prototype for laboratory-style tasks, built by integrating dual OpenArm manipulators with a mobile base, vertical slide, RGB-D sensing, lidar-based mapping, ROS2/MoveIt execution, and profile-defined skill interfaces. The system is organized around representation handoffs: natural language requests are constrained into registered skill calls, sensor observations are grounded into maps and object poses, object priors provide role and skill constraints, and runtime bindings compile validated skills into executable motion goals. We use dry-run traces and startup checks to evaluate this integration path, showing how the prototype exposes missing calibration, incomplete object assets, and unfinished real-scene visual grounding as explicit deployment blockers. These intermediate representations serve as practical debugging interfaces for integrating language, perception, planning, and robot safety in embodied systems.

## Metadata
- **Published**: 2026-08-07T12:19:50Z
- **Authors**: Yang Shen, Chonghao Cheng, Ziyi Zhao, Jialuo Zhu, Zhenyi Yi, Qi Zhao, Jian Yang, Yuhui Shi, Chin-Teng Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07154v1)