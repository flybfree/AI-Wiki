---
title: When to Review: Spaced Repetition for Continual Pre-Training of Language Models
published: 2026-08-18T08:51:47Z
authors: Alankar Atreya, Devesh Batra, Yoages Kumar Mantri, Geremy Bantug, Greig A Cowan, Raad Khraishi
url: http://arxiv.org/abs/2608.17530v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When to Review: Spaced Repetition for Continual Pre-Training of Language Models

## Abstract
Continual pre-training of large language models must acquire new information without erasing old knowledge. Existing replay methods often choose a global old/new mixture and sample uniformly, ignoring that examples differ in how quickly they are forgotten. We formulate continual pre-training as adaptive review scheduling: the training loop should decide not only how much history to replay, but which examples should return at each step. We introduce Spaced Repetition Training (SRT), a continual learning framework inspired by cognitive science, which schedules sample-rehearsal using the SuperMemo-2 (SM-2) algorithm. SRT maintains per-example review state, maps per-example perplexity to a recall-quality signal, and schedules historical examples for retention and new examples for consolidation while leaving the model, objective, and optimizer unchanged. On temporally separated Wikipedia and code corpora, SRT improves the stability-plasticity trade-off, recovering 5 to 37 percentage points of old-knowledge accuracy lost by naive continual pre-training across model scales while preserving or improving new-knowledge acquisition. At larger scale, SRT preserves broad benchmark performance that naive continual pre-training and uniform replay substantially degrade. Experiments with vision and tabular data further suggest that the scheduling principle extends beyond language when paired with an appropriate recall signal.

## Metadata
- **Published**: 2026-08-18T08:51:47Z
- **Authors**: Alankar Atreya, Devesh Batra, Yoages Kumar Mantri, Geremy Bantug, Greig A Cowan, Raad Khraishi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17530v1)