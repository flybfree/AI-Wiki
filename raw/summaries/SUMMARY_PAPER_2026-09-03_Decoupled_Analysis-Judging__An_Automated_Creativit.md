---
title: Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks
url: http://arxiv.org/abs/2609.03432v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_06-44-04Z_DecoupledAnalysis_Judging_AnAutomatedCreativityEva.md
generated_at: 2026-09-03 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CreaEval, an automated creativity evaluator that separates the analysis and judging phases for Contextually-Grounded and Procedurally-Structured Tasks. By decoupling these steps, CreaEval reduces LLM biases such as verbosity and leniency, achieving a 22.74% average performance improvement over second‑best baselines on CGPST and two simple creativity tasks.

## Key Takeaways
- Memory-augmented analysis converts multi‑step responses into structured evaluation evidence while maintaining cross‑step memory, enabling the system to capture dependencies across steps.
- Evidence‑based judging uses only the extracted evidence rather than raw responses, preventing direct exposure to LLM biases and improving reliability.
- The approach yields a 22.74% average improvement across tasks, demonstrating its generalizability beyond CGPST.

## Context
Automated evaluation of creativity remains challenging because large language models exhibit systematic biases that degrade consistency in complex multi‑step tasks. Existing methods either require task‑specific training or apply LLM‑as‑a‑Judge directly, both of which struggle with reliability and bias mitigation.

## Implications
The decoupled CreaEval framework offers a scalable solution for trustworthy automated grading of creative outputs, benefiting educational platforms, content creation tools, and research that rely on objective creativity metrics. By reducing bias and enhancing stability, it can support more reliable decision‑making in high‑stakes applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03432v1)
