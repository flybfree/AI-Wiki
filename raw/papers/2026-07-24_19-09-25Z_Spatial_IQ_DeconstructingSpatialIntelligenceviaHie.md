---
title: Spatial-IQ: Deconstructing Spatial Intelligence via Hierarchical Capability Tests
published: 2026-07-24T19:09:25Z
authors: Patrick Rim, Tom Long, Ekta Prashnani, Ruth Rosenholtz, Ben Boudaoud, Peter Xenopoulos, Alex Wong, Joohwan Kim, Jae-Hyun Jung
url: http://arxiv.org/abs/2607.22864v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spatial-IQ: Deconstructing Spatial Intelligence via Hierarchical Capability Tests

## Abstract
Multimodal large language models (MLLMs) excel at visual interpretation but fail on spatial reasoning tasks that humans solve reliably. Existing benchmarks evaluate these models as black boxes, limiting their ability to identify the underlying causes of lower performance: when a model fails a spatial reasoning task, it remains difficult to ascertain whether the hurdle is perceptual, such as recognizing object boundaries, or cognitive, such as reasoning about occlusion to infer hidden geometry. We introduce Spatial-IQ, a hierarchical diagnostic framework that decomposes object counting in stacked 3D structures into 9 perceptual and cognitive sub-tasks organized by the developmental stages of human spatial cognition, with mental rotation as an additional target probe. Using NVIDIA Isaac Sim, we procedurally generated a diverse dataset of roughly 80,000 stacked 3D structures with per-task ground truth. We evaluate models across three output formats (free-response text, multiple-choice images, and image editing) alongside a human baseline. The Spatial-IQ framework shows that top-performing models often succeed at the target task (object counting) without succeeding on the lower-level sub-tasks intended to support it, and that models differ in how much of these hierarchical chains they preserve, often revealing shortcut behavior that raw target-task accuracy alone would obscure. Finally, we demonstrate that training models with chain-of-thought (CoT) supervision over our hierarchical sub-tasks, combined with reinforcement learning with verifiable rewards, significantly improves both spatial consistency across sub-tasks and target-task accuracy, supporting the value of the proposed decomposition as both a diagnostic tool and a training signal.

## Metadata
- **Published**: 2026-07-24T19:09:25Z
- **Authors**: Patrick Rim, Tom Long, Ekta Prashnani, Ruth Rosenholtz, Ben Boudaoud, Peter Xenopoulos, Alex Wong, Joohwan Kim, Jae-Hyun Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22864v1)