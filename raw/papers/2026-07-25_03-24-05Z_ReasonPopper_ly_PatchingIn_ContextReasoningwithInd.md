---
title: Reason Popper-ly: Patching In-Context Reasoning with Inductive Logic Programming
published: 2026-07-25T03:24:05Z
authors: Zirong Chen, Meiyi Ma
url: http://arxiv.org/abs/2607.23019v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reason Popper-ly: Patching In-Context Reasoning with Inductive Logic Programming

## Abstract
Chain-of-thought (CoT) prompting enables large language models (LLMs) to tackle multi-step reasoning tasks, yet the generated intermediate steps are not guaranteed to be logically sound. We present Reason Popper-ly, a neurosymbolic framework that uses inductive logic programming (ILP) to learn relation composition rules from reasoning traces and deploys them as an online verifier for step-level correction. Given an LLM-generated trace, the method checks each inferred step against the learned rule table, diagnoses the violation type, rewrites incorrect steps with symbolically derived repairs, and regenerates the remaining suffix so that the model can produce its final answer conditioned on a verified trace. We evaluate on CLUTRR, a multi-hop kinship reasoning benchmark, using five language models over reasoning chains of 2 to 10 hops. Across all models, Reason Popper-ly consistently improves terminal accuracy over standard CoT, with gains of up to 48 percentage points for small models and 15 points for frontier models on the longest chains. Compared with a fully exogenous symbolic pipeline, our method performs better on harder instances by preserving the model's successful grounding while correcting only verifiable reasoning failures. In addition, step-level ILP verification yields a fine-grained error taxonomy that provides diagnostic insight beyond final-answer accuracy.

## Metadata
- **Published**: 2026-07-25T03:24:05Z
- **Authors**: Zirong Chen, Meiyi Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23019v1)