---
title: Convergence-Latency-Aware Adaptive Modulation and Resource Allocation in RIS-Assisted Wireless Federated Learning
url: http://arxiv.org/abs/2607.19759v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_05-09-22Z_Convergence_Latency_AwareAdaptiveModulationandReso.md
generated_at: 2026-07-23 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a convergence‑latency aware communication scheme for federated learning over RIS‑assisted wireless networks with blocked links. It derives an upper bound linking symbol error rate to FL loss decay and formulates a joint optimization problem solved by a hybrid alternating algorithm. Experiments on MNIST, CIFAR‑10, and Speech Commands show faster convergence and higher test accuracy than prior adaptive schemes.

## Key Takeaways
- The derived convergence‑related upper bound quantifies how symbol error rate directly degrades FL loss decay.
- A mixed‑integer nonlinear programming formulation captures the trade‑off between modulation choice and sub‑channel allocation.
- Hybrid alternating optimization solves the MINLP efficiently, enabling real‑time adaptation in wireless FL.

## Context
Wireless federated learning is limited by unreliable transmission and high latency, which hinder model convergence. RISs offer a promising way to mitigate these issues but their impact on communication dynamics remains underexplored. This work bridges that gap by integrating adaptive modulation with sub‑channel scheduling under realistic blocked‑link conditions.

## Implications
The framework provides a principled method for balancing speed and accuracy in distributed AI training, applicable to edge devices and mobile networks. Practitioners can leverage the derived bounds to set conservative SER thresholds without sacrificing convergence, accelerating deployment of federated learning services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19759v1)
