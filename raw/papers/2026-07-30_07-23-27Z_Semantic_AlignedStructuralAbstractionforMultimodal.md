---
title: Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis
published: 2026-07-30T07:23:27Z
authors: Wei Chen, Junkai Li, Tongguan Wang, Hui Liu, Feiyue Xue, Chuanxiang Ma, Ying Sha
url: http://arxiv.org/abs/2607.27790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis

## Abstract
Multimodal Sentiment Analysis (MSA) aims to interpret complex human emotions by integrating natural language with non-verbal modalities. Non-verbal modalities share a structural isomorphism with natural language, as both can be viewed as feature sequences evolving over time. This isomorphism enables the transformation of non-verbal modalities into text-like tokens for unified semantic reasoning. Large Language Models (LLMs), designed to understand and generate sequential data, can thus be utilized to interpret complex affective sequences. However, existing LLM-based methods primarily capture low-level superficial features, failing to model affective semantics arising from structural variations and contextual interactions. To address this limitation, we propose \textbf{SentiLLM}, a unified framework that leverages \textit{Semantic-Aligned Structural Abstraction} to distill continuous raw signals into compact, semantically meaningful tokens. Specifically, we introduce a \textit{Dual-Stream Salience-Context Calibration Mechanism}, which disentangles non-verbal feature sequences into a focus stream and an ambient stream. The focus stream captures salient sentiment shifts (e.g., facial expressions) guided by textual priors, while the ambient stream characterizes stable background states. Through calibrating these dynamic sentiment shifts against background states, SentiLLM effectively projects non-verbal modalities into a unified semantic space, making them naturally understandable for LLMs. Serving as a plug-and-play module, SentiLLM significantly improves discriminative performance with only a small number of trainable parameters. Our method achieves superior performance on four datasets, MOSI, MOSEI, CH-SIMS, and CH-SIMS v2, demonstrating the effectiveness of the structural abstraction paradigm in MSA. Our code is available at: \href{https://github.com/especiallyW/SentiLLM}.

## Metadata
- **Published**: 2026-07-30T07:23:27Z
- **Authors**: Wei Chen, Junkai Li, Tongguan Wang, Hui Liu, Feiyue Xue, Chuanxiang Ma, Ying Sha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27790v1)