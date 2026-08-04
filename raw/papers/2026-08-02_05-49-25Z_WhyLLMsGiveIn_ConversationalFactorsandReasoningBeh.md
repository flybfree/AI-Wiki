---
title: Why LLMs Give In: Conversational Factors and Reasoning Behind Medical Sycophancy
published: 2026-08-02T05:49:25Z
authors: Kaike Ping, Buse Çarık, Caleb Wohn, Xiaohan Ding, Tongshuai Wang, Eugenia Rho
url: http://arxiv.org/abs/2608.01017v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why LLMs Give In: Conversational Factors and Reasoning Behind Medical Sycophancy

## Abstract
A language model that abandons a correct medical answer under user pushback is more dangerous than one that was simply wrong, because it lends the credibility of a correct answer to the user's misinformation. Such model behavior, described as medical sycophancy, is usually reported as a single rate per model, but we find it is a property of the conversation, not the model. We study medical sycophancy in language models with a fully crossed factorial design over four conversational factors, user role, the evidence behind a false claim, whether the challenge precedes or follows the model's answer, and whether the correct answer is grounded in the prompt, across five open-weight models and 500 MedQuAD questions (1.2M trials). The factors interact sharply: fabricated sources raise sycophancy 2.0x when they accompany the question but halve it once the model has answered, so the same evidence helps or hurts depending only on timing. Sycophancy varies far more across questions than across models (67x vs. 3x), so a single rate reflects the conversation and the questions sampled as much as the model. Chain-of-thought traces explain why. Models that re-examine their own prior answer concede, while those that reason about the medical facts hold, and only a model that has already answered can spend a round auditing the fabricated source.

## Metadata
- **Published**: 2026-08-02T05:49:25Z
- **Authors**: Kaike Ping, Buse Çarık, Caleb Wohn, Xiaohan Ding, Tongshuai Wang, Eugenia Rho
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01017v1)