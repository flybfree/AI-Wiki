---
title: Similarity-Aware Machine Unlearning
published: 2026-07-31T19:41:55Z
authors: Madhavan Citalamangalam Kumaran, Midhun Parakkal Unni, Vicky Kouni, Haripriya Harikumar
url: http://arxiv.org/abs/2608.00246v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Similarity-Aware Machine Unlearning

## Abstract
Machine unlearning removes the influence of user-specified training examples from a trained model, avoiding the need to retrain it from scratch. Localization-based methods improve unlearning efficiency by identifying a subset of influential model parameters. However, existing approaches select parameters based solely on forget-set importance, neglecting their role in retained dataset and often causing collateral damage to semantically similar retained examples. We address this limitation with a retain-aware localization method that considers parameter importance to both forgotten and retained data. We also introduce a retain-similar evaluation set, constructed using cosine similarity in the model embedding space, to directly measure collateral damage. Across eleven experimental settings on CIFAR-10 dataset and ResNet18 model, our method consistently reduces collateral damage while improving standard unlearning metrics, demonstrating the effectiveness of retain-aware localization for similarity-aware machine unlearning.

## Metadata
- **Published**: 2026-07-31T19:41:55Z
- **Authors**: Madhavan Citalamangalam Kumaran, Midhun Parakkal Unni, Vicky Kouni, Haripriya Harikumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00246v1)