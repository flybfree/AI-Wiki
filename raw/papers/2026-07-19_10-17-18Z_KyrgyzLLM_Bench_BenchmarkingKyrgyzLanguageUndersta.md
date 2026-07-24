---
title: KyrgyzLLM-Bench: Benchmarking Kyrgyz Language Understanding
published: 2026-07-19T10:17:18Z
authors: Timur Turatali, Aida Turdubaeva, Rustem Izmailov, Anton M. Alekseev, Sergey I. Nikolenko
url: http://arxiv.org/abs/2607.17173v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KyrgyzLLM-Bench: Benchmarking Kyrgyz Language Understanding

## Abstract
Evaluating large language models (LLMs) across languages remains challenging, as most multilingual benchmarks rely on translated English datasets, often obscuring linguistic and cultural specificity in the target language. This issue is particularly pronounced for less-resourced languages such as Kyrgyz, where reliable natively authored evaluation data are scarce. Building on previously introduced Kyrgyz-language evaluation datasets, this work reports the first systematic and large-scale evaluation of LLMs in Kyrgyz using the KyrgyzLLM-Bench benchmark suite. KyrgyzLLM-Bench comprises two natively authored datasets$-$KyrgyzMMLU and KyrgyzRC$-$together with carefully translated and manually post-edited versions of WinoGrande, HellaSwag, BoolQ, and TruthfulQA. We evaluate 26 open- and closed-source LLMs under zero-shot and few-shot settings, analyzing model performance, cross-lingual transfer, and the impact of translation artifacts on evaluation reliability. Across families and tasks, model rankings transfer broadly from English to Kyrgyz on WinoGrande and BoolQ, and to a lesser extent on MMLU, while HellaSwag exhibits a substantial English-Kyrgyz performance gap consistent with translation-induced plausibility shifts. Few-shot prompting improves several open-source models on reading comprehension but behaves inconsistently for proprietary models on translated tasks. We publicly release all datasets, evaluation code, and per-model results, and integrate the Kyrgyz tasks into a widely used multilingual evaluation framework to support future research on Kyrgyz NLP.

## Metadata
- **Published**: 2026-07-19T10:17:18Z
- **Authors**: Timur Turatali, Aida Turdubaeva, Rustem Izmailov, Anton M. Alekseev, Sergey I. Nikolenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17173v1)