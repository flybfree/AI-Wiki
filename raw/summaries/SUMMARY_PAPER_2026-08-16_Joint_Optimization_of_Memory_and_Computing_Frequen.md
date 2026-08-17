---
title: Joint Optimization of Memory and Computing Frequency for Energy-Efficient DNN Inference
url: http://arxiv.org/abs/2608.13863v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_01-25-00Z_JointOptimizationofMemoryandComputingFrequencyforE.md
generated_at: 2026-08-16 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the high energy consumption of DNN inference on mobile devices by jointly optimizing memory and computing frequencies while respecting deadline constraints. It derives a near-optimal closed-form solution for local inference and an optimal transmission power formula for edge inference, achieving up to 10.4% lower energy use compared with prior methods.

## Key Takeaways
- The study shows that memory frequency impacts inference time just as much as computing frequency, revealing a previously overlooked resource.
- A convex optimization yields a near-optimal solution for local devices that meets deadlines within a 2.5% performance gap to the theoretical optimum.
- The proposed heuristic algorithm solves the full problem in polynomial time, delivering up to 10.4% energy savings over alternative approaches.

## Context
Mobile AI inference faces dual constraints: limited CPU power and volatile memory bandwidth, both of which affect latency and energy use. Existing DVFS techniques ignore memory frequency, leading to suboptimal resource allocation that hampers real‑time applications. These constraints are particularly acute for real-time applications such as augmented reality and voice assistants where latency directly impacts user experience.

## Implications
This work provides a practical framework for system designers seeking to balance accuracy, latency, and power in edge AI devices. By integrating memory and compute frequencies into joint optimization, it enables more sustainable inference pipelines across smartphones and IoT platforms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13863v1)
