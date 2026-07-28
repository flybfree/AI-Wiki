---
title: Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval
published: 2026-07-27T08:46:27Z
authors: Sungguk Cha, DongWook Kim, Mintae Kim, Youngsub Han, Byoung-Ki Jeon, Sangyeob Lee
url: http://arxiv.org/abs/2607.24165v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval

## Abstract
Finding a long document relevant to a multi-part request is not the same as establishing that it contains every requested piece of evidence. We study this gap for conjunctive document retrieval, where two or three explicit conditions must be supported on different pages of one document. We use n-Clue as a controlled measurement instrument: 1{,}000 queries over 2{,}021 documents pair all-condition golds with naturally occurring documents that satisfy only a subset, and a complete-first success requires a top-10 gold to precede every released subset qrel. Across 70 configurations, condition-wise decomposition improves two dense backbones by 6.8--7.3 points and lexical--visual fusion adds 8.7, while four generic rerankers all reduce Gold-NDCG; these directions replicate on a four-source stress set. Scaling one dense family from 0.6B to 8B changes complete-first success by 0.0 points. The strongest displayed hybrid illustrates the resulting gap: it finds a gold for 81.1\% of queries but succeeds complete-first on only 35.8\%, and the gap persists across condition count, target length, candidate density, query rendering, and the four-source stress set. Finally, page-aware visual systems surface stored support for every condition on only 5.1--5.3\% of queries. These results identify condition coverage, rather than gold discovery alone, as the central bottleneck.

## Metadata
- **Published**: 2026-07-27T08:46:27Z
- **Authors**: Sungguk Cha, DongWook Kim, Mintae Kim, Youngsub Han, Byoung-Ki Jeon, Sangyeob Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24165v1)