---
title: SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models
published: 2026-08-03T08:36:18Z
authors: Jing Wu, Jianhua Wu, Jiayi Guan, Jiahong Chen, Jinghui Lu, Hangjun Ye, Bingzhao Gao, Long Chen
url: http://arxiv.org/abs/2608.01899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

## Abstract
Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning. Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs' general-purpose capabilities after spatial fine-tuning. To this end, we propose a parameter-efficient \textit{\textbf{Spatio}-vision \textbf{L}anguage \textbf{M}odels (SpatioLM)}, that enhances spatial intelligence without extra 3D prior inputs or third-party spatial encoders. Concretely, we design a plug-and-play and non-invasive spatio-vision module that elicits the spatial knowledge inherent in VLMs. Furthermore, we innovatively leverage pseudo depth and camera information as supervision to guide the model in learning physically coherent representations. Extensive experiments show that SpatioLM achieves significant improvements in diverse tasks, including spatial perception and understanding while effectively limiting the degradation of general capabilities. Notably, the model achieves an impressive score of 71.6 on the VSI-Bench (the first model to surpass 70). In addition, it attains competitive performance when transferred to embodied manipulation tasks. Code is available at \href{https://github.com/xiaomi-research/spatio-lm}{\faGithub~spatio-lm}.

## Metadata
- **Published**: 2026-08-03T08:36:18Z
- **Authors**: Jing Wu, Jianhua Wu, Jiayi Guan, Jiahong Chen, Jinghui Lu, Hangjun Ye, Bingzhao Gao, Long Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01899v1)