---
title: Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning
published: 2026-07-24T06:22:40Z
authors: Hao Yang, Jin Wang, Xuejie Zhang
url: http://arxiv.org/abs/2607.22013v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning

## Abstract
Multimodal chain-of-thought (CoT) reasoning integrates visual and textual cues through step-by-step inference. In small models with limited token budgets, modality-interaction fusion often suppresses tiny cross-modal differences. In particular, multimodal CoT often struggles when different images pair with identical text or different texts pair with an identical image, making such inputs nearly indistinguishable after fusion. This study proposes Visual Saliency Steering Distillation (VSSD). VSSD leverages the attention maps of multimodal large language models to generate perturbed images that capture task-sensitive feature directions, and then applies singular value decomposition to extract dominant steering vectors to guide inter-layer distillation. Experiments on ScienceQA and M$^3$CoT demonstrate that VSSD improves rationale generation and answer inference. The code is available at https://github.com/BGWH123/VSSD.

## Metadata
- **Published**: 2026-07-24T06:22:40Z
- **Authors**: Hao Yang, Jin Wang, Xuejie Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22013v1)