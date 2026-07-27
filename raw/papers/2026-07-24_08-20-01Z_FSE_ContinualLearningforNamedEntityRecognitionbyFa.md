---
title: FSE: Continual Learning for Named Entity Recognition by Fast-Slow Experts
published: 2026-07-24T08:20:01Z
authors: Yunan Zhang, Yang Fan, Heng Li, Xiangping Wu, Qingcai Chen
url: http://arxiv.org/abs/2607.22075v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FSE: Continual Learning for Named Entity Recognition by Fast-Slow Experts

## Abstract
Continual Learning for Named Entity Recognition (CLNER) enable models to incrementally learn new entity types without forgetting previously acquired ones. However, existing methods suffer from catastrophic forgetting and insufficient exploitation of shared information across tasks. This paper proposes FSE, a Fast-Slow Experts enhanced span-based NER model for CLNER. The shared fast expert learns token-level links to efficiently filter out unlikely spans, while the task-specific slow expert performs span classification only on the remaining candidates. It stabilizes learning by promoting knowledge sharing across tasks and maintains plasticity by reducing learning burden at each task. A length-decay negative sampling strategy to mitigate span imbalance is also introduced. Extensive experiments on OntoNotes and FewNERD synthestic datasets demonstrate that FSE achieves state-of-the-art performance in CLNER scenarios, with effectiveness of each component, empirical evidence of faster convergence and expected functionality of both experts.

## Metadata
- **Published**: 2026-07-24T08:20:01Z
- **Authors**: Yunan Zhang, Yang Fan, Heng Li, Xiangping Wu, Qingcai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22075v1)