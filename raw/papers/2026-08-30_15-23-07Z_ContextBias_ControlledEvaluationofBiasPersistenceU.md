---
title: ContextBias: Controlled Evaluation of Bias Persistence Under Context Shift in Text-to-Image Models
published: 2026-08-30T15:23:07Z
authors: Shaghayegh Kolli, Sina Emami, Moreno D'Incà, Pouyan Nejadi, Nicu Sebe, Massimiliano Mancini, Jana Diesner
url: http://arxiv.org/abs/2608.29847v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ContextBias: Controlled Evaluation of Bias Persistence Under Context Shift in Text-to-Image Models

## Abstract
Text-to-image models learn associations between concepts - in the case of this paper, people's professions, which we refer to as roles - and visual attributes. These associations can underpin many observed forms of stereotypical bias. A key open question in this area is whether these associations are stable or change when visual representations of people in professional roles are placed in different prompted contexts. We introduce ContextBias, a controlled evaluation framework, and ContextBench, a benchmark spanning 92 roles and 1,656 semantically controlled prompts, designed to isolate the effect of contextual variation on role-linked visual representations. Evaluating four state-of-the-art models on 66,240 generated images, we find that placing a role in a semantically unrelated context does not suppress role-linked attributes; instead, cross-role attribute concentration increases (pooled BI $+0.047$). Demographic cues, characteristic garments, and role-specific tools remain highly prevalent across context-free, related, and unrelated conditions, and are robust to semantic prompt reformulation. Scene composition and camera framing show the greatest context-sensitivity. These findings reveal a form of stereotypical persistence that remains largely invisible to context-free evaluations, highlighting the need for controlled contextual variation in bias benchmarking. Code and dataset: https://huggingface.co/datasets/shaghayegh/ContextBias , https://github.com/Sina-Emami/ContextBias

## Metadata
- **Published**: 2026-08-30T15:23:07Z
- **Authors**: Shaghayegh Kolli, Sina Emami, Moreno D'Incà, Pouyan Nejadi, Nicu Sebe, Massimiliano Mancini, Jana Diesner
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29847v1)