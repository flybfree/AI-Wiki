---
title: EEG-JEPA: Structured Latent Prediction for EEG Foundation Models
published: 2026-07-31T08:57:53Z
authors: Jinhao Li, Zhiyuan Ma, Xueqiao Han, Zhongye Xia, Xinche Zhang, Shanghong Xie, Yixuan Liu, Yongjian Li, Runmin Gan, Tianlin Huo, Sen Song
url: http://arxiv.org/abs/2608.00114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EEG-JEPA: Structured Latent Prediction for EEG Foundation Models

## Abstract
Electroencephalography (EEG) foundation models aim to learn reusable representations from large-scale unlabeled recordings. A common pretraining strategy is masked waveform reconstruction, but applying supervision directly to noisy EEG may encourage models to recover predictable background activity, acquisition effects, and artifacts rather than neural structure that transfers across tasks. This raises a central question: what should an EEG foundation model predict to learn transferable representations? We introduce EEG-JEPA a structured latent-prediction framework for EEG foundation modeling. Rather than reconstructing masked voltage samples, a masked context encoder and predictor infer contextual latent states produced by an exponential-moving-average target encoder that observes the complete input. EEG-JEPA organizes target design along three complementary dimensions: target content specifies what representation is predicted, target support specifies where prediction occurs over structured electrode--time regions through Neurotopology-Aware Multi-scale Electrode-Temporal Masking (N-MET), and target depth specifies at which encoder layers supervision is applied. Together, these designs shift EEG pretraining from recovering missing measurements to inferring latent states from structured electrode--time context. We evaluate EEG-JEPA through controlled objective comparisons, frozen multitask transfer, and full fine-tuning. Under the same backbone, pretraining corpus, and training duration, EEG-JEPA improves the 14-task frozen macro balanced accuracy from 40.49% to 50.42% over CBraMod-style masked waveform reconstruction. Multi-source continuation further raises this result to 52.94%, the highest average among the EEG foundation models evaluated on EEG-FM-Bench. Under protocol-matched full fine-tuning, EEG-JEPA also improves the nine-task average balanced accuracy from 68.98% to 70.65%.

## Metadata
- **Published**: 2026-07-31T08:57:53Z
- **Authors**: Jinhao Li, Zhiyuan Ma, Xueqiao Han, Zhongye Xia, Xinche Zhang, Shanghong Xie, Yixuan Liu, Yongjian Li, Runmin Gan, Tianlin Huo, Sen Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00114v1)