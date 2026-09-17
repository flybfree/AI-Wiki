---
title: Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents
published: 2026-09-15T18:19:48Z
authors: Caiqi Zhang, Xiaochen Zhu, Chengzu Li, Yulong Chen, Dharshan Kumaran, Nigel Collier
url: http://arxiv.org/abs/2609.17708v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents

## Abstract
Reliable confidence estimation is increasingly central to the trustworthy deployment of language models: a calibrated estimate of the probability that an output is correct decides what to ship, what to escalate, and what to retry. Existing confidence estimators, however, share one design premise: they only read the current inference process, either by introspecting on it, scoring its token probabilities, or resampling it. We argue that the current inference is not a sufficient basis for confidence. We propose XConf (eXperiential Confidence): estimating confidence together with the model's accumulated experience. The experience is stored as a record of the model's own graded past episodes, each holding the task, the model's reflection, its stated confidence, the outcome, and a lesson written once the grade arrived. Given a new task, XConf's Recall stage retrieves past episodes on similar tasks met with a similar stated confidence, and reads off their historical success rate; its Reflect stage shows the model this record, has it name its recurring failure mode, and restate a confidence now informed by its own track records. Our estimator is format-general, requiring no logit access or weight updates, and costs only one answer generation. Across nine benchmarks spanning reasoning, coding, multimodal QA, and interactive agents, and four models from three families, XConf beats or matches ten-sample self-consistency in discrimination (AUROC) on 23 of 24 comparisons, with much lower calibration error (ECE), at a tenth of the generation cost. Used for selective prediction, abstaining on the 10% least-confident episodes raises the delivered success rate by up to 8.7 points on agent tasks. We therefore see experiential confidence estimation as a new paradigm for future general-purpose confidence estimation.

## Metadata
- **Published**: 2026-09-15T18:19:48Z
- **Authors**: Caiqi Zhang, Xiaochen Zhu, Chengzu Li, Yulong Chen, Dharshan Kumaran, Nigel Collier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17708v1)