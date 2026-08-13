---
title: LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification
url: http://arxiv.org/abs/2608.11753v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_07-46-29Z_LabelFusion_TS_FusingLargeLanguageModels_Transform.md
generated_at: 2026-08-12 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether market time series can improve classification of Federal Reserve statements into hawkish, dovish, or neutral stances. It introduces LabelFusion-TS, a voting network combining RoBERTa, an LLM, and time‑series transformers, achieving 70.2% weighted F1 on 2015–2022 data versus 64.1% for zero‑shot LLM.

## Key Takeaways
- The fused system outperforms the zero‑shot LLM by using market series as an auxiliary input, raising accuracy to 70.2% weighted F1.
- Only a few hundred human labels are needed because RoBERTa is first pre‑trained on LLM‑generated pseudo‑labels before fine‑tuning.
- The approach demonstrates that time‑series transformers can be integrated into financial text classification with minimal labeled data.

## Context
Financial text analysis often ignores contextual market dynamics, limiting the ability to capture sentiment shifts. This work shows that incorporating macroeconomic signals can enhance model performance without large annotated corpora, aligning with trends toward multimodal AI for domain‑specific tasks.

## Implications
Practitioners in finance and policy monitoring can leverage this fusion to build more robust stance classifiers using real‑time market data. The method offers a scalable template for other domains where external time series may inform textual sentiment analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11753v1)
