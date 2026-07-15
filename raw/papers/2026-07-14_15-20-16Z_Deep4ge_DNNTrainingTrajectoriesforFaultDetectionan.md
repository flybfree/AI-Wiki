---
title: Deep4ge: DNN Training Trajectories for Fault Detection and Diagnosis
published: 2026-07-14T15:20:16Z
authors: Sigma Jahan
url: http://arxiv.org/abs/2607.12868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deep4ge: DNN Training Trajectories for Fault Detection and Diagnosis

## Abstract
Deep learning systems often fail due to subtle implementation faults that alter training behavior. Recent work has studied how to detect and diagnose such failures from changes observed across training epochs. However, the software engineering community still lacks a public dataset of per-epoch training runs with documented fault history, feature extraction details, and clear reuse support for fault detection and diagnosis tasks. We present Deep4ge, a controlled benchmark of 14,227 training runs generated from 59 adapted TensorFlow/Keras deep neural network (DNN) programs collected from Stack Overflow. We generated faulty variants using 27 source-code transformations that introduce known faults across seven categories. The dataset contains 9,845 faulty runs and 4,382 correct baseline runs. For each run, we record 4 evaluation metrics and 26 features that measure training behavior at every epoch. These features capture weights, gradients, activations, accuracy and loss trends, learning rate, and hardware use. Deep4ge supports binary fault detection, multi-class fault diagnosis, and early fault prediction from partial training runs. We release the dataset and fault-injection framework at https://doi.org/10.5281/zenodo.20337241.

## Metadata
- **Published**: 2026-07-14T15:20:16Z
- **Authors**: Sigma Jahan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.12868v1)