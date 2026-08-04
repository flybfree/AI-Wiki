---
title: MineGrad: Gradient Inversion Attacks on LoRA Fine-Tuning
published: 2026-08-02T22:18:34Z
authors: Hasin Us Sami, Swapneel Sen, Basak Guler
url: http://arxiv.org/abs/2608.01521v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MineGrad: Gradient Inversion Attacks on LoRA Fine-Tuning

## Abstract
Parameter-efficient fine-tuning (PEFT), such as low-rank adaptation (LoRA), has recently been adopted in federated learning to reduce communication and computation costs. In this setup, users download a pretrained model from the server prior to fine-tuning, and then fine-tune lightweight LoRA modules locally while keeping the pretrained model frozen, sharing only the gradients of the fine-tuning parameters with the server. Despite its growing popularity, robustness of federated fine-tuning against an adversarial server remains underexplored, where the server maliciously tampers with the training protocol to breach the privacy of users' data. In this work, we investigate gradient inversion attacks on LoRA fine-tuning. We propose an analytical attack that enables a malicious server to recover private user data by leveraging a poisoned pretrained model and fine-tuning parameters. Our design embeds fine-tuning data within the shared gradients, to allow the server to analytically reconstruct user data. Unlike prior works, our attack is applicable to both language and vision tasks, does not rely on computationally expensive (adversarial) pretraining with public datasets or require the number of training tokens to be less than the rank of LoRA modules. Experimental results on both language and vision tasks demonstrate high-fidelity data recovery across multiple baselines, revealing several critical vulnerabilities.

## Metadata
- **Published**: 2026-08-02T22:18:34Z
- **Authors**: Hasin Us Sami, Swapneel Sen, Basak Guler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01521v1)