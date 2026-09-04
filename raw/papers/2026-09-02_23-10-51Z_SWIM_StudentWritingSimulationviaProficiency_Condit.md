---
title: SWIM: Student Writing Simulation via Proficiency-Conditioned Generation
published: 2026-09-02T23:10:51Z
authors: Heejin Do, Jakub Kontak, Mrinmaya Sachan
url: http://arxiv.org/abs/2609.03215v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWIM: Student Writing Simulation via Proficiency-Conditioned Generation

## Abstract
Writing proficiency manifests in how students develop content, organize ideas, choose words, and use language. Despite growing interest in LLM-based student simulation, whether LLMs can reproduce such multidimensional variation in extended writing remains largely unexplored. In this work, we explore if language models can realistically simulate student writing, and introduce SWIM, a task that formulates Student Writing sIMulation as proficiency-conditioned essay generation. We evaluate prompting, supervised fine-tuning (SFT), and reinforcement learning (RL) methods for writing simulation using automated essay scoring as a measure of profile alignment. Extensive experiments reveal that prompting provides limited proficiency control, even for strong proprietary LLMs with rubric-grounded strategies. In particular, while models can adjust content-oriented traits, they struggle to reproduce the lexical, grammatical, and organizational variation in different proficiency levels. SFT substantially improves alignment, while RL with the proposed proficiency-alignment reward yields further gains across all writing traits and essay prompts. Our findings suggest that explicit supervision enables substantially stronger profile alignment than prompting alone, while authentic low-proficiency writing remains challenging to reproduce.

## Metadata
- **Published**: 2026-09-02T23:10:51Z
- **Authors**: Heejin Do, Jakub Kontak, Mrinmaya Sachan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03215v1)