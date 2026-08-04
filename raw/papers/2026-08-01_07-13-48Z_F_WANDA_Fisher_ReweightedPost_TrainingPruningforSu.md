---
title: F-WANDA: Fisher-Reweighted Post-Training Pruning for Sustainable Deployment of Large Language Models
published: 2026-08-01T07:13:48Z
authors: Himanshu Mishra
url: http://arxiv.org/abs/2608.00481v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# F-WANDA: Fisher-Reweighted Post-Training Pruning for Sustainable Deployment of Large Language Models

## Abstract
One-shot post-training pruning is the most energy-frugal compression strategy for largelanguage models (LLMs), yet existing approaches trade either quality (WANDA) or compute cost (SPARSEGPT). We introduce F-WANDA, a drop-in modification of WANDA that reallocates the per-row keep budget across output neurons in proportion to the empirical Fisher information of the pre-activation. The Fisher signal is collected in a single additional backward pass over the same calibration corpus WANDA already uses; no weights are updated. On LLAMA-2-7B at 50 % unstructured sparsity, F-WANDA attains WikiText-2 perplexity of 6.85, matches WANDA fluency, and improves 5-shot MMLU by +1.6 pp over WANDA and +1.1 pp over SPARSEGPT, while incurring only one-third of SPARSEGPT pruning wall-clock and energy. The headline trade-off is achieved without extra calibration data or fine-tuning, placing F-WANDA on the Pareto frontier of quality versus pruning cost for sustainable LLM compression.

## Metadata
- **Published**: 2026-08-01T07:13:48Z
- **Authors**: Himanshu Mishra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00481v1)