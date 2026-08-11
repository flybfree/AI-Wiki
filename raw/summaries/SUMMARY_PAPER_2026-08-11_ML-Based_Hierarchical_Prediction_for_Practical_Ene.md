---
title: ML-Based Hierarchical Prediction for Practical Energy Scheduling in Dynamic NTN-WPT Systems
url: http://arxiv.org/abs/2608.08804v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-09_16-41-13Z_ML_BasedHierarchicalPredictionforPracticalEnergySc.md
generated_at: 2026-08-11 13:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a hierarchical prediction framework that jointly optimizes energy efficiency task completion rate and waiting time for wireless power transfer between low Earth orbit satellites and terrestrial mobile devices. It uses state forecasting, a graph neural network mapping, and multi‑objective reinforcement learning decision making to balance competing goals under mobility and channel uncertainty.

## Key Takeaways
- The framework decomposes scheduling into three layers: state prediction, interaction mapping via GNN, and decision making with MORL. 
- Multi‑agent deep learning with self‑attention and MAPPO is introduced to improve objective balancing. 
- Simulation results show improved trade‑offs compared to baselines while maintaining competitive task completion rates energy efficiency and lower waiting times.

## Context
This work extends AI for dynamic wireless power transfer by integrating reinforcement learning and graph neural networks within a multi‑agent setting, addressing the need for real‑time adaptive scheduling. It demonstrates how hierarchical prediction can handle stochastic propagation effects in space‑based networks.

## Implications
For industry, the approach offers a scalable method to schedule energy resources across distributed nodes, reducing waste and improving user experience. Practitioners can apply similar multi‑layer ML pipelines to other dynamic resource allocation problems such as network load balancing or IoT device power management.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08804v1)
