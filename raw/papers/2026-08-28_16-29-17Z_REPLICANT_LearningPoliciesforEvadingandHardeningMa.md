---
title: REPLICANT: Learning Policies for Evading and Hardening Malware Detectors
published: 2026-08-28T16:29:17Z
authors: Shae McFadden, Ilias Tsingenopoulos, Mario D'Onghia, Alexander Herzog, Myles Foley, Chris Hicks, Lorenzo Cavallaro, Fabio Pierazzi
url: http://arxiv.org/abs/2608.28499v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REPLICANT: Learning Policies for Evading and Hardening Malware Detectors

## Abstract
To determine the real-world effectiveness of machine learning based malware detection, it is vital to evaluate its robustness against highly capable adversaries. However, state-of-the-art attacks do not effectively model realistic adversaries, as they often assume access to privileged information such as the training data, feature space, or confidence scores of the target. In this work, we present Replicant, a deep reinforcement learning framework that learns the realistic task of evasion under a strict label-only black-box threat model. Replicant learns a reusable policy on how to modify a malware sample and when to query the target, which transfers across samples, detectors, and feature spaces. Across seven Android malware detectors and three feature spaces, Replicant is the strongest and most query-efficient approach achieving a mean attack success rate of 78.8%, a relative improvement of 20.9%-39.2% over the state-of-the-art. Furthermore, when used for adversarial training, Replicant also outperforms the state-of-the art by producing detectors with more generalizable robustness. With Replicant we demonstrate that learning the task of evasion not only results in stronger attack performance but, crucially, provides a better signal for hardening malware detectors.

## Metadata
- **Published**: 2026-08-28T16:29:17Z
- **Authors**: Shae McFadden, Ilias Tsingenopoulos, Mario D'Onghia, Alexander Herzog, Myles Foley, Chris Hicks, Lorenzo Cavallaro, Fabio Pierazzi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28499v1)