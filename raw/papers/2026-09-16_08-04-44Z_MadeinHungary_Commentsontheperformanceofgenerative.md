---
title: Made in Hungary: Comments on the performance of generative language models
published: 2026-09-16T08:04:44Z
authors: Mátyás Osváth, Enikő Héja, Noémi Ligeti-Nagy
url: http://arxiv.org/abs/2609.18284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Made in Hungary: Comments on the performance of generative language models

## Abstract
In recent years, three initiatives have emerged to develop generative language models in Hungary. The motivation behind them is the same. For Hungarian, no model with the given capability existed, or existing English-centric models offered limited proficiency. A detailed examination of the corresponding studies, however, reveals several methodological limitations. First, the reliability of the evaluation protocols is questionable. Contrary to the findings of Csibi et al. [2026], evaluation under the recommended inference settings shows that Qwen3-4B achieves higher scores than Racka-4B, its Hungarian-adapted version. Data contamination is evident in the work of Yang et al. [2025d] and Szentmihályi et al. [2025], potentially biasing the reported results. Second, the training pipelines fall short of current best practices in corpus curation and data mixture, which risks wasting substantial compute on low-quality data. The lack of controlled ablations prevents reliable assessment of these choices. Third, none of the three papers assessed forgetting or capability loss. Testing the adapted models on a subset of the original benchmarks indicates performance decline in all three cases, especially Racka-4B. These observations emphasize the importance of rigorous experimental design in language model development, given the significant computational and financial costs involved.

## Metadata
- **Published**: 2026-09-16T08:04:44Z
- **Authors**: Mátyás Osváth, Enikő Héja, Noémi Ligeti-Nagy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18284v1)