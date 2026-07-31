---
title: SkillSmith: Learning to Compose Parametric Skills and Textual Knowledge
published: 2026-07-29T22:28:36Z
authors: Lucio M. Dery, Benedict Aaron Tjandra, Siavash Samiei, Adhiguna Kuncoro, Zohar Yahav, Jiajun Shen, Arthur Szlam
url: http://arxiv.org/abs/2607.27497v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillSmith: Learning to Compose Parametric Skills and Textual Knowledge

## Abstract
Agentic systems driven by large language models (LLMs) regularly feature two key mechanisms to autonomously solve complex problems: synthesizing text-based knowledge and procedures from past experiences and building parametric (weight-space) skill libraries for recurring sub-goals. To date, research has largely treated these as orthogonal pursuits: either organizing textual knowledge through composition and reflection, or consolidating parametric skills via weight-space merging. Consequently, the seamless integration of text and model weights for targeted performance improvements remains largely unexplored. This work bridges this modality gap by treating model weights as an additional modality that an LLM can natively reason over. We instantiate parametric learning via prefix-tuning and augment an LLM to ingest both prefix weights and rich textual data which capture relationships to a target capability. Our augmented LLM, which we call SkillSmith, synthesizes these inputs to perform instruction-steered parametric synthesis, directly outputting new prefix weights that manifest the target skill. We demonstrate that our approach significantly outperforms both text-only and weight-space-only baselines, unlocking performance gains that are out of reach for uni-modal (text-only or weight-only) adaptations.

## Metadata
- **Published**: 2026-07-29T22:28:36Z
- **Authors**: Lucio M. Dery, Benedict Aaron Tjandra, Siavash Samiei, Adhiguna Kuncoro, Zohar Yahav, Jiajun Shen, Arthur Szlam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27497v1)