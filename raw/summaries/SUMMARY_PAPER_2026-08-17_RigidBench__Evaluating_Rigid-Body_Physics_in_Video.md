---
title: RigidBench: Evaluating Rigid-Body Physics in Video Generation Models
url: http://arxiv.org/abs/2608.15555v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_06-05-20Z_RigidBench_EvaluatingRigid_BodyPhysicsinVideoGener.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RigidBench, a benchmark for evaluating rigid-body physics in video generation models by comparing generated continuations to ground-truth rollouts from the same initial frame and motion description. It presents five tasks varying objects, materials, viewpoints, indoor/outdoor scenes with per-frame masks, depth, 6-DoF trajectories, and contacts. Evaluation on eight models shows no model dominates all ten metrics; higher SSIM correlates strongly with larger 3D trajectory error (r=0.89). Fine‑tuning Wan2.2 TI2V-5B reduces 3D trajectory error by ~20% with minimal SSIM impact, indicating object position is represented in the diffusion transformer.

## Key Takeaways
- RigidBench separates motion, geometry, identity, background stability, and visual similarity into distinct measurements using per‑frame masks, depth, 6‑DoF trajectories, and contact data.  
- The benchmark demonstrates that higher SSIM often accompanies larger 3D trajectory error, revealing a trade‑off between visual fidelity and physical correctness.  
- Fine‑tuning Wan2.2 TI2V-5B with RigidBench’s ground‑truth simulator state improves 3D trajectory accuracy by about twenty percent while preserving visual quality.

## Context
Video generation models aim to produce realistic continuations, but current metrics conflate multiple failure modes such as motion errors and visual artifacts. RigidBench addresses this gap by providing a physics‑grounded evaluation framework that isolates each aspect of realism, offering a more nuanced benchmark for research and industry.

## Implications
For practitioners, RigidBench guides model development toward balanced performance across physical accuracy and visual fidelity. Researchers can leverage the fine‑tuned Wan2.2 TI2V-5B as a baseline to improve 3D motion without sacrificing image quality, advancing both AI research and practical video generation applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15555v1)
