---
title: A Parameter-Free Few-Shot Evaluation for Elephant Vocalisation Classification
published: 2026-08-14T18:54:24Z
authors: Christiaan M. Geldenhuys, Thomas R. Niesler
url: http://arxiv.org/abs/2608.14824v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Parameter-Free Few-Shot Evaluation for Elephant Vocalisation Classification

## Abstract
We present a parameter-free episodic evaluation of nearest-centroid classification for elephant vocalisations on fixed pretrained acoustic embeddings, across the Elephant Voices (EV) and Linguistic Data Consortium (LDC) datasets. Rather than asking which embedding yields the best classifier when trained on all available labelled data, we ask how the simplest classifier performs as labelled exemplars per class are varied. Each class is represented by the mean of its support-set embeddings, and each query is assigned to the nearest centroid under squared Euclidean distance. We evaluate this centroid classifier on the Perch (ver. 1), Perch (ver. 2), and HuBERT (base, layer 2) embeddings, together with mel frequency cepstral coefficient (MFCC) features, in an N-way k-shot manner under the same cross-validation protocol as the trained baselines. A bootstrap over 100 resampled support sets quantifies the sampling noise. On the smaller, low-resource EV dataset, the centroid classifier using the stronger Perch (ver. 1) and Perch (ver. 2) embeddings overtakes the fully-trained logistic regression classifier from a single exemplar per class and the stronger recurrent classifier from two. Over the reduced set of call types on which the strongly-supervised end-to-end baseline was trained, the centroid classifier matches and then surpasses that baseline in mean average precision (mAP), from a few exemplars per class. On the larger LDC dataset, where labelled exemplars are abundant, the trained baselines retain their advantage at every k considered. At five exemplars per class, the centroid classifier using the strongest embedding, Perch (ver. 2), attains a mAP of 0.542 on the EV dataset and 0.368 on the LDC dataset. Parameter-free nearest-centroid classification is the stronger choice when labelled exemplars are few and the fixed embedding already encodes the features that separate the call types.

## Metadata
- **Published**: 2026-08-14T18:54:24Z
- **Authors**: Christiaan M. Geldenhuys, Thomas R. Niesler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14824v1)