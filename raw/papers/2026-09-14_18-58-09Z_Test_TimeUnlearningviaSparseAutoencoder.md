---
title: Test-Time Unlearning via Sparse Autoencoder
published: 2026-09-14T18:58:09Z
authors: Pingzhi Li, Jinhao Duan, Vaishnav Tadiparthi, Nakul Agarwal, Kwonjoon Lee, Ehsan Moradi Pari, Hossein Nourkhiz Mahjoub, Sijia Liu, Tianlong Chen
url: http://arxiv.org/abs/2609.16229v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Test-Time Unlearning via Sparse Autoencoder

## Abstract
Machine unlearning aims to remove specific knowledge from a trained large language model (LLM) without retraining from scratch. Existing methods modify model weights via gradient ascent and its advances. While effective on certain benchmarks, these weight-based approaches exhibit a sharp forget-utility trade-off, where stronger forgetting of target knowledge can degrade model utility, and unlearned knowledge may reappear under post-unlearning fine-tuning or prompt attacks. We propose ARIA (autoencoder-gated inference-time unlearning), a test-time unlearning method that leaves model weights intact and gates access to unwanted knowledge only when generation enters a forget-related state. ARIA uses sparse autoencoder (SAE) latents to train a lightweight linear detector, then applies an interpretable intervention on triggered states with negligible test-time overhead. Empirical evaluations on TOFU, R-TOFU, and WMDP show that ARIA improves the forget-retain trade-off over weight-based baselines across both a thinking model (DeepSeek-R1-Distilled-Qwen-1.5B) and an instruction model (Gemma-3-1B-it), e.g., reducing WMDP-cyber forget-set accuracy significantly while keeping MMLU within 1% of the pre-unlearning model. We further introduce three post-unlearning adversarial attacks targeting weight-space and decoding-space recovery, and find that ARIA remains robust under all three, with forgetting changing by less than 1% under attack. A feature-level case study leveraging the interpretability of ARIA suggests that some retain degradation may reflect response styles underlying the unlearning data rather than leakage of the targeted knowledge itself, highlighting a potential source of bias in unlearning task construction.

## Metadata
- **Published**: 2026-09-14T18:58:09Z
- **Authors**: Pingzhi Li, Jinhao Duan, Vaishnav Tadiparthi, Nakul Agarwal, Kwonjoon Lee, Ehsan Moradi Pari, Hossein Nourkhiz Mahjoub, Sijia Liu, Tianlong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16229v1)