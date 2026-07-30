---
title: Sky sphere representation in language models
published: 2026-07-29T16:19:43Z
authors: Aleksandr Berdnikov, Yevgeny Liokumovich
url: http://arxiv.org/abs/2607.27092v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sky sphere representation in language models

## Abstract
We analyze whether language models of size ~100B have a representation of the night sky map that is decodable from their residual stream. We find that most of the considered open-source models do have such a representation, and it often even surfaces to the top principal components on prompts that ask questions like ``what is close to this object in the night sky''. In all but one model this representation showed significant scores in LOO testing, containing up to 65-85% of variance ($R^2$-score) and having median angular error down to $12^\circ-21^\circ$. We verify that our representation is not a simple leak from a correlated flat representation. To our knowledge, this representation is the first example of a curved high-dimensional irreducible feature manifold.   Codes used in the paper are published at https://github.com/l3erdnik/Decodable-sky

## Metadata
- **Published**: 2026-07-29T16:19:43Z
- **Authors**: Aleksandr Berdnikov, Yevgeny Liokumovich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27092v1)