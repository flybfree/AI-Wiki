---
title: Free-Text Evaluation of LLMs for 5G Domain Knowledge and Fault Analysis using LLM-as-Judge
published: 2026-08-21T12:09:51Z
authors: Rishiraj Sengupta, Sotiris Chatzimiltis, Mohammad Shojafar, Xiatian Zhu
url: http://arxiv.org/abs/2608.21021v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Free-Text Evaluation of LLMs for 5G Domain Knowledge and Fault Analysis using LLM-as-Judge

## Abstract
Real-world fault analysis in 5G and emerging 6G networks demands domain expertise to analyze free-text diagnostics, including root-cause explanations and recommended actions. LLMs have emerged as a promising approach to automating this, yet whether lightweight, edge-deployable models are capable of performing in-depth free-text diagnostics remains an open question. While existing benchmarks rely on restrictive MCQs with fixed answer keys, this paper evaluates 5G domain understanding and fault analysis in a free-text generation format. Transitioning to this paradigm requires evaluating lightweight, edge-deployable AI models on open-ended diagnostic reasoning, alongside a dependable framework to validate these text outputs at scale. To address this we evaluate three lightweight LLMs, Claude-Haiku-4.5, GPT-5.4-Mini, and Gemini-3.1-Flash-Lite, on free-text 5G domain knowledge and fault-analysis tasks across three benchmarks, TeleQNA ORAN FT, 5G-Faults FT, and TeleInter FT. Three independent frontier judges score outputs, and pairwise inter-judge agreement is measured as an empirical test of the LLM-as-Judge methodology. All three models reach at least 90% accuracy on fault diagnosis, while zero-shot recall of 3GPP and O-RAN specifications remains the critical gap, with all models scoring below 60%. Mean inter-judge agreement is at least 0.90 across all runs, indicating that multi-judge LLM scoring produces consistent, reproducible grades for open-ended telecom responses. Operationally, Gemini-3.1-Flash-Lite offers the best efficiency trade-off, combining competitive accuracy with the lowest inference cost and latency, making it the most suitable candidate for production telecom deployments.

## Metadata
- **Published**: 2026-08-21T12:09:51Z
- **Authors**: Rishiraj Sengupta, Sotiris Chatzimiltis, Mohammad Shojafar, Xiatian Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21021v1)