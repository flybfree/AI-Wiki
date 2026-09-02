---
title: CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN
published: 2026-09-01T02:30:02Z
authors: Pranshav Gajjar, Vijay K Shah
url: http://arxiv.org/abs/2609.00590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN

## Abstract
The next generation of mobile networks is envisioned as fully AI-native, with AI-RAN architectures embedding small language models (SLMs) to perform reasoning over real-time telemetry. The state-of-the-art training paradigms for telecom LLMs, exemplified by RANSTRUCT-style supervised fine-tuning (SFT) on curated instruction data, are limited to post hoc rationalization. Here, the explanations, when produced at all, are generated after or independently of the decision, leaving the decision process unauditable. Pre-hoc reasoning, where a causal reasoning trace is produced before the output label, is preferable, and the broader LLM reasoning literature has made real progress toward it via RL methods such as Group Relative Policy Optimization (GRPO). Here we observe that transplanting this recipe into the telecom setting runs into a cold-start barrier: SLMs either learn to output the desired format or learn to predict the label, but rarely both. We identify this barrier and propose CRAFT, which stands for Cold-start Reasoning Alignment via Fine-Tuning, a data-centric method to autonomously generate a verified dataset of (input, trace, label) triplets. CRAFT fine-tunes SLMs on this verified data using low-rank adaptation (LoRA), requiring substantially less compute and wall-clock time than GRPO-based methods. On the TRACTOR and IC xApp telecom datasets, CRAFT achieves up to 86.5% and 94.6% for accuracy and F1 with no parse failures, while direct GRPO and SFT+GRPO fail to exceed 28% and 53.5% F1 with multiple parse failures. We further show that CRAFT-initialized policies serve as a robust foundation for subsequent GRPO fine-tuning, as under diverse reward functions the performance remains consistent with no parse failures. Finally, we demonstrate that CRAFT consumes 59% less energy than GRPO-based baselines, making it a sustainable path to deployable, auditable AI in 6G RAN.

## Metadata
- **Published**: 2026-09-01T02:30:02Z
- **Authors**: Pranshav Gajjar, Vijay K Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00590v1)