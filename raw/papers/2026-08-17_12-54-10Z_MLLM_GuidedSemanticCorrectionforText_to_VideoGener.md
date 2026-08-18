---
title: MLLM-Guided Semantic Correction for Text-to-Video Generation
published: 2026-08-17T12:54:10Z
authors: Junhao Chen, Zheqi Lv, Keting Yin, Shengyu Zhang, Zhou Zhao, Feiyang Chen, Xinyu Duan, Baoxing Huai, Fei Wu
url: http://arxiv.org/abs/2608.16513v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MLLM-Guided Semantic Correction for Text-to-Video Generation

## Abstract
Recent advances in diffusion models and Transformer architectures have led to significant progress in text-to-video generation. However, these models often suffer from semantic errors such as missing objects, incorrect attributes, or mismatched actions. Although some semantic correction methods perform optimization before sampling or refinement after sampling, how to detect and correct semantic deviations during the video generation process remains underexplored. In this paper, we introduce a training-free, interpretable mid-generation correction framework that integrates multimodal large language model (MLLM) feedback directly into the diffusion sampling loop. Our framework achieves diffusion trajectory correction by injecting semantic evaluation signals during video synthesis, enabling the model to optimize the generated content through continuous self-reflection. We propose two key modules: a Semantic Assessment Supervisor that generates intermediate preview frames for semantic evaluations and deviation diagnostics, and a Semantic Modification Assistant that corrects semantic drift during inference via a controllable latent trajectory intervention. Our method improves semantic alignment, visual fidelity, and temporal consistency without modifying model parameters. We validate the effectiveness of our approach through extensive experiments across multiple benchmarks.

## Metadata
- **Published**: 2026-08-17T12:54:10Z
- **Authors**: Junhao Chen, Zheqi Lv, Keting Yin, Shengyu Zhang, Zhou Zhao, Feiyang Chen, Xinyu Duan, Baoxing Huai, Fei Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16513v1)