---
title: MPQ: A Message-Passing View of Post-Training Quantization
published: 2026-10-23T03:54:41Z
authors: Yanshuo Chen, Chenxi Liu, Reza Shirkavand, Heng Huang
url: http://arxiv.org/abs/2610.32127v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MPQ: A Message-Passing View of Post-Training Quantization

## Abstract
Post-training quantization (PTQ) is a key technique for efficiently deploying large language models, as it compresses weights into low-bit representations without retraining. Existing PTQ solvers, including GPTQ, LDLQ, and block coordinate descent, commit each weight block to a single codeword before its neighbors are considered, leaving near-optimal alternatives unexplored. In this work, we cast row-wise PTQ as posterior inference over discrete codebooks, in which existing solvers correspond to a zero-temperature, hard-decision limit retaining only the top codeword per block. We propose Message-Passing Quantization (MPQ), which preserves soft posterior information across blocks during inference and commits to hard codewords only at the output stage. MPQ first uses vector approximate message passing to compute approximate blockwise posteriors, then refines a hard-decision initialization by exact block coordinate descent. Across 2-bit lattice and 3- and 4-bit scalar quantization on dense language models from Llama, Qwen, and Mistral families, MPQ improves perplexity and zero-shot accuracy over strong hard-decision baselines, and composes favorably with preprocessing techniques such as activation-aware scaling and incoherence processing. Our implementation is available at https://github.com/poseidonchan/MPQ.

## Metadata
- **Published**: 2026-10-23T03:54:41Z
- **Authors**: Yanshuo Chen, Chenxi Liu, Reza Shirkavand, Heng Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32127v1)