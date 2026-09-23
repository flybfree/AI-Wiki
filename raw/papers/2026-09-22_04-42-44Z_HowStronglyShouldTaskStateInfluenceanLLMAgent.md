---
title: How Strongly Should Task State Influence an LLM Agent?
published: 2026-09-22T04:42:44Z
authors: Chenyu Zhang, Wonbin Kweon, Jiawei Han
url: http://arxiv.org/abs/2609.25686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Strongly Should Task State Influence an LLM Agent?

## Abstract
Long-horizon assigned work requires an LLM agent to track the state of a task: which steps are done, blocked, cancelled, or open to repetition. Agent systems either keep this state as text in the prompt and rely on the model to read that text, or move the state into a module that enforces it, and each system is evaluated as a whole, so no one knows how much reliability comes from the state being shown, told, or enforced. We fix the task rules, the model, and paired episodes and vary how strongly task state reaches the agent: a raw transcript, an exact checklist, per-turn directives from a state machine compiled from the brief and advanced only by execution receipts, or an enforcement gate on that machine that refuses state-violating actions; every episode is scored by exact payload matching against dynamic ground truth. Across three models, two reasoning regimes, and two domains, four findings hold without per-turn reasoning: displaying accurate state is unreliable, an unverified ledger the agent writes itself beats an accurate checklist it is shown, directives help in proportion to the model's obedience, and enforcement needs no obedience but is bounded by the correctness of its state and by the matcher that maps requests to steps; per-turn reasoning at a 235B agent compresses these separations without repairing the text rungs. The same gate, compiled from $τ^2$-bench's airline policy, raises a 235B agent's pass$^1$ from 0.39 to 0.54 and changes nothing for a 35B agent that rarely violates the policy; on PM-Bench, where acting turns on recognizing a cue rather than on state, showing the record is the best rung--matching or beating both gates and reversing the ledger-over-checklist finding--and enforcing the matcher's judgement drops a 35B agent below its raw transcript. Enforcement pays when failures are state-decidable and frequent, and hurts when the gate's judgement is wrong.

## Metadata
- **Published**: 2026-09-22T04:42:44Z
- **Authors**: Chenyu Zhang, Wonbin Kweon, Jiawei Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25686v1)