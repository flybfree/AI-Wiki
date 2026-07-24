---
title: Disentangling Curriculum Learning in NLP: Towards a Unifying Taxonomy
published: 2026-07-21T11:18:16Z
authors: Vanessa Toborek, Florian Seiffarth, Sebastian Müller, Tamás Horváth
url: http://arxiv.org/abs/2607.18984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling Curriculum Learning in NLP: Towards a Unifying Taxonomy

## Abstract
Despite more than a decade of curriculum learning (CL) research in NLP, the field lacks a principled account of which difficulty function or scheduler to use for a given problem. To understand what has hindered progress towards this account, we propose a fine-grained taxonomy separating difficulty evaluation from training scheduling to enable systematic analysis of CL strategies. For difficulty evaluation, we distinguish attribution source and task dependence, revealing difficulty as a perspectival concept encoding different assumptions about what makes an instance hard to learn. For scheduling, we provide the first formalisation of CL schedulers in terms of expected training contribution, enabling comparison across implementations by introducing retention regimes and monotonicity properties. Applied in a dedicated analysis of CL works in NLP, our taxonomy reveals a systematic incomparability problem: prior works conflate distinct notions of difficulty and scheduling, often pursuing different objectives under the same CL label -- hindering comparison and the accumulation of a coherent evidence base. Beyond diagnosis, the taxonomy supports the design, analysis, and comparison of CL strategies, and motivates evaluation practices that disentangle the sources of observed improvement.

## Metadata
- **Published**: 2026-07-21T11:18:16Z
- **Authors**: Vanessa Toborek, Florian Seiffarth, Sebastian Müller, Tamás Horváth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18984v1)