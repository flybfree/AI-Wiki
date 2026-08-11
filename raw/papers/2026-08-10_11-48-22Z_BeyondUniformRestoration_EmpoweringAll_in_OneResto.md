---
title: Beyond Uniform Restoration: Empowering All-in-One Restoration with Pixel-Level Multimodal Guidance
published: 2026-08-10T11:48:22Z
authors: Chunxiao Liu, Wei Liu, Anbin Xiong, Erli Meng
url: http://arxiv.org/abs/2608.09482v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Uniform Restoration: Empowering All-in-One Restoration with Pixel-Level Multimodal Guidance

## Abstract
All-in-one image restoration is a unified low-level vision task that aims to effectively recover high-quality images from inputs degraded by various types and levels of corruption using a single model. Recent works have achieved remarkable progress by learning degradation-adaptive prompts or network architectures. However, these methods typically apply a uniform restoration strategy across the entire image, neglecting the fact that different regions may suffer from distinct degradation types and varying degrees of severity. In contrast, we propose to perform restoration at the pixel level, thereby enabling more fine-grained and precise control over the restoration process. Specifically, we present MGN-AIR, a novel pixel-level restoration framework for all-in-one image restoration. Our approach first learns to estimate a pixel-level visual prompt. Then, it leverages both textual and visual prompts to provide global and local degradation cues, guiding the model on where to look and how to restore at each pixel. We conduct extensive experiments on multiple all-in-one image restoration benchmarks, covering a wide range of tasks including denoising, deraining, deblurring, dehazing, desnowing, and low-light enhancement. Experimental results demonstrate that our proposed method consistently and significantly outperforms existing approaches.

## Metadata
- **Published**: 2026-08-10T11:48:22Z
- **Authors**: Chunxiao Liu, Wei Liu, Anbin Xiong, Erli Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09482v1)