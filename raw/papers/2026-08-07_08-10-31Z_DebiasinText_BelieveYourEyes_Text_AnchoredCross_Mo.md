---
title: Debias in Text, Believe Your Eyes: Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning
published: 2026-08-07T08:10:31Z
authors: Chen Ling, Hanqian Li, Dongnan Liu, Keyu Qian, Jungang Li, Xinglong liu, Shiyi Wang, Xin Dong, Pengcheng Zhu, Wei Zhou, Linjian Mo, Nai Ding
url: http://arxiv.org/abs/2608.06938v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Debias in Text, Believe Your Eyes: Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning

## Abstract
The visual reasoning ability of multimodal large language models (MLLMs) is crucial for downstream applications, particularly counter-commonsense reasoning, which requires models to reason beyond common assumptions. Recent studies mainly improve visual counter-commonsense reasoning by enhancing visual inputs, following the assumption that failures originate from insufficient visual grounding. However, our empirical analysis reveals that the bottleneck is not visual perception. MLLMs already capture the relevant visual evidence, and the correct answer exists in their decoding space. Instead, the shared language decoder resolves prior--evidence conflicts by favoring dominant language priors, especially for low-frequency factual scenarios. Motivated by this, we first propose a text-anchored data construction pipeline, whose core component, Fact-Frequency Distillation (FFD), estimates the prior strength of commonsense facts and distills verified counter-commonsense scenarios into a high-quality text corpus. Building upon this corpus, we introduce TACT, a text-anchored post-training framework that debiases the shared language decoder without requiring any visual training data. TACT routes evidence-following and prior-driven reasoning trajectories into different optimization stages, enabling the decoder to resolve prior--evidence conflicts. Across counter-commonsense visual benchmarks, TACT substantially improves visual reasoning while preserving general capabilities, demonstrating effective text-to-vision cross-modal transfer.

## Metadata
- **Published**: 2026-08-07T08:10:31Z
- **Authors**: Chen Ling, Hanqian Li, Dongnan Liu, Keyu Qian, Jungang Li, Xinglong liu, Shiyi Wang, Xin Dong, Pengcheng Zhu, Wei Zhou, Linjian Mo, Nai Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06938v1)