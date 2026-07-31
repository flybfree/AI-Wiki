---
title: Private Face Recognition Training Dataset Publication via Identity-Decoupled and Geometry-Preserving Face Distillation
url: http://arxiv.org/abs/2607.27764v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_07-01-58Z_PrivateFaceRecognitionTrainingDatasetPublicationvi.md
generated_at: 2026-07-30 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Private Face Distillation, a method for publishing private face recognition training datasets by releasing identity‑decoupled proxies that preserve useful geometry. Experiments show the approach improves TAR@FAR to 1e-3 on IJB‑C surveillance while lowering source‑identity linkability compared with baselines.

## Key Takeaways
- The privacy paradox arises because removing identity cues too much destroys class structure, yet preserving them fully increases linkage risk.  
- Private Face Distillation uses Orthogonal Geometry Preservation to keep hyperspherical geometry and Relational Topology Alignment to maintain identity relations for learning.  
- On IJB‑C, the method raises TAR@FAR by 3.94% over baseline datasets while reducing linkability.

## Context
Privacy‑preserving AI training is a growing concern as facial data can directly reveal personal identities. Current solutions often sacrifice model utility or privacy, highlighting a need for balanced approaches that separate source identity from recognition‑useful geometry.

## Implications
For practitioners, Private Face Distillation offers a practical way to release datasets without compromising performance. The field may adopt similar decoupling techniques to advance privacy‑aware machine learning in surveillance and consumer applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27764v1)
