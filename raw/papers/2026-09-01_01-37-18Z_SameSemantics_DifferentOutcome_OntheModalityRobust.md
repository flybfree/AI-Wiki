---
title: Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict
published: 2026-09-01T01:37:18Z
authors: Jungyeon Lee, Yejin Yoon, Taeuk Kim
url: http://arxiv.org/abs/2609.00550v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict

## Abstract
Multimodal large language models (MLLMs) are increasingly provided with contextual evidence in heterogeneous forms: as a text passage, as a rendered image of the same passage, or as both together. However, it remains unclear how consistently these surface forms are processed, especially when the evidence conflicts with the model's parametric knowledge. We study modality robustness under knowledge conflict across 13 MLLMs and two datasets, and find them far from robust. (1) Contrary to common belief, models favor a context that contradicts parametric knowledge more readily in image form than in text form; (2) when a contradicting text and image are presented together, the preferred modality is essentially arbitrary, varying with input order, model, and dataset. We further demonstrate that this instability has practical consequences: it degrades performance in multimodal RAG and can be exploited by adversarial attacks. To alleviate this brittleness, we examine several simple techniques---prompting, steering, supervised fine-tuning (SFT), and direct preference optimization; the majority prove ineffective, whereas SFT achieves moderate success. We therefore call for greater awareness of this inconsistency and argue that it is fundamental, demanding attention at multiple training stages.

## Metadata
- **Published**: 2026-09-01T01:37:18Z
- **Authors**: Jungyeon Lee, Yejin Yoon, Taeuk Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00550v1)