---
title: More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning
published: 2026-08-22T17:24:28Z
authors: Orion Powers, Daniella Seum, Khaled Slhoub
url: http://arxiv.org/abs/2608.22048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning

## Abstract
Large language models are increasingly deployed on local hardware for privacy, cost, and accessibility reasons. Yet many evaluations emphasize accuracy while fewer quantify local runtime and energy, characterize failure modes, or apply paired statistical comparisons under controlled conditions. This paper presents a controlled, documented procedure for evaluating locally hosted LLMs on mathematical reasoning. It combines fixed inference settings, hierarchical answer extraction and verification, explicit failure-mode classification, and per-question resource measurement, and reports accuracy with paired significance tests and effect sizes. We demonstrate it in a preliminary study of three compact open-weight models under five billion parameters, Gemma3:4b (Google), Phi3:3.8b (Microsoft), and Qwen3:4b (Alibaba), across datasets spanning Grade 8 Math, Calculus I, and Advanced Probability and Statistics. All models ran through the same local inference server on one workstation, using a shared prompt template, controlled settings, and a matched question set per dataset. No single model dominates. Qwen3:4b is most accurate on two datasets and Gemma3:4b on Calculus I, yet Gemma3:4b returns roughly three times more correct answers per watt-hour than Qwen3:4b on every dataset while generating far fewer output tokens; Qwen3:4b requires substantially more generation time, energy, and output per question. Phi3:3.8b is substantially less accurate on all three datasets; its low extraction-failure rate indicates incorrect answers rather than unparsed output, though we caveat possible prompt-format effects. These preliminary findings indicate that accuracy alone is an insufficient basis for selecting a local model.

## Metadata
- **Published**: 2026-08-22T17:24:28Z
- **Authors**: Orion Powers, Daniella Seum, Khaled Slhoub
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22048v1)