---
title: LLMs Learn Better In-Context from Rules than from Examples
published: 2026-09-02T23:02:38Z
authors: Xiang Fu, Seungmin Cho, Yukyung Lee, Najoung Kim
url: http://arxiv.org/abs/2609.03213v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs Learn Better In-Context from Rules than from Examples

## Abstract
Large language models (LLMs) exhibit in-context learning capabilities, where they can learn new tasks from prompt contexts without weight updates. We compare the learning efficacies of two prominent modes of in-context learning: (1) learning from descriptions of rules (instruction following); and (2) learning from examples of input-output demonstrations (few-shot prompting). Through five learning tasks that cover diverse domains (games, arithmetic, linguistic inferences), we compare two modes of learning (rules vs. examples) specifying the same underlying task. We furthermore explore model and task properties that modulate the learning efficacies. We find that models generally learn more reliably from rules than from examples alone, and additional examples on top of rules or simply scaling up the number of examples do not lead to consistent and significant gains. Instruction tuning amplifies the benefit of rule-based learning while keeping example-based learning capacities intact. Surprisingly, we find no privileged effect of example-based learning in base models, and rules still lead to gains in algebraic task domains. Overall, the comparative efficacy of rules over examples is larger when the task recruits algebraic abstractions and computations, and smaller when the task requires distributional sensitivity and/or recruits parametric knowledge.

## Metadata
- **Published**: 2026-09-02T23:02:38Z
- **Authors**: Xiang Fu, Seungmin Cho, Yukyung Lee, Najoung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03213v1)