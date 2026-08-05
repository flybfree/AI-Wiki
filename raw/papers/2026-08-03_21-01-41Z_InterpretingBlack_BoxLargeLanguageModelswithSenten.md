---
title: Interpreting Black-Box Large Language Models with Sentence-Level Energy Landscapes
published: 2026-08-03T21:01:41Z
authors: Maryam Rezaee, Pooriya Safaei, Maryam Asgarinezhad, Fatemeh Seyyedsalehi
url: http://arxiv.org/abs/2608.02879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpreting Black-Box Large Language Models with Sentence-Level Energy Landscapes

## Abstract
The widespread adoption of proprietary Large Language Models (LLMs) accessed strictly through closed APIs has created a critical challenge for responsible deployment: a fundamental lack of interpretability. To address this, we propose a model-agnostic, post-hoc attribution interpreter operating at the sentence level. Our approach trains an Energy-Based Model (EBM) as a surrogate to capture the LLM's internal conceptual consistency between prompts and responses. This energy landscape guides the training of a lightweight interpreter network. Uniquely, our interpreter operates as a standalone tool; once trained, it quantifies the influence of prompt sentences on a user-specified target output without requiring further API queries to the LLM. By globally training a local interpreter across diverse inputs, our framework captures broader generation patterns and mitigates instance-specific biases. Experiments demonstrate that our EBM accurately simulates the target LLM, allowing the interpreter to effectively identify the prompt sentences most influential in generating specific target outputs.

## Metadata
- **Published**: 2026-08-03T21:01:41Z
- **Authors**: Maryam Rezaee, Pooriya Safaei, Maryam Asgarinezhad, Fatemeh Seyyedsalehi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02879v1)