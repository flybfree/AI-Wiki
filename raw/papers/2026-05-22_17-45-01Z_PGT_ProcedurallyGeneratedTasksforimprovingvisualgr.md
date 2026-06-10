---
title: 'PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs'
published: 2026-05-22T17:45:01Z
authors: Rim Assouel, Amir Bar, Michal Drozdzal, Adriana Romero-Soriano
url: http://arxiv.org/abs/2605.23883v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs

## Abstract
Despite remarkable progress in Multimodal Large Language Models (MLLMs), these models still struggle with fine-grained understanding tasks. In this work, we propose Procedurally Generated Tasks (PGT), a simple data-driven framework that serves a dual purpose: inducing fine-grained visual understanding and acting as a low-cost diagnostic tool to identify the source of perception failures. By overlaying unambiguous geometric primitives on images, PGT generate additional dense supervision that disentangles visual grounding capability from semantic priors. Extensive experiments on relational, quantitative, and 3D/depth understanding benchmarks show that PGT yields remarkable gains across diverse architectures. Instruction tuning MLLMs on LLaVA-v1.5-Instruct augmented with PGT data results in improvements of up to +20% on the What'sUp benchmark and +13.3% on CV-Bench-2D, while maintaining general perception capabilities. Moreover, finetuning state-of-the-art MLLMs on PGT data leads to boosts of up to +5.5% on What'sUp and +8.3% on CV-Bench-2D. These findings demonstrate that PGT effectively address the bottleneck of fine-grained perception, revealing that many spatial reasoning deficits stem from inadequate supervision signals rather than inherent architectural or resolution limitations.

## Metadata
- **Published**: 2026-05-22T17:45:01Z
- **Authors**: Rim Assouel, Amir Bar, Michal Drozdzal, Adriana Romero-Soriano
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23883v1)