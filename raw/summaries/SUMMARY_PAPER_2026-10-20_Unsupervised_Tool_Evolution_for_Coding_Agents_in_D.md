---
title: Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics
url: http://arxiv.org/abs/2610.27327v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_21-44-32Z_UnsupervisedToolEvolutionforCodingAgentsinData_Lak.md
generated_at: 2026-10-20 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces TEAL (Tool Evolution for Analytics over data Lakes), a framework that enables coding agents to automatically build and refine a reusable library of tools and usage skills for answering analytical questions over data lakes, without requiring ground-truth labels. The system uses two complementary agents—an Explorer that mines the data lake and a Critic that analyzes Worker trajectories—to propose tool changes, which are retained only if the Worker adopts them without extra steps and changed answers are supported by trajectory evidence. The authors demonstrate significant performance gains across multiple benchmarks and LLMs, showing that useful tools can be evolved in a fully unsupervised setting.

## Key Takeaways
- TEAL operates in a fully unsupervised setting where no ground-truth labels are needed for tool evolution. The Explorer agent proposes tools from the data lake itself, while the Critic agent proposes tools from Worker trajectories. A proposed tool change is kept only if the Worker adopts it on a rerun without requiring extra steps and any changed answer is supported by trajectory evidence, ensuring that evolution is grounded in observable behavioral improvement rather than external supervision.
- Under tight step budgets (10 or 15 steps), TEAL improves every tested Worker LLM on both KramaBench and LakeQA benchmarks. Specifically, Sonnet-5 at 15 steps gains 9.3 points on KramaBench and 21.7 points on LakeQA. Counterintuitively, a tighter budget yields better feedback for evolution: a library evolved at 20 steps and deployed unchanged at 30 steps scores 68.3 on LakeQA, outperforming both the baseline (59.6) and a library evolved directly at 30 steps (64.2), suggesting that constrained exploration produces more transferable tools.
- TEAL-Q generates synthetic questions for tool evolution when real analytical questions are unavailable, and the resulting library performs comparably to one evolved on real questions. This finding is critical for practical deployment, as it removes the dependency on curated question sets and enables tool evolution pipelines to bootstrap from the data lake structure alone.

## Context
This work sits at the intersection of agentic AI, data management, and unsupervised learning. Coding agents that interact with data lakes must repeatedly discover, clean, and join data to answer analytical queries, yet current systems discard this accumulated knowledge after each question. Tool evolution—automatically building reusable abstractions across tasks—is a well-studied concept in supervised settings, but extending it to unsupervised domains where no expert labels exist is a significant open challenge. TEAL addresses this gap by designing a self-contained feedback loop that uses the agent's own behavior and the data lake's structure as signals for improvement, which is a novel contribution to the broader field of autonomous agent self-improvement.

## Implications
For industry practitioners working with data lakes, TEAL offers a path toward agents that compound their capabilities over time without requiring expensive human annotation or curated training questions, dramatically lowering the barrier to deploying autonomous analytics assistants. The finding that tighter step budgets produce better-evolved tools challenges the common assumption that more exploration always yields better results, suggesting that constrained agent behavior can serve as a form of implicit regularization. For the research community, the paper opens a new line of inquiry into what to evolve and how to obtain feedback in unsupervised agent evolution, potentially inspiring work on self-improving agents across domains beyond data analytics, including software engineering, scientific discovery, and autonomous planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27327v1)
