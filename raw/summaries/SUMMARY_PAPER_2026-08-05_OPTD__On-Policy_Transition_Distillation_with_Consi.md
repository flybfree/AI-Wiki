---
title: OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models
url: http://arxiv.org/abs/2608.02942v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_23-09-43Z_OPTD_On_PolicyTransitionDistillationwithConsistenc.md
generated_at: 2026-08-05 01:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OPTD, an on‑policy transition distillation method for few‑step diffusion language models that compresses multiple teacher denoising steps into a single student transition while preserving rollout outcomes. By sampling partial states from the student’s own trajectories and ordering future candidates by confidence, OPTD selects the longest prefix whose joint commitment matches the teacher’s rollout. Experiments on reasoning and code‑generation benchmarks show improved quality–efficiency trade‑off and the highest quality‑constrained AUP among few‑step baselines.

## Key Takeaways
- The method relies on on‑policy sampling rather than off‑policy trajectories to avoid context drift that occurs when early parallel commitments alter later predictions.  
- It orders future candidate states by current‑state confidence, ensuring the selected prefix best preserves teacher rollout outcomes while allowing adaptive compression.  
- A set‑bottleneck objective pushes verified candidates to the decoder’s release threshold and a frozen‑teacher KL anchor regularizes all other active positions without requiring gold responses.

## Context
Diffusion language models benefit from parallel token prediction but suffer from long decoding times due to iterative denoising. Few‑step distillation aims to compress many teacher steps into one student transition, yet existing approaches often produce mismatched rollouts that degrade generation quality. OPTD addresses this by aligning the student’s transitions with the teacher’s actual outcomes using on‑policy consistency.

## Implications
This work provides a principled framework for efficient few‑step diffusion decoding that can be applied to any dLLM without retraining, offering faster inference and higher output quality. Practitioners can adopt OPTD to reduce latency in real‑time applications while maintaining strong language generation performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02942v1)
