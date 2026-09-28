---
title: In-Context Binding Capacity in Language Models
published: 2026-09-24T23:41:03Z
authors: Manas Venkata Sai Ravulapalli, Samrath Singh Chadha
url: http://arxiv.org/abs/2609.30634v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Context Binding Capacity in Language Models

## Abstract
How many assignments can a language model recall before it loses track of which value belongs to which entity? We measure this limit using continuous recall curves for 12 models at or below 3B parameters and a threshold sweep over 30 open models up to 12B. On the continuous curves, the load at which recall falls halfway to chance follows $K_{50}=cN^α$, with $α=0.820$ and $R^2=0.73$. The broader sweep shows an eightfold range associated with pretraining recipe, although the continuous curves show no detectable recipe effect after controlling for scale, with few modern models in the fit. We derive why interference can lower measured capacity by reducing single-binding recall even when the load-dependent recall profile is unchanged. Direct task training also exceeds the extrapolated zero-shot law, but different measurement criteria prevent interpreting that comparison as a capacity gain. Its formation times follow a power-law form in two independent codebases, conditional on runs that succeed. Together, these results characterize capacity at the model's query interface. Bounds on joint recall and a decomposition of policy errors connect this measurement to working memory and instruction following, without treating recall as a measure of alignment. The controlled task also provides a baseline for testing whether binding limits constrain world-state tracking; the present experiments do not measure state updates or downstream transfer.

## Metadata
- **Published**: 2026-09-24T23:41:03Z
- **Authors**: Manas Venkata Sai Ravulapalli, Samrath Singh Chadha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30634v1)