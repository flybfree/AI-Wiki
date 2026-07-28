---
title: Semantic Semi-Incremental Data-Association-Free Object SLAM
published: 2026-07-25T22:31:31Z
authors: Yihao Zhang, Jungseok Hong, John J. Leonard
url: http://arxiv.org/abs/2607.23384v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Semantic Semi-Incremental Data-Association-Free Object SLAM

## Abstract
Data association between landmark measurements and landmark variables has long been a central challenge in SLAM, as estimation accuracy depends critically on associating measurements with the correct landmark variables. Recent advances in deep learning have created new opportunities for the problem; data association can now leverage not only positional measurements but also semantic information about object landmarks, such as class labels from neural object detectors and feature vectors from visual foundation models. In this paper, we present a generalized data-association-free SLAM framework that jointly estimates data associations, robot poses, landmark positions, and landmark semantics from odometry, and positional and semantic measurements of landmarks. The proposed framework (i) creates a synergy between data association and landmark semantics estimation; (ii) adopts a semi-incremental estimation scheme for improved accuracy and computational efficiency; and (iii) provides a principled justification, guidelines, and heuristics for landmark-number estimation, improving the interpretability and practical usability of the framework. The proposed framework and algorithms are evaluated on synthetic and real-world datasets with two types of semantic information, class labels and real-valued feature vectors, and demonstrate superior performance compared to strong baselines.

## Metadata
- **Published**: 2026-07-25T22:31:31Z
- **Authors**: Yihao Zhang, Jungseok Hong, John J. Leonard
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23384v1)