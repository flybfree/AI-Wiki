---
title: Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models
published: 2026-08-20T06:14:31Z
authors: Tenghui Huang, Jiawen Kang, Dongning Liu, Changyan Yi, Chengjun Cai, Anjia Yang, Li Li, Dong In Kim
url: http://arxiv.org/abs/2608.19680v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models

## Abstract
Smart contract vulnerability detection with Large Language Models (LLMs) faces three causally linked challenges. First, new vulnerability categories demand parameter-efficient adaptation, since full retraining is prohibitive for sequentially arriving tasks. Second, training per-task adapters on a shared backbone causes catastrophic forgetting of previously learned vulnerabilities. Third, the resulting multiplicity of adapters must be consolidated into a single model, since task identity is unknown at inference time. Each challenge arises directly from the solution to its predecessor, making an integrated framework essential. We propose a three-stage pipeline in which each stage addresses one challenge and feeds into the next. The adaptation stage uses Frequency-Aware Low-Rank Adaptation (FA-LoRA), which performs adaptation in the Fourier domain with per-frequency importance gates, requiring only 0.4% trainable parameters while outperforming standard LoRA and QLoRA. The continual learning stage applies Forget-Aware Replay (FAR), which uses these frequency gates to estimate per-sample forgetting risk via loss dynamics and prioritizes vulnerable knowledge for rehearsal, achieving an average Micro-F1 of 0.8022 across sequential tasks. The deployment stage employs Anchor-Protected Progressive Merging (APPM), which exploits the asymmetric generalization produced by FAR training to identify the strongest-generalizing adapter as an anchor and consolidates all adapters into a single model via anchor-protected weighted merging with frequency-domain gate competition. APPM achieves a Micro-F1 of 0.8085, within 2.7% of the independent per-task upper bound, at a merge cost of 156 ms and no additional runtime memory. Experiments on DIVE confirm the framework effectively addresses all three challenges for evolving blockchain ecosystems.

## Metadata
- **Published**: 2026-08-20T06:14:31Z
- **Authors**: Tenghui Huang, Jiawen Kang, Dongning Liu, Changyan Yi, Chengjun Cai, Anjia Yang, Li Li, Dong In Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19680v1)