---
title: Leveraging existing sparse point annotations for benthic imagery dense segmentation
published: 2026-08-18T09:22:31Z
authors: Cesar Borja, Breck A. McCollum, Jarret E. Byrnes, Kenneth Sebens, Ana C. Murillo
url: http://arxiv.org/abs/2608.17561v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leveraging existing sparse point annotations for benthic imagery dense segmentation

## Abstract
The health of marine ecosystems is a critical indicator of global environmental change, yet the physical constraints of underwater observation and the intrinsic challenges of processing marine imagery severely limit the scalability of systematic monitoring. While recent visual foundation models such as the Segment Anything Model (SAM) series show great promise, they still struggle with the fine-grained recognition required in these complex scenarios and still require expert supervision. Our work addresses this gap by bridging state-of-the-art foundation models with existing sparse supervision. Because historical benthic surveys are typically annotated with only a few sparse expert points per image, we utilize these legacy point-labels as visual prompts for SAM2. Our primary contribution is a novel mechanism to automatically identify which of these points are suitable, and which are actively harmful, when used for propagation. By filtering out unreliable points, we extract high-quality pseudo-ground-truth masks capable of training more accurate, fine-grained semantic segmentation models. We demonstrate the effectiveness of our approach on public benthic data and introduce a new, challenging benchmark featuring real-world sparse expert annotations, paving the way for scalable ecological analysis.

## Metadata
- **Published**: 2026-08-18T09:22:31Z
- **Authors**: Cesar Borja, Breck A. McCollum, Jarret E. Byrnes, Kenneth Sebens, Ana C. Murillo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17561v1)