---
title: Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable
published: 2026-08-27T10:59:03Z
authors: Zhichen Dong, Zhixuan Liu, Yuyu Fan, Xiangtian Li, Shuyang Zhang, Chao Yang
url: http://arxiv.org/abs/2608.26958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable

## Abstract
Scaling model-generated data is usually viewed as improving distillation: more examples should increase coverage, reduce noise, and produce stronger students. We show a second effect: larger datasets can make subtle teacher-specific signals easier to detect in the trained student, even when examples are off-task and never mention the trait. In a controlled setup inspired by subliminal learning, a teacher induced to express a target trait generates restricted off-task data, such as number-only completions. Students trained on different amounts of independent off-task data are evaluated in a separate domain, with matched no-trait controls isolating target-specific transfer. Our main finding is that larger independent datasets make the teacher's induced trait stand out more clearly in the student's later behavior. Other plausible traits may also strengthen with scale, but the target usually grows more. When the small-scale student already favors the target, scaling mainly amplifies that behavior; when it favors a related or salient alternative, more data can shift behavior toward the intended trait. Analyses of learned LoRA updates show a parallel trend. These effects appear across model families, trait types, multi-trait settings, and cross-model transfer. Our results suggest that scaling generated distillation data should be paired with trait-aware curation and evaluation, even when the data appears off-task or benign.

## Metadata
- **Published**: 2026-08-27T10:59:03Z
- **Authors**: Zhichen Dong, Zhixuan Liu, Yuyu Fan, Xiangtian Li, Shuyang Zhang, Chao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26958v1)