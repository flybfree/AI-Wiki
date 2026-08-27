---
title: From Passive Response to Proactive Correction: Enhancing LLM Robustness Against Input Fact Perturbations
url: http://arxiv.org/abs/2608.25894v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_15-13-50Z_FromPassiveResponsetoProactiveCorrection_Enhancing.md
generated_at: 2026-08-26 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DEDUCE, a three‑stage framework that converts large language models from passive responders into proactive error correctors when faced with factually erroneous inputs. Experiments on TruthfulQA, FalseQA, and the newly created MisFactQA benchmark show that DEDUCE markedly boosts both response accuracy and the model’s ability to detect and fix misconceptions. The improvements are observed across Qwen, LLaMA, and Gemma families, confirming the approach’s effectiveness and scalability.

## Key Takeaways
- DEDUCE adds a detection stage that extracts fine‑grained facts from inputs and verifies them against external knowledge sources before generating an answer.  
- The framework includes a deliberation step where multiple perspectives are considered to devise correction strategies, ensuring robust fixes rather than superficial edits.  
- Evaluation on MisFactQA introduces new metrics for robustness, revealing that DEDUCE reduces factual hallucinations and improves overall performance.

## Context
Hallucination mitigation in LLMs has traditionally relied on assuming user inputs are reliable, which often fails when users introduce misleading premises. This work addresses the gap by treating input fact errors as active perturbations that can mislead model reasoning, thereby advancing research toward more resilient AI systems.

## Implications
For practitioners, DEDUCE offers a practical pathway to deploy LLMs in high‑stakes environments where factual correctness is critical, such as medical or legal advice. The framework’s scalability across major model families suggests it could become a standard component of future LLM pipelines, fostering trust and reducing downstream errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25894v1)
