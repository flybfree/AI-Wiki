---
title: Rethinking Pre-Training and Augmentation for Zero-Shot Cross-City Object Detection
published: 2026-08-25T07:16:42Z
authors: Long Hoang Pham, Quoc Pham-Nam Ho, Huy-Hung Nguyen, Duong Nguyen-Ngoc Tran, Ngoc Doan-Minh Huynh, Cu Quoc Le, Hoang-Khang Nguyen, Hyung-Min Jeon, Chi Dai Tran, Son Hong Phan, Duong Khac Vu, Trinh Le Ba Khanh, Jae Wook Jeon
url: http://arxiv.org/abs/2608.24154v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Pre-Training and Augmentation for Zero-Shot Cross-City Object Detection

## Abstract
Real-world deployment of traffic surveillance systems is bottlenecked by geographic domain shift, in which models trained in one city underperform when applied to an unseen target city. Conventional domain adaptation relies on hyperparameter-sensitive architectures or direct profiling of target data. Both are fundamentally precluded in privacy-conscious ecosystems that require completely blind training and evaluation loops. In this setting, we explore the effects of pre-training and augmentation in addressing the domain shift problem. Specifically, we propose a new modular training pipeline for object detection structured around two core orthogonal pillars: (1) a multi-dataset pre-training strategy featuring a class-agnostic objectness distillation to decouple structural vehicle geometry from semantic taxonomies, and (2) a domain-resilient augmentation stream featuring a novel Grayworld transformation that forces global attention heads to strip volatile chromatic shortcuts in favor of robust shape priors. When evaluated with the real-time transformer-based detector RF-DETR, our framework bridges cross-city distribution gaps while using limited GPU memory (16GB). Our optimized variants, RF-DETR-HR and RF-DETR-Grayworld, deliver a substantial empirical gain of +24.29 over the baseline, achieving 1st place (47.53 mAP) on the AI City Challenge Track 6 leaderboard. Code and data are available at: \href{https://github.com/SKKUAutoLab/aic26_cross_city}{SKKUAutoLab/aic26\_cross\_city}.

## Metadata
- **Published**: 2026-08-25T07:16:42Z
- **Authors**: Long Hoang Pham, Quoc Pham-Nam Ho, Huy-Hung Nguyen, Duong Nguyen-Ngoc Tran, Ngoc Doan-Minh Huynh, Cu Quoc Le, Hoang-Khang Nguyen, Hyung-Min Jeon, Chi Dai Tran, Son Hong Phan, Duong Khac Vu, Trinh Le Ba Khanh, Jae Wook Jeon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24154v1)