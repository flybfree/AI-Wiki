---
title: For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances
published: 2026-09-16T23:41:25Z
authors: Alexander Shirnin, Aleksey Kudelya
url: http://arxiv.org/abs/2609.19504v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances

## Abstract
As model-generated content is increasingly consumed by other model instances in automated workflows, a practically important question arises: can a model embed a signal in natural language that an independent instance of the same model can detect, relying only on shared pre-training and task instructions, without any shared memory or coordination-specific training? We introduce For Your Eyes Only, a cooperative signalling game designed to evaluate this directly. A Sender produces free-form descriptions for two words, one of which is a hidden target; an isolated Receiver must identify it. We evaluate seven contemporary models from four architectural families on 300 word pairs from established psycholinguistic corpora, using the Double-Pass Success Rate to control for output biases. We find that most models struggle to maintain coordination once they are required to avoid detectable signals, while one frontier model retains near-perfect performance even after such filtering. We further show that models can direct this capability toward deliberate misdirection, and that coordination is consistently weaker across architectures than within them.

## Metadata
- **Published**: 2026-09-16T23:41:25Z
- **Authors**: Alexander Shirnin, Aleksey Kudelya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19504v1)