---
title: Characterizing Overconfident Failure in LLM-Based Code Generation
published: 2026-10-08T06:07:44Z
authors: Ravishka Rathnasuriya, Wei Yang
url: http://arxiv.org/abs/2610.11300v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Characterizing Overconfident Failure in LLM-Based Code Generation

## Abstract
Large language models (LLMs) are increasingly used for automated code generation, but generated programs can appear syntactically plausible while still failing execution-based correctness checks. Existing validation methods, such as testing and program analysis, remain essential but are often incomplete, costly, or applied only after generation. Model-derived uncertainty is therefore a natural early reliability signal. This paper studies the dilemma of overconfidence in code LLMs where incorrect programs are often generated with token-level confidence comparable to correct programs. We study this dilemma across four open-source code models and three execution-based benchmarks. Our analysis begins by investigating whether existing uncertainty metrics provide reliable proxies for execution correctness in code generation. We then characterize overconfidence at both global and local token levels, asking whether incorrect programs remain indistinguishable from correct ones under confidence and entropy summaries, including selective generation and the limits of instruction tuning. Finally, we evaluate whether common mitigation strategies reduce this failure mode. Our study yields four findings. First, existing uncertainty signals provide only partial and model-dependent evidence of execution failure. Second, overconfidence persists at both program and token levels, and uncertainty-based selection does not consistently improve accepted-set accuracy. Third, instruction tuning can increase certainty on failing generations without consistently improving correctness discrimination. Fourth, common mitigation techniques improve specific aspects of reliability but do not reliably resolve overconfident failure. Our exploratory latent analysis suggests that hidden representations may encode correctness-related signals that output confidence does not expose.

## Metadata
- **Published**: 2026-10-08T06:07:44Z
- **Authors**: Ravishka Rathnasuriya, Wei Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11300v1)