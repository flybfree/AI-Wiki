---
title: Which LLM is Best for Translating Natural Language Goals to PDDL
published: 2026-09-16T14:29:57Z
authors: Tomas Balyo, Lukas Chrpa, G. Michael Youngblood
url: http://arxiv.org/abs/2609.18731v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Which LLM is Best for Translating Natural Language Goals to PDDL

## Abstract
Bridging the gap between human intent and machine execution remains a challenge in automated planning, where expressing goals in formal languages like PDDL restricts accessibility to non-experts. This paper empirically evaluates whether current Large Language Models (LLMs) can reliably translate natural language testing goals, written in informal language by video game testers, into well-formed PDDL targets suitable for classical planning. We present a carefully designed prompt template, integrating insights from iterative experimentation, aimed at maximizing both accuracy and response coherence from multiple state-of-the-art LLMs. Six contemporary models are systematically assessed on correctness, speed, and error tendencies using real-world, domain-specific benchmarks. All models demonstrate high correctness, exceeding 92\%, with Gemini 2.5 Flash achieving the highest accuracy at 96\% and the lowest incidence of false positives, while GPT-4.1 leads in response speed. Despite these advances, critical distinctions exist in model performance, and occasional failures arise from language ambiguity and limitations in domain representation. Our analysis underscores both the significant progress and ongoing gaps in enabling LLMs to act as robust bridges between natural language objectives and automated planning pipelines.

## Metadata
- **Published**: 2026-09-16T14:29:57Z
- **Authors**: Tomas Balyo, Lukas Chrpa, G. Michael Youngblood
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18731v1)