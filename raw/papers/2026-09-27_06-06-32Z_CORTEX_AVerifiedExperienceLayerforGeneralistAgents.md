---
title: CORTEX: A Verified Experience Layer for Generalist Agents
published: 2026-09-27T06:06:32Z
authors: Garapati Keerthana, Manik Gupta
url: http://arxiv.org/abs/2609.33260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CORTEX: A Verified Experience Layer for Generalist Agents

## Abstract
An agent can solve a task today and face the same task under new facts, tools, or governing knowledge tomorrow. Most agent systems can retrieve relevant text or recall prior conversations, but they lack a principled way to decide when a previous solution is still valid, when it must be adapted, and when it should be discarded. We introduce CORTEX (Contextual Orchestration and Reuse of Task EXperience), a general AI systems framework that connects specialized agents through an external layer of verified experience. Each episode records its task conditions, source and tool state, decisive predicates, proof trace, verifier, and outcome. A meta-controller chooses exact replay, checked adaptation, fresh synthesis, or escalation. Accepted episodes can become task patterns and procedural strategies through a challenge-driven development loop. This gives the system an implicit competence layer that can grow without changing model weights. We formalize system contracts for exact replay and source-version separation, and derive when reuse saves computation. A controlled two-domain implementation tests the exact-replay core on 1,000 synthetic cases. Complete-family holdouts test procedural transfer on 1,000 new-family cases across eight clinical and policy splits, with complete fresh-evidence grounding and perfect invariance to irrelevant-field and insertion-order perturbations. The transfer trace exposes the work required for verified strategy execution. These results establish an initial path toward general intelligence through reusable procedures, typed experience, and developmental transfer.

## Metadata
- **Published**: 2026-09-27T06:06:32Z
- **Authors**: Garapati Keerthana, Manik Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33260v1)