---
title: Reglos: A Self-Evolving Personal Memory Agent with Recursive Self-Improvement
published: 2026-11-04T06:56:04Z
authors: Sen Yang, Jiaduo Lin, Zehong Huang, Wen Liu
url: http://arxiv.org/abs/2611.06049v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reglos: A Self-Evolving Personal Memory Agent with Recursive Self-Improvement

## Abstract
Personal agents draw on past conversations to tailor their responses to each user. Their memory systems store and update what each user says, and coding agents now also rewrite the harness that turns this memory into the model's context. Such patches risk overfitting, because one tested only on the failures it targets can fix those cases and help nowhere else. We present Reglos, a training-free personal memory agent that tests whether harness changes help beyond the failures they were written to fix. Its self-evolving memory adds to each user's append-only record with every conversation, as new preferences supersede old ones and facts can be forgotten. Its harness improves through recursive self-improvement, in which a coding agent proposes patches from failure traces and a critic from a second model family screens each one for benchmark gaming. After the harness is frozen, a fixed evaluator decides which further patches to accept. With the same backbone behind every system, Reglos outperforms state-of-the-art memory systems such as Mem0, MemOS and EverOS, reaching 61.3% and 84.0% on PersonaMem-v2 and LongMemEval-S with Qwen3.8-27B, and 57.5% and 87.2% with GPT-5.6 Luna.

## Metadata
- **Published**: 2026-11-04T06:56:04Z
- **Authors**: Sen Yang, Jiaduo Lin, Zehong Huang, Wen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.06049v1)