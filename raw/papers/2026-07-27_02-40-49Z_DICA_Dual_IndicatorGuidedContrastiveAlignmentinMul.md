---
title: DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models
published: 2026-07-27T02:40:49Z
authors: Hao Yang, Jin Wang, Xuejie Zhang
url: http://arxiv.org/abs/2607.23944v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models

## Abstract
Human visual reasoning typically follows a coarse-to-fine attention process, starting from global scene understanding and gradually focusing on question-relevant regions. However, multimodal large language models may deviate from this pattern due to attention drift and the underutilization of visual evidence, which can lead to hallucinations. To mitigate these issues, this study proposes a Dual-Indicator Guided Contrastive Alignment (DICA), which tracks two information-theoretic indicators during inference: Visual Attention Entropy (VAE), which reflects the concentration of visual attention, and Output Image Correlation (OIC), which measures the dependence of generated outputs on the visual input. An abnormal increase in VAE or a decrease in OIC corresponds to different failure modes, which trigger targeted contrastive alignment to restore visual grounding. Experimental results across multiple benchmarks demonstrate that DICA consistently outperforms existing approaches and substantially reduces hallucinations, highlighting the effectiveness of indicator-driven intervention in improving multimodal inference reliability. The code is publicly available at https://github.com/BGWH123/DICA/.

## Metadata
- **Published**: 2026-07-27T02:40:49Z
- **Authors**: Hao Yang, Jin Wang, Xuejie Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23944v1)