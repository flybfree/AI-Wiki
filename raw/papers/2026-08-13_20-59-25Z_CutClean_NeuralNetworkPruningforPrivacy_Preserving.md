---
title: CutClean: Neural Network Pruning for Privacy-Preserving Inference
published: 2026-08-13T20:59:25Z
authors: Leonardo Magliolo, Vito Paolo Pastore, Giuseppe Valenzise, Enzo Tartaglione
url: http://arxiv.org/abs/2608.13773v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CutClean: Neural Network Pruning for Privacy-Preserving Inference

## Abstract
Neural networks are increasingly deployed in high-stakes applications with growing privacy leakage concerns. We show that this privacy leakage can occur even in the absence of representation imbalances that lead to traditional dataset biases. This poses significant privacy risks when deploying models that process sensitive attributes. In this context, we propose CutClean, a privacy-aware pruning method that allows to reduce privacy information flow through the network, while increasing its sparsity. Our approach employs auxiliary linear privacy heads placed at each network's block to quantify information leakage, and further applies increasing levels of sparsity to remove the private attribute leakage, measured in terms of the accuracy of the privacy head attached to the last block. Experiments on synthetic and real-world datasets demonstrate that our approach effectively minimizes private information flow while achieving high sparsity rates and preserving classification target accuracy.

## Metadata
- **Published**: 2026-08-13T20:59:25Z
- **Authors**: Leonardo Magliolo, Vito Paolo Pastore, Giuseppe Valenzise, Enzo Tartaglione
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13773v1)