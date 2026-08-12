---
title: Persona Conditioning as an Assessor-Sensitivity Probe for LLM-Based IR Evaluation
url: http://arxiv.org/abs/2608.10385v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_02-26-47Z_PersonaConditioningasanAssessor_SensitivityProbefo.md
generated_at: 2026-08-11 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how persona‑conditioned judging affects the reliability of large language model (LLM) relevance assessments in information retrieval. By comparing five specialized assessor personas with a standard UMBRELA baseline across six LLM backbones on two benchmark datasets, the authors find that sensitivity is structured and domain‑specific rather than uniform.

## Key Takeaways
- Assessor judgments remain close to the baseline while shifting assessment strictness, evidential thresholds, or interpretation emphasis instead of causing widespread relevance reversals.  
- High‑capacity models preserve system ranking agreement, whereas smaller models amplify persona‑induced instability in evaluations.  
- Sensitivity concentrates on particular retrieval systems and system types, especially neural ranking/reranking pipelines on DL20 and RAG‑oriented pipelines on RAG24.

## Context
The growing reliance on LLMs for IR evaluation raises concerns about hidden biases introduced by assessor framing. This work provides empirical evidence that persona conditioning can be used as a diagnostic tool to expose such biases without altering the underlying retrieval performance.

## Implications
Practitioners should treat persona‑conditioned judgments as controlled probes when stress‑testing LLM‑based IR pipelines, ensuring that evaluation outcomes are not overly influenced by assessor role or model capacity. This insight helps align reported metrics with more stable, system‑specific relevance scores.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10385v1)
