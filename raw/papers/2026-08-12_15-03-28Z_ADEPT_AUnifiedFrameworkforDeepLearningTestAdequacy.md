---
title: ADEPT: A Unified Framework for Deep Learning Test Adequacy
published: 2026-08-12T15:03:28Z
authors: Yidi Kao, Shawn Burnham, Tommi Rose Fahy, Ali Ghanbari
url: http://arxiv.org/abs/2608.12144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ADEPT: A Unified Framework for Deep Learning Test Adequacy

## Abstract
Over the past decade, many test adequacy metrics have been proposed for deep learning that characterize test dataset adequacy from different perspectives, e.g., neuron activation behavior, latent feature coverage, decision-boundary exploration, etc. However, these metrics are typically released as independent research prototypes with substantially different installation and preprocessing requirements, execution workflows, and configuration mechanisms. These complications make them quite difficult to reproduce, compare, and adopt in research work and practical deployment alike. In this paper, we present the engineering details of ADEPT, a framework that integrates representative adequacy techniques, including neuron-coverage-based metrics, surprise adequacy, input distribution coverage, boundary coverage, and source- and model-level mutation score, under a consistent execution workflow. ADEPT provides a template-based metric interface with well-defined extension points for integrating new adequacy metrics. Furthermore, it provides YAML-based configuration management, preprocessing-cache reuse, and structured result reporting, making it easy to use in any research and development workflows. ADEPT is designed for researchers and practitioners who wish to reproduce and apply adequacy metrics without spending days or weeks implementing missing tooling or configuring disparate research prototypes. A demo video is available at https://aub.ie/ADEPT_video.

## Metadata
- **Published**: 2026-08-12T15:03:28Z
- **Authors**: Yidi Kao, Shawn Burnham, Tommi Rose Fahy, Ali Ghanbari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12144v1)