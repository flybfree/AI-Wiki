---
title: Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less
published: 2026-05-07T17:57:02Z
authors: Yuxing Liu, Jianyu Wang, Tong Zhang
url: http://arxiv.org/abs/2605.06654v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less

## Abstract
Optimizers play an important role in both pretraining and finetuning stages when training large language models (LLMs). In this paper, we present an observation that full finetuning with the same optimizer as in pretraining achieves a better learning-forgetting tradeoff, i.e., forgetting less while achieving the same or better performance on the new task, than other optimizers and, possibly surprisingly, LoRA, during the supervised finetuning (SFT) stage. We term this phenomenon optimizer-model consistency. To better understand it, through controlled experiments and theoretical analysis, we show that: 1) optimizers can shape the models by having regularization effects on the activations, leading to different landscapes around the pretrained checkpoints; 2) in response to this regularization effect, the weight update in SFT should follow some specific structures to lower forgetting of the knowledge learned in pretraining, which can be obtained by using the same optimizer. Moreover, we specifically compare Muon and AdamW when they are employed throughout the pretraining and SFT stages and find that Muon performs worse when finetuned for reasoning tasks. With a synthetic language modeling experiment, we demonstrate that this can come from Muon's strong tendency towards rote memorization, which may hurt pattern acquisition with a small amount of data, as for SFT.

## Metadata
- **Published**: 2026-05-07T17:57:02Z
- **Authors**: Yuxing Liu, Jianyu Wang, Tong Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.06654v1)