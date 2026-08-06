---
title: Understanding Fault Tolerance of Adversarially Robust Pruned Models
published: 2026-08-04T19:31:43Z
authors: Manali Dangarikar, Cory Merkel
url: http://arxiv.org/abs/2608.04173v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Fault Tolerance of Adversarially Robust Pruned Models

## Abstract
Deep neural networks (DNNs) deployed on resource-constrained neuromorphic hardware face three concurrent challenges: the need for model compression through pruning, vulnerability to adversarial input perturbations, and susceptibility to hardware-induced weight faults such as stuck-at-zero errors. While each of these factors has been studied in isolation, their combined effects on model reliability have received little attention. This paper presents an empirical investigation of how pruning, adversarial training, and hardware fault injection interact to affect the robustness of convolutional neural networks. Using a compact three-layer CNN trained on MNIST, we conduct three experiments: (1) comparing the fault tolerance of naturally and adversarially trained models under simultaneous hardware faults and adversarial attacks, (2) evaluating how pruning affects adversarial robustness, and (3) characterizing the joint accuracy surface across fault rates, adversarial perturbation magnitudes, and pruning levels. Our results show that adversarial training improves robustness against input perturbations but increases sensitivity to stuck-at-zero weight faults. Contrary to intuition, pruning did not significantly increase fault sensitivity, and varying the pruning level had little effect across fault rates and attack strengths. These results highlight the need to jointly consider adversarial robustness and hardware reliability.

## Metadata
- **Published**: 2026-08-04T19:31:43Z
- **Authors**: Manali Dangarikar, Cory Merkel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04173v1)