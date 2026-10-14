---
title: PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models
published: 2026-10-12T20:33:53Z
authors: Quentin Fruytier, Anton Xue, Sanjay Shakkottai, Sujay Sanghavi
url: http://arxiv.org/abs/2610.17375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models

## Abstract
Diffusion language models accelerate generation by decoding multiple masked positions per forward pass. However, accuracy is known to drop when parallel decoding trajectories deviate from their sequential counterparts, which are slow and expensive "oracles" that adhere to the joint distribution of language. In this paper, we propose Parallel Inconsistency Guidance (PIG), a new paradigm that uses a trained auxiliary model to directly estimate the inconsistency between parallel and sequential generation from a single model forward pass. During inference, masked positions are traversed by decreasing confidence, and tokens are added to the parallel decode set one-at-a-time until the total estimated inconsistency between the parallel and sequential generation exceeds a threshold. Surprisingly, it suffices to train a lightweight ~2M parameter auxiliary model on a small mixture drawn from OpenCoder, GSM8K-train, MATH-train, and MBPP-train. For LLaDA-8B Instruct and NemotronDiffusion-3B Instruct, PIG extends the accuracy-TPF frontier on GSM8K, MATH500, MBPP, HumanEval, and MMLU, when compared to the industry standard Fast-dLLM and measures favorably on LLaDA-8B Instruct against DAPD, KLASS, EB-sampler, and other learned unmasking policies.

## Metadata
- **Published**: 2026-10-12T20:33:53Z
- **Authors**: Quentin Fruytier, Anton Xue, Sanjay Shakkottai, Sujay Sanghavi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17375v1)