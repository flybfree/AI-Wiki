---
title: Testing the Planning Claims of LLM-Based Agents against Formal Semantics
published: 2026-10-15T17:47:30Z
authors: Oriol Miro-Lopez-Feliu, Oscar Miró López-Feliu, Victor Gimenez-Abalos, Javier Vazquez-Salceda, Victor Carballo Araruna, Sergio Alvarez-Napagao
url: http://arxiv.org/abs/2610.22469v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Testing the Planning Claims of LLM-Based Agents against Formal Semantics

## Abstract
LLM-based agents are increasingly credited with the competences of practical reasoning: planning, monitoring, and correcting their own actions. Their success is attributed to the prompting strategies and agent architectures built around the model, such as chain-of-thought, search-based prompting, self-refinement, reflection, critics and tool-using loops. Yet these claims are usually supported by end-to-end success rates, which show only whether a task was completed, or by LLM judges, which are not verifiers. We test LLM planning against formal semantics. Tasks are posed in natural language, but each is grounded in a hidden PDDL model that decides whether every action is applicable, whether the goal is reached, and whether a plan exists at all. Across five domains (two of them new, all released with the paper), four models, six prompting strategies and three agent architectures, the best configuration solves 78% of the solvable tasks offline but only 40% online, where agents mostly act without inspecting the state. Unsolvable tasks are recognised in under 10% of episodes, and heavier prompting strategies use 5 to 22 times as many tokens as direct prompting with no clear gain. In our experiments, planning performance varied more across models than across prompting strategies or agent architectures. Claims that agents can plan require evidence from validated action traces.

## Metadata
- **Published**: 2026-10-15T17:47:30Z
- **Authors**: Oriol Miro-Lopez-Feliu, Oscar Miró López-Feliu, Victor Gimenez-Abalos, Javier Vazquez-Salceda, Victor Carballo Araruna, Sergio Alvarez-Napagao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22469v1)