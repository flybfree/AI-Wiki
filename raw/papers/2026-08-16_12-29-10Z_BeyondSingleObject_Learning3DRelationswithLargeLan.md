---
title: Beyond Single Object: Learning 3D Relations with Large Language Models
published: 2026-08-16T12:29:10Z
authors: Kohsuke Ide, Ryousuke Yamada, Yue Qiu, Xianzheng Ma, Yoshihiro Fukuhara, Hirokatsu Kataoka, Yutaka Satoh
url: http://arxiv.org/abs/2608.15710v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Single Object: Learning 3D Relations with Large Language Models

## Abstract
We address a fundamental gap in 3D-LLMs: existing models focus on single-object/scene description, struggling with detailed, inter-object comparison. We propose a framework for detailed object-level reasoning across multiple objects with three components: (1) MO3D (Multi-Object in 3D), an instruction dataset requiring fine-grained multi-object comparison; (2) Multi-3DLLM, using a minimal Patch-Interaction Transformer (PIT) that models inter-/intra-object relationships while preserving local geometry; (3) Mini-apps, two application-driven benchmarks (Shape Mating, Change Captioning) that probe geometric understanding for practical use. Recent 3D-LLMs and 2D-VLMs perform poorly on these tasks, lacking both comparison-centric design and geometric awareness. In contrast, Multi-3DLLM trained on our mixture data learns geometric reasoning, surpasses all baselines on MO3D, and provides positive transfer to single-object classification.

## Metadata
- **Published**: 2026-08-16T12:29:10Z
- **Authors**: Kohsuke Ide, Ryousuke Yamada, Yue Qiu, Xianzheng Ma, Yoshihiro Fukuhara, Hirokatsu Kataoka, Yutaka Satoh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15710v1)