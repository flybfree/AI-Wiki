---
title: On the Interaction Between Model Compression and Test-Time Adaptation
published: 2026-09-03T09:49:29Z
authors: Francesco Corti, Dong Wang, Young D. Kwon, Cecilia Mascolo, Olga Saukh
url: http://arxiv.org/abs/2609.03604v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Interaction Between Model Compression and Test-Time Adaptation

## Abstract
Deep neural networks deployed in the wild must be both efficient and adaptable, requiring model compression and test-time adaptation (TTA). While both are well studied in isolation, their interaction remains poorly understood. We systematically analyze how structured compression affects a model's ability to adapt under distribution shift. Using ResNet-18 and ViT-Base on CIFAR-10-C and ImageNet-C, we evaluate multiple compression methods combined with standard TTA techniques. We introduce a diagnostic framework that examines representational expressivity and adaptation subspace compatibility. Our results reveal a consistent gap: although compressed models retain high accuracy under supervised adaptation, their TTA performance degrades significantly with increasing compression. We show that this stems from reduced representational diversity and structural constraints that limit recoverability. These effects strongly depend on the compression method, highlighting the need to design compression strategies that preserve adaptability.

## Metadata
- **Published**: 2026-09-03T09:49:29Z
- **Authors**: Francesco Corti, Dong Wang, Young D. Kwon, Cecilia Mascolo, Olga Saukh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03604v1)