---
title: MAUPITI: On-Device Prototype-Based Learning on a Smart Infrared Sensor
url: http://arxiv.org/abs/2608.07192v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_13-07-24Z_MAUPITI_On_DevicePrototype_BasedLearningonaSmartIn.md
generated_at: 2026-08-09 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a prototype‑based Nearest Class Mean classifier for a low‑resolution infrared sensor that learns on the device while staying within tight memory and power limits. The system integrates a 16×16 thermal MOSFET array with a RISC‑V microcontroller, operating below 32 KB memory and 1.5 mW power budget. Experiments show classification accuracy comparable to conventional models with minimal latency overhead.

## Key Takeaways
- Quantization reduces model size to under 8 KB while preserving accuracy, enabling storage within the tight limit.
- Streaming prototype updates avoid storing full training data, minimizing memory pressure.
- Latency overheads are measured in milliseconds, well below typical frame rates.

## Context
In privacy‑preserving AI, on‑device learning reduces data transmission while maintaining performance; this work demonstrates feasibility with a tiny thermal sensor. Such on‑device adaptation is crucial for applications where user privacy must be preserved and network resources are scarce.

## Implications
Industry can adopt this framework to build low‑cost, self‑learning sensors without cloud dependency, accelerating deployment of smart wearables. The approach opens new possibilities for real‑time human interaction in edge environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07192v1)
