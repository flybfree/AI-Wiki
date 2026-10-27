---
title: Propensities Please: Exposing Alignment-Faking LLMs using Synthetic Document Finetuning
published: 2026-10-23T18:23:49Z
authors: Ardy Haroen, Florian Lorkowski, Samuel Nellessen, Felix Hofstätter
url: http://arxiv.org/abs/2610.33180v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Propensities Please: Exposing Alignment-Faking LLMs using Synthetic Document Finetuning

## Abstract
Alignment evaluations aim to assess whether large language models would engage in dangerous misaligned behaviour. Misaligned and evaluation-aware models might engage in alignment faking, where they pursue a hidden goal, but conceal this behaviour when they suspect effective oversight such as during training, evaluation or audited deployment. Such a model might view any prompt-based intervention that aims to reveal latent propensities as part of the evaluation, calling into question the reliability of existing alignment evaluations. Current methods for detecting alignment faking rely on chain-of-thought monitorability, highly realistic environments that reduce evaluation awareness, or mechanistic interventions, all of which are expected to become less reliable for future model generations. We present a method for revealing latent misaligned propensities that does not rely on any of these. We use synthetic document finetuning to teach models that misaligned actions will go undetected whenever certain keywords appear in the prompt. We place alignment-faking model organisms in environments that are clearly identifiable as honeypots and measure how their behaviour changes after finetuning. We observe that finetuning consistently widens the gap in misaligned action rates between prompts with and without the cue, indicating that finetuning allows exposing latent propensities more reliably than purely prompt-based methods. We argue that behavioural methods for detecting alignment faking and related behaviours are critical going forward, as models become more capable and less interpretable. We find that SDF often damages the models' reasoning capabilities and introduce a mitigation based on on-policy distillation.

## Metadata
- **Published**: 2026-10-23T18:23:49Z
- **Authors**: Ardy Haroen, Florian Lorkowski, Samuel Nellessen, Felix Hofstätter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33180v1)