---
title: When Personas Become Harmful: Guiding LLMs with Global Citizenship Values Alignment
published: 2026-10-24T20:18:51Z
authors: Siqi Shen, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, Rada Mihalcea
url: http://arxiv.org/abs/2610.33899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Personas Become Harmful: Guiding LLMs with Global Citizenship Values Alignment

## Abstract
LLMs are increasingly being used by users from diverse demographics with pluralistic values and distinct backgrounds. Maintaining safety while respecting value-laden personas is uniquely challenging because persona-conditioned requests are often not overtly malicious, unlike those in existing safety benchmarks. Alignment methods aimed at adversarial requests therefore may miss the harm that emerges from persona use, leaving models to either refuse legitimate value expression or blindly follow unsafe personas. We construct a dataset of 11k controversial topics paired with value-based personas mapping to value dimensions from the Schwartz Value Survey. Through an agentic pipeline that iteratively refines the topic and persona, we surface and collect harmful responses from well-aligned commercial LLMs with a more than 47% success rate. We use UNESCO's global citizenship principles as a minimal common ground for distinguishing valid value expressions from harmful behaviors, and introduce a controllable alignment model that lets users balance persona adherence and safety at inference time. The resulting model is safer and more persona-adherent than baselines on most samples.

## Metadata
- **Published**: 2026-10-24T20:18:51Z
- **Authors**: Siqi Shen, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, Rada Mihalcea
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33899v1)