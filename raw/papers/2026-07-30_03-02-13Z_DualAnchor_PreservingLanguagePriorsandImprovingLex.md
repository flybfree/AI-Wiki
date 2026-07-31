---
title: DualAnchor: Preserving Language Priors and Improving Lexical Fidelity in Gloss-Free Sign Language Translation
published: 2026-07-30T03:02:13Z
authors: Hongbin Zhang, Junhao Liu, Xuefeng Bai, Youcheng Pan, Yang Xiang, Kehai Chen
url: http://arxiv.org/abs/2607.27614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DualAnchor: Preserving Language Priors and Improving Lexical Fidelity in Gloss-Free Sign Language Translation

## Abstract
Recent advances in large language models (LLMs) have led sign language translation (SLT), the task of converting sign-language videos into spoken-language text, to increasingly adopt LLMs as textual backbones. However, despite their strong language modeling capabilities, existing LLM-based SLT methods often undermine rather than exploit this language prior, producing disfluent translations, a failure we term language-prior degradation. Meanwhile, existing methods typically align videos and text at the sentence level, which does not ensure accurate lexical details and creates a lexical fidelity gap. To address both issues, we propose DualAnchor, a gloss-free LLM-based SLT training framework that couples two complementary anchors for linguistically fluent and visually faithful generation. Token-level Prior Anchoring (TPA) preserves the LLM's language prior by regularizing the multimodal decoder at each decoding step toward the next-token distribution of a frozen LLM conditioned on the same autoregressive prefix. Optimal Transport Alignment (OTA) improves lexical fidelity by formulating visual-textual matching as entropy-regularized partial optimal transport, with Sinkhorn optimization inducing a soft alignment between visual tokens and textual content tokens under a cosine cost. DualAnchor achieves strong overall performance on both PHOENIX-2014T and CSL-Daily. Targeted analyses attribute these gains to the complementary effects of the two anchors: TPA improves fluency, whereas OTA reduces fine-grained lexical errors.

## Metadata
- **Published**: 2026-07-30T03:02:13Z
- **Authors**: Hongbin Zhang, Junhao Liu, Xuefeng Bai, Youcheng Pan, Yang Xiang, Kehai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27614v1)