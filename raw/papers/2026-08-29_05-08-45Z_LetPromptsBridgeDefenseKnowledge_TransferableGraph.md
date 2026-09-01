---
title: Let Prompts Bridge Defense Knowledge: Transferable Graph Purification via Vulnerability-Aware GPL
published: 2026-08-29T05:08:45Z
authors: Shuomin Xue, Jingyuan Li, Ju Jia, Jingxuan Yu, Xiaojun Jia
url: http://arxiv.org/abs/2608.29054v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Let Prompts Bridge Defense Knowledge: Transferable Graph Purification via Vulnerability-Aware GPL

## Abstract
Graph Neural Networks (GNNs) have emerged as a cornerstone for representing complex relational dependencies in diverse multimedia tasks, particularly in cross-platform user interest modeling and cross-modal semantic alignment. In the real world, a practical defense against graph adversarial perturbations is needed. However, we observe that the prevailing adversarial purification methods are essentially domain-restricted defenses, which leads to the following shortcomings: (1) single-domain data provides insufficient structural and semantic diversity for learning robust purification criteria; (2) training of domain-specific defense strategies from scratch consumes substantial computational cost. To address the above limitations, we propose a transferable graph purification scheme, named ProGAP, to bridge adversarial defense knowledge via vulnerability-aware graph prompt learning. Firstly, to capture universal adversarial patterns, a perturbation-capture edge detector is pretrained on data-rich graphs by jointly modeling topological and semantic information. Subsequently, to achieve more knowledge transfer w.r.t. robustness, vulnerability-aware prompts are designed that inject targeted purification guidance into biased nodes, during which the pretrained detector adapts to distribution shifts in downstream graphs without parameter-laborious updates. Experimental results demonstrate that compared with state-of-the-art baselines, our ProGAP achieves 1%-9% improvement, and reduces the time consumption by up to 2.2x. The code for ProGAP is available at https://github.com/Lieyoufffff/ProGAP.

## Metadata
- **Published**: 2026-08-29T05:08:45Z
- **Authors**: Shuomin Xue, Jingyuan Li, Ju Jia, Jingxuan Yu, Xiaojun Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29054v1)