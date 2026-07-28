---
title: Source-Free Controlled Adaptation of Teachers for Continual Test-Time Adaptation
published: 2026-07-26T16:06:18Z
authors: Anurag Roy, Riddhiman Moulick, Vinay Kumar Verma, Saptarshi Ghosh, Abir Das
url: http://arxiv.org/abs/2607.23735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Source-Free Controlled Adaptation of Teachers for Continual Test-Time Adaptation

## Abstract
In many real-world scenarios, encountering continual shifts in domain during inference is very common. Consequently, continual test-time adaptation (CTTA) techniques leveraging a teacher-student framework have gained prominence, allowing models to adapt continuously even after deployment. In such a framework, a weight-averaged mean teacher is used to produce pseudo-labels from test data for self-training. The mean teacher gets updated as an exponential moving average of the student parameters using a high value of momentum that is kept fixed even if different distributions of test data are encountered. To combat the resulting drift of the model, we propose a novel controlled teacher adaptation methodology that dynamically sets a proper momentum value depending on the quality of the incoming data. Additionally, we estimate class prototypes from the source pretrained model to help align the target data as they come in. Importantly, our method does not require access to source data or its statistics at any stage of the pipeline, making it truly source-free. We perform extensive experiments on benchmark datasets to demonstrate that our approach outperforms different state-of-the-art adaptation frameworks, many of which require access to source data.

## Metadata
- **Published**: 2026-07-26T16:06:18Z
- **Authors**: Anurag Roy, Riddhiman Moulick, Vinay Kumar Verma, Saptarshi Ghosh, Abir Das
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23735v1)