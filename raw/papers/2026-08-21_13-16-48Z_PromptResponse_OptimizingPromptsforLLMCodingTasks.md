---
title: PromptResponse: Optimizing Prompts for LLM Coding Tasks
published: 2026-08-21T13:16:48Z
authors: Erik Thureck, Robert Kühnen, Tim Jacobowitz
url: http://arxiv.org/abs/2608.21074v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PromptResponse: Optimizing Prompts for LLM Coding Tasks

## Abstract
Large language models (LLMs) are increasingly used in research workflows and software development pipelines, yet their output remains sensitive to input prompt variations. This paper presents $\unicode{x00AB}$PromptResponse$\unicode{x00BB}$, a controlled study examining how formatting and LLM-based tuning of coding task prompts affect the resulting code's performance, efficiency, and stability. Using five semantically identical yet syntactically distinct variants of the HumanEval dataset$\unicode{x2014}$baseline, JSON, Markdown, YAML, and an LLM-tuned version$\unicode{x2014}$we had GPT-4o solve its coding problems over 8200$\unicode{x00A0}$executions. Our results show that consistent formatting$\unicode{x2014}$especially JSON$\unicode{x2014}$improves generation efficiency and syntactic stability, with minor gains in task performance. Conversely, the LLM-tuned prompts resulted in significantly degraded task performance without significant improvements in any other dimension. These findings suggest that low-effort reformatting alone can yield measurable improvements, while tuning must account for model alignment. We conclude our work with providing a set of practical recommendations informed by our results as well as releasing our dataset variants and evaluation pipeline for future work.

## Metadata
- **Published**: 2026-08-21T13:16:48Z
- **Authors**: Erik Thureck, Robert Kühnen, Tim Jacobowitz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21074v1)