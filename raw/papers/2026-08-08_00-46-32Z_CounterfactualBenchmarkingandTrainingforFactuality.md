---
title: Counterfactual Benchmarking and Training for Factuality Consistency and Order-Robust Grounded Reasoning in LLMs over Heterogeneous Knowledge
published: 2026-08-08T00:46:32Z
authors: Shibo Chu, Yuze Liu, Tiehua Zhang, Zhishu Shen, Lianghua He, Haofen Wang, Zhijun Ding
url: http://arxiv.org/abs/2608.07838v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Counterfactual Benchmarking and Training for Factuality Consistency and Order-Robust Grounded Reasoning in LLMs over Heterogeneous Knowledge

## Abstract
Large language models (LLMs) have increasingly supported response generation grounded in user-provided knowledge spanning heterogeneous structures. However, existing benchmarks provide limited assessment of whether LLMs can faithfully perform multi-hop reasoning chains across such knowledge contexts while remaining robust to variations in their input order. We introduce TKFQA, a factuality consistency benchmark comprising 10,130 question-answering (QA) pairs grounded in tables, texts, and knowledge graphs (KGs). Each example is constructed from an explicit counterfactual reasoning chain, enabling the joint evaluation of answer correctness, reasoning-chain accuracy, and robustness to different input-order. An extensive evaluation of 14 open- and closed-source LLMs reveals that state-of-the-art models exhibit limited reasoning-chain accuracy and remain sensitive to variations in the input order of heterogeneous knowledge contexts. To address these limitations, we propose ORLF, an LLM-agnostic training framework that models cross-context topological relations through knowledge-specific latent vectors. ORLF integrates context-wise position encoding, a latent-bridge attention mask, and topological knowledge bias to preserve knowledge-specific bias and encode topological semantics. Experiments across four LLM backbones show that ORLF outperforms competitive training-free and LoRA-based baselines, improving average Exact Match and Reasoning-Chain Accuracy by 2.15% and 4.29%, respectively, while reducing order-induced performance standard deviation by 0.04% to 3.01%.

## Metadata
- **Published**: 2026-08-08T00:46:32Z
- **Authors**: Shibo Chu, Yuze Liu, Tiehua Zhang, Zhishu Shen, Lianghua He, Haofen Wang, Zhijun Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07838v1)