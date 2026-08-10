---
title: TOFD: Target-Oriented Feature Decoupling against Poisoning Attacks in Split Federated Learning
published: 2026-08-07T14:34:24Z
authors: Yuhan Xie, Jingrong Huang, Chen Lyu
url: http://arxiv.org/abs/2608.07274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TOFD: Target-Oriented Feature Decoupling against Poisoning Attacks in Split Federated Learning

## Abstract
Split Federated Learning (SFL) facilitates privacy-preserving collaborative training with reduced client-side overhead. However, its split architecture introduces unique attack surfaces, rendering it vulnerable to diverse poisoning attacks. Most existing defenses fail to exploit the split paradigm, limiting their ability to detect and contain malicious behaviors at an early stage. To bridge this gap, we propose Target-Oriented Feature Decoupling (TOFD), a unified framework that jointly enables proactive detection and robust optimization against a wide range of poisoning attacks. TOFD operates in three stages: (1) Target Inference, which identifies potential attack targets by refining class-wise safe zones via class-specific Margin Perturbation (MP); (2) Sample Purification, which adaptively filters poisoned smashed data using thresholds calibrated through cross-class min-max normalization of MP; and (3) Decoupling Optimization, which leverages an adversarial guidance model to capture attack-induced patterns and decouple their influence during optimization, thereby suppressing residual adversarial effects. We provide theoretical guarantees for the convergence of TOFD. Extensive experiments on five datasets demonstrate that TOFD consistently outperforms state-of-the-art defenses under diverse attack scenarios, achieving superior robustness with low computational overhead suitable for practical deployment.

## Metadata
- **Published**: 2026-08-07T14:34:24Z
- **Authors**: Yuhan Xie, Jingrong Huang, Chen Lyu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07274v1)