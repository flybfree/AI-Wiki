---
title: "Summary: GROW$^2$: Grounding Which and Where for Robot Tool Use"
url: http://arxiv.org/abs/2606.30632v1
type: paper-summary
date: 2026-06-30
source_paper: 2026-06-29_17-56-53Z_GROW__2__GroundingWhichandWhereforRobotToolUse.md
generated_at: 2026-06-30 01:00
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces GROW$^2$, a method for grounding robot tool use by selecting an appropriate object as a tool and pinpointing its action region. It combines semantic reasoning from vision‑language models with geometric extraction from RGB‑D data, achieving strong performance on affordance prediction tasks and zero‑shot generalization across open categories.

## Key Takeaways  
- GROW$^2$ splits grounding into semantic (task interpretation) and geometric (3D localization) stages without requiring end‑to‑end training.  
- The system leverages commonsense reasoning from VLMs to choose tools and identify relevant parts, then uses vision models to map those parts to precise 3D regions.  
- Experiments show superior results on affordance prediction benchmarks and zero‑shot performance over open categories in both simulation and real robot tool use.

## Context  
Affordance grounding remains a bottleneck for generalizable robotic manipulation because it relies heavily on labeled data and complex pipelines. This work offers a modular approach that integrates existing vision and language models, reducing reliance on large annotated datasets and enabling rapid adaptation to new tools or tasks.

## Implications  
For robotics engineers, GROW$^2$ provides a practical framework for deploying creative tool use in real‑world settings with minimal custom training. In industry, it could accelerate the development of service robots that perform diverse household chores without extensive reconfiguration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.30632v1)
