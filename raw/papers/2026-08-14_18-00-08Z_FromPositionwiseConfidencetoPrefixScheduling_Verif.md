---
title: From Positionwise Confidence to Prefix Scheduling: Verifier Skipping in Speculative Decoding
published: 2026-08-14T18:00:08Z
authors: Haoxuan Luo, Jameson Sandler, Ferdinando Fioretto
url: http://arxiv.org/abs/2608.14787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Positionwise Confidence to Prefix Scheduling: Verifier Skipping in Speculative Decoding

## Abstract
Speculative decoding is a leading technique to reduce the cost of autoregressive generation by using a small drafter to propose several tokens, which are then verified in parallel by a larger target model. Speculative diffusion decoding (SDD) further removes sequential drafting by generating every position in a draft block in parallel with a discrete diffusion model. However, SDD still invokes the target on every block, leaving verification as a potential bottleneck. This paper recognizes that this creates a new control handle: whether to invoke the verifier at all. Thus, we study verifier skipping, a lossy policy that commits a selected draft prefix directly, and ask which confidence signal should schedule it. Interestingly, our study finds that better token predictors need not yield better schedulers: skips require contiguous high-confidence prefixes, while short skips can induce additional drafting rounds. To study this mismatch, we compare raw confidence with learned marginal and conditional survival scores under the same policy, using Strict SDD, lenience, and top-$k$ acceptance as baselines. On HumanEval with DiffuCoder-7B-Instruct and Qwen3-32B, all three confidence signals save $9.6\%$ to $13.5\%$ of verifier calls at the same observed pass@1 as Strict SDD. Surprisingly, raw confidence saves the most; marginal survival has higher positionwise AUROC than raw confidence at most positions, yet neither learned signal dominates online. Our analysis shows that verifier skipping is a useful new lossy axis and, surprisingly, its key challenge is prefix scheduling rather than token prediction alone.

## Metadata
- **Published**: 2026-08-14T18:00:08Z
- **Authors**: Haoxuan Luo, Jameson Sandler, Ferdinando Fioretto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14787v1)