---
title: Tokenizer Generator Coupling in Medical Image Generation
published: 2026-08-07T18:57:09Z
authors: Liam Chalcroft
url: http://arxiv.org/abs/2608.07713v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tokenizer Generator Coupling in Medical Image Generation

## Abstract
Latent medical image generators usually treat the tokenizer as fixed preprocessing. We test whether this separation is valid in a controlled ChestMNIST study at 64x64, crossing discrete tokenizers, generator families, and sampler settings under a shared latent grid, with continuous-latent reference cells. In this controlled setting, rankings depend jointly on the tokenizer, generator, and sampler: the best quantizer changes with the generator, and validation-based sampler selection changes the apparent generator ranking. We retrain the vocabulary-1024 interaction block at three seeds and the interaction survives (6 of 9 pairwise quantizer comparisons exceed three seed standard deviations), and we scope the wider single-seed grid accordingly. Reconstruction PSNR alone is not a reliable selection criterion; we instead introduce a generator-free statistic, neighbour-conditional predictive gain, that separates the quantizer families by downstream generation quality (rank-AUC 1.00) where reconstruction PSNR and marginal token entropy do not. On LFQ-1024, retuning D3PM and SE-D3PM (selected on a held-out validation split) moves them from default FID-192 0.44/0.41 to 0.09/0.10 at lower NFE, replicated across seeds; the continuous references were not given an equivalent sampler sweep. We report FID-192 as an internal ranking metric; it ranks consistently with standard FID-2048 (Spearman 0.80) and with a label-free classifier two-sample test (0.78). We interpret these results through a rate-distortion-modelability framing, where modelability is conditional on the generator, sampler, and inference budget. All experiments are at 64x64 on low-resolution medical-style images, unconditional, and evaluated with non-clinical FID-based metrics, and we scope every claim to that setting. Code: https://github.com/liamchalcroft/medtokenizers and https://github.com/liamchalcroft/medlatents.

## Metadata
- **Published**: 2026-08-07T18:57:09Z
- **Authors**: Liam Chalcroft
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07713v1)