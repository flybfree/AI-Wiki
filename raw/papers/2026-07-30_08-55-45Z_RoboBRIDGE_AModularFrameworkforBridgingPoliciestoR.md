---
title: RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents
published: 2026-07-30T08:55:45Z
authors: Sihyung Yoon, Minjong Yoo, Sanghyun Ahn, Seojeong Choi, Honguk Woo
url: http://arxiv.org/abs/2607.27881v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents

## Abstract
Vision-Language-Action (VLA) models have attracted growing interest as a scalable approach to robotic manipulation. While these models are effective action predictors, deploying them as robotic agents exposes critical gaps: no mechanism for failure recovery, inconsistent execution over long horizons, and limited robustness to shifts in observations, tasks, or embodiments. Existing solutions address these limitations individually through model retraining or environment-specific modules, yet what is needed is a general framework that systematically transforms a pretrained VLA into a robotic agent. We present RoboBRIDGE, a modular framework that provides an orchestration layer over five coordinated modules, namely Monitor, Perceptor, Planner, Controller, and Robot Interface, to compose robust robotic agents from off-the-shelf components, including pretrained VLAs. The Monitor pairs rapid failure detection with hierarchical recovery to correct errors before they cascade. When the environment diverges from the current plan, the Planner triggers replanning while the Perceptor updates scene understanding asynchronously, avoiding execution stalls. Within the Controller, primitive skill fine-tuning factors manipulation into domain-invariant primitives with dedicated LoRA adapters, reducing sensitivity to domain shifts when a VLA is used. Across LIBERO, RoboCasa, and real-world case studies spanning multiple robot platforms and VLA backbones, RoboBRIDGE consistently outperforms both standalone policies and prior augmented VLA deployments. These results suggest that reliable robotic agency does not arise from scaling action predictors alone, but from structured orchestration around them.

## Metadata
- **Published**: 2026-07-30T08:55:45Z
- **Authors**: Sihyung Yoon, Minjong Yoo, Sanghyun Ahn, Seojeong Choi, Honguk Woo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27881v1)