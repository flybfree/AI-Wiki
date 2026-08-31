---
title: CNeo-Bench: Diagnosing Large Language Models on Chinese Neologisms
published: 2026-08-28T08:17:30Z
authors: Kaiyan Zhao, Zhongtao Miao, Zheyong Xie, Shaosheng Cao, Yoshimasa Tsuruoka
url: http://arxiv.org/abs/2608.28053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CNeo-Bench: Diagnosing Large Language Models on Chinese Neologisms

## Abstract
Chinese neologisms exploit diverse and unique linguistic mechanisms, such as phonetic substitution (e.g., 886 for ``bye-bye'') and visual character decomposition that are rare in other languages. We introduce CNeo-Bench, a benchmark of 4,759 such neologisms with reference definitions, organized into five top-level categories and nine subcategories by the linguistic mechanism behind each expression. CNeo-Bench is paired with a two-tier evaluation framework that separates whether a model can describe a neologism from whether it can operate on its underlying mechanism. Evaluating 18 LLMs, we find that Chinese neologisms remain an open challenge; most models fall below 40\% on definition generation, and on several subcategories a systematic recognition-manipulation gap emerges: models describe neologisms correctly but, in source-form restoration tasks, substitute a semantic equivalent (paraphrase) for the source form rather than producing the source form itself. A few-shot analysis on 1,058 hard items shows that in-context examples can solve many difficult cases, but leave a noticeable portion of errors remaining, indicating challenges beyond prompting alone can address.

## Metadata
- **Published**: 2026-08-28T08:17:30Z
- **Authors**: Kaiyan Zhao, Zhongtao Miao, Zheyong Xie, Shaosheng Cao, Yoshimasa Tsuruoka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28053v1)