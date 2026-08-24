---
title: Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control
published: 2026-08-21T10:01:46Z
authors: Xu Yang, Yiqin Yang, Qianchuan Zhao
url: http://arxiv.org/abs/2608.20936v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control

## Abstract
World models for continuous control are commonly trained for a fixed physical system and can degrade when known morphology parameters such as link lengths, masses, damping, and actuation change. Existing approaches often provide these parameters as conditioning information, but leave unspecified which part of the learned transition should remain reusable and which part should change with morphology. We propose Graph-Operator World Models (GraphOp-WM), a structured world model for generalization across unseen morphology parameters within related articulated robot families. GraphOp-WM represents bodies and their kinematic relations as an attributed graph and factorizes each transition into a morphology-independent local dynamics basis and a morphology-conditioned structured operator. The operator combines node-local modulation, kinematic-tree coupling, and a low-rank global correction, while architectural information separation, basis normalization, and paired-morphology supervision encourage static morphology dependence to be carried by the operator pathway. Graph-level readout and edge-wise action representations provide a compatible interface for reward, value, and TD-MPC-style planning. We further define controlled MuJoCo parameter splits covering interpolation, extrapolation, and held-out compositions of link geometry, mass, damping, and actuation parameters in Hopper, Walker2d, and HalfCheetah.

## Metadata
- **Published**: 2026-08-21T10:01:46Z
- **Authors**: Xu Yang, Yiqin Yang, Qianchuan Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20936v1)