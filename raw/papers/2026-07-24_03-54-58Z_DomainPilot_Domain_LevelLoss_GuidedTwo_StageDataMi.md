---
title: DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning
published: 2026-07-24T03:54:58Z
authors: He Zhang
url: http://arxiv.org/abs/2607.22769v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning

## Abstract
The training efficacy of large language models (LLMs) is fundamentally constrained by the quality and composition of training data. Existing dynamic data scheduling methods face critical limitations in industrial-scale pretraining and supervised fine-tuning (SFT): data selection incurs prohibitive O(N) costs on terabyte-scale corpora, mixture optimization schemes introduce severe I/O bottlenecks or require training auxiliary reference models, and sample-level reweighting strategies rely on loss signals that conflate noise, difficulty, and novelty.   We present DomainPilot, a domain-level loss-guided two-stage data mixture optimization framework. DomainPilot introduces token-level domain loss monitoring to capture per-domain learning dynamics during training without halting the data pipeline. Building on these signals, we propose a Scaling Law guided coarse optimization stage that fits domain-specific convergence curves and derives a principled prior for mixture adjustment. A subsequent Mixing Law guided fine optimization stage refines the mixture by modeling cross-domain interaction effects through controlled sweep experiments. The entire mechanism is realized via a patch-based architecture that injects domain-aware loss computation into existing training frameworks (e.g., MindSpeed/Megatron-LM) with only ~30 lines of framework-specific adapter code.   We validate DomainPilot on the Qwen3-1.7B model during SFT. Compared to the original data mixture, our optimized mixture achieves improvements of +2% on MMLU-Redux, +1.8% on AIME24, +3.8% on LiveCodeBench v5, and +3.6% on BFCL v3, without increasing total data volume or training cost. These results demonstrate that domain-level training signals provide an effective, lightweight alternative to expensive data selection or auxiliary model training for mixture optimization.

## Metadata
- **Published**: 2026-07-24T03:54:58Z
- **Authors**: He Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22769v1)