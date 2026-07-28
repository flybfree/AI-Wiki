---
title: When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles
published: 2026-07-25T21:58:17Z
authors: Tobias Bersia, Tatiana Gaintseva
url: http://arxiv.org/abs/2607.23379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles

## Abstract
Activation Oracles (AOs) are language models trained to answer natural-language questions about another model's internal activations. They offer a flexible interface for reading hidden information from model states, especially when relevant information is internally represented but absent or incomplete in visible behavior. However, AOs are themselves learned systems: their answers are shaped by training data, objectives, and learned reporting behavior, rather than being neutral readouts of represented information. We study this in a controlled Taboo Word Guessing setting, where subject models are fine-tuned to internally use a hidden concept while avoiding direct disclosure. Contrary to the expectation that an AO trained on such a subject becomes a specialist reader, we find that fine-tuned AOs can become concept-specific anti-readers: they selectively fail to recover the concept persistently present during their own training. This failure is not simply explained by absence of the concept from the subject or oracle representations: the target remains decodable inside the oracle, while LogitLens and layer-ablation analyses indicate that the failure arises in the AO readout pathway. Our results show that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising a reliability concern for learned interpretability interfaces.

## Metadata
- **Published**: 2026-07-25T21:58:17Z
- **Authors**: Tobias Bersia, Tatiana Gaintseva
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23379v1)