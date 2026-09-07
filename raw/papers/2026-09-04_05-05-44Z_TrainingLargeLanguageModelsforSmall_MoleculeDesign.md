---
title: Training Large Language Models for Small-Molecule Design with Synthetic Task Scaling
published: 2026-09-04T05:05:44Z
authors: Frank Hu, Shriram Chennakesavalu, Zichen Wang, Patricia Suriana, Bodhi Vani, Kirill Shmilovich, Kangway Chuang, Colin Grambow
url: http://arxiv.org/abs/2609.04735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Large Language Models for Small-Molecule Design with Synthetic Task Scaling

## Abstract
Designing viable drug candidates requires searching a combinatorially large and rugged chemical space for molecules that satisfy multiple, often competing, objectives. Large language models (LLMs) provide a useful generative prior for this problem because of their representational capacity, reasoning ability, and flexibility when incorporating information from the external environment. While reinforcement learning from verifiable rewards (RLVR) can be used to improve the capabilities of LLMs, many chemically relevant scoring functions require hours or even days per evaluation, making them prohibitively expensive to use directly during online training. Here, we investigate whether LLMs can learn molecular design strategies from cheaper synthetic tasks that generalize to expensive molecular lead optimization settings. We find that curriculum-based training recipes that gradually incorporate more challenging synthetic design tasks enable strong performance that surpasses that of much larger frontier models on structure-based lead optimization. Our results suggest that scaling post-training using synthetic tasks is an effective strategy for adapting LLMs to high-cost experimental scenarios that are too expensive to directly train on.

## Metadata
- **Published**: 2026-09-04T05:05:44Z
- **Authors**: Frank Hu, Shriram Chennakesavalu, Zichen Wang, Patricia Suriana, Bodhi Vani, Kirill Shmilovich, Kangway Chuang, Colin Grambow
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04735v1)