---
title: Understanding the Impact of Linguistic Realization Choices on LLM Stance with Causal Tracing
published: 2026-07-22T13:19:58Z
authors: Langchen Huang, Sebastian Padó, Franziska Weeber
url: http://arxiv.org/abs/2607.20115v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding the Impact of Linguistic Realization Choices on LLM Stance with Causal Tracing

## Abstract
Large language models (LLMs) are known to be sensitive to prompt and input formulations. However, existing studies have focused on lexical realization and largely ignored constructional choice. This paper studies whether linguistic construction can systematically shift LLM decisions and where these shifts can be causally localized inside the model. We use political stance judgment as a meaning-sensitive case study and extend an English political statements dataset, resulting in six controlled linguistic rewrite types that preserve or invert the meaning of a statement. Experiments on four open-weight models show that stance instability affect both meaning-preserving and meaning-inversing rewrites. Because output shifts reveal that rewrites affect stance, but not where in the model, we apply activation patching, where activations from the original statement are substituted into the forward pass for the rewritten statement and measure which components recover the original stance distribution. The results show that mid-to-late decoder layers, especially block outputs at the final prompt position, provide the strongest restoration signal.

## Metadata
- **Published**: 2026-07-22T13:19:58Z
- **Authors**: Langchen Huang, Sebastian Padó, Franziska Weeber
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20115v1)