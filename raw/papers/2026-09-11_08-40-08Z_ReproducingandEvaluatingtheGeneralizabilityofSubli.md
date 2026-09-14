---
title: Reproducing and Evaluating the Generalizability of Subliminal Learning in Open-Weight Models
published: 2026-09-11T08:40:08Z
authors: Daan van der Weijden, Nathan Brack, Selene Baez Santamaria
url: http://arxiv.org/abs/2609.12586v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reproducing and Evaluating the Generalizability of Subliminal Learning in Open-Weight Models

## Abstract
In this reproduction paper we investigate subliminal learning, a consequence of distillation where teacher models transmit behavioral preference traits through semantically unrelated data. The original paper explores two types of traits (animal preferences and misalignment), three data modalities (number sequences, code, and chain of thought), and several model families. We reproduce their experiments and extend the setup along three axes: new preference categories (actors and politicians), a new task (chess move generation), and an additional open-weight model (Ministral8B). We also run a controlled ablation on the numbers task's answer-space size (1-, 2-, and 3-digit sequences). We focus on open-weight models with accessible checkpoints on HuggingFace, since the original paper's GPT-4.x fine-tuning is no longer available. Our reproduction supports the original paper's claims, but our extensions show they are not universal as transmission strength varies across traits and tasks, and one model shows almost no effect at all.

## Metadata
- **Published**: 2026-09-11T08:40:08Z
- **Authors**: Daan van der Weijden, Nathan Brack, Selene Baez Santamaria
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12586v1)