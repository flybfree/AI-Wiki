---
title: FedSLIM: Privacy-Preserving Federated MDL-Based Descriptive Pattern Mining Across Data Silos
published: 2026-07-25T14:45:00Z
authors: Samar Samir Khalil, Noha S. Tawfik, Marco Spruit
url: http://arxiv.org/abs/2607.23236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedSLIM: Privacy-Preserving Federated MDL-Based Descriptive Pattern Mining Across Data Silos

## Abstract
Federated learning has achieved considerable success for predictive modelling, yet federated descriptive analytics remains largely unexplored. Existing federated pattern mining approaches are predominantly support-based and do not optimise a principled global objective such as Minimum Description Length (MDL). We introduce FedSLIM, the first federated MDL-based framework for descriptive pattern mining. Building on the SLIM principle, FedSLIM enables collaborative optimisation of compact pattern models across distributed databases without sharing raw transactions. We propose two complementary variants that balance privacy, communication, and optimisation fidelity under different deployment assumptions. To evaluate federated MDL mining, we introduce fidelity and discovery-oriented metrics that quantify agreement with a centralised baseline and assess recovery of globally informative patterns. Experiments on multiple real-world datasets under IID and non-IID partitioning show that both variants preserve high-quality compression structure while requiring orders of magnitude less search than the centralised baseline. We further reveal a local-global discovery gap in distributed MDL mining, where globally compressive patterns may be undiscoverable through isolated local optimisation. Both variants recover globally informative patterns absent from all standalone local models, demonstrating the benefits of federated optimisation beyond independent local mining. These results establish federated MDL mining as a practical foundation for privacy-preserving descriptive analytics across distributed data silos.

## Metadata
- **Published**: 2026-07-25T14:45:00Z
- **Authors**: Samar Samir Khalil, Noha S. Tawfik, Marco Spruit
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23236v1)