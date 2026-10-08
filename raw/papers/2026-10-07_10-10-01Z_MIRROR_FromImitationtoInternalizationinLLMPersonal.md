---
title: MIRROR: From Imitation to Internalization in LLM Personalization
published: 2026-10-07T10:10:01Z
authors: Huayi Lai, Jicheng Yang, Min Yi, Chong Meng
url: http://arxiv.org/abs/2610.09795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MIRROR: From Imitation to Internalization in LLM Personalization

## Abstract
The demand for personalized LLMs is shifting from style imitation toward content quality. We investigate whether self-distillation can bridge this gap in existing fine-tuning paradigm. To address this limitation, we introduce MIRROR(Meta- personalization by Internalizing Reference-Revealed On-policy Reflections), a novel self-distillation framework that shifts LLM personalization from imitation toward preference internalization. First, we replace reference-token imitation with reference-revealed on-policy self-distillation, aligning the model's next-token distributions along its own generation trajectories with those of its reference-conditioned self, thereby internalizing user preferences rather than reproducing reference wording.Second, we introduce MIRROR-F, a focal plug-in that augments on-policy distributional alignment with selective supervision over informative reference tokens, thereby strengthening content generation while preserving user-specific expression. Across three personalized generation benchmarks, two model scales, and complementary reference-based and LLM-based evaluations, MIRROR and MIRROR-F achieve leading overall personalization performance and superior text quality, while exhibiting less catastrophic forgetting than SFT-based baselines on three unseen personalized generation tasks. The gains are consistent across model scales and application scenarios, translating to improved performance in LLM personalization tasks.

## Metadata
- **Published**: 2026-10-07T10:10:01Z
- **Authors**: Huayi Lai, Jicheng Yang, Min Yi, Chong Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09795v1)