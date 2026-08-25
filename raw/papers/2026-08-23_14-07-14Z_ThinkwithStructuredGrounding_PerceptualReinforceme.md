---
title: Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding
published: 2026-08-23T14:07:14Z
authors: Changjiang Jiang, Qiannian Zhao, Lei Xin, Jinxiang Xie, Preslav Nakov, Zhuohan Xie
url: http://arxiv.org/abs/2608.22429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding

## Abstract
Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and structurally relational visuals (e.g., charts and visual tables) where strict relative spatial arrangements bind textual elements. Without external tools, standard MLLMs struggle with such fine-grained visual reasoning tasks. To address these issues, we propose Think with Structured Grounding (TwSG), a novel fine-grained image perception framework designed to internalize complex images's tool-use capabilities within the model. TwSG distills the benefits of multi-step reasoning and micro-cropping into a single efficient forward pass during inference. Specifically, we use an MLLM to identify key regions guided by ground-truth answers, and then prompt a teacher model to generate high-quality visual question-answering (VQA) data. These fine-grained, region-based supervisory signals are subsequently distilled back into the full-image representation. Our training pipeline consists of two stages: (1) a cold-start supervised fine-tuning (SFT) phase using multi-turn data with focused area descriptions to foster complex reasoning and error recovery; and (2) a reinforcement fine-tuning (RFT) phase driven by a novel process reward mechanism, TL-GRPO, which encourages strategic reasoning. Extensive experiments across various MLLM architectures demonstrate that TwSG reduces inference latency while substantially improving accuracy and robustness, endowing models with native fine-grained region description and flexible reasoning capabilities.

## Metadata
- **Published**: 2026-08-23T14:07:14Z
- **Authors**: Changjiang Jiang, Qiannian Zhao, Lei Xin, Jinxiang Xie, Preslav Nakov, Zhuohan Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22429v1)