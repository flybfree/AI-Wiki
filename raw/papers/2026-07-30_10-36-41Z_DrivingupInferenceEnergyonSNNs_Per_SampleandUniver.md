---
title: Driving up Inference Energy on SNNs: Per-Sample and Universal Sponge Attacks
published: 2026-07-30T10:36:41Z
authors: Spyridon Raptis, Haralampos-G. Stratigopoulos
url: http://arxiv.org/abs/2607.27990v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Driving up Inference Energy on SNNs: Per-Sample and Universal Sponge Attacks

## Abstract
Spiking Neural Networks (SNNs) communicate through sparse binary spike events rather than dense activations, enabling energy-efficient inference on neuromorphic hardware and motivating their use in always-on, battery-powered edge systems. We show that this same efficiency advantage creates a distinct security risk: sponge attacks can increase inference-time spike activity and synaptic workload, inflating energy consumption while remaining difficult to detect through correctness-based monitoring alone. Prior input-space efficiency attacks on SNNs have focused on per-sample optimization, primarily in rate-coded settings. We extend this threat to native event-based binary inputs and study two attack models. First, we develop a per-sample sponge attack that crafts a custom adversarial spike train for each input via gradient-based optimization. This attack increases per-inference SynOps by 1.5-2.6x on three SNN models for the NMNIST, SHD, and IBM DVS Gesture datasets, while preserving the predicted class on at least 98% of evaluated samples. Second, to the best of our knowledge, we introduce the first universal sponge attack for native event-based SNN inputs: a fixed binary perturbation computed offline and applied via XOR to all subsequent inputs. Although weaker, it still inflates SynOps by 1.09-1.24x across all three datasets and represents a more realistic deployment threat because it requires no per-input optimization. Mapping SynOp inflation to estimated Loihi-1 energy yields per-inference overheads from 14 $μ$J to 13.24 mJ. These results show that native event-based SNNs are vulnerable to practical input-space efficiency attacks, and that reusable universal perturbations can accumulate into meaningful battery drain in continuously deployed edge systems.

## Metadata
- **Published**: 2026-07-30T10:36:41Z
- **Authors**: Spyridon Raptis, Haralampos-G. Stratigopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27990v1)