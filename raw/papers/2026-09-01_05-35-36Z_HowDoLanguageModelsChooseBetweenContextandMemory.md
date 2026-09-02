---
title: How Do Language Models Choose Between Context and Memory?
published: 2026-09-01T05:35:36Z
authors: Benjamin Shih, John Winnicki, Arianna Cao
url: http://arxiv.org/abs/2609.00753v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Do Language Models Choose Between Context and Memory?

## Abstract
When contextual information conflicts with the knowledge stored in model parameters, activation directions can be used to decode and steer which source the model follows. However, steering along a direction does not establish causality: whether the unedited model would naturally use that direction or whether the direction is reusable across tasks. We test these distinctions through counterfactual experiments in unambiguous settings. First, we estimate authority directions from agreement prompts, in which the context and parametric knowledge support the same answer. We then interchange naturally occurring coordinates along these directions between matched prompts that direct the model to prioritize either the supplied context or its parametric knowledge. Across Qwen, Llama, and OLMo models, this intervention reproduces 30-68% of the authority-induced shift in source choice, whereas matched controls reproduce almost none. To test cross-task reuse, we learn authority directions on two tasks separately and see that cross-task transferability closes only 9% of the authority gap while the local direction learned on the given task closes 57%. These results distinguish authority representation, causal use, and cross-task causal reuse, and suggest that authority computations may be task-dependent, rather than reusable across tasks.

## Metadata
- **Published**: 2026-09-01T05:35:36Z
- **Authors**: Benjamin Shih, John Winnicki, Arianna Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00753v1)