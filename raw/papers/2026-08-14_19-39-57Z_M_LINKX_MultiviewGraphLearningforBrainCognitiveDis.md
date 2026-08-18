---
title: M-LINKX: Multiview Graph Learning for Brain Cognitive Disease Detection
published: 2026-08-14T19:39:57Z
authors: An Phan, Yufei Jin, Xingquan Zhu
url: http://arxiv.org/abs/2608.14847v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# M-LINKX: Multiview Graph Learning for Brain Cognitive Disease Detection

## Abstract
Electroencephalogram (EEG) is a non-invasive and relatively low-cost procedure that measures brain electricity for the detection of cognitive diseases. EEG-based classification of dementia-related conditions, including Alzheimer's disease (AD), mild cognitive impairment (MCI), and frontotemporal dementia (FTD), remains challenging because EEG signals are noisy, non-stationary, and vary across subjects. Segment-based learning provides a practical way to model long EEG recordings by converting them into fixed-length inputs. For each segment, discriminative information may be explored by using signals within each channel (i.e. electrode), as well as interactions between EEG channels. In this paper, we propose M-LINKX, a multi-view graph learning framework for EEG-based dementia classification. For each segment, we extract channel-level node features and construct multiple functional-connectivity (FC) graph views, where each view is defined by a specific combination of connectivity metric, frequency band, and topology filter, respectively. Instead of relying on message passing over the constructed graphs, M-LINKX follows a simple design in modeling node features and adjacency-based connectivity representations. The graph-view representations are fused using global trainable view weights, and subject-level prediction is obtained by averaging segment-level probabilities. Experiments on two three-class EEG datasets with different diagnostic groups, CAUEEG (HC/MCI/Dementia) and AHEAP (HC/AD/FTD), show that M-LINKX achieves the best subject-level performance under the main experimental settings. Our study suggests that multi-view functional connectivity can improve EEG-based dementia classification when integrated with an appropriate graph-learning architecture. Code and data are available at https://github.com/anphantt/MLINKX.

## Metadata
- **Published**: 2026-08-14T19:39:57Z
- **Authors**: An Phan, Yufei Jin, Xingquan Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14847v1)