---
title: GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding
published: 2026-08-22T08:04:59Z
authors: Md Abrar Jahin, Md Rizwan Parvez
url: http://arxiv.org/abs/2608.21832v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding

## Abstract
Computer-use agents ground natural-language instructions in screenshots to locate interface elements, yet existing benchmarks do not isolate whether models bind relational language to the correct element. We introduce GUI-Primitives, a 994-item benchmark of contrastive instruction pairs over seven spatial relations in graphical user interfaces (left/right, above/below, containment, alignment, proximity, list ordinal, occlusion). Each pair holds the screenshot and anchor fixed while changing the relation expression, so the correct target moves between two designated candidates. Five annotators validate a 196-item subset ($κ= 0.94$ well-formedness; $κ= 0.79$ target selection). Nineteen vision-language models reach at most $32\%$ strict point-in-box accuracy. Because models emit unconstrained coordinates, we classify each prediction by the candidate region it falls within. Predictions fall outside both candidates on $60-92\%$ of items. Conditional on falling within a candidate region, target selection reaches 0.82-0.90 for horizontal position, vertical position, proximity, and list ordinal, but does not differ significantly from 0.50 for containment and occlusion: most failures reflect candidate localization rather than relation understanding. Across ten models, benchmark accuracy correlates with ScreenSpot-Pro accuracy (Spearman $ρ= +0.74$), an exploratory association at this sample size. Marking the two designated candidates raises selection accuracy by 35--57 percentage points, an oracle diagnostic that supplies the candidate set rather than a deployable method. We release the benchmark, predictions, and code.

## Metadata
- **Published**: 2026-08-22T08:04:59Z
- **Authors**: Md Abrar Jahin, Md Rizwan Parvez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21832v1)