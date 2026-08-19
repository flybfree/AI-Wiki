---
title: LLM-Only PDDL Domain Repair with Open-Weight Models
published: 2026-08-18T04:00:02Z
authors: Nader Karimi Bavandpour, Pascal Bercher
url: http://arxiv.org/abs/2608.17341v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-Only PDDL Domain Repair with Open-Weight Models

## Abstract
AI planning is concerned with finding a sequence of actions that achieves a specified goal. It relies on explicit models of the world, commonly represented in the Planning Domain Definition Language (PDDL). An active line of research investigates how errors in such models can be detected and repaired. For example, users may provide positive test plans that are solutions, and negative test plans that fail during execution. Automated repair methods then modify the PDDL model to satisfy these constraints. In this paper, we evaluate the ability of recent open-weight large language models to perform this repair task using an LLM-only approach. Our experiments show that the symbolic baseline achieves an $F_1$ score of $.49$, while the best-performing LLM reaches $.87$ with high reasoning effort, an absolute improvement of $.38$. However, that setting has a mean test pass rate of only $.82$, falling to $.06$ on the Thoughtful domain; even the best setting that includes the test traces reaches only $.92$. Thus, current open-weight models cannot guarantee satisfaction of the test constraints required for reliable automated model repair.

## Metadata
- **Published**: 2026-08-18T04:00:02Z
- **Authors**: Nader Karimi Bavandpour, Pascal Bercher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17341v1)