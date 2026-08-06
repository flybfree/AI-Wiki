---
title: When Absence Is Evidence: Evaluating Completeness-Sensitive Negative Reasoning in Large Language Models
published: 2026-08-05T08:53:16Z
authors: Byoungjae Min, Kennedy Edemacu, Sae-Hong Cho, Yoonhyuk Choi, Beakcheol Jang, Jong Wook Kim
url: http://arxiv.org/abs/2608.04591v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Absence Is Evidence: Evaluating Completeness-Sensitive Negative Reasoning in Large Language Models

## Abstract
Large language models (LLMs) are often asked whether something is absent from a record, list, or retrieved context. Yet non-observation licenses a negative answer only when evidence completely covers the query scope; otherwise, the answer should remain unknown. We call this completeness-sensitive negative reasoning. We introduce CROWN-QA, comprising CROWN-Synth, a controlled paired core that fixes the question and observed facts while varying only query-relative coverage, and CROWN-Real, a real-document contrast-set evaluation with controlled coverage variants. Across three LLM families, models show unstable closure judgments and substantial over-closure, failing to reliably distinguish a justified negative answer (Certified-Negative) from insufficient evidence (Unknown). The dominant CROWN-Synth failure is asymmetric: models often recognize implicitly complete evidence yet treat implicitly partial evidence as query-covering. Prompting redistributes errors between over- and under-closure rather than consistently resolving them. Structured certificate elicitation traces many errors to evidence-coverage mischaracterization. CROWN-Real shows that the core partial-coverage asymmetry persists on real-document content, while its strength and the balance between over- and under-closure vary by model, prompt, and source.

## Metadata
- **Published**: 2026-08-05T08:53:16Z
- **Authors**: Byoungjae Min, Kennedy Edemacu, Sae-Hong Cho, Yoonhyuk Choi, Beakcheol Jang, Jong Wook Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04591v1)