---
title: Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration
published: 2026-08-01T19:15:17Z
authors: Yizhou Wu, Yuheng Li, Xiaofeng Yang, Chih-Wei Chang
url: http://arxiv.org/abs/2608.00831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration

## Abstract
Head-and-neck (HN) proton therapy is highly sensitive to anatomical change over a 4-to-6-week course, as tumor shrinkage, weight loss, and setup variation can misposition the Bragg peak near critical organs such as the parotids, oral cavity, brainstem, and spinal cord, leading to target underdosing or organ-at-risk overdosing. Online adaptive proton therapy replans on the anatomy of the day, yet standard workflows rely on offline replanning that requires repeated CT acquisition and roughly a week of preparation, adding burden, cost, and delay. We investigate whether a patient's treatment-day anatomy can be predicted before image acquisition by transferring longitudinal change from a population database. We propose a digital-twin framework built on a pretrained foundation-model deformable registration network used without patient-specific training. A first registration aligns a prior patient's planning CT to the target and carries the prior's during-treatment quality assurance CT (QACT) into the target frame; a second registration estimates the prior's planning-to-QACT change, which is then applied to the target's own planning CT to synthesize predicted CTs (pdCTs) with propagated contours. Using 88 HN patients, each with a planning CT and three QACTs, we show that pdCTs better match treatment-day anatomy than the static planning CT. Compared with the planning CT alone, normalized cross-correlation improves by 22.8%, Dice for organs-at-risk by 20.2%, and CT-number error decreases by 23.4%. Gains are largest for patients with major anatomical change and negligible when anatomy is stable. This cross-patient motion transfer leverages the digital-twin concept to anticipate treatment-day anatomy, enabling personalized online adaptive proton therapy without repeated imaging.

## Metadata
- **Published**: 2026-08-01T19:15:17Z
- **Authors**: Yizhou Wu, Yuheng Li, Xiaofeng Yang, Chih-Wei Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00831v1)