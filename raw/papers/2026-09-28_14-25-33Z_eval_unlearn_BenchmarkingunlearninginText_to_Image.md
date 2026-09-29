---
title: eval-unlearn: Benchmarking unlearning in Text-to-Image Diffusion Models
published: 2026-09-28T14:25:33Z
authors:  Mansi, Nikhil Raghavan, Zixia Huang, Kai Sheng Ong, Ji Shen Lim, Brandon Siao Xiang Ling, Francesco Leofante
url: http://arxiv.org/abs/2609.35269v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# eval-unlearn: Benchmarking unlearning in Text-to-Image Diffusion Models

## Abstract
The rising number of concept unlearning techniques for text-to-image (T2I) diffusion models has produced a fragmented evaluation landscape. Methods are assessed under heterogeneous experimental conditions making principled cross-method comparison difficult. We present eval-unlearn, an open-source Python library providing a unified, reproducible benchmarking framework for concept unlearning in T2I Diffusion models. eval-unlearn integrates twelve published unlearning techniques spanning fine-tuning, closed-form model editing, and inference-time intervention, alongside nine complementary evaluation metrics covering erasure efficacy, adversarial robustness, generative quality, and concept retention. Its plugin architecture lets third-party techniques and metrics self-register without modifying the core framework, and its streaming, batched pipeline supports efficient evaluation of both standard NSFW concepts and arbitrary general concepts. As a further contribution, we release a public leaderboard on HuggingFace along with an interactive tool for real-time evaluation of unlearning techniques. The leaderboard compares nudity concept erasure case study across all twelve techniques, exposing significant accuracy-quality trade-offs that are obscured by heterogeneous evaluation. eval-unlearn is released under the MIT license; the package, code, leaderboard, and documentation are all available at https://eval-unlearn.readthedocs.io.

## Metadata
- **Published**: 2026-09-28T14:25:33Z
- **Authors**:  Mansi, Nikhil Raghavan, Zixia Huang, Kai Sheng Ong, Ji Shen Lim, Brandon Siao Xiang Ling, Francesco Leofante
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35269v1)