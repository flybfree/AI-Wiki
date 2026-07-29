---
title: Image Quality Dependent Degradation for AI Systems
published: 2026-07-28T14:00:38Z
authors: Yannick Kees, Elena Hoemann, Frank Köster, Sven Hallerbach
url: http://arxiv.org/abs/2607.25736v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Image Quality Dependent Degradation for AI Systems

## Abstract
Perception is one of the primary applications where neural networks outperform conventional algorithms. One example is AI systems for automated driving, which can detect pedestrians based on image data and avoid them accordingly. A substantial challenge with these AI systems is that their output depends heavily on the quality of the input images. For example, if an image is of inferior quality due to heavy contamination, such as noise or darkness, accurate predictions are hardly feasible. Additionally, various types of errors can occur, each with varying relevance to the trustworthiness of the underlying AI system. In particular, it may be more critical not to detect an existing person than to detect a person where there is none. Therefore, we want to show that we can still avoid the most critical errors in situations of inferior image quality. To achieve this, we aim to establish a fail-degraded system by lowering the network's confidence threshold based on the estimated image quality, enabling it to detect objects more cautiously in uncertain situations. Additionally, we present a novel method for estimating the quality of incoming images by comparing them to the training data using normalizing flows. We will also conduct experiments applying our method to state-of-the-art object detection. In summary, we will present a design strategy for AI-based systems in automated driving that can deal with poor-quality input data without resorting to fallback solutions. Such measures enhance trust in AI-based systems and lead to an increased provision of the AI component.

## Metadata
- **Published**: 2026-07-28T14:00:38Z
- **Authors**: Yannick Kees, Elena Hoemann, Frank Köster, Sven Hallerbach
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25736v1)