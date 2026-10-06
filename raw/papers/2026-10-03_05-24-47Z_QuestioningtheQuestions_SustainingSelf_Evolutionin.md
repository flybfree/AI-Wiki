---
title: Questioning the Questions: Sustaining Self-Evolution in Reasoning Models
published: 2026-10-03T05:24:47Z
authors: Jinyuan Li, Chengsong Huang, Langlin Huang, Donghong Cai, Shiping Gao, Yuyi Yang, Jiaxin Huang
url: http://arxiv.org/abs/2610.04299v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Questioning the Questions: Sustaining Self-Evolution in Reasoning Models

## Abstract
Self-evolving reasoning models learn from their own generated questions, yet repeated self-training can lead to performance collapse. In this paper, we investigate why performance deteriorates over successive rounds and how to sustain self-evolution. Our analysis identifies two recurring quality problems in self-generated questions: invalid questions and repeated variants of the same mathematical questions. First, invalid questions become more prevalent across rounds, and answer-consistency filtering further increases their proportion in training data. Second, existing question diversity controls based on lexical similarity can miss mathematically equivalent questions expressed in different ways, which leads to question diversity collapse in later training rounds. Building on these findings, we introduce R-Quest, which uses question validity and novelty feedback to guide self-evolution. We first train the solver to recognize and reject invalid questions, then use its judgments to guide questioner rewards and filter solver training data. To avoid question repetition, we use a frozen base model to compare sampled question pairs and provide novelty feedback. Empirically, our method consistently achieves the highest average performance on 12 benchmarks in mathematical reasoning, general-domain reasoning, and code generation across two model families. Additionally, R-Quest maintains stable performance gains over ten rounds of self-evolution, peaking in the final round and outperforming R-Zero by 17.32 points.

## Metadata
- **Published**: 2026-10-03T05:24:47Z
- **Authors**: Jinyuan Li, Chengsong Huang, Langlin Huang, Donghong Cai, Shiping Gao, Yuyi Yang, Jiaxin Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04299v1)