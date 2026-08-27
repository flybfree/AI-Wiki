---
title: DCGC: Draft-Conditioned Global Correction for Complex Reasoning with Masked Diffusion Models
published: 2026-08-26T06:35:26Z
authors: Minhae Oh, Nakyung Lee, Jungwoo Lee
url: http://arxiv.org/abs/2608.25428v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DCGC: Draft-Conditioned Global Correction for Complex Reasoning with Masked Diffusion Models

## Abstract
Correcting flawed reasoning traces remains a significant challenge for Large Language Models (LLMs), whose autoregressive generation can propagate early mistakes into subsequent reasoning. We introduce DCGC, a Masked Diffusion Model (MDM) framework for global correction that uses an imperfect solution draft from an upstream solver as auxiliary context. DCGC combines task-specific Supervised Fine-Tuning (SFT) with a novel inference-time mechanism called Dynamic Dual-CFG. This mechanism separates problem-only and joint problem-draft branches and scales the draft-conditioned residual using a relative confidence gap. Across math, code, and knowledge reasoning benchmarks, DCGC outperforms standard sampling and simpler CFG variants, with additional results suggesting transfer to different diffusion backbones. In test-time setting where ground-truth failure labels are unavailable, DCGC improves full test set accuracy by correcting low-consensus upstream outputs, highlighting its utility as a verifier-free global correction module for difficult reasoning instances.

## Metadata
- **Published**: 2026-08-26T06:35:26Z
- **Authors**: Minhae Oh, Nakyung Lee, Jungwoo Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25428v1)