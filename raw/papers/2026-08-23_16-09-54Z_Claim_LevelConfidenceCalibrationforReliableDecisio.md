---
title: Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models
published: 2026-08-23T16:09:54Z
authors: Toghrul Abbasli, Kentaroh Toyoda, Yuan Wang, Li Chen
url: http://arxiv.org/abs/2608.22483v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models

## Abstract
Large Language Models (LLMs) increasingly support decision-making in high-stakes domains, but they often hallucinate and express confidence that is misaligned with factual correctness. Response-level confidence is a coarse signal: a single generation can mix correct and incorrect statements, so a single number is not actionable for users that must accept, reject, or verify individual pieces of information. We study claim-level confidence calibration as a decision-relevant uncertainty signal: each response is decomposed into atomic, verifiable claims, and each claim is assigned a calibrated confidence using inference-time signals from consistency across samples and self-verification. Our framework operates in closed-box settings (no logits, no fine-tuning) and applies post-hoc calibration directly at the claim level, enabling selective intervention such as evidence retrieval or human review for low-confidence claims. Across TriviaQA and TruthfulQA we evaluate seven baselines on six recent models (Llama-3.1, Mistral, Qwen2.5, DeepSeek-R1, GPT-4, GPT-4o), and show that claim-level decomposition combined with post-hoc calibration reduces expected calibration error on factual questions while exposing failure modes on adversarial false-premise questions where decision-makers most need reliable uncertainty estimates.

## Metadata
- **Published**: 2026-08-23T16:09:54Z
- **Authors**: Toghrul Abbasli, Kentaroh Toyoda, Yuan Wang, Li Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22483v1)