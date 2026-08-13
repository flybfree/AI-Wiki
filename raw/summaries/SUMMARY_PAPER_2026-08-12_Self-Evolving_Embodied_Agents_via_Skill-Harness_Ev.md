---
title: Self-Evolving Embodied Agents via Skill-Harness Evolution
url: http://arxiv.org/abs/2608.11350v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_18-55-58Z_Self_EvolvingEmbodiedAgentsviaSkill_HarnessEvoluti.md
generated_at: 2026-08-12 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SHAPER, a self‑evolving framework that adapts frozen foundation models to new embodied environments without retraining the model or collecting additional data. By evolving reusable skills and a context‑code harness through target‑environment rollouts, SHAPER improves performance across diverse low‑level action interfaces.

## Key Takeaways
- SHAPER evolves non‑parametric components such as skills and execution harnesses instead of updating model weights.  
- The framework uses target‑environment rollouts to iteratively refine these components while keeping the frozen model unchanged.  
- Experiments on VLABench and ESI‑Bench show that skill‑and‑harness optimization outperforms pure execution, supervised fine‑tuning, and test‑time‑scaling baselines.

## Context
The rapid adoption of foundation models in robotics has highlighted a bottleneck: adapting these models to new physical settings often demands costly training or extensive data. Existing solutions either rely on supervised fine‑tuning or require verifier‑free selection methods that are limited by fixed APIs, leaving a gap for train‑free adaptation.

## Implications
SHAPER offers a practical path for deploying foundation‑model agents in real‑world robotics where retraining is impractical. By focusing on skill and harness evolution, practitioners can maintain model stability while achieving significant performance gains across varied environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11350v1)
