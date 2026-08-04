---
title: Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages
published: 2026-08-01T08:44:32Z
authors: Sean Gip Lim, William Chandra Tjhi, Hai Leong Chieu
url: http://arxiv.org/abs/2608.00533v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages

## Abstract
Large Language Models have achieved substantial progress in reasoning capabilities. Yet in low-resource native settings, many suffer from cross-lingual collapse, reverting to English during intermediate steps that require complex logical reasoning. This presents a cold-start bottleneck for policy optimization, whereas standard fine-tuning risks catastrophic forgetting due to cross-lingual representation drift. To address these challenges, we introduce the Onramp-Sequence Cross-Distillation (OSCD), a post-training algorithm that projects high-resource reasoning trajectories into low-resource vocabulary subspaces during generative training rollouts via an integrated translator agentic loop, ensuring the stable and efficient translation of dynamically generated reference samples for fine-tuning. This is coupled with joint-embedding semantic alignment of both reference and target-language reasoning traces, thereby bridging the pairwise cross-lingual representational gaps. Comprehensive evaluations using the AIME25 and HMMT25 benchmarks demonstrate that OSCD yields up to 3.2 times overall improvements in native Southeast Asian languages for mathematical reasoning, of which the joint-embedding semantic alignment component contributes up to 6.4% improvements in linguistic debiasing over translation-only baselines.

## Metadata
- **Published**: 2026-08-01T08:44:32Z
- **Authors**: Sean Gip Lim, William Chandra Tjhi, Hai Leong Chieu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00533v1)