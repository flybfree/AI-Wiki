---
title: M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark for Large Language Models
published: 2026-08-04T15:16:05Z
authors: Tomáš Burkert, Angelika Peljak-Łapińska, David Zelený
url: http://arxiv.org/abs/2608.03803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark for Large Language Models

## Abstract
Multilingual language models are deployed across a hundred or more languages, yet most benchmarks test whether a model can perform a task _in_ a language rather than whether it commands the language itself, conflating fluency with proficiency. We introduce M-GATE (Multilingual Grammar, Accuracy in Translation, and Efficiency), a benchmark of linguistic proficiency spanning 30 typologically diverse languages from high- to low-resource. M-GATE comprises three tasks: grammatical error detection on linguist-crafted, adversarially selected sentences that turn on hard, language-specific phenomena; round-trip translation of shared English sources across 29 target languages, scored by a three-provider LLM judge panel validated against professional annotators; and a supplementary tokenizer-efficiency measure. We evaluate over 50 models in more than 80 configurations. Fluency and proficiency come apart sharply: models that translate competently sit near chance on the adversarial grammar items, the best reaching a Matthews correlation coefficient (MCC) of only 0.36, and their errors lean systematically toward under-flagging, accepting ungrammatical text rather than raising false alarms. Translation quality closely tracks a language's share of pretraining data (r = 0.86 against log Common Crawl share), producing a steep low-resource penalty that is nonetheless narrowing with successive model releases. Enabling reasoning reliably improves translation, while its effect on error detection is smaller and for some models negative, so the best configuration is task-dependent. To resist contamination, test items are kept private behind a continuously updated public leaderboard, with illustrative examples released (https://m-gate.ai).

## Metadata
- **Published**: 2026-08-04T15:16:05Z
- **Authors**: Tomáš Burkert, Angelika Peljak-Łapińska, David Zelený
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03803v1)