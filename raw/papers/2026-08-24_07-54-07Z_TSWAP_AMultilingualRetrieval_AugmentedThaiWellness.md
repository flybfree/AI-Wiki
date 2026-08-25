---
title: TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor
published: 2026-08-24T07:54:07Z
authors: Pornthep Ukosaramig, Kobkrit Viriyayudhakorn
url: http://arxiv.org/abs/2608.22917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor

## Abstract
We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers. An unmodified open-weight LLM (Qwen3.6-35B-A3B on vLLM) is grounded on a ~30.6K-chunk Thai index by a hybrid dense-sparse retriever with cross-encoder reranking; a first-turn query classifier forces tool-based retrieval for entity lookups; a rule-based safety layer enforces medical scope and Thai emergency routing; and all eight languages are served zero-shot with translate-then-retrieve. We release the first Thai traditional-medicine/wellness retrieval benchmark (50 questions with gold document IDs; Recall@5 = 0.88), production QA logs (91.1% test-retest pass over 259 cases), and a 71-question frontier no-retrieval probe showing what each grounding pillar contributes: without the safety prompt the backend model family produced a full drug-dosing schedule and complied with out-of-scope requests, and without the knowledge base it produced zero verifiable provider recommendations. We further report two transferable deployment findings: English-calibrated 4-bit AWQ quantization corrupts Thai tone marks, and forced-retrieval routing is necessary for reliable grounding.

## Metadata
- **Published**: 2026-08-24T07:54:07Z
- **Authors**: Pornthep Ukosaramig, Kobkrit Viriyayudhakorn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22917v1)