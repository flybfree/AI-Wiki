---
title: Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation
url: http://arxiv.org/abs/2609.01604v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-59-49Z_BeyondScores_UnderstandingLLM_as_a_JudgeMechanisms.md
generated_at: 2026-09-01 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how LLM evaluators assign ratings by probing mechanisms across readability and adequacy dimensions using controlled perturbations, attention tracing, logit‑lens projection, and attention‑head knockout on Themis (Llama‑3‑8B) and Prometheus (Mistral‑7B). It discovers that the evaluation pipeline operates in two stages: below layer 15 local error comparison routes to the final input position, while above it an MLP cascade integrates the signal and writes the rating at a late residual stream (L=26 for Themis, L=25 for Prometheus).

## Key Takeaways
- Evaluation uses a structured pipeline with two mechanisms: local error comparison routing and MLP cascade integration.  
- Crystallization occurs in the residual stream at a late layer, indicating where the decision is finalized.  
- Fine‑tuning suppresses earlier MLP contribution at the last position and advances crystallization depth, showing fine‑tuning modifies an existing substrate rather than building the pipeline from scratch.

## Context
LLM‑as‑a‑judge systems are widely used for automatic scoring of natural language generation, yet their internal evaluation logic remains opaque. Understanding these mechanisms is crucial for assessing reliability, fairness, and robustness of automated judgments in AI research and industry practice.

## Implications
Practitioners can use this insight to design more transparent evaluators that reduce hidden bias from layer‑specific artifacts. This knowledge also supports the development of training signals that reflect genuine content quality rather than model‑specific evaluation artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01604v1)
