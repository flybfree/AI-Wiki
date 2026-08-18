---
title: Do LLMs Know What to Ask and When? Evaluating Multi-Turn Information Seeking
published: 2026-08-14T18:23:32Z
authors: Yepeng Huang, Jiawen Zhang, Michelle Dai, Xiaorui Su, Shanghua Gao, Zi Wang, Marinka Zitnik
url: http://arxiv.org/abs/2608.14808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do LLMs Know What to Ask and When? Evaluating Multi-Turn Information Seeking

## Abstract
When a user question is underspecified, a capable model should recognize that its context is insufficient, identify the missing information, ask for it, and respond only once that information determines a unique answer. We formalize multi-turn information seeking as solving a k-underspecified constraint satisfaction problem, where k is the number of variables jointly required to determine the target and therefore measures the degree of missing information. We instantiate the formulation in MT-InfoSeek, a controlled evaluation suite of 5,251 problems and 9,006 task instances spanning mathematics, logic, biology, medicine, and general knowledge. We evaluate models along three axes: what they ask, when they ask it, and how the acquired information affects the final answer. Performance degrades across models and domains as underspecification increases. Models recognize that additional information is needed but underestimate how much, and in logical problems at k = 2 they under-predict the degree of missing information about four times as often as they over-predict it. They also fail to identify a minimal sufficient set of queries, improve only marginally when given the true k, and often stop before acquiring sufficient information. In tasks with ordered dependencies, an incorrect query order reduces final accuracy even when the model eventually acquires all necessary information. We measure information seeking directly through final sufficiency, which records whether the acquired information determines the target independent of answer generation. This separation shows differences between models that final accuracy alone does not capture, and indicates that the ability to seek information over multiple turns is distinct from the ability to generate answers and is not measured by current LLM evaluations.

## Metadata
- **Published**: 2026-08-14T18:23:32Z
- **Authors**: Yepeng Huang, Jiawen Zhang, Michelle Dai, Xiaorui Su, Shanghua Gao, Zi Wang, Marinka Zitnik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14808v1)