---
title: Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models
published: 2026-07-29T22:41:25Z
authors: Shreyas Subramanian, Mecit Gungor, Vikram Elango
url: http://arxiv.org/abs/2607.27506v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models

## Abstract
Language and embedding models used in RAG systems are conventionally assumed to require large-scale pretraining and explicit grounding supervision. We present B1ade, an efficient RAG architecture comprising two purpose-built components: a compact embedding model and a purpose-built SLM. B1ade-embed, a 335M parameter retrieval model constructed via parameter-free fusion of five pretrained encoders achieves top MTEB scores among sub-500M models with zero additional training, and B1ade-1B, an SLM trained on low-cost GPUs using Group Relative Policy Optimization (GRPO) on 723M tokens (2.2M examples) of curated context-question pairs with rewards that optimize only answer similarity. Our central finding is emergent attribution: despite receiving no explicit supervision for source citation, B1ade-1B cites retrieved passages in 42.4% of responses, exceeding the attribution rate of its training distribution by 5.5 percentage points. This demonstrates that grounding behavior can emerge as an accuracy-maximizing strategy under RL training, without explicit reward engineering. On standard QA benchmarks, B1ade-1B achieves 81.82% on PopQA, 65.8% on PubMedQA, and 51.09% on FEVER. In end-to-end RAG evaluation, B1ade-1B achieves an average score of 0.654 across correctness, completeness, coherence, and faithfulness, a 10.8% improvement over the SFT, while closing the gap with models 1.5x its size. These results show that strategic model composition and reward design suffice for resource-efficient RAG, without large-scale pretraining.

## Metadata
- **Published**: 2026-07-29T22:41:25Z
- **Authors**: Shreyas Subramanian, Mecit Gungor, Vikram Elango
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27506v1)