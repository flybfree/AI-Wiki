---
title: Lumen-bench: Cross-Lingual Safety Gaps and the Say-Do Problem in Tool-Calling Large Language Models
published: 2026-10-10T19:19:50Z
authors: Giovana Kerche Bonás, Thiago Laitz, Thales Sales Almeida, João Guilherme Alves Santos
url: http://arxiv.org/abs/2610.15134v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lumen-bench: Cross-Lingual Safety Gaps and the Say-Do Problem in Tool-Calling Large Language Models

## Abstract
When a large language model refuses an unethical request, what does refusal mean? In conversation, refusal is bounded by what the model says; once the model is equipped with executable tools, what it does can diverge from what it says, a failure mode that English-only evaluations cannot fully reveal. We introduce Lumen-bench, a behavioral benchmark of tool-calling ethics spanning 30 models, five languages (Portuguese, English, Spanish, Mandarin Chinese, Hindi), 108 Portuguese-authored scenarios, six social-pressure conditions, two system prompts (ethical and neutral), and 21 generic tools. The evaluation comprises 194,400 trials. Judgments come from a reasoning-model judge (o4-mini), calibrated against one Portuguese-speaking author ($n=83$; harmful/non-harmful $κ=0.78$), compared with two other provider judges (Fleiss' $κ=0.78$, $n=607$), and complemented by retrospective sandbox replay. Four findings emerge. (i) Within-model comparisons support higher harmful-action rates in Hindi and Portuguese than English under the ethical prompt, and Hindi and Spanish under the neutral prompt, after multiple-testing correction. (ii) Premium models have lower median violation rates, although price does not guarantee safety or competence. (iii) Replacing the ethical system prompt with a neutral one raises pooled violation rates from 2.76\% to 13.64\%. (iv) In 8.57\% of substantive-call cases, refusal or ethical objection accompanies a harmful tool call: the judges consistently identify the say-do gap, although they differ in how many responses they assign to this category. Matched benign controls demonstrate legitimate task completion in 82.8\% of 3,300 trials. Code and reproduction scripts are available at https://github.com/TropicAI-Research/lumen.

## Metadata
- **Published**: 2026-10-10T19:19:50Z
- **Authors**: Giovana Kerche Bonás, Thiago Laitz, Thales Sales Almeida, João Guilherme Alves Santos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15134v1)