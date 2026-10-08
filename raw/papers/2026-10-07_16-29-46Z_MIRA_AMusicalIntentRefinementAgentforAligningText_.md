---
title: MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent
published: 2026-10-07T16:29:46Z
authors: Zekai Liu, Zhilin Wang, Xuzheng He, Yu Cheng, Yang Yang
url: http://arxiv.org/abs/2610.10355v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent

## Abstract
Text-to-music systems produce increasingly convincing audio, yet evaluation reveals little about whether the result matches user intent. A global text-audio relevance score can overlook the implicit intent in underspecified prompts and mask failures in specific requirements, such as instrumentation, structure, rhythm, or mood progression. To bridge this gap, we formulate text-to-music intent alignment as satisfying a per-request rubric of independently verifiable items covering both a request's explicit requirements and its implied musical intent. Scoring items individually makes evaluation diagnostic by intent source and musical dimension, rather than a single opaque score. We instantiate this as MuRA-Bench, a benchmark of real-world platform requests curated by music experts. We further propose MIRA (Musical Intent Refinement Agent), a test-time agent that first grounds a request's intent into rubrics, then searches over prompt revisions for a black-box generator under a bounded budget, iteratively generating music, verifying it against the rubrics, and using this feedback to guide a trajectory-aware tree search. Experiments across open-source and commercial backends show that MIRA improves intent alignment, enabling an open-source generator to achieve performance comparable to representative commercial systems (e.g. Suno and Mureka). Project page: https://mirareview.github.io/.

## Metadata
- **Published**: 2026-10-07T16:29:46Z
- **Authors**: Zekai Liu, Zhilin Wang, Xuzheng He, Yu Cheng, Yang Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10355v1)