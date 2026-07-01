---
title: Automated Background Swapping for Robustness against Spurious Backgrounds
published: 2026-06-30T17:50:24Z
authors: Cesar Roder, Kajetan Schweighofer
url: http://arxiv.org/abs/2606.32018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automated Background Swapping for Robustness against Spurious Backgrounds

## Abstract
Classifiers based on Deep Neural Networks exhibit strong performance across domains, yet can fail catastrophically if they rely on spurious correlations, i.e., features that are predictive of the target label in the training data but are not causally linked and thus fail to generalize. For the vision domain, many such spurious correlations manifest themselves within the background of the image, where only the foreground is predictive of the class label. In this paper, we introduce Automated Background Swapping (AutoBackSwap) to reduce the reliance of classifiers on such spurious backgrounds. AutoBackSwap uses a secondary network to disentangle the foreground and background, followed by infilling to synthesize complete backgrounds, and finally combines different foregrounds and inpainted backgrounds to augment the training data. We find that patch-wise labeling of just a few hundred samples suffices to train the secondary network and automatically augment the full training dataset on challenging image classification tasks. In contrast to many previous methods, AutoBackSwap proves very effective even if there is not a single sample in the training data breaking the spurious correlation. Across a range of image classification tasks with spurious backgrounds, AutoBackSwap consistently outperforms prior methods.

## Metadata
- **Published**: 2026-06-30T17:50:24Z
- **Authors**: Cesar Roder, Kajetan Schweighofer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.32018v1)