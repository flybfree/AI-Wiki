---
title: Crayotter: Learning Long-Horizon Video Editing Agents via Group-Relative Preference Backpropagation
published: 2026-08-03T10:41:25Z
authors: Lecheng Yan, Jianze Lin, Yichong Zhang, Ben Pan, Wenxi Li, Chenyang Lyu, Liting Zhou, Cathal Gurrin
url: http://arxiv.org/abs/2608.02694v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Crayotter: Learning Long-Horizon Video Editing Agents via Group-Relative Preference Backpropagation

## Abstract
Long-horizon video editing agents receive final-product feedback only after many interdependent decisions. Yet editing quality is subjective, admits multiple valid solutions, and is not meaningfully calibrated across heterogeneous requests, making a global scalar objective both ambiguous and temporally uninformative. Our key observation is that fixing the request, materials, and production constraints converts this subjective objective into an ordinal comparison among directly comparable alternatives. We introduce Group-Relative Preference Backpropagation (GRPB), which transforms same-task rankings into zero-sum advantages and redistributes them as bounded credit over semantic editing segments. A lagged allocator and guarded transmission prevent current judgments or unreliable estimates from directly shaping the same rollout group. We manually construct a project-disjoint, horizon-stratified suite of realistic editing tasks for training and controlled evaluation. Across matched baselines, credit interventions, external benchmarking, and blinded human evaluation, GRPB improves both editing behavior and rendered products. The resulting 9B Crayotter model surpasses several proprietary systems on AgenticVBench, supporting task-local preference reduction as a practical approach to learning from subjective, delayed outcomes. Code and all supporting materials are publicly available at https://github.com/idwts/Crayotter.

## Metadata
- **Published**: 2026-08-03T10:41:25Z
- **Authors**: Lecheng Yan, Jianze Lin, Yichong Zhang, Ben Pan, Wenxi Li, Chenyang Lyu, Liting Zhou, Cathal Gurrin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02694v1)