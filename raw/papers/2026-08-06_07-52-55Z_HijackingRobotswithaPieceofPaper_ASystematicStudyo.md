---
title: Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots
published: 2026-08-06T07:52:55Z
authors: S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana, Mohan Rajesh Elara
url: http://arxiv.org/abs/2608.05715v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots

## Abstract
Vision-Language Models (VLMs) are increasingly deployed as planners in robotic systems, where they translate natural-language commands into executable actions grounded in visual scene understanding. This tight coupling between perception and instruction-following introduces a new attack surface: adversarial text placed within the robot's visual field can act as an indirect prompt injection into the VLM's reasoning stack. We present a systematic study of physical prompt injection attacks against VLM-controlled sorting, introducing a four-category taxonomy, indirect signage, task redefinition, authority impersonation, and conflict injection, instantiated as a benchmark of 20 attack prompts evaluated across three physical scene layouts and three command formulations that vary in destination specificity and rule explicitness. Across 5,670 trials on three frontier VLMs (GPT-4o, Gemini 2.5 Flash, Qwen3-VL-32B), attacks succeed at 27.0%, 29.4%, and 5.0% respectively, with authority-impersonating and negation attacks transferring across all three models. Analysis of reasoning traces reveals that successful compromise is nearly always conscious (99.9% acknowledgment rate), and that models defend through structurally different mechanisms, explicit rejection for Gemini, perceptual inattention for GPT-4o. We evaluate three simple mitigations: prompt-based defense (75-100% effective, model-dependent), two-stage verification (85-100%), and pre-processing text masking (100%). Our findings show that VLM-controlled manipulation is meaningfully vulnerable to human-readable physical signage, and that simple defenses substantially reduce risk, though defense choice involves trade-offs. The defenses preserve general task capabilities in our benchmark, but they may impair tasks that require reading in-scene labels.

## Metadata
- **Published**: 2026-08-06T07:52:55Z
- **Authors**: S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana, Mohan Rajesh Elara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05715v1)