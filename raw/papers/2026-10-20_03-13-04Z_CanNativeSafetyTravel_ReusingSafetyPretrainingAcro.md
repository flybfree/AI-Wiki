---
title: Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation
published: 2026-10-20T03:13:04Z
authors: Bingqi Shang, Yang Zhang, Yiwei Chen, Changsheng Wang, Shiyu Chang, Bingquan Shen, Sijia Liu
url: http://arxiv.org/abs/2610.27555v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation

## Abstract
Safety pretraining has emerged as a promising paradigm for embedding safety deeply into a model during pretraining, yielding robustness to subsequent fine-tuning that conventional safety post-training often lacks. We refer to this safety acquired during model pretraining as native safety. Yet native safety is expensive to acquire, confined to the model in which it was pretrained, and often accompanied by lower general utility. In this work, we rethink the practical value of safety-pretrained models and introduce, for the first time, the native safety reuse problem: Can native safety be transferred from a specialized, potentially smaller, safety-pretrained "teacher" to standard-pretrained "students," enabling them to inherit its robustness while preserving their general utility? We show that native safety can "travel" through on-policy distillation. A standard-pretrained student generates responses to safety-pretraining prompts, while a small safety-pretrained teacher supervises the student's token-level predictions along its own generated trajectories; cross-tokenizer alignment further enables transfer across model families. The resulting students exhibit substantially greater safety robustness than their safety-post-trained counterparts while retaining higher general utility than the teacher: subsequent fine-tuning raises the average attack success rate (ASR) of the 1.7B student by only 5.00%, compared with 11.58% for safety post-training, and its average utility of 48.20% far exceeds the aligned teacher's 27.42%. Unlike conventional large-to-small knowledge distillation, our framework enables selective, small-to-large safety transfer: it reuses the robust safety expertise of a smaller pretrained teacher without inheriting its utility limitations. These findings establish native safety as a reusable model property rather than one permanently tied to the originally pretrained model.

## Metadata
- **Published**: 2026-10-20T03:13:04Z
- **Authors**: Bingqi Shang, Yang Zhang, Yiwei Chen, Changsheng Wang, Shiyu Chang, Bingquan Shen, Sijia Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27555v1)