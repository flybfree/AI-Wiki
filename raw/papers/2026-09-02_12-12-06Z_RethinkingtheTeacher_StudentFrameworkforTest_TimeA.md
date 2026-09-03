---
title: Rethinking the Teacher-Student Framework for Test-Time Adaptation
published: 2026-09-02T12:12:06Z
authors: Damian Sójka, Marc Masana, Bartłomiej Twardowski, Sebastian Cygert
url: http://arxiv.org/abs/2609.02507v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking the Teacher-Student Framework for Test-Time Adaptation

## Abstract
Test-Time Adaptation (TTA) has recently emerged as a promising strategy that allows the adaptation of pre-trained models to changing data distributions at deployment time, without access to any labels. To mitigate error accumulation, researchers have widely adopted the teacher-student framework, though its long-term stability is often taken for granted. In this work, we challenge the common strategy of setting the teacher weights to an exponential moving average of the student by showing that error accumulation still occurs, although it is mostly apparent on longer sequences compared to those commonly utilized. We analyze the stability-plasticity trade-off within the teacher-student framework and propose to use an intransigent teacher that does not update its weights. Surprisingly, we show that this simple change allows TTA methods to significantly improve their performance on multiple datasets with longer scenarios and result in increased robustness to changes in hyperparameters. Finally, we show that those changes can be seamlessly and effectively applied to various architectures and experimental setups, including semantic segmentation. The code is available at https://github.com/dmn-sjk/intransigent_teacher.

## Metadata
- **Published**: 2026-09-02T12:12:06Z
- **Authors**: Damian Sójka, Marc Masana, Bartłomiej Twardowski, Sebastian Cygert
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02507v1)