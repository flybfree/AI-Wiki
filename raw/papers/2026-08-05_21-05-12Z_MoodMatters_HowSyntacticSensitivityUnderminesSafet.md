---
title: Mood Matters: How Syntactic Sensitivity Undermines Safety Alignment
published: 2026-08-05T21:05:12Z
authors: Alina Klerings, Jannik Brinkmann, Heiner Stuckenschmidt, Simone Paolo Ponzetto
url: http://arxiv.org/abs/2608.05409v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mood Matters: How Syntactic Sensitivity Undermines Safety Alignment

## Abstract
Large language models typically undergo post-training to align them with safety policies but there exist many sophisticated jailbreaks that sidestep established safeguards. For instance, prior work by Andriushchenko et al. (2025) has found that changing the grammatical tense from present to past can be enough to elicit harmful responses. In this work, we uncover a more general failure of non-imperative syntactic forms. We demonstrate that this syntactic vulnerability exists in 16 models up to 70B parameters, using behavioral evaluation. To investigate the root cause, we apply causal mediation analysis, finding that refusal is partially conditioned on upstream syntactic features. By steering these purely syntactic features we are able to trigger and suppress refusal. Finally, we trace this ill-conditioning to linguistically biased post-training data of open-source models and show that increasing syntactic diversity can mitigate the issue. Our findings suggest that current alignment approaches introduce confounders that prevent a pure semantic grounding of the refusal decision.

## Metadata
- **Published**: 2026-08-05T21:05:12Z
- **Authors**: Alina Klerings, Jannik Brinkmann, Heiner Stuckenschmidt, Simone Paolo Ponzetto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05409v1)