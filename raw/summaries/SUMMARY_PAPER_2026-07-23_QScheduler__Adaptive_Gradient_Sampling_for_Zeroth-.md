---
title: QScheduler: Adaptive Gradient Sampling for Zeroth-Order On-Device Training on INT8 NPUs
url: http://arxiv.org/abs/2607.18802v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_07-30-08Z_QScheduler_AdaptiveGradientSamplingforZeroth_Order.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents QScheduler, an adaptive algorithm that dynamically selects the number of gradient samples (q) during zeroth-order on‑device training to balance accuracy and computational cost. Experiments on EuroSAT and STL-10 demonstrate that QScheduler achieves performance comparable to well‑tuned fixed‑q setups for ResNet18 and MobileNetV2 without prior hyperparameter optimization, using INT8 quantization on the STM32N6 Neural‑ART NPU.

## Key Takeaways
- The adaptive algorithm QScheduler reduces the need for costly manual q selection by continuously adjusting gradient sampling based on training progress.  
- It enables high‑accuracy training with minimal computational overhead, matching fixed‑q configurations that are typically found through extensive search.  
- The approach proves feasible INT8 quantized on‑device learning on microcontroller NPUs such as the STM32N6 Neural‑ART.

## Context
Zeroth-order optimization is a promising technique for on‑device machine learning because it avoids backpropagation and large memory footprints, making deep neural networks runnable on resource‑constrained hardware. Prior work has relied on fixed q values that often require extensive tuning, limiting practical deployment.

## Implications
QScheduler opens the door to more efficient AI inference and training in edge devices without sacrificing accuracy or requiring extensive offline optimization. Practitioners can deploy quantized models directly on microcontrollers, accelerating real‑time applications such as sensor data analysis and mobile robotics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18802v1)
