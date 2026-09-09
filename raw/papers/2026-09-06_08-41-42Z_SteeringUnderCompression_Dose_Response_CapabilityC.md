---
title: Steering Under Compression: Dose-Response, Capability Cost, and Failure Asymmetry in Quantized LLMs
published: 2026-09-06T08:41:42Z
authors: Saurav Bhandari, Benjamin Wade
url: http://arxiv.org/abs/2609.06473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Steering Under Compression: Dose-Response, Capability Cost, and Failure Asymmetry in Quantized LLMs

## Abstract
Inference-time activation steering enables behavioral control of large language models without parameter modification, while post-training quantization reduces memory and compute costs for deployment. Despite their growing convergence in practice, the interaction between these two techniques remains uncharacterized. We systematically study activation steering under weight-only quantization (INT8 and NF4) across four open-weight 7-9B models and two behavioral targets: judged sentiment and judge-free reasoning length. Using an iso-effect framework that compares capability costs at matched behavioral effect, we find that sentiment steering survives quantization intact. After correcting a GSM8K parser artifact with a uniform v2.3.1 rescore, the pooled INT8 contrast is -0.010 (90% CI [-0.026, +0.007]), descriptively Equivalent under the preregistered three-label rule, while NF4 remains Inconclusive at -0.017 ([-0.067, +0.033]). In contrast, reasoning length exhibits a surprising asymmetric dose-response: lengthening is graded but terminates in cap-runaway and collapse, while shortening is a step function with only 12-30% shortening (model-dependent) before discontinuous failure. We expose a methodological pitfall: the naive iso-effect ladder anchors on the collapse floor for floor-bounded targets, and we introduce a censored construction that restores interpretable crossings. We also quantify a substantial baseline capability shift for Mistral-NF4 (0.545 to 0.365 GSM8K at alpha=0), demonstrating that compression can dominate the steering intervention. Despite this, steering vectors remain highly collinear with their FP16 siblings (cosine similarity 0.989-0.998 for INT8, 0.945-0.990 for NF4), confirming that the behavioral direction survives quantization even when the cost structure does not. All code and data are released.

## Metadata
- **Published**: 2026-09-06T08:41:42Z
- **Authors**: Saurav Bhandari, Benjamin Wade
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06473v1)