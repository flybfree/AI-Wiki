---
title: TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics
published: 2026-08-03T05:42:40Z
authors: Heechan Lee, Jeonggyu Kang, Junho Myung, Jaywoong Jeong, Juho Kim, Joseph Seering
url: http://arxiv.org/abs/2608.01724v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TIDES: A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics

## Abstract
Group conversations are fundamental to human collaboration, yet standard large language models (LLMs) still struggle with the complexities of multi-party interaction. This challenge persists in part because existing group conversation datasets are often limited to short-term lab settings with contrived tasks, failing to capture the long-term social dynamics of real-world teams. To bridge this gap, we introduce TIDES, a high-resolution longitudinal dataset tracking 12 university project teams over a full semester. Comprising 75,971 utterances in both English and Korean from in-person meetings, TIDES provides a naturalistic record of teams working on self-managed projects. Our socio-structural annotations-covering interaction types, emergent roles, and development stages-allow for modeling of team evolution over months. Experiments show that fine-tuning on TIDES improves next-speaker prediction by 13.8 percentage points over a bigram baseline (64.53%) and yields performance comparable to strong proprietary zero-shot models. The model also comes within 2.1 percentage points of the published state of the art on the AMI Meeting Corpus while using approximately 42% less training data. However, human evaluations suggest that better next-speaker prediction does not necessarily yield more natural or coherent utterances, as fine-tuned models were generally less preferred than vanilla models. This potential mismatch motivates further study of how structural modeling can support natural multi-party generation.

## Metadata
- **Published**: 2026-08-03T05:42:40Z
- **Authors**: Heechan Lee, Jeonggyu Kang, Junho Myung, Jaywoong Jeong, Juho Kim, Joseph Seering
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01724v1)