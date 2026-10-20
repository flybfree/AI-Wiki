---
title: CoMem: Learning to Anticipate Failures from Retrieved Experience
published: 2026-10-19T04:54:46Z
authors: Yun Shen, Ming Shen, Tianjun Yao
url: http://arxiv.org/abs/2610.25790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoMem: Learning to Anticipate Failures from Retrieved Experience

## Abstract
Reflection lets LLM agents improve from their own attempts, but the memory it builds is local to a single task, so an agent reflecting on its own tends to revisit the same explanation for failure. Cross-task reflective memory addresses this in two forms: retrieved memory keeps past experience explicit and looks up related cases, which is specific but bounded by the bank, and parametric memory internalizes experience into parameters, which generalizes but is grounded in nothing beyond the task description. When both are used, existing agents combine them additively, feeding their outputs to the solver side by side, so retrieved experience never changes what the learned memory produces. We introduce CoMem (Compounding Memory), which makes retrieved experience an input to the learned memory itself, at training and at inference. The agent builds a bank of its own successful and failed reflections, learns from retrieved cases to write failure hypotheses, candidate explanations of how an attempt is likely to go wrong, and at test time reasons from newly retrieved cases to guide each attempt. Varying the retrieved cases gives the memory different perspectives, yielding reflective diversity that is not merely sampled but also grounded in retrieved experience. Across two backbones and five benchmarks in math, code, and multi-hop QA, CoMem achieves strong overall performance. Additional evaluations show that it generalizes to out-of-distribution tasks and enables smaller models to provide effective guidance to stronger solvers.

## Metadata
- **Published**: 2026-10-19T04:54:46Z
- **Authors**: Yun Shen, Ming Shen, Tianjun Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25790v1)