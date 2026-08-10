---
title: Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models
published: 2026-08-07T07:36:19Z
authors: Minseok Kang, Hyunwoo Kim, Chanyoung Kim, Minwoo Kim, Jaekoo Lee, Dahuin Jung
url: http://arxiv.org/abs/2608.06901v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models

## Abstract
Vision-language models (VLMs) have achieved remarkable generalization across diverse multimodal tasks through large-scale pre-training, yet their rapidly increasing computational and memory requirements pose significant challenges for deployment in constrained environments. Existing pruning strategies often depend on task-specific criteria or LLM-oriented importance measures, making them unsuitable for task-agnostic pruning, where no task-specific samples are available at pruning time and the pruned model remains broadly applicable. We introduce a retraining-free VLM pruning framework called PORTA that derives a task- and modality-agnostic importance formulation based on activation variation, estimated from generic calibration data, which reliably captures feature-level representation utility across modalities. PORTA further incorporates an adaptive sparsity allocation mechanism that assigns layer-wise pruning ratios based on output feature variability, avoiding the limitations of uniform sparsity and reducing performance degradation at high compression levels. Extensive experiments across VLM architectures, such as CLIP, BLIP, and Qwen2-VL, demonstrate that PORTA achieves competitive downstream performance under high sparsity without requiring any retraining, supporting efficient VLM compression. Code is available at https://github.com/cau-hai-lab/PORTA.git.

## Metadata
- **Published**: 2026-08-07T07:36:19Z
- **Authors**: Minseok Kang, Hyunwoo Kim, Chanyoung Kim, Minwoo Kim, Jaekoo Lee, Dahuin Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06901v1)