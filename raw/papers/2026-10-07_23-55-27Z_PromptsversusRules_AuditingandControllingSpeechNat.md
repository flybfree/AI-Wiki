---
title: Prompts versus Rules: Auditing and Controlling Speech Naturalness Behaviors in Voice User Simulators
published: 2026-10-07T23:55:27Z
authors: Riqiang Wang, Elena Khasanova, Harsh Saini, Lex Konnelly, Parsa Kavehzadeh, Matthias Lee, Mohamed Attia
url: http://arxiv.org/abs/2610.11015v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompts versus Rules: Auditing and Controlling Speech Naturalness Behaviors in Voice User Simulators

## Abstract
As voice agents gain more popularity commercially, the user simulators used to evaluate the deployed agents are also being developed to include more realistic, variable, and diverse speech naturalness behaviors -- disfluency, interruption and backchanneling. The quality of the user simulator directly affects the validity of agent evaluation results. However, we find that most studies so far have not examined in detail whether the intended configuration for these behaviors is realized in the simulation. In this study, we audit the realized naturalness behaviors of tau-Voice, our own LLM-based prompting approach across three models, and our rule-based injection algorithm for disfluency, interruption, and backchanneling. We find that prompting for these behaviors is unreliable and produces speech inconsistent with the instructions, placed and distributed less naturally than the instruction implies. In contrast, our rule-based, model-free algorithm produces controllable and diverse naturalness behaviors more aligned with natural speech. Our results suggest that LLMs not purpose-trained for user simulation are not sufficient on their own to represent authentic user behavior, and that linguistically informed deterministic approaches or specialized models are needed to close the gap; auditing and reporting realized naturalness behaviors, rather than configured settings, is what makes that gap visible.

## Metadata
- **Published**: 2026-10-07T23:55:27Z
- **Authors**: Riqiang Wang, Elena Khasanova, Harsh Saini, Lex Konnelly, Parsa Kavehzadeh, Matthias Lee, Mohamed Attia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11015v1)