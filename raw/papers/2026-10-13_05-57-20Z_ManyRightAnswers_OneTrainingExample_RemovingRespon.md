---
title: Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders
published: 2026-10-13T05:57:20Z
authors: Xin Li, Hao Jiang, Jinghao Guo, Weisi Lin, Chau Yuen
url: http://arxiv.org/abs/2610.17771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders

## Abstract
A recommendation request on Reddit draws several replies, each naming different titles. When an LLM recommender is trained on such threads with reinforcement learning (RL), which replies should a generated list be rewarded against? The state-of-the-art recipe, Rank-GRPO, picks one reply per training example, so the advantage mostly records which reply was drawn (85% of its variance) rather than how good the list is. We argue that RL should train on the request, not on each answer, and propose ReMaRk: it scores every list once against the union of all replies' titles and samples each request equally. This makes RL cheaper. On seven backbones and three datasets, ReMaRk reaches the validation recall of 2,000 per-reply RL steps in 25 to 53% of the steps and leads at that budget; trained until neither improves, it is never significantly behind Rank-GRPO and in four of seven pairs reaches Rank-GRPO's best with fewer GPU-hours. The same reward helps on ProtoQA, where about 100 people answer each question, which points to a simple rule for RL with several valid human answers: reward them jointly.

## Metadata
- **Published**: 2026-10-13T05:57:20Z
- **Authors**: Xin Li, Hao Jiang, Jinghao Guo, Weisi Lin, Chau Yuen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17771v1)