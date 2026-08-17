---
title: Seeing Red, Thinking Bad: Color Bias in Vision Language Models
published: 2026-08-14T13:14:58Z
authors: Kohsuke Ide, Ryousuke Yamada, Yoshihiro Fukuhara, Hirokatsu Kataoka, Yutaka Satoh
url: http://arxiv.org/abs/2608.14286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Seeing Red, Thinking Bad: Color Bias in Vision Language Models

## Abstract
Vision language models (VLMs) are increasingly used in industrial decision-making systems, such as recruitment support and recommendation. This motivates careful analysis of how VLMs process visual and textual information. In this work, we study how VLMs interpret text rendered as an image, and investigate the influence of visual styling biases. To this end, we introduce Stealth Visual Prompts, which subtly change visual styling of text, such as color and contrast, while preserving semantic content. Using these prompts, we systematically control the visual styling of words in text and measure their impact on the analysis performed by VLMs. We further analyze how such visual perturbations affect the latent representations of the vision encoder. From our experiments, we observed that coloring positive words in green consistently shifts sentiment predictions toward a positive direction. As a result, VLMs often fail to properly account for negative words present in the text. Our analysis suggests that this behavior is correlated with changes in the latent representations of the vision encoder induced by color variations. In addition, we show that reducing text--background contrast increases reliance on visually salient cues and leads to more incorrect Visual Question Answering (VQA) outputs. These results suggest that the visual styling of rendered text can guide VLMs' interpretation in ways that diverge from human semantic understanding.   Project page: https://github.com/KohsukeIde/color-bias-vlm

## Metadata
- **Published**: 2026-08-14T13:14:58Z
- **Authors**: Kohsuke Ide, Ryousuke Yamada, Yoshihiro Fukuhara, Hirokatsu Kataoka, Yutaka Satoh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14286v1)