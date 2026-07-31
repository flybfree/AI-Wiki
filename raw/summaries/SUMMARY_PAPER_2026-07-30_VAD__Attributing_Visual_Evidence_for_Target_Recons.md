---
title: VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy Distillation
url: http://arxiv.org/abs/2607.28590v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-43-46Z_VAD_AttributingVisualEvidenceforTargetReconstructi.md
generated_at: 2026-07-30 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Visual Attribution Distillation (VAD) to estimate which teacher corrections are supported by visual evidence in multimodal on-policy distillation. VAD uses counterfactual target reconstruction where the student prefix is paired with relevant visual evidence present and absent, and the change defines a proxy that aligns with visual direction. Experiments show VAD outperforms direct privileged-view distillation and visual-advantage weighting across six fine-grained benchmarks at 4B and 9B scales.

## Key Takeaways
- VAD estimates visually attributable parts of teacher corrections by evaluating centered log-probabilities between evidence present and removed, providing a signed proxy for evidence direction.
- The reconstruction yields an intervention-aligned component that is enriched in task-relevant visual corrections and produces stronger target shifts, especially when evidence refutes a mistaken answer.
- Training with the reconstructed target serves as primary supervision while the teacher acts only as a weak regularizer.

## Context
Multimodal on-policy distillation aims to transfer fine-grained visual knowledge from large language models to smaller students using teacher-generated trajectories. Current methods suffer from source-mixed corrections that blend linguistic priors and teacher effects, limiting effectiveness. VAD addresses this by separating evidence-driven signals from noise.

## Implications
VAD demonstrates that counterfactual target reconstruction can replace or supplement traditional supervision in visual knowledge transfer, offering a more accurate alignment between visual evidence and model updates. This could improve performance of vision-language models and reduce reliance on privileged views, benefiting researchers and industry practitioners seeking efficient fine-tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28590v1)
