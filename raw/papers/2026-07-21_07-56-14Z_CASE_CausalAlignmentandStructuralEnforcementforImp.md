---
title: CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness
published: 2026-07-21T07:56:14Z
authors: Ziming Wang, Yinghua Yao, Changwu Huang, Ke Tang, Xin Yao
url: http://arxiv.org/abs/2607.18820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness

## Abstract
Chain-of-thought (CoT) reasoning is widely used to improve both the performance and interpretability of large language models (LLMs), yet the generated reasoning may not faithfully support the final answer. We study this problem from a causal perspective, where a faithful CoT process should follow the chain $Z\rightarrow X\rightarrow Y$, with $Z$, $X$, and $Y$ denoting the instruction, reasoning chain, and final answer, respectively. In this process, the instruction should affect the answer only through the reasoning chain. However, conventional autoregressive LLMs condition answer generation on both the instruction and the CoT, which still allows a direct instruction-to-answer shortcut. To address this issue, we propose CASE, a framework that combines training-time causal alignment and inference-time structural enforcement. During training, CASE builds counterfactual-CoT, biased-instruction, and empty-instruction datasets, and applies selective-loss fine-tuning to strengthen CoT-to-answer dependence while suppressing instruction shortcuts. During inference, CASE masks direct attention from instruction tokens to answer tokens, preventing the model from bypassing the generated CoT. We provide an information-theoretic analysis showing how these components promote faithful chains. Experiments on three models and four benchmarks show that CASE achieves a 37\% average per-setting relative improvement in overall CoT faithfulness over the strongest baselines, exhibits stronger cross-dataset faithfulness transfer, and maintains competitive average accuracy. Code is available at https://github.com/oddwang/CASE.

## Metadata
- **Published**: 2026-07-21T07:56:14Z
- **Authors**: Ziming Wang, Yinghua Yao, Changwu Huang, Ke Tang, Xin Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18820v1)