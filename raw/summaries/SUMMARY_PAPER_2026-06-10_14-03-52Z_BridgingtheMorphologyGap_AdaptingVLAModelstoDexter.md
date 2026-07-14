---

title: "Summary: Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning"
url: http://arxiv.org/abs/2606.12109v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_14-03-52Z_BridgingtheMorphologyGap_AdaptingVLAModelstoDexter.md
generated_at: "2026-06-11 10:56"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-06-10 14-03-52Z Bridgingthemorphologygap Adaptingvlamodelstodexter


## Summary
The paper introduces InDex, a framework that adapts pre‑trained Vision‑Language‑Action (VLA) models from low‑degree parallel grippers to high‑degree dexterous hands by bridging the morphology gap. By repurposing the 1‑DoF grasp output as a continuous virtual grasp intent proxy and using an intent‑conditioned diffusion head, InDex achieves strong performance with only minimal demonstration data while preserving the original VLA’s spatial reasoning.

## Key Takeaways
- The framework repurposes the 1‑DoF parallel grasp output as a continuous, macroscopic virtual grasp intent proxy to sequentialize the control topology.  
- It employs a two‑stage decoupled learning: the first stage aligns the VLA backbone to predict continuous arm trajectories and a scalar grasp intent; the second stage freezes this spatial backbone and uses an intent‑conditioned denoising diffusion head to decode fine‑grained joint articulations for multi‑fingered end‑effectors.  
- Experiments demonstrate that with minimal demonstration data, InDex outperforms monolithic baselines while maintaining robust spatial generalizability.

## Context
The challenge of transferring low‑DoF robotic manipulation knowledge to high‑DoF dexterous hands is a central bottleneck in VLA applications, often leading to catastrophic forgetting and collapse of the action manifold. This work shows that preserving semantic priors across morphologies can mitigate these issues, offering a more reliable path forward.

## Implications
This approach enables efficient adaptation for multi‑fingered end‑effectors without retraining large models, making it practical for industry deployment where hardware constraints are tight. Practitioners can leverage the intent‑conditioned diffusion head to customize VLA outputs for specific robotic platforms and tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12109v1)
