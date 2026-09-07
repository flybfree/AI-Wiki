---
title: Coupled Control and Wireless World Models for Resilient Remote Robotic Control
published: 2026-09-04T08:09:55Z
authors: H. P. Madushanka, Sumudu Samarakoon, Mehdi Bennis
url: http://arxiv.org/abs/2609.04851v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coupled Control and Wireless World Models for Resilient Remote Robotic Control

## Abstract
Remote robotic systems operating over wireless networks must maintain reliable control despite limited communication resources, changing channel conditions, and environmental disturbances.However, continuously transmitting high-dimensional sensory observations, such as camera images, increases communication overhead and energy consumption while reducing robustness under unreliable connectivity.To address these challenges, this paper proposes a resilient communication-aware remote robotic control framework based on coupled control and wireless Joint Embedding Predictive Architecture (JEPA) world models that jointly capture robot dynamics and wireless channel evolution from visual observations and a combination of raw and structured radio frequency (RF) representations based on spectrograms and Persistence Images(PIs).The learned latent representations enable predictive communication scheduling by jointly forecasting future robot states and wireless conditions, thereby reducing unnecessary uplink transmissions while maintaining reliable control performance.Furthermore, an adaptive resilience mechanism detects latent prediction discrepancies and efficiently adapts perception embeddings to accommodate wireless and visual environmental changes without retraining the complete control policy.The proposed framework is evaluated in a synchronized Gazebo-Robot Operating System (ROS)-Sionna robot-wireless simulation environment under diverse wireless propagation and perception perturbations.Experimental results demonstrate significant improvements in communication efficiency, robustness, and resilience while maintaining navigation performance compared with conventional Proportional Integral Derivative (PID), model-free Deep Q-Network (DQN), and predictive approaches based on Vision Transformers(ViTs).

## Metadata
- **Published**: 2026-09-04T08:09:55Z
- **Authors**: H. P. Madushanka, Sumudu Samarakoon, Mehdi Bennis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04851v1)