---
title: Two Regimes of Chain-of-Thought Unfaithfulness: Behavioral Detection Fails Where Models Are Wrong
published: 2026-07-26T04:43:53Z
authors: Suramya R. Angdembay, Dikshant Aryal, Nick Rahimi
url: http://arxiv.org/abs/2607.23458v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Two Regimes of Chain-of-Thought Unfaithfulness: Behavioral Detection Fails Where Models Are Wrong

## Abstract
Chain-of-thought (CoT) explanations support oversight only if they are faithful: the stated reasoning must actually produce the answer. Auditing black-box (behavioral) detection of unfaithful CoT against FaithCoT-Bench's human annotations, we find answer correctness structures the problem at every level. Answer incorrectness alone (an oracle diagnostic, not a deployable detector) outperforms every purpose-built signal (AUROC 0.696), because 69% of annotated unfaithfulness occurs on incorrect answers. Stratifying by correctness splits detection into two regimes: on correct answers, behavioral signals moderately separate faithful from post-hoc reasoning (0.63-0.67); on incorrect answers, where most unfaithfulness lives, no tested signal is detectably above chance (replicated on all four models for benchmark-wide signals). The standard step-removal metric anti-correlates with human labels; this inversion reproduces on the benchmark's released scores and on hint-dependent counterfactually labeled traces. Linear probes decode the behaviorally blind regime in Llama-3.1-8B and the correct-answer regime in Qwen-2.5-7B, with no shared, positively aligned direction detected across regimes; instructed answer-first traces (7 models) transfer to neither annotated regime, while hint-induced unverbalized answer flips do, in model- and source-dependent settings. We also independently verify and resolve a documentation-data mismatch in the benchmark's label semantics.

## Metadata
- **Published**: 2026-07-26T04:43:53Z
- **Authors**: Suramya R. Angdembay, Dikshant Aryal, Nick Rahimi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23458v1)