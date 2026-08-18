---
title: Picking the Right Image to Classify: Reliable-Input Selection in Teledermatology
published: 2026-08-17T07:28:26Z
authors: Fabian Gröger, Marco Weishaupt, Philippe Gottfrois, Simone Lionetti, Linda Wermelinger, Nipun Ranasekara, Ludovic Amruthalingam, Alexander A. Navarini, Marc Pouly
url: http://arxiv.org/abs/2608.16198v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Picking the Right Image to Classify: Reliable-Input Selection in Teledermatology

## Abstract
Dermatology models face distribution shifts in teledermatology settings, where submitted images differ from the training data in lighting, angle, distance, focus, and framing. These test-time images are ordinary clinical photographs, but some fall outside the model's training conditions, leading the model to often misclassify them due to shifts in acquisition between training and deployment. When multiple images of the same case exist (several photos of one patient or lesion), a natural way to improve accuracy is therefore to select the image the model is most likely to classify correctly. We call this task reliable-input selection. An oracle that, for each case, selects a correctly classified image when one exists raises weighted F1 by about 20 percentage points on average across six dermatology datasets and nine frozen backbones. This oracle is an upper bound that sees the labels, whereas a selector must choose blindly. Capturing this gain in practice is hard. A selector that needs no pretraining data applies to any frozen model, including those whose data is not public. It must judge reliability from quantities the model exposes at inference: its embeddings, their norms, and its confidence. We benchmark four such training-data-free selectors: the embedding norm, the neighborhood consensus among a case's images, the stability of the prediction under small perturbations, and the model's own confidence. No training-data-free selector substantially narrows this oracle gap. The best of them is the model's own confidence, but it recovers only a small part of the gap on the clinical datasets. A small labeled reference set does not help either: the best selector overall, a fusion of confidence and Mahalanobis distance, still leaves most of the gap. To our knowledge, this is the first study to introduce and benchmark reliable input selection, a clinically important, unsolved task.

## Metadata
- **Published**: 2026-08-17T07:28:26Z
- **Authors**: Fabian Gröger, Marco Weishaupt, Philippe Gottfrois, Simone Lionetti, Linda Wermelinger, Nipun Ranasekara, Ludovic Amruthalingam, Alexander A. Navarini, Marc Pouly
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16198v1)