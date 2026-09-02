---
title: Bridging Lexical Divergence: LLM-Assisted, Cost-Efficient, Zero-shot Scientific Entity Linking
published: 2026-08-31T18:37:27Z
authors: Md Rasel Khondokar, Qiao Qiao, Farjana Sultana Samia, Nhat Le, Yuepei Li, Qi Li
url: http://arxiv.org/abs/2609.00228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bridging Lexical Divergence: LLM-Assisted, Cost-Efficient, Zero-shot Scientific Entity Linking

## Abstract
Scientific domain entity linking (EL) differs from general domain EL because mentions and entity names often lack lexical overlap. Another challenge is that specialized terminology is used in the scientific domain, which is rarely encountered in models pretrained on general domains. Therefore, models trained on general domains transfer poorly to scientific domains. To address this, in-domain fine-tuning is the natural remedy. However, many scientific domains lack expert-annotated data, motivating the need for a zero-human-annotation approach. Existing zero-shot methods heavily rely on LLMs to generate aliases across entire mention corpora, which incurs substantial computational cost, and those methods provide no mechanism to filter out noise from LLMs. To address these challenges, we propose Sci-ZSEL, a framework that selectively generates entity aliases with an LLM to control computational cost, and applies an ontology-aware filter to remove aliases that semantically drift toward ontology neighbors. Then, filtered aliases are used to construct pseudo-labeled mention-entity pairs for fine-tuning. To enable evaluation of EL under low lexical overlap, we also release a new animal science EL benchmark linked to three livestock trait ontologies, where mentions and entities exhibit substantially lower lexical overlap than in existing benchmarks. Across five benchmarks, Sci-ZSEL outperforms the non-fine-tuned baseline, is most useful on nonoverlapping mentions, and combining it with curated synonyms gives the best performance in most settings.

## Metadata
- **Published**: 2026-08-31T18:37:27Z
- **Authors**: Md Rasel Khondokar, Qiao Qiao, Farjana Sultana Samia, Nhat Le, Yuepei Li, Qi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00228v1)