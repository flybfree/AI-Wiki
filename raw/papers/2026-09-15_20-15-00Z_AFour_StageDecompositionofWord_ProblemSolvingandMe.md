---
title: A Four-Stage Decomposition of Word-Problem Solving and Mechanistic Fragility in LLM Math Reasoning
published: 2026-09-15T20:15:00Z
authors: Zhongdi Qu, Carla P. Gomes
url: http://arxiv.org/abs/2609.17804v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Four-Stage Decomposition of Word-Problem Solving and Mechanistic Fragility in LLM Math Reasoning

## Abstract
Large language models solve grade-school math word problems with high accuracy, yet a single irrelevant clause inserted into the problem can collapse it. We reconcile these observations with a mechanistic account. We show that the model's internal computation decomposes into a four-stage sequential pipeline, Schema Abstraction, Operation Planning, Operand Binding, and Computation, each stage producing a distinct intermediate representation in an identifiable band of layers. Using the same scaffold to diagnose distractor-induced failure, we localize the corruption to a single stage, Operation Planning, implemented by a set of attention heads whose causal role we validate bidirectionally. In short, we provide a mechanistic interpretation of math word problem reasoning in LLMs, and their failure when distracted.

## Metadata
- **Published**: 2026-09-15T20:15:00Z
- **Authors**: Zhongdi Qu, Carla P. Gomes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17804v1)