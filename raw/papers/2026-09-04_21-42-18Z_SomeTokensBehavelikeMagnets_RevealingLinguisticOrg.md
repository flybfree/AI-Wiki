---
title: Some Tokens Behave like Magnets: Revealing Linguistic Organization in the Layers of Language Models
published: 2026-09-04T21:42:18Z
authors: Andrew Liu, Devan Srinivasan, Gerald Penn
url: http://arxiv.org/abs/2609.05743v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Some Tokens Behave like Magnets: Revealing Linguistic Organization in the Layers of Language Models

## Abstract
We identify a special group of token vectors inside large language models (LLMs), which we term magnetic vectors, that organize the surrounding tokens by either attracting or repelling them. Particularly, tokens pointing the same way as an attracting magnet are elongated; tokens pointing the same way as a repelling magnet are compressed. Just as physical magnets pull or push away the iron filings around them, these vectors organize their surroundings through two opposing polarities. Moreover, we identify a statistically significant pattern in linguistic category where function words consistently act as repelling magnets in early layers, and we also find magnets consistently reorganize their polarities in unique ways deeper in the model. In a further case study we find this observation may unveil a deliberate, layer-wise organization in how LLMs process language.   This pattern is consistent across different LLM architectures, sizes, and layer configurations. It is also causally relevant. When the LLM is fine-tuned for a downstream task, the task-functional tokens emerge as magnets. E.g., in question answering, the answer-span tokens become uniquely repelling magnets in the final layer, geometrically carving the answer out of the surrounding context. Furthermore, removing early-layer repelling magnets devastates syntactic tasks (POS tagging accuracy drops from 91% to below 10%) while sparing semantic ones, and removing late-layer attracting magnets does the reverse. We believe this phenomenon warrants further investigation, as it opens the first probe-free path to understanding how language models geometrically organize linguistic computation across their layers.

## Metadata
- **Published**: 2026-09-04T21:42:18Z
- **Authors**: Andrew Liu, Devan Srinivasan, Gerald Penn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05743v1)