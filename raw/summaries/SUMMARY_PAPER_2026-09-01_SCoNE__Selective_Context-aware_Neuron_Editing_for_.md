---
title: SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation
url: http://arxiv.org/abs/2609.00689v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_04-10-32Z_SCoNE_SelectiveContext_awareNeuronEditingforRobust.md
generated_at: 2026-09-01 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SCoNE, a training‑free model editing method that boosts the robustness of retrieval‑augmented generation (RAG) systems to noisy document retrieval. By selectively strengthening context‑aware feed‑forward neurons identified through high attribution and cross‑input variability scores, SCoNE reduces hallucinations without requiring fine‑tuning or inference overhead. Experiments on multiple knowledge‑intensive QA benchmarks with two LLM backbones show consistent gains over baseline approaches.

## Key Takeaways
- SCoNE improves RAG robustness by selectively strengthening neurons that exhibit both high attribution and high cross‑input variability, directly addressing retrieval noise.
- The method is training‑free, requiring only a small set of mining samples to identify target neurons, eliminating fine‑tuning steps.
- Results demonstrate consistent performance improvements across diverse QA datasets and two LLM architectures.

## Context
RAG systems rely heavily on the quality of retrieved documents; even minor noise can cause LLMs to generate inaccurate answers. Recent work focuses on post‑hoc editing techniques that adjust model behavior without retraining, aiming to make retrieval outputs more reliable. SCoNE’s approach aligns with this trend by offering a lightweight, attention‑based neuron selection strategy.

## Implications
For practitioners, SCoNE provides an easy way to enhance RAG reliability in production systems where retraining is costly or impractical. In industry, it can reduce hallucination rates and improve user trust in AI‑driven answer generation, supporting broader adoption of retrieval‑augmented applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00689v1)
