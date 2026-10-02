---
title: Cross-Lingual Alignment for Decoder-Only Models using MoE Routers
url: http://arxiv.org/abs/2610.01921v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_15-56-54Z_Cross_LingualAlignmentforDecoder_OnlyModelsusingMo.md
generated_at: 2026-10-01 22:13
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces a novel method for cross-lingual alignment in decoder-only Large Language Models (LLMs) by leveraging the outputs of Mixture-of-Experts (MoE) routers as targets for contrastive learning, addressing the limitations of traditional hidden-state alignment due to tokenization variance. Experiments on four open-source MoEs demonstrate that this routing loss effectively aligns underlying representations across languages and significantly improves multilingual performance without requiring auxiliary alignment losses on hidden states.

## Key Takeaways
- Cross-lingual contrastive learning has historically been effective for multilingual encoder training, but explicit representation alignment is challenging in decoder-only LLMs due to varying tokenization across languages; however, research indicates that higher representational alignment correlates with better cross-lingual transfer capabilities even in these architectures.
- Instead of applying auxiliary losses to hidden states, the authors propose aligning the outputs of MoE routers, which are more suitable for pooling over multiple tokens and enable reliable sequence-level cross-lingual comparisons that better suit the decoder architecture constraints.
- Controlled continual pre-training experiments on four open-source MoEs reveal that incorporating this routing loss not only aligns hidden representations across languages but also yields measurable improvements in multilingual performance across a diverse evaluation suite, validating the potential of cross-lingual MoE router alignment.

## Context
Multilingual capabilities are increasingly critical for LLMs deployed globally, yet decoder-only architectures have lagged behind encoder-based models in achieving robust cross-lingual transfer due to architectural and tokenization barriers. This work bridges a significant gap by adapting contrastive learning techniques to the specific constraints of modern MoE-based decoders, expanding the toolkit for enhancing multilingual proficiency without altering core model structures.

## Implications
Practitioners can adopt this routing-based alignment strategy to boost multilingual performance in existing MoE models during continual pre-training, offering a scalable

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01921v1)
