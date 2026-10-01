---
title: ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation
published: 2026-09-30T08:49:03Z
authors: Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
url: http://arxiv.org/abs/2609.39306v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation

## Abstract
Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving PI-conditioned behavior as the student becomes the next teacher. We introduce Retentive and Selective Augmentation for Iterative Self-Distillation (ReSAIL), a plug-in augmentation for iterative PI-based self-distillation. ReSAIL selects interaction steps where PI most strongly changes the teacher's predictions and balances the resulting distillation losses across trajectories. It also regularizes the student's PI-conditioned output distributions toward those of the frozen teacher at selected and unselected steps to preserve PI-conditioned behavior for supervision in the next cycle. On ALFWorld and TextCraft, ReSAIL sustains substantial gains across model scales over three cycles, with an average absolute gain of 22.5% in final-cycle success rates when added to self-distillation baselines. Sensitivity-guided selection of offline data also improves action prediction accuracy for multimodal GUI agents on AITZ. These findings provide the first evidence that a more robust learning mechanism can effectively mitigate performance collapse in iterative agent self-distillation over deployment trajectories.

## Metadata
- **Published**: 2026-09-30T08:49:03Z
- **Authors**: Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39306v1)