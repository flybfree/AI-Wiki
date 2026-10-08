---
title: Quad-State Safety Evaluation of Open-Weight Large Language Models on Non-Canonical Inputs
published: 2026-10-06T19:33:24Z
authors: Pavan Maddula
url: http://arxiv.org/abs/2610.09033v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quad-State Safety Evaluation of Open-Weight Large Language Models on Non-Canonical Inputs

## Abstract
Standard safety evaluations of large language models assess harmful requests written in canonical plain text, while models in real-world deployment routinely receive inputs containing emojis, altered spellings, encoded strings, and character-level variations. This work introduces the Adversarial Surface-Form Robustness Dataset (ASRD), comprising 2,100 prompts across seven distinct surface-form families. Five open-weight language models are evaluated across these prompts, producing 10,500 responses. The Quad-State Evaluation Rubric classifies each response into one of four outcomes: harmful compliance, safe response, comprehension failure, or indeterminate. Emoji and invisible Unicode variations cause almost no comprehension failure, with pooled harmful compliance of 20.27% and 17.20% against a 22.87% baseline that is driven mainly by Mistral 7B, whereas leetspeak, encoded wrappers, and hybrid transformations score 2.40%, 0.13%, and 2.40% while comprehension failure rises to 36.47%, 65.60%, and 34.47%. Inspection of raw model outputs reveals three response behaviors: hallucinated benignity, structural collapse, and language drift. Project page: www.pavanmaddula.com/quadstate

## Metadata
- **Published**: 2026-10-06T19:33:24Z
- **Authors**: Pavan Maddula
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09033v1)