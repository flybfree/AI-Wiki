---
title: Driving on Memory
url: http://arxiv.org/abs/2608.31029v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_16-10-04Z_DrivingonMemory.md
generated_at: 2026-08-31 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether autonomous driving models rely on current sensor input to achieve high scores on benchmark suites like NAVSIM and Bench2Drive, or if they can perform similarly using only memories of past drives at the same location. The authors replace camera data with retrieved memories and find that memory alone is nearly sufficient on NAVSIM, even surpassing leading end‑to‑end methods, indicating that a high score does not necessarily require reacting to the present traffic scene.

## Key Takeaways
- Memory replacement can yield performance comparable to or better than models using live sensor data on NAVSIM.  
- The effect is benchmark dependent: memory causes large drops in performance on Bench2Drive and RealEngine, suggesting that some benchmarks are more sensitive to current context.  
- A high NAVSIM score may reflect persistent scene knowledge rather than real‑time reaction, warranting cautious interpretation.

## Context
The study highlights a gap between benchmark design and the true capabilities of autonomous driving systems. By decoupling perception from sensor input, researchers reveal that many evaluation metrics may overestimate the necessity for up‑to‑date observations, influencing how we assess model safety and compliance in real‑world deployment.

## Implications
For industry practitioners, this suggests that relying solely on benchmark scores could mislead decisions about model readiness. Practitioners should consider both memory‑based and live‑sensor performance to obtain a balanced view of autonomous driving capability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.31029v1)
