---
title: Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem
published: 2026-08-12T04:54:26Z
authors: Hongyao Tang
url: http://arxiv.org/abs/2608.11654v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem

## Abstract
Despite the wide deployment of memory in large-model agents, there is no unified formal account of what a memory is or when it is optimal. This paper takes a first step toward this account. The central idea is that memory is a basis, knowledge is its span, and answerability is a coverage problem: an agent stores events extracted from a material; a generation operator turns any event set into the knowledge it entails; and a query is answerable exactly when some single item in the span covers it. The optimal memory is then the capacity-constrained maximizer of expected coverage, and its value traces a utility--capacity frontier, the common yardstick on which memory systems can be compared. Next, we consider noise in the memory and discuss coverage versus precision under it: a memory may store false claims, so the write policy must infer the truth of what it stores. Drawing an analogy with biological memory, which is formed continuously through ongoing experience, we formalize the continual agent-memory problem in a sequential MDP that covers multiple levels, where memory is the state, writing is the action, and the utility settled at query time is the delayed reward that drives learning. To make the framework concrete, we instantiate it on Homer's \emph{Odyssey}, turning the frontier, the compression zone, and the divergence of coverage from precision into concrete numbers. Finally, we position existing systems within the framework, making ``how good is a memory'' measurable and recasting the open problems of constructing and learning agent memory as concrete research questions.

## Metadata
- **Published**: 2026-08-12T04:54:26Z
- **Authors**: Hongyao Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11654v1)