---
title: NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution
published: 2026-08-25T01:36:54Z
authors: Anjun Gao, Yueyang Quan, Yufei Xia, Zhuqing Liu, Minghong Fang
url: http://arxiv.org/abs/2608.23959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution

## Abstract
Safety alignment in large language models (LLMs) remains brittle against a growing spectrum of attacks. Jailbreak attacks bypass safety mechanisms through crafted prompts, while neuron-level attacks directly prune safety-critical neurons post-deployment. Both exploit a common weakness: safety-relevant information concentrates in a sparse neuron subset. We present NeuronGuard, a fine-tuning-stage defense that simultaneously hardens LLMs against both attack classes by redistributing safety signals across a broader set of neurons. NeuronGuard dynamically identifies safety-critical neurons via periodically refreshed per-layer linear classifiers, forces refusal behavior under deliberate neuron ablation, and applies KL-divergence regularization for distributional consistency. A randomized gradient projection strategy preserves downstream task utility by resolving conflicts between the defense and task objectives. We provide a formal guarantee that NeuronGuard strictly reduces the attack success rate (ASR) upper bound, and experiments across three LLMs, six state-of-the-art attack strategies, and multimodal settings confirm near-zero ASR while maintaining task accuracy, including against white-box adaptive adversaries.

## Metadata
- **Published**: 2026-08-25T01:36:54Z
- **Authors**: Anjun Gao, Yueyang Quan, Yufei Xia, Zhuqing Liu, Minghong Fang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23959v1)