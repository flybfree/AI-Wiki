---
title: FAS-R1: A Unified Multi-Task MLLM for Reasoning Face Anti-Spoofing
published: 2026-07-29T03:19:12Z
authors: Hongyang Wang, Yichen Shi, Hongrui Li, Yiru Huo, Jun Feng, Zitong Yu
url: http://arxiv.org/abs/2607.26432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FAS-R1: A Unified Multi-Task MLLM for Reasoning Face Anti-Spoofing

## Abstract
Face anti-spoofing (FAS) is increasingly expected to provide not only bona fide/spoof decisions, but also attack semantics and image-grounded evidence for human inspection. Existing discriminative FAS models remain largely label-centric, while recent MLLM-based methods offer structured outputs but still rely mainly on supervised fine-tuning, often producing template-like rationales and weak optimization for difficult attacks. We propose FAS-R1, a two-stage reasoning-oriented MLLM framework for unified FAS prediction, covering authenticity classification, attack-type recognition and spoof-region localization. FAS-R1 first uses FAS-R1-23K, a high-quality long-CoT dataset, for cold-start supervised fine-tuning, and then performs FAS-specific GRPO post-training. Degradation-Simulated Augmentation (DSA) encourages stable spoof-cue reasoning across visual-quality shifts, while Difficulty-Aware GRPO (DA-GRPO) mitigates easy-sample dominance that may leave difficult task--attack groups under-optimized, especially for subtle or ambiguous attacks such as makeup and mask attacks. The main 3B FAS-R1 model achieves 98.75\% authenticity accuracy, 93.33\% attack-type accuracy, and 96.30/94.73\% AP@40/AP@50 in-domain. It also outperforms the compared systems in cross-domain authenticity generalization and answer-and-rationale quality. Experiments with different base models further show favorable scaling behavior. The code will be released soon.

## Metadata
- **Published**: 2026-07-29T03:19:12Z
- **Authors**: Hongyang Wang, Yichen Shi, Hongrui Li, Yiru Huo, Jun Feng, Zitong Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26432v1)