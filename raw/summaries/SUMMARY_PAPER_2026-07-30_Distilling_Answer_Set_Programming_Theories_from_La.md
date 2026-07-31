---
title: Distilling Answer Set Programming Theories from Large Language Models
url: http://arxiv.org/abs/2607.28086v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_11-53-43Z_DistillingAnswerSetProgrammingTheoriesfromLargeLan.md
generated_at: 2026-07-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper explores whether large language models can automatically generate complete and correct Answer Set Programming theories using a neurosymbolic protocol. The study shows that several frontier models achieve high accuracy on three VQA benchmarks while others perform poorly, especially GPT‑5 when reference theories are not provided.

## Key Takeaways
- Frontier models such as Claude Sonnet 4.6, Claude Opus 4.7, and DeepSeek V4 Pro reach near‑perfect scores (100% on CLEVR, ~93% on GQA) by deriving accurate theories within the one‑hour limit.  
- GPT‑5’s performance is highly dataset dependent: it excels on CLEVR but drops to 42% on GQA and 87% on CLEVRER without reference theories, indicating a need for external guidance.  
- Adding handwritten reference theories improves most models by only ±3.4 percentage points but can reduce GPT‑5’s accuracy by 3–19 points, highlighting the trade‑off between assistance and model reliance.

## Context
The work addresses a longstanding challenge in AI reasoning: translating natural language into formal logical systems. By testing large language models against ANSWER SET PROGRAMMING tasks, the research illustrates how neural networks can be leveraged for symbolic computation without explicit programming knowledge.

## Implications
For practitioners, this suggests that integrating LLMs with solvers could accelerate theory generation in automated planning and constraint solving. However, it also warns that reliance on external references may degrade model robustness, urging careful evaluation of assistance mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28086v1)
