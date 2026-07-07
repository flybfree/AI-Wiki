---
title: WeightCLIP: Aligning Datasets and Models for Weight Space Learning
published: 2026-07-03T18:27:18Z
authors: Aron Asefaw, Konstantinos Tzevelekakis, Damian Falk, Léo Meynent, Damian Borth
url: http://arxiv.org/abs/2607.03551v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WeightCLIP: Aligning Datasets and Models for Weight Space Learning

## Abstract
Weight space learning aims to learn representations of neural network (NN) weights, enabling different downstream tasks. Existing approaches show promising performance, but lacking a way to shape these weight-space representations using information about the datasets the models were trained on, thus limiting downstream applications. We propose WeightCLIP, a method for learning a dataset-aligned latent space for neural networks, where datasets information is induced during training. The NNs are encoded as latent representations using an autoencoder, while dataset samples are encoded using a dataset encoder. The two representations are aligned using a contrastive objective, effectively reshaping the weight-space representations according to the datasets. We demonstrate that such representations can be used for different downstream tasks, including mapping dataset information to a weight-space representation that decode to strong models. In addition, we introduce a latent refinement process for generating models that outperforms standard fine-tuning. Overall, our results demonstrate that explicitly incorporating dataset information improves what can be achieved with weight-space representations across retrieval, generation, and refinement. Code will be available at https://github.com/HSG-AIML/WeightCLIP.

## Metadata
- **Published**: 2026-07-03T18:27:18Z
- **Authors**: Aron Asefaw, Konstantinos Tzevelekakis, Damian Falk, Léo Meynent, Damian Borth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03551v1)