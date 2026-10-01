---
title: ContextAdapt: Evaluating Contextual Adaptation and Value Alignment in LLMs
published: 2026-09-29T11:52:52Z
authors: Olivia Macmillan-Scott, Mirco Musolesi
url: http://arxiv.org/abs/2609.38260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ContextAdapt: Evaluating Contextual Adaptation and Value Alignment in LLMs

## Abstract
Values such as honesty, autonomy, and confidentiality are often regarded as general principles underpinning AI alignment. However, what it means to act in accordance with these values can depend on the context in which a decision is made. In this paper, we ask whether large language models (LLMs) appropriately adapt the application of a value across professional settings, while remaining consistent when contextual changes do not alter the relevant professional norm. To study this, we introduce ContextAdapt, an evaluation framework covering honesty, autonomy, and confidentiality across medicine, law, finance, and national security. Drawing on primary-source professional and regulatory documents, we construct a value x domain framework and use this to develop scenarios testing both default professional rules and recognised exceptions. We evaluate 12 LLMs on both the actions they recommend and the justifications they provide. In our main experiment, models achieve 95.6% mean appropriateness, although the use of the correct domain-specific justification varies substantially across models, from 25.6% to 76.9%. In a separate factorial experiment, explicitly naming the professional domain and changing the role of the model have limited effect on behaviour. Varying stakes, however, reveals severe but localised failures: in some cases, models alter their responses even though the underlying professional obligation remains unchanged. In particular, perceived severity appears to act as a cue for disclosure across both honesty and confidentiality scenarios. These results show that evaluating value alignment requires us to consider not only whether models follow abstract principles, but whether they apply them appropriately across different contexts.

## Metadata
- **Published**: 2026-09-29T11:52:52Z
- **Authors**: Olivia Macmillan-Scott, Mirco Musolesi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38260v1)