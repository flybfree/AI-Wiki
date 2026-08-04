---
title: AOS: Adaptive Optimizer Switching via Training-State Signals for Faster Convergence and Better Generalization
published: 2026-08-03T09:57:50Z
authors: Alok Kumar Pandey, Umang Chaturvedi, Aatish Rana, Gopi Krishna Nedanuri
url: http://arxiv.org/abs/2608.01997v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AOS: Adaptive Optimizer Switching via Training-State Signals for Faster Convergence and Better Generalization

## Abstract
Single-optimizer training is a poor fit for the distinct phases of deep network optimization: adaptive methods handle noisy early gradients well but overshoot flat minima, while SGD with momentum generalizes better in the late phase but converges slowly early on.   We introduce AOS-R (Adaptive Optimizer Switching, Rule-Based), a lightweight controller that monitors six online gradient-space signals -- gradient noise scale (GNS), Hutchinson curvature trace, loss stagnation, update stability ratio, gradient stability index (GSI), and loss improvement ratio (LIR) -- and switches among AdamW, SGD-M, and Lion as the optimization landscape evolves. State-preserving momentum transfer and a 400-step learning-rate bridge prevent accuracy degradation at every transition point.   On CIFAR-100/WRN-28x10, AOS-R reaches 78% top-1 in 81 epochs -- 26% fewer than AdamW (109), 43% fewer than SGD-M (143), and 16% fewer than Lion (96). Across eight model-dataset benchmarks, AOS-R achieves best accuracy on 6 of 8 combinations with a mean +0.4 pp gain and 0.80x convergence speedup over AdamW under a single shared hyperparameter configuration.

## Metadata
- **Published**: 2026-08-03T09:57:50Z
- **Authors**: Alok Kumar Pandey, Umang Chaturvedi, Aatish Rana, Gopi Krishna Nedanuri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01997v1)