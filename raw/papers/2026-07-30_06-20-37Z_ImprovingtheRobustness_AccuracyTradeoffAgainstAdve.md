---
title: Improving the Robustness/Accuracy Tradeoff Against Adversarial Attacks Using Information Bottleneck Distillation Through Dual Teachers
published: 2026-07-30T06:20:37Z
authors: Vincent Ryusuke Takahashi, Yoshinari Takeishi, Jun'ichi Takeuchi, Kave Salamatian
url: http://arxiv.org/abs/2607.27737v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving the Robustness/Accuracy Tradeoff Against Adversarial Attacks Using Information Bottleneck Distillation Through Dual Teachers

## Abstract
Deep neural networks (DNNs) have achieved remarkable success in classical machine learning problems. However, they are known to be vulnerable to adversarial attacks. Countermeasures proposed in the literature, notably Information Bottleneck Distillation (IBD) introduced by Kuang et al., degrade the classification accuracy on clean inputs while improving the robustness to adversarial inputs. In this work, we extend the IBD framework by introducing an extra teacher model (clean teacher) trained with only clean inputs, into the distillation process from a robust teacher model trained by adversarial training. The features of both clean and robust teachers are transferred to the student through a cross-layer attention matrix. Experimental results on the CIFAR-10 and CIFAR-100 datasets show that the proposed method improves classification accuracy on clean samples compared to the original IBD, while maintaining similar accuracy on adversarial samples. Furthermore, our methods are competitive with state-of-the-art approaches, including the recent dual-teacher distillation framework B-MTARD, particularly in terms of the harmonic mean between clean and robust accuracy. We also analyze the impact of different training settings that have different influences on the attention module.

## Metadata
- **Published**: 2026-07-30T06:20:37Z
- **Authors**: Vincent Ryusuke Takahashi, Yoshinari Takeishi, Jun'ichi Takeuchi, Kave Salamatian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27737v1)