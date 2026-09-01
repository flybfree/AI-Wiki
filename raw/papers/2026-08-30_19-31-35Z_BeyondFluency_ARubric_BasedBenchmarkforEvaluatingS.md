---
title: Beyond Fluency: A Rubric-Based Benchmark for Evaluating Saudi Dialect and Cultural Competence in Large Language Models
published: 2026-08-30T19:31:35Z
authors: Ghassan Al-Sumaidaee, Sajjad Abdoli, Ahmed Rashad, Maxim Legg
url: http://arxiv.org/abs/2608.29990v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Fluency: A Rubric-Based Benchmark for Evaluating Saudi Dialect and Cultural Competence in Large Language Models

## Abstract
Large language models are increasingly deployed in Arabic-speaking markets, yet standard benchmarks overwhelmingly reward Modern Standard Arabic (MSA) fluency while leaving dialectal and culturally grounded competence unmeasured. This gap is consequential: everyday Arabic is largely dialectal, and dialect encodes social meaning that MSA-centric evaluation cannot capture. We present a rubric-based benchmark for the Saudi dialect, comprising 31 expert-authored prompts spanning idiomatic, pragmatic, lexical, and culturally-embedded phenomena, each paired with an expert-established ground truth. Our methodology separates evaluation into a model-agnostic phase, in which atomic, MECE positive criteria are derived solely from the ground truth, and a model-specific phase, in which four state-of-the-art systems -- Claude Opus 5, Gemini 3.7, GPT-5.6, and Kimi K3 -- are scored against those criteria and penalised for errors they actively introduce. Across 124 model-prompt evaluations we catalogue 466 error instances under a nine-category taxonomy. The four systems cluster within a narrow macro-average band (42.7%-53.1%), with no model exceeding 55% and every model recording at least one negative-scoring prompt, confirming that Saudi dialectal competence remains broadly unsolved. Notably, Ambiguous Framing is the dominant failure mode (37.3% of errors) while outright Hallucination accounts for only 11.2%, indicating that models fail less by stating falsehoods than by distorting register and flattening pragmatic nuance. We further observe a consistency-versus-ceiling trade-off and model-distinctive error signatures. We release the full prompt set, ground truths, and scored rubrics to support reproducible dialectal evaluation.

## Metadata
- **Published**: 2026-08-30T19:31:35Z
- **Authors**: Ghassan Al-Sumaidaee, Sajjad Abdoli, Ahmed Rashad, Maxim Legg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29990v1)