---
title: DocIntent: Answerability-Guided Agentic Restoration for Real-World Document Visual Question Answering
published: 2026-08-29T04:07:41Z
authors: Zihan Huang, Shihang Wu, Junle Liu, Peirong Zhang, Yongxin Shi, Xuhan Zheng, Lianwen Jin
url: http://arxiv.org/abs/2608.29037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DocIntent: Answerability-Guided Agentic Restoration for Real-World Document Visual Question Answering

## Abstract
Real-world degradations such as blur, shadow, distortion, and moire patterns severely impair the document question-answering capabilities of Multimodal Large Language Models (MLLMs). Applying restoration tools before Visual Question Answering (VQA) is an intuitive solution. However, existing restoration approaches remain limited, as manually designing and executing restoration strategies is labor-intensive and requires domain expertise. Agentic restoration offers new possibilities for automation, yet existing frameworks primarily target natural images and pursue perceptual quality, overlooking that restoration should serve downstream tasks rather than optimize generic image quality metrics. To this end, we explore the value of agentic restoration for real-world degraded document VQA and propose DocIntent, a training-free Answerability-Guided Agentic Restoration framework. DocIntent first assesses question answerability, then identifies task-relevant degradations and selectively invokes restoration tools. A Comparison-Based Rollback mechanism validates each restoration step and reverts it when question-relevant evidence becomes less decipherable. The entire process requires no additional pretrained degradation classifier or image quality assessment model. Extensive experiments on the WildDoc benchmark show that DocIntent consistently improves the average score and consistency of different open- and closed-source MLLMs. The code and experimental data will be publicly available.

## Metadata
- **Published**: 2026-08-29T04:07:41Z
- **Authors**: Zihan Huang, Shihang Wu, Junle Liu, Peirong Zhang, Yongxin Shi, Xuhan Zheng, Lianwen Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29037v1)