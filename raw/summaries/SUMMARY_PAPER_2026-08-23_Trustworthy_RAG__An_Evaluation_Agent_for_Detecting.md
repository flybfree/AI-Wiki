---
title: Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems
url: http://arxiv.org/abs/2608.21095v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_13-42-41Z_TrustworthyRAG_AnEvaluationAgentforDetectingMisinf.md
generated_at: 2026-08-23 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an Evaluation Agent that detects misinformation and knowledge poisoning in Retrieval-Augmented Generation (RAG) systems by combining factual verification with a multi‑signal poison detector. On TruthfulQA, it achieves 91% accuracy, 100% precision, and 100% recall for instruction injection attacks.

## Key Takeaways
- The agent uses Natural Language Inference (NLI) to verify retrieved facts, achieving high factual verification scores.
- It employs a five‑signal poison detector with relevance‑weighted aggregation and a Trust Index formula T = 0.4F + 0.35C + 0.25(1‑P), which balances factuality, confidence, and poisoning probability.
- The detection remains robust across three LLMs, delivering ROC‑AUC values between 0.73 and 0.81, while per‑LLM threshold calibration improves baseline performance.

## Context
RAG systems are widely used to extend LLM capabilities with external data, yet they inherit the trust gap where relevance does not equal truth. This work addresses that gap by providing a systematic evaluation framework for detecting poisoning attacks before generation occurs.

## Implications
For practitioners, the Trust Index offers a lightweight metric for integrating safety checks into RAG pipelines without sacrificing generation quality. The findings suggest that model size is less important than how feedback loops are calibrated, guiding future research toward domain‑specific calibration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21095v1)
