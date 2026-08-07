---
title: iARCS: Iterative Agentic RL for Controllable 3D Scene Generation
url: http://arxiv.org/abs/2608.06161v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_15-30-21Z_iARCS_IterativeAgenticRLforControllable3DSceneGene.md
generated_at: 2026-08-06 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces iARCS, an iterative agentic reinforcement learning framework that adapts a pretrained 3D scene generator to natural‑language task constraints. Experiments demonstrate that iARCS improves walkability, reachability, and clearance compliance while maintaining competitive diversity in generated scenes.

## Key Takeaways  
- iARCS performs universal‑reward pretraining to boost physical plausibility before fine‑tuning with LLM‑generated reward programs.  
- The framework iteratively refines reward functions using training feedback to optimize task‑specific constraints such as walkability and reachability.  
- Generated scenes from iARCS enhance the base generator, showing value beyond simple scene editing.

## Context  
Synthetic 3D environments are a key resource for computer vision and embodied AI research, yet most generators lack reliable adherence to functional constraints. This work addresses that gap by integrating reinforcement learning with language models to produce task‑aligned data. The approach aligns with broader trends toward controllable, data‑driven synthetic generation.

## Implications  
iARCS provides a practical tool for developers needing high‑quality, constraint‑compliant scenes for training embodied agents. By improving downstream performance and enabling iterative refinement, it can reduce reliance on costly real‑world data collection in robotics and AR/VR applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06161v1)
