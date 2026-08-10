---
title: Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models
published: 2026-08-07T14:17:34Z
authors: Zili Zhang, Yilin Wang, Heng Wang, Herun Wan, Minnan Luo
url: http://arxiv.org/abs/2608.07261v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models

## Abstract
Large language models (LLMs) can solve complex multi-hop problems yet exhibit puzzling failures on simple two-hop queries: although a model may correctly store each individual hop, it often fails to combine them. To understand the internal mechanisms of this phenomenon, we train transformers from scratch in a controlled symbolic environment. Our experiments reveal a pattern in two-hop generalization: models generalize reliably when the second hop follows the training distribution, but always fail when it deviates.   Through mechanistic analysis, we provide a complete explanation for these distinct generalization behaviors: in settings where models generalize successfully, performance is driven by the emergence of consistent intermediate representations for the same entities across contexts, whereas failures on settings where the second hop is out-of-distribution arise from a mismatch across layers: lower layers correctly construct these intermediate representations, but upper layers, while trained on corresponding atomic facts, primarily learn to map them to outputs rather than to reason over them.   Driven by this insight, we propose a recurrent-style training strategy, which enables transformers to reuse their reasoning circuitry across input forms and substantially improves generalization on out-of-distribution two-hop queries.

## Metadata
- **Published**: 2026-08-07T14:17:34Z
- **Authors**: Zili Zhang, Yilin Wang, Heng Wang, Herun Wan, Minnan Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07261v1)