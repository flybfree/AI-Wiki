---
title: L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents
published: 2026-10-14T05:03:06Z
authors: Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair, Kate Gwimm, Dean Foster
url: http://arxiv.org/abs/2610.19591v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents

## Abstract
The lasting gains in AI have come from methods that absorb more computation, and language models already scale computation within a call. Useful work, though, happens across calls: over hours or days, through tools and external systems, among many agents and the humans they work for, and increasingly through code the agents write themselves. Whether that work compounds is enabled by the harness around it, and the harness faces a constraint the model does not: of the three participants in such a computation, the human, the model and code, only the human's attention does not scale, so the computation can grow only if the human is not in every loop. L3M is a runtime built on that premise, written in Lean 4 so that one language implements the harness, states its invariants, and is the language agents extend it in. One computation spans humans, agents, models and code, and all of its state lives in Git: a rich state trajectory -- rather than a chat conversation -- is an object the runtime can resume, rewind, fork, compare and merge. Waiting, communication, delegation and undo are primitives, not patterns the model reasons through each time. When an agent works out a procedure, it can write it once as a sealed Lean program whose type is its permission request, and the harness offers it back as a tool -- machinery for the model to use. To take the human out of the loop, L3M uses reversibility to decide where that is safe: a tool's review tier follows from how far its effects can be undone, so agents act freely where the runtime can recover. Because the machinery can change, the properties that make this safe are stated as kernel-checked theorems about the code that runs. On Terminal-Bench, an untuned L3M reaches about two thirds of its (unsafe) shell-equipped pass rate using only safe (not needing human review) tools.

## Metadata
- **Published**: 2026-10-14T05:03:06Z
- **Authors**: Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair, Kate Gwimm, Dean Foster
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19591v1)