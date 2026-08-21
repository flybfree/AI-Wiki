---
title: Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization
published: 2026-08-20T17:14:24Z
authors: Qian Kou, Xiaofeng Shi, Xiaosong Qiu, Hua Zhou
url: http://arxiv.org/abs/2608.20281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization

## Abstract
Large language models often fail to answer questions about a bounded document collection when the source documents are not retrieved at inference time. We study this setting as document knowledge internalization: converting a fixed corpus into usable parametric knowledge for retrieval-free question answering. We propose IAR (Inject, Align, and Recover), a three-stage post-training framework that separates structured document knowledge injection, QA behavior alignment, and general ability recovery. Unlike conventional continued pretraining, Inject converts source documents into continuation, rewrite, and instruction-conditioned reconstruction objectives. Align then adapts the injected model with answer-only QA supervision, while Recover merges the domain-adapted model with the base instruction model to recover general capabilities. Across Common Corpus (CC) and CCI, and across Llama, Phi, Qwen, and SmolLM model families, IAR improves the domain-primary domain-general frontier for retrieval-free document internalization. In the main comparison, IAR improves over Vanilla SFT on all four reported metrics in 7 of 8 dataset-model settings, with average gains of 3.6 percentage points in domain QA accuracy and 12.1 percentage points in mean general performance across IFEval, MMLU, and MSBench. Extended CC baselines show that LoRA and FAPM can win individual general metrics, but among methods that also reach leading or near-leading domain internalization, IAR retains one of the strongest general profiles.

## Metadata
- **Published**: 2026-08-20T17:14:24Z
- **Authors**: Qian Kou, Xiaofeng Shi, Xiaosong Qiu, Hua Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20281v1)