---
title: Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation
url: http://arxiv.org/abs/2607.24731v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_17-57-02Z_RethinkingClassifier_FreeGuidanceinOn_PolicyDiffus.md
generated_at: 2026-07-27 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how on‑policy distillation (OPD) should be adapted when classifier‑free guidance (CFG) is used in diffusion models. It discovers that simply matching teacher and student guided velocities can lead to under‑identified branch errors, where positive and negative branches cancel each other out. The authors identify a failure mode called Negative Branch Asymmetry (NBA) and propose Positive‑Direction Matching (PDM), which separately constrains the positive prediction and the CFG conditional direction.

## Key Takeaways
- Naive velocity matching can reduce both branch errors only when the teacher’s negative branch shares information with the student, but this benefit disappears if the teacher’s native CFG schema contains privileged knowledge unavailable to the student.  
- The joint reduction of positive and negative errors is a symptom of NBA, which causes antagonistic dynamics that increase one error while decreasing the other.  
- PDM resolves NBA by imposing independent constraints on each branch, leading to more robust knowledge transfer in video control tasks.

## Context
The study addresses a gap in diffusion model training where guidance mechanisms are standard but their interaction with distillation objectives is unclear. Understanding how CFG influences OPD improves the reliability of transferring knowledge from teacher to student models across diverse modalities such as video.

## Implications
For practitioners, PDM offers a practical fix that reduces sensitivity to guidance scale variations and stabilizes training in on‑policy diffusion pipelines. This can lead to faster convergence and higher performance in applications requiring precise control over generated content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24731v1)
