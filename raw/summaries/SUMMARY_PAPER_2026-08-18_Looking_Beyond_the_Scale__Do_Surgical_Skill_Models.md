---
title: Looking Beyond the Scale: Do Surgical Skill Models Learn Transferable Representations Across Assessment Rubrics?
url: http://arxiv.org/abs/2608.17519v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_08-44-31Z_LookingBeyondtheScale_DoSurgicalSkillModelsLearnTr.md
generated_at: 2026-08-18 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether vision-based surgical skill models learn representations that can transfer across different assessment rubrics such as GOALS and OSATS using the LASANA and JIGSAWS datasets. It compares supervised training, ASAM, self-supervised contrastive learning and augmentation methods to see if cross-rubric skill transfer is possible. The results show that models trained on one scale can perform well on the other when supervision aligns, but fail otherwise.

## Key Takeaways
- Backbones pretrained on JIGSAWS achieve CCC values of 0.77 to 0.80 on LASANA, matching end-to-end training, indicating transfer is feasible under consistent supervision.
- Transfer to JIGSAWS fails across all methods due to annotation inconsistencies between the datasets.
- Control experiments reveal that task-specific heads carry most skill prediction burden while the backbone only needs adequate spatiotemporal features.

## Context
Vision-based surgical skill assessment models are widely used but their ability to generalize beyond a single scoring system remains unclear. This study addresses a gap by systematically testing cross-rubric transfer, providing empirical evidence on what limits such generalization in medical imaging AI.

## Implications
For clinicians and developers, the findings suggest that aligning annotation standards is crucial for reliable skill transfer between assessment tools. Practitioners should focus on head design and ensure consistent visual data across scales to maximize model utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17519v1)
