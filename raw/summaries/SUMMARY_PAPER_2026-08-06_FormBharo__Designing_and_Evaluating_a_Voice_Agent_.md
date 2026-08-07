---
title: FormBharo: Designing and Evaluating a Voice Agent for Conversational Form Filling in Rural India
url: http://arxiv.org/abs/2608.06027v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_13-34-22Z_FormBharo_DesigningandEvaluatingaVoiceAgentforConv.md
generated_at: 2026-08-06 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
FormBharo is a voice‑based system that fills structured enrollment forms by phone in rural India using large language models paired with deterministic rule‑based validation and flow control. The pilot with ARMMAN showed that end‑to‑end form completion can drop up to ~41 points when noisy real‑speech transcripts replace reference ones, but rule controls recover many errors. Optimal model choice is determined through a Pareto‑based weighted‑sum scalarization balancing accuracy, cost and latency.

## Key Takeaways
- FormBharo integrates LLM transcription, extraction, and reply generation with deterministic validation; error‑prone real‑speech transcripts cause up to ~41 point loss in form completion.  
- Rule‑based flow control recovers many turn‑level extraction errors, allowing cheaper models to match or exceed frontier models on end‑to‑end tasks.  
- End‑to‑end evaluation is essential because component performance does not predict final outcome; GPT‑5.5 leads extraction accuracy but ranks lower on completion.

## Context
This work fills a gap between AI language models and low‑resource settings where voice interfaces must operate under strict latency and cost constraints. It shows that deterministic controls can mitigate LLM weaknesses, offering a practical path for deploying LLMs in constrained environments such as rural health enrollment programs.

## Implications
Hybrid approaches combining LLMs with rule‑based systems are viable for scalable AI deployment in underserved populations. Practitioners should prioritize end‑to‑end evaluation over component metrics when selecting models for cost‑sensitive applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06027v1)
