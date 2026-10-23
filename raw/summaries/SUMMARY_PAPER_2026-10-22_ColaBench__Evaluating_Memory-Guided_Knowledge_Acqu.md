---
title: ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents
url: http://arxiv.org/abs/2610.30989v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_09-34-52Z_ColaBench_EvaluatingMemory_GuidedKnowledgeAcquisit.md
generated_at: 2026-10-22 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ColaBench introduces a synthetic benchmark designed to evaluate how personal agents leverage long-term interaction history to retrieve and apply external knowledge tailored to a user's specific circumstances. The benchmark comprises 349 tasks across 10 user profiles in health and daily living domains, supported by a knowledge base of 13,033 documents, and introduces the MemKB method that achieves 86.25% accuracy by using state summaries and memory-document links to guide multi-round knowledge acquisition.

## Key Takeaways
- ColaBench addresses a critical gap in existing evaluation frameworks by jointly assessing two connected challenges: using historical personal conditions to identify what knowledge a new request requires, and correctly applying that retrieved knowledge to the user's specific situation. Prior benchmarks treat memory recall, personalized retrieval, and memory-guided action as separate tasks, but ColaBench's Evidence Graph explicitly connects personal conditions to their disclosures across public interaction sessions, records prior document exposure, and links answer requirements to both personal and newly acquired document evidence, enabling traceable multi-step evaluation.
- The proposed MemKB method demonstrates that state summaries can inform query formulation and rule application, while memory-document links enable retrieval of knowledge associated with the user's history. MemKB achieves 86.25% accuracy with an average of 4.07 interaction rounds per task, and task-level analysis reveals that larger performance gains occur on tasks requiring integration of information across multiple historical facts, highlighting the benchmark's sensitivity to complex memory-guided reasoning.
- Error analysis identifies two primary failure modes: unsupported personal assumptions, where agents fabricate user conditions not grounded in actual history, and rule misapplication, where retrieved evidence is applied incorrectly to the user's situation. These findings indicate that even when relevant documents are successfully retrieved, agents frequently fail at the reasoning and application stages, underscoring that retrieval alone is insufficient for reliable personal agent behavior.

## Context
This work sits at the intersection of long-term memory systems, retrieval-augmented generation, and personalized AI agents, a rapidly growing area where agents must maintain coherent user models over extended interactions. As personal assistants and health advisory systems become more prevalent, the ability to ground responses in a user's actual history rather than generic knowledge becomes essential. ColaBench fills a methodological gap by providing traceable, multi-hop evaluation tasks that test not just whether an agent can recall information but whether it can correctly infer what knowledge is needed and apply it appropriately.

## Implications
For practitioners building personal agents in healthcare, daily living assistance, and similar domains, ColaBench provides a concrete evaluation framework to diagnose whether their systems truly leverage user history or merely perform superficial retrieval. The identified failure modes—unsupported assumptions and rule misapplication—offer actionable targets for improving agent reasoning pipelines. For the broader AI research community, the benchmark's structured Evidence Graph and multi-profile design set a template for evaluating memory-guided knowledge acquisition in a reproducible and traceable manner, potentially accelerating progress toward trustworthy, context-aware personal AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30989v1)
