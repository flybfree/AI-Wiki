---
title: Unfolding the Leech Lattice: Fused Multi-Shell Decoding and VRAM Layouts for 2-Bit LLM Weights
published: 2026-09-02T14:26:06Z
authors: Pier-Jean Malandrino
url: http://arxiv.org/abs/2609.02652v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unfolding the Leech Lattice: Fused Multi-Shell Decoding and VRAM Layouts for 2-Bit LLM Weights

## Abstract
Leech-lattice vector quantization holds the strongest reported 2-bit quality under its own evaluation protocol. Its kernel decodes one shell; we found no implementation of the multi-shell decoder the rate requires. This paper supplies one and measures its serving cost for decode-phase GEMV at batch 1. First, a serving path for the full 301-class codebook: an offline expansion into GPU layouts and a fused dequantize-plus-matvec kernel reading them without warp divergence, verified against f64. Second, the in-VRAM rate is a design axis distinct from the on-disk rate. Four bit-exact layouts timed in one process show binary bit planes beating one-hot masks on size and speed at constant bandwidth (4.80 bits per weight, 2.15x FP16). Below 4.3 bits a second, irregular stream enters; at 3.6 the decode stops being shifts and masks. Third, deployed four-bit (AWQ) and two-bit (QTIP) GEMV kernels run in the same process. The trellis kernel reads 2.40x fewer bytes than our served layout and runs 2.27x faster at near-equal fractions of their byte bounds: the time gap tracks the traffic gap, the price of unfolding a codebook too large for a lookup table. Fourth, the validity envelope: the trellis kernel outruns our no-weights control, so our launch geometry sets that floor, and on a second memory hierarchy every lattice arm falls below FP16. With the output head held identical across arms, the kernel-and-format path gains 1.11x, 1.29x and 1.41x end to end at 4B, 8B and 14B; with an int8 output head the served 4B reaches 87.0 tok/s in 2.60 GB. The quality cost, 1.38x perplexity and 14.7 MMLU points at 4B, shrinks across the three sizes measured.

## Metadata
- **Published**: 2026-09-02T14:26:06Z
- **Authors**: Pier-Jean Malandrino
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02652v1)