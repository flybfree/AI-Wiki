---
title: RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation
published: 2026-07-30T05:30:14Z
authors: Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou, Yan Zhan, Weiqi Tan, Zhiqiong Lu, Zhengping Liang
url: http://arxiv.org/abs/2607.27699v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation

## Abstract
We propose RefineSVG, a single-step closed-loop visual feedback framework that enables multimodal large language models (MLLMs) to perform high-fidelity image-to-SVG generation through self-correction. Existing MLLM-based approaches rely on single-pass open-loop inference, where the model receives visual input only once and must generate thousands of SVG code tokens without intermediate verification. This paradigm inevitably leads to geometric drift, error accumulation, and visual hallucination on complex images. RefineSVG overcomes this limitation by invoking an external rendering engine after an initial SVG generation pass to compare the rendered output against the target image. The comparison yields a multi-dimensional visual residual map (Diff-Map) that is fed back to the model as a ReAct-style correction signal, driving a targeted correction step. To support this render-observe-correct interaction, we further introduce an SVG-oriented semantic vocabulary that compresses token sequences by over 52%. A progressive training pipeline spanning supervised fine-tuning, rejection-sampling cold-start data construction, and end-to-end agentic reinforcement learning aligns the model with closed-loop visual correction. Extensive experiments show that RefineSVG consistently outperforms existing baselines in reconstruction fidelity, structural accuracy, and code efficiency.Code is available at https://github.com/liuxiaobo66/RefineSVG.

## Metadata
- **Published**: 2026-07-30T05:30:14Z
- **Authors**: Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou, Yan Zhan, Weiqi Tan, Zhiqiong Lu, Zhengping Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27699v1)