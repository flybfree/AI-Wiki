---
title: SAGE: State-Grounded, Abstention-Aware Evaluation of Task-Oriented Dialogue Agents
published: 2026-08-31T22:14:52Z
authors: Rayan Khoury, Shih-Yao Lin, Pratyush Mishra
url: http://arxiv.org/abs/2609.00434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGE: State-Grounded, Abstention-Aware Evaluation of Task-Oriented Dialogue Agents

## Abstract
Evaluating task-oriented dialogue agents requires judging not merely whether a reply reads well but whether each turn advances the underlying workflow state correctly--a distinction conventional holistic LLM judges can miss because they evaluate the available context as a single unit and require one or more full-model calls per turn. We propose SAGE (State-Grounded Abstention-Aware Evaluation), which compiles a workflow specification and per-turn state diff into atomic, schema-grounded criteria and routes each through a cascade of symbolic and encoder/NLI verifiers that abstain rather than guess, aggregating criterion verdicts into a turn-level decision with an evidence trace. Its recommended operating point, SAGE-Core, decides 81--91% of criteria with only the compiler, symbolic rules, and on-device encoders--at zero paid LLM cost--while SAGE-LLM adds an optional focused-LLM fallback for open-class criteria. Across four slices spanning MultiWOZ, Schema-Guided Dialogue, and ABCD, no evaluated LLM-as-a-judge baseline--including a state-aware GPT-4.1 judge and cheaper GPT-4.1-mini variants--significantly exceeds SAGE-Core on any slice, even though the GPT-4.1 G-Eval judge costs $4.7--8.0 per 1,000 turns to SAGE-Core's $0. A two-annotator human audit (n=200, $κ$=0.94) confirms strong label fidelity on the transcript-visible failure classes--where, excluding the weak-salience IUV class, SAGE-Core is statistically tied with the strongest LLM judge--and honestly scopes ignored-user-value as a state-consistency signal with weak broad-human salience. We analyze construct-validity limits from injected failures and partial symbolic circularity.

## Metadata
- **Published**: 2026-08-31T22:14:52Z
- **Authors**: Rayan Khoury, Shih-Yao Lin, Pratyush Mishra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00434v1)