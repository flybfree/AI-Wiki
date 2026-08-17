---
title: Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use
url: http://arxiv.org/abs/2608.14047v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_07-53-18Z_EvolveVision_Language_ActionModelintoanAgentwithOn.md
generated_at: 2026-08-16 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents Agentic Robot with Tool-use (ART), a framework that combines end-to-end visual‑language‑action models with modular tool modules to enable agents to perform tasks using off‑the‑shelf tools. By injecting these tools, ART reduces the complexity of continuous action spaces, leading to higher task generalizability and lower data requirements compared with baseline VLA methods.

## Key Takeaways
- The framework introduces a tool‑injection mechanism that maps high‑level affordances to specific off‑the‑shelf tool actions, thereby simplifying the continuous action solution space.  
- Training on only 30 K tool‑use trajectories and demonstrations demonstrates that ART achieves a 20 % higher success rate than mainstream baselines in both simulated and real‑world pick‑and‑place tasks performed in darkness at novel viewpoints.  
- The modular design enables lightweight deployment, efficient training of long‑trajectory reasoning, and easy integration of new tools without retraining the entire model.

## Context
The integration of tool use into vision‑language models aligns with recent advances in embodied AI, where agents must navigate complex environments using limited sensory inputs. This work addresses a key bottleneck: the need for massive annotated action data to train continuous control policies, which is impractical for real‑world deployment.

## Implications
ART’s modularity and low data dependency make it suitable for industry applications requiring rapid prototyping of new tool capabilities. Practitioners can scale VLA systems across diverse tasks by simply adding appropriate tool modules, fostering robustness and adaptability in autonomous robotics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14047v1)
