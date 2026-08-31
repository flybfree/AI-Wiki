---
title: SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing
published: 2026-08-28T06:13:23Z
authors: Wanli Cheng, Haiya Xiang, Juntao Li, Hongling Wang, Wenliang Chen
url: http://arxiv.org/abs/2608.27963v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing

## Abstract
Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\%--39.8\% on average while maintaining competitive accuracy with full-length reasoning.

## Metadata
- **Published**: 2026-08-28T06:13:23Z
- **Authors**: Wanli Cheng, Haiya Xiang, Juntao Li, Hongling Wang, Wenliang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27963v1)