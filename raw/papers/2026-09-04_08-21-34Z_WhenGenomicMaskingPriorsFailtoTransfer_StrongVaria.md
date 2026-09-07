---
title: When Genomic Masking Priors Fail to Transfer: Strong Variant Prediction, Weak Functional Generation
published: 2026-09-04T08:21:34Z
authors: Susu Hu, Preetam Gattogi, Jens Lehmann, Sahar Vahdati, Stefanie Speidel, Julien Vibert
url: http://arxiv.org/abs/2609.04861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Genomic Masking Priors Fail to Transfer: Strong Variant Prediction, Weak Functional Generation

## Abstract
Bidirectional discrete diffusion model appears naturally suited to genomic modeling because it can reconstruct missing sequence from both flanks. We developed GenDA (Genomic Density-optimized Absorbing Diffusion) under the additional hypothesis that entropy-guided span placement would concentrate reconstruction pressure on compositionally complex regions, improving both downstream variant-effect prediction and functional sequence generation. Our results only partially support this premise. After supervised fine-tuning, the 202M-parameter GenDA model reaches a pooled ClinVar SNV AUROC of 0.774, exceeding a similarly scaled autoregressive model by 0.103. However, a matched random-span variant reaches 0.777, providing no evidence that entropy guidance causes the ClinVar improvement. More unexpectedly, GenDA fails a zero-shot functional inpainting stress test: across promoters, enhancers, exon boundaries, and intron boundaries, it does not consistently outperform a control that shuffles the native gap while exactly preserving 3-mer composition. Failure is already present for 50--500-bp gaps, although enhancer degradation worsens at longer gaps. Diagnostics identify several boundary conditions: entropy measures local sequence complexity rather than functional importance; 1-mer tokenization limits physical context; training spans are capped at 300 bp; and high absolute AlphaGenome fidelity can coexist with negative control-normalized restoration. These results show that strong fine-tuned variant prediction, a plausible corruption prior, and functional generation are distinct claims that require separate validation.

## Metadata
- **Published**: 2026-09-04T08:21:34Z
- **Authors**: Susu Hu, Preetam Gattogi, Jens Lehmann, Sahar Vahdati, Stefanie Speidel, Julien Vibert
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04861v1)