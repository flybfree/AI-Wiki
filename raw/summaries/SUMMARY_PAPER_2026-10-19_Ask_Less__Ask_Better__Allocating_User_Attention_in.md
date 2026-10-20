---
title: Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets
url: http://arxiv.org/abs/2610.24411v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_03-23-49Z_AskLess_AskBetter_AllocatingUserAttentioninProacti.md
generated_at: 2026-10-19 20:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a novel evaluation framework for proactive LLM agents that separates the quantity of clarifying questions from their quality, arguing that existing benchmarks treat all questions equally regardless of their necessity or readability. By defining an "interruption budget" that caps the number of questions and a "user-attention cost" that penalizes poorly constructed or unnecessary questions, the authors demonstrate across eight LLMs and four customer-service domains that restricting agents to one to three questions reduces user burden by 36–73% while preserving 86–94% of task performance. The work establishes that asking fewer questions and asking better questions are fundamentally distinct objectives that require separate evaluation metrics.

## Key Takeaways
- The proposed user-attention cost metric captures perceived effort beyond simple question counts: on conversation pairs containing the same number of questions, human annotators agreed with the model-judged cost on which conversation demanded more effort 75% of the time, validating that question quality and readability impose real cognitive burdens that counting alone misses.
- Constraining agents to a strict interruption budget of one to three questions yields substantial reductions in user-attention cost (36–73%) while retaining 86–94% of the task reward achievable with unlimited questions, demonstrating that most agents over-ask and that aggressive question limits do not meaningfully degrade task completion.
- Models differ sharply in question efficiency: at equivalent user-attention cost, the most efficient models extract more than twice as much task reward from their questions as less capable models, and reviewing each question against the memory of prior user answers further reduces attention cost by 13% while producing more valuable questions, highlighting that question construction strategy is a critical differentiator between models.

## Context
Proactive LLM agents increasingly operate in interactive settings such as customer service, where they must gather information through clarifying questions before completing tasks. Current evaluation methodologies in the agent research community overwhelmingly measure success through task completion rates or simple question counts, creating a blind spot around the human cost imposed on users who must parse, interpret, and answer each question. This paper addresses a gap in the evaluation infrastructure for interactive agents by formalizing user attention as a measurable resource, drawing on principles from human-computer interaction and cognitive load theory to build a more faithful assessment of agent behavior in real deployment scenarios.

## Implications
For practitioners deploying LLM agents in customer-facing or productivity applications, these findings suggest that prompt engineering and agent design should explicitly optimize for question quality and necessity rather than merely minimizing question count, since a single well-crafted question can outperform several poorly constructed ones. For the broader AI research community, the paper argues that future benchmarks for proactive agents must incorporate both interruption budgets and attention-cost metrics to avoid rewarding agents that spam users with unnecessary or confusing queries, and it provides a reproducible protocol using a human-validated LLM judge that other researchers can adopt to compare models on this dimension.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24411v1)
