---
title: Logit-Origin Centering for Singleton Test-Time Adaptation
published: 2026-08-02T08:18:56Z
authors: Mayank Sharma, Rohit Kumar Mourya, Pratik Mazumder
url: http://arxiv.org/abs/2608.01074v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Logit-Origin Centering for Singleton Test-Time Adaptation

## Abstract
Tabular data is used extensively in many real-world use cases. Deep learning models have been developed to deal with tabular data, but generally perform poorly when the test data distribution differs from that of the training data. Researchers have proposed test-time adaptation approaches to deal with this problem. The fully test-time adaptation (FTTA) setting involves adapting deployed classifiers to shifted target distributions using only unlabeled test data. Leading FTTA methods inherit a batch-dependent approach from computer vision literature. This paper demonstrates for the first time that such approaches degrade sharply in strict streaming regimes where examples arrive and must be classified one at a time. This occurs because at a batch size of one, batch-level statistics become unavailable or poorly estimated. We argue that singleton tabular FTTA is not merely a small-batch variant of ordinary FTTA, but a distinct identifiability problem where only the location of the model's score stream remains directly observable. To address this, we propose Prequential Logit-Origin Centering (PLOC), a lightweight approach that keeps the source model frozen and shifts the logit space at each step. PLOC stores only a single running number (the mean of past logits), requires no labels, estimates no priors, and bypasses weight updates entirely. A deferred variant applies a static shift that preserves the source ranking, and thus the AUROC, exactly. Evaluated across five tabular benchmarks, three architectures (MLP, FT-Transformer, and TabTransformer), and five independent source checkpoints, PLOC significantly outperforms strong tabular and entropy-based baselines.

## Metadata
- **Published**: 2026-08-02T08:18:56Z
- **Authors**: Mayank Sharma, Rohit Kumar Mourya, Pratik Mazumder
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01074v1)