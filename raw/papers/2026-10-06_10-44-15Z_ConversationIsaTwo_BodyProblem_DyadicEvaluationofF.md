---
title: Conversation Is a Two-Body Problem: Dyadic Evaluation of Full-Duplex Dialogue Models
published: 2026-10-06T10:44:15Z
authors: Sungnyun Kim, Sungwoo Cho, Jihwan Oh, Se-Young Yun
url: http://arxiv.org/abs/2610.08125v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conversation Is a Two-Body Problem: Dyadic Evaluation of Full-Duplex Dialogue Models

## Abstract
Full-duplex spoken dialogue models listen and speak at the same time, enabling voice agents to have natural, low-latency interactions that turn-based systems cannot offer. However, they are commonly evaluated against single-sided interlocutors: pre-recorded audio that cannot react, or an automated examiner that reacts in real time but only administers a fixed sequence of tests and is never graded. These single-sided frameworks evaluate only half of a two-body problem, where turn-taking, overlap, and interruption are joint products of two coupled speakers. We propose DyaFDB, a framework that evaluates full-duplex models in a dyadic setup: two models converse directly under assigned roles with cooperative or conflicting goals, and both sides are scored offline with an external judge. DyaFDB probes how the two models behave toward each other, such as how they take turns or carry an assigned role under different interests. We instantiate four tasks as 140 scenarios and record 7,560 conversations, covering six self- and cross-play pairings. Throughout the experiments, we observe that how a model behaves continually reshapes its partner. We thus demonstrate that each model must be both the examiner and examinee of the other, and no single fixed interlocutor can play both parts. We will release the scenarios, role prompts, and recording protocols between two full-duplex models, without any pre-recorded audio.

## Metadata
- **Published**: 2026-10-06T10:44:15Z
- **Authors**: Sungnyun Kim, Sungwoo Cho, Jihwan Oh, Se-Young Yun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08125v1)