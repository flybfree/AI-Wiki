---
title: VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System
url: http://arxiv.org/abs/2607.27380v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_18-38-23Z_VideoCoCo_Code_as_CoTforPhysically_ConsistentVideo.md
generated_at: 2026-07-30 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VideoCoCo, an agentic dual‑engine system that generates executable Blender code as a chain‑of‑thought process to create physically consistent videos and demonstrates improved performance on benchmark datasets. It achieves higher scores than OmniWeaving.

## Key Takeaways
- Executable Blender code serves as an explicit, process‑level chain of thought that defines scene dynamics over time.
- The system separates reasoning from high‑fidelity rendering by using draft‑conditioned editing to transform simulation output into photorealistic video.
- VideoCoCo improves OmniWeaving’s PhyGenBench score from 0.475 to 0.558 and VBench‑2.0 score from 52.18 to 77.88, showing code as an effective intermediate representation.

## Context
Text‑to‑video generation often lacks physical realism because temporal dynamics are inferred from compressed prompts. Current chain‑of‑thought methods rely on non‑executable or sparse visual states, limiting control over the full spatiotemporal process. This work addresses that gap by providing a runnable program that can be inspected and modified.

## Implications
The ability to generate videos with physically consistent motion opens new possibilities for simulation‑driven content creation in gaming, robotics, and virtual production. Practitioners can now rely on an inspectable code artifact to debug or adapt simulations without sacrificing visual fidelity, accelerating research and deployment of realistic video generation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27380v1)
