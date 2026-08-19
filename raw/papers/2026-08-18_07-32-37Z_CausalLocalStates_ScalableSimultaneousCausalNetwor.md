---
title: Causal Local States: Scalable Simultaneous Causal Network Inference and Forecasting for Dynamical Systems
published: 2026-08-18T07:32:37Z
authors: Jonas Braun, Fabian Fischbach, Daniel Köglmayr, Sebastian Baur, Christoph Räth
url: http://arxiv.org/abs/2608.17452v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal Local States: Scalable Simultaneous Causal Network Inference and Forecasting for Dynamical Systems

## Abstract
Machine learning methods predict many real-world systems with remarkable accuracy, but they are typically treated as black boxes that offer no insight into which interactions drive the dynamics. Causal discovery methods reconstruct the interaction network from observational data, but without regard to whether the inferred structure supports prediction. Existing approaches combining both tasks rely on a single global hyperparameter, such as a causal threshold or a fixed neighborhood size, which cannot recover the structure of heterogeneous systems. Here we introduce causal local states (CLS), a framework that simultaneously infers an approximate Granger-causal interaction network and forecasts the system dynamics. For each node independently, we select the smallest set of neighbors that allows a predictive model to forecast the node near-optimally, and the resulting neighborhoods are then combined for a forecast of the full system. On three benchmarks of increasing difficulty, we achieve reconstruction of the underlying networks with high fidelity and forecasts on par with a model that is supplied with the true network, providing a step toward explainable and scalable forecasting of complex systems.

## Metadata
- **Published**: 2026-08-18T07:32:37Z
- **Authors**: Jonas Braun, Fabian Fischbach, Daniel Köglmayr, Sebastian Baur, Christoph Räth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17452v1)