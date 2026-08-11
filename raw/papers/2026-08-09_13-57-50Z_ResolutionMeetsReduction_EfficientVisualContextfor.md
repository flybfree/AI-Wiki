---
title: Resolution Meets Reduction: Efficient Visual Context for 3D Radiology Report Generation
published: 2026-08-09T13:57:50Z
authors: Jonathan Suprijadi, Raphael Stock, Moritz Langenberg, David Zimmerer, Kim-Celine Kahl, Stefan Denner, Yannick Kirchhoff, Karol Gotkowski, Maximilian Rokuss, Jeremias Traub, Tassilo Wald, Constantin Ulrich, Klaus Maier-Hein
url: http://arxiv.org/abs/2608.08713v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resolution Meets Reduction: Efficient Visual Context for 3D Radiology Report Generation

## Abstract
Vision-language models offer a promising path toward automating radiology report generation, but applying them to full 3D CT volumes poses substantial computational challenges. Modern foundation vision encoders (VEs) can produce tens of thousands of vision tokens per scan, making the visual sequence passed to the large language model (LLM) a primary computational bottleneck. Vision-to-language projectors can compress this sequence to reduce computation, but may discard clinically relevant detail; conversely, effective compression can accommodate higher-resolution inputs while keeping the downstream token count fixed. How this vision-token budget should be allocated across input field of view, spatial resolution, and vision-to-language projection therefore remains an open design question. We systematically evaluate four heterogeneous VEs (CNN- and ViT-based), five token-reducing projectors at up to 64x compression alongside a non-reducing MLP projector baseline, and five instruction-tuned LLMs (1.7B--4B) on two large-scale CT report datasets (CT-RATE and Merlin). At matched LLM token budgets, anatomy-guided region of interest cropping is the most consistent strategy, improving clinical macro F1 in 19 of 20 settings by +3.7 points on average for the 3D ViT Primus encoder and +1.1 for the slice-based 2D ViT Curia encoder. Increasing input resolution further is strongly projector-dependent: the PerceiverResampler, paired with higher-resolution Curia features, yields the strongest configuration in the resolution study on both datasets. Our best configurations achieve state-of-the-art clinical macro F1 on the test sets, reaching 49.5 on CT-RATE and 49.0 on Merlin. Code and models will be published upon publication.

## Metadata
- **Published**: 2026-08-09T13:57:50Z
- **Authors**: Jonathan Suprijadi, Raphael Stock, Moritz Langenberg, David Zimmerer, Kim-Celine Kahl, Stefan Denner, Yannick Kirchhoff, Karol Gotkowski, Maximilian Rokuss, Jeremias Traub, Tassilo Wald, Constantin Ulrich, Klaus Maier-Hein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08713v1)