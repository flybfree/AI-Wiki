---
title: Cognitive Graph Intelligence for Adaptive and Robust DDoS Attack Detection in Next Generation Networks
published: 2026-08-18T04:18:31Z
authors: Mohammad Arif Hossain, Yeahia Sarker, Md Jafrin Hossain, Most. Humayra Khanom Rime, Nirwan Ansari
url: http://arxiv.org/abs/2608.17352v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cognitive Graph Intelligence for Adaptive and Robust DDoS Attack Detection in Next Generation Networks

## Abstract
Distributed Denial-of-Service (DDoS) attacks threaten network availability, requiring a cognitive detection process that senses traffic, infers intent, and supports an adaptive response under severe class imbalance and non-stationary conditions. This paper proposes a Graph-based Generative Adversarial Network (GraphGAN) that serves as the cognitive detection engine for this task. GraphGAN captures the relational structure among traffic flows while addressing imbalance through adversarial generation of synthetic samples. Sequential flows are converted into $k$-nearest neighbor graphs using sliding windows to preserve feature-similarity and temporal dependencies among flows. The generator learns the distribution of DDoS attacks to synthesize realistic minority samples, while a Graph Convolutional Network (GCN)-based discriminator distinguishes real from synthetic graph data. A separate GCN classifier, trained on the balanced dataset, performs the final detection decision. Evaluations on four benchmark datasets show that GraphGAN achieves superior accuracy, precision, and recall compared to state-of-the-art approaches, particularly in data-scarce scenarios. By integrating temporal graph construction, adversarial augmentation, and GCN classification, GraphGAN effectively models coordinated attack behaviors and mitigates class imbalance, providing a robust and topology-aware solution for intrusion detection in data-constrained environments.

## Metadata
- **Published**: 2026-08-18T04:18:31Z
- **Authors**: Mohammad Arif Hossain, Yeahia Sarker, Md Jafrin Hossain, Most. Humayra Khanom Rime, Nirwan Ansari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17352v1)