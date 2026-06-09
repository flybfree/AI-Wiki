---
title: SAM for Robust Mitochondria Instance Segmentation in Fluorescence Microscopy
published: 2026-05-29T13:19:02Z
authors: Suyog Jadhav, Dilip K. Prasad, Krishna Agarwal
url: http://arxiv.org/abs/2605.31284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAM for Robust Mitochondria Instance Segmentation in Fluorescence Microscopy

## Abstract
The morphological analysis of mitochondria in fluorescence microscopy (FM) is crucial for understanding cellular health, energy production, and metabolic regulation. While foundation models like the Segment Anything Model (SAM) have revolutionized natural image segmentation, their direct application to FM is hindered by a significant domain shift characterized by diffraction-limited resolution, low contrast, and complex overlapping organelle networks. Furthermore, the development of robust models is bottlenecked by a severe lack of high-quality, manually annotated instance segmentation datasets for mitochondria. In this paper, we propose a scalable solution to this data scarcity by finetuning SAM exclusively on synthetically generated FM data. We simulate realistic mitochondria data and emulate the optical properties of fluorescence microscopes to create a large-scale annotated dataset. We evaluate our fine-tuned model on a curated dataset of real, manually annotated FM images. Qualitative and quantitative analyses demonstrate that our synthetically fine-tuned model improves precision and average dice score over strong baselines. This work establishes the potential of simulation-assisted training for FM instance segmentation.

## Metadata
- **Published**: 2026-05-29T13:19:02Z
- **Authors**: Suyog Jadhav, Dilip K. Prasad, Krishna Agarwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.31284v1)