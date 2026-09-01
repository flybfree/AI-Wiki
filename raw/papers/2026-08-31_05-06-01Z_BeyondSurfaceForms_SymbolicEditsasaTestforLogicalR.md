---
title: Beyond Surface Forms: Symbolic Edits as a Test for Logical Reasoning with LLMs
published: 2026-08-31T05:06:01Z
authors: Ramya Keerthy Thatikonda, Wray Buntine, Ehsan Shareghi
url: http://arxiv.org/abs/2608.30256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Surface Forms: Symbolic Edits as a Test for Logical Reasoning with LLMs

## Abstract
Logical reasoning with large language models (LLMs) is a critical capability, as it reflects a system's ability to correctly deduce hypotheses from a given context using faithful deductive processes. However, LLM reasoning has often been shown to be sensitive to small surface-level variations in problem formulation, raising questions about whether models truly follow the underlying logical structure. Studying this behavior is challenging because the symbolic components of logical problems, such as operators and predicates, are difficult to systematically manipulate in natural language. We introduce a tool-driven framework for generating controlled, label-preserving edits to logical reasoning problems. Our method operates on symbolic representations of first-order logic and constraint satisfaction problem tasks, enabling targeted modifications to logical operators and other structural components before translating them back into natural language. Using this framework, we evaluate various LLMs under cumulative and individual operator edits and analyze their behavior in response to these changes. Our quantitative and qualitative analyses show that LLM reasoning behavior under controlled operator edits is inconsistent, regardless of model size or family: models sometimes adapt correctly to structural changes but often fail to track their logical consequences. The results from this automated stress test enable an evaluation of language models across different dimensions and help measure the reliability of their reasoning.

## Metadata
- **Published**: 2026-08-31T05:06:01Z
- **Authors**: Ramya Keerthy Thatikonda, Wray Buntine, Ehsan Shareghi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30256v1)