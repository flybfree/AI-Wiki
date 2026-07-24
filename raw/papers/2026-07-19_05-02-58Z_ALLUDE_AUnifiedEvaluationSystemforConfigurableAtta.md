---
title: ALLUDE: A Unified Evaluation System for Configurable Attacks in Differentiable Environments
published: 2026-07-19T05:02:58Z
authors: Mansi Phute, Alexander Greenhalgh, Matthew Hull, Haoran Wang, Alec Helbling, ShengYun Peng, Elliott Faa, Willian Lunardi, Martin Andreoni, Wenke Lee, Duen Horng Chau
url: http://arxiv.org/abs/2607.17077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ALLUDE: A Unified Evaluation System for Configurable Attacks in Differentiable Environments

## Abstract
Adversarial attacks against vision models like object detectors are often evaluated under limited conditions, leaving their performance under-characterized. Bridging simulation and differentiable rendering enables more robust, end-to-end evaluation of these adversarial attacks, yet there is no easy-to-use, unified system that offers a rich set of customizable configurations for adversarial attacks across multiple scenes, objects, environmental and lighting conditions, and camera trajectories. We present ALLUDE, which addresses these gaps, offering first-of-its-kind evaluation capabilities across Linux and Windows. We comprehensively demonstrate ALLUDE's evaluation breadth through a two-pronged strategy: (1) using Latin Hypercube Sampling, we draw a representative subset from 5,400 configurations spanning 10 scene-object pairs, 9 weather conditions, 4 optimizers, 5 camera trajectories, and 3 detection models; (2) we stress-test existing attacks (CAMOU, RAUCA, FCA) under diverse weather conditions and continuous camera trajectories, revealing degradation of attack success across every attack, exposing evaluation gaps in prior work. Through ALLUDE's end-to-end differentiable rendering, adversarial attacks can be optimized against shifting real-world deployment conditions. Our cross-platform code is open source.

## Metadata
- **Published**: 2026-07-19T05:02:58Z
- **Authors**: Mansi Phute, Alexander Greenhalgh, Matthew Hull, Haoran Wang, Alec Helbling, ShengYun Peng, Elliott Faa, Willian Lunardi, Martin Andreoni, Wenke Lee, Duen Horng Chau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17077v1)