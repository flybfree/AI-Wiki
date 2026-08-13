---
title: Can Vision Models Read the Radar Display? On the Feasibility of Radar Imagery for Air Traffic Complexity Estimation
published: 2026-08-12T08:53:22Z
authors: Hyewook Kim, Byul Kang, Seokbin Yoon, Keumjin Lee
url: http://arxiv.org/abs/2608.11810v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Vision Models Read the Radar Display? On the Feasibility of Radar Imagery for Air Traffic Complexity Estimation

## Abstract
Air traffic controllers perceive traffic complexity through the radar display, suggesting that a computer vision model operating on the same imagery may provide a natural architecture for modeling controller-perceived complexity; however, whether radar imagery is a viable input format for deep learning vision models remains unclear. Unlike natural images, radar images are extremely sparse and self-similar, consisting primarily of a black background and a few visually identical aircraft blobs, while small changes in aircraft positions can substantially alter sector-level complexity. To test whether a vision model can capture these operationally important differences, we encode each traffic situation as a position image supplemented by five channels representing aircraft state variables, including heading, speed, and altitude, and train a Vision Transformer (ViT) to regress four intrinsic complexity components derived from pairwise geometric relations among aircraft. The model achieves $R^2 > 0.96$ for all four components, and a one-aircraft-removal perturbation study shows that its response changes proportionally to how much the removed aircraft contributed to sector complexity rather than treating every removal as equivalent. These results demonstrate that, despite its atypical visual characteristics, radar imagery is a viable input format for air traffic complexity modeling.

## Metadata
- **Published**: 2026-08-12T08:53:22Z
- **Authors**: Hyewook Kim, Byul Kang, Seokbin Yoon, Keumjin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11810v1)