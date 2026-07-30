---
title: The Art of Not Forgetting A Local Learning Architecture for Continual Learning
published: 2026-07-29T06:42:23Z
authors: Ashmith Atmuri, Yashaswini Rao Bhogarajula
url: http://arxiv.org/abs/2607.26523v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Art of Not Forgetting A Local Learning Architecture for Continual Learning

## Abstract
We introduce CMP (Cognitive Memory Primitive), a continual-learning architecture that repre?sents inputs as sparse relational codes, stores them in a two-tier competitive memory, and learns through local updates without end-to-end backpropagation through its feature-generating system. We investigate whether combining sparse representations, local learning, and persistent memory can reduce catastrophic forgetting relative to conventional backpropagation-based continual?learning approaches. On a controlled domain-incremental byte-level language modeling protocol, CMP demonstrates substantially lower backward transfer than a parameter-matched Trans?former trained with online Elastic Weight Consolidation (EWC). Across a three-seed replicated 15-domain experiment, CMP exhibits stable forgetting behavior, while separate head-to-head comparisons and domain-order analyses show consistently lower forgetting than the evaluated Transformer baseline under the reported experimental settings. We report these findings alongside a substantial single-domain accuracy gap relative to the Transformer, a null result on a vision benchmark, and a documented failure to combine CMP with an independent accuracy-improving mechanism, reflecting our commitment to reporting both positive and negative outcomes. These results suggest that the combination of sparse representations, local learning, and persistent memory is a promising direction for continual learning, while motivating further investigation into the respective roles of learning rules, representations, and architectural design in mitigating catastrophic forgetting.

## Metadata
- **Published**: 2026-07-29T06:42:23Z
- **Authors**: Ashmith Atmuri, Yashaswini Rao Bhogarajula
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26523v1)