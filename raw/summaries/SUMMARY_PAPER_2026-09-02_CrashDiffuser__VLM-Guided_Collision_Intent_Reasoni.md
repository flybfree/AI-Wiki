---
title: CrashDiffuser: VLM-Guided Collision Intent Reasoning for Fine-Grained Safety-Critical Traffic Scenario Generation
url: http://arxiv.org/abs/2609.02270v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-18-20Z_CrashDiffuser_VLM_GuidedCollisionIntentReasoningfo.md
generated_at: 2026-09-02 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces CrashDiffuser, a VLM‑guided diffusion framework that generates fine‑grained safety‑critical traffic scenarios requiring both a target collision and precise control over the impact location. It achieves high success rates by decoupling semantic reasoning from continuous trajectory synthesis through a hierarchical interface.

## Key Takeaways  
- CrashDiffuser uses a VLM to extract scene context and predict structured action tuples that specify speed change, turning behavior, and collision stage, enabling precise control over where the impact occurs.  
- The model integrates collision‑guided sampling with short‑horizon replanning, allowing adaptive generation of adversarial trajectories that match the target vehicle’s evolving behavior.  
- Evaluation on WOMD scenarios shows a 50.33% single‑attempt target‑collision rate and 67.98% after three attempts, with a contact‑region control success of 40.05%, indicating strong performance in fine‑grained safety generation.

## Context  
Generating realistic safety‑critical driving scenarios remains a bottleneck for autonomous vehicle testing because most tools focus solely on collision occurrence without spatial precision. This work advances the field by integrating vision‑language models with diffusion synthesis to produce spatially accurate, executable trajectories.

## Implications  
The approach offers practitioners a controllable tool for training and evaluating perception and control systems in high‑stakes environments. By ensuring both collision and contact region fidelity, it can improve safety validation pipelines and reduce costly failure modes in real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02270v1)
