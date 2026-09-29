---
title: From Attention Sensitivity to Layer Role: Revisiting Mixed-Precision Quantization of Transformers
published: 2026-09-28T10:53:49Z
authors: Nafiseh HosseinpourFardi, Negar Alihadi, Mahmoudreza Babaei, Milad Hosseini, Adrian Weller
url: http://arxiv.org/abs/2609.34866v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Attention Sensitivity to Layer Role: Revisiting Mixed-Precision Quantization of Transformers

## Abstract
Most post-training quantization pipelines fit each weight matrix to its pretrained counterpart, one matrix at a time. Whether that proxy tracks what an attention block actually computes, or how errors in the Q, K and V projections compound inside the softmax, is rarely checked. We write the objective on the attention output instead, over all three projections at once, and reuse it throughout the pipeline. JAB defines one scalar loss over the joint Q, K, V weights of a block, evaluated against the block's real causally-masked attention output, and uses it twice: to fit the quantized weights (GPTQ warm start, then STE with learnable scales), and to score the block for a multiple-choice knapsack allocation.   On attention-only quantization of Mistral-7B this works. At 3 bits JAB recovers 77-90% of the gap between uniform GPTQ and full precision, and its sensitivity estimate tracks an oracle costing 73 forward passes to within a fraction of a point. It stops working once MLP layers enter the allocation. A role-aware offset rule needing no sensitivity estimate at all beats JAB on GPT-2's MLP and on the full Mistral-7B model: with a 3-bit floor it quantizes 96.4% of the weights to 4.5 bits per parameter at 6.933 perplexity, within 4.4% of full precision (6.643) at 3.56x compression, against 7.158 for JAB at the same budget. Which matrix a weight sits in matters more than any sensitivity estimate we computed.   Two things came out sideways. Block-local reconstruction is an unreliable proxy for end-to-end perplexity: one run improved a block's own objective 4.6x while perplexity rose 32x, which is why every allocation here is validated end-to-end. And on attention-only quantization, fine-tuning moved weights farther from their pretrained values while pulling attention outputs closer, with net gains. Post-training seems to recover attention behavior, not weights.

## Metadata
- **Published**: 2026-09-28T10:53:49Z
- **Authors**: Nafiseh HosseinpourFardi, Negar Alihadi, Mahmoudreza Babaei, Milad Hosseini, Adrian Weller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34866v1)