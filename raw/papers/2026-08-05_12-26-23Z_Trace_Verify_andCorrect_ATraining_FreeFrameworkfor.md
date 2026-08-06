---
title: Trace, Verify, and Correct: A Training-Free Framework for Spatial Reasoning in Multimodal LLMs
published: 2026-08-05T12:26:23Z
authors: Yang Yang, Jiawei Chen, Tairan Chen, Zhaoxia Yin
url: http://arxiv.org/abs/2608.04759v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trace, Verify, and Correct: A Training-Free Framework for Spatial Reasoning in Multimodal LLMs

## Abstract
Although Multimodal Large Language Models (MLLMs) have made substantial progress, their spatial reasoning may still produce intermediate judgments inconsistent with the input image, allowing errors to propagate through the reasoning chain and affect the final answer. Existing methods mainly improve spatial reasoning through training or additional spatial information, without considering whether the reasoning process itself is faithful to the model input. Our study shows that unfaithful reasoning chains significantly reduce final-answer accuracy. To address this issue, we propose a modular and training-free framework for spatial reasoning verification and correction. The framework constructs a Spatial Evidence Graph (SEG), which associates atomic spatial evidence extracted from Chain-of-Thought reasoning with visual entities, spatial relations, source steps, and visual evidence. Spatial Evidence Reliability Assessment (SERA) evaluates the reliability of visual evidence based on object existence, localization, and geometric measurements. The framework then identifies the earliest spatial evidence unit contradicted by reliable visual evidence and guides the original MLLM to revise the subsequent reasoning and final answer. Across 15 model-dataset settings, our method achieves an average accuracy of 68.94%, outperforming the compared baselines by 8.55 percentage points on average. Our code will be open-sourced.

## Metadata
- **Published**: 2026-08-05T12:26:23Z
- **Authors**: Yang Yang, Jiawei Chen, Tairan Chen, Zhaoxia Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04759v1)