---
title: Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching
published: 2026-08-23T10:05:16Z
authors: Murat Dura, Serkan Öztürk, Selma Tekir
url: http://arxiv.org/abs/2608.22332v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching

## Abstract
Large Language Models (LLMs) demonstrate remarkable problem-solving capabilities when guided by Chain-of-Thought (CoT) prompting, yet the internal mechanisms underlying these improvements remain poorly understood. In this work, we investigate where CoT-related causal effects emerge across the generated reasoning trajectory and which attention heads carry signals that contribute to final-answer computation. Because CoT reasoning unfolds over multiple generated tokens, standard activation patching at a single static token position is insufficient to characterize these temporally distributed effects. To address this limitation, we introduce a sequential activation patching framework that traces CoT-conditioned attention-head activations across token positions and aggregates their effects using Part-of-Speech-guided analysis. We further introduce Sequential Multi-Head Patching to evaluate the joint contribution of distributed head sets, together with cross-question and random activation controls. Targeted zero-ablation experiments show that the identified heads are functionally important for successful answer generation and affect several overlapping mechanisms, including reasoning-trajectory maintenance, answer anchoring, exemplar-target separation, and numerical generation. Overall, our results provide evidence for distributed reasoning-support sub-circuits associated with CoT-conditioned computation.

## Metadata
- **Published**: 2026-08-23T10:05:16Z
- **Authors**: Murat Dura, Serkan Öztürk, Selma Tekir
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22332v1)