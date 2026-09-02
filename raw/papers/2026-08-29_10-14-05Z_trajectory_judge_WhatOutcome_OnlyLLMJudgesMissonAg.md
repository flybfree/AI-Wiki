---
title: trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories
published: 2026-08-29T10:14:05Z
authors: Hadi Mohammadi
url: http://arxiv.org/abs/2609.00038v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories

## Abstract
Outcome-only evaluation is the production default for LLM agents: show a judge the request and the final reply and ask whether it was handled well. The metric is structurally blind to an agent that reaches the right answer the wrong way. We measure that blind spot where ground truth is known by construction: a deterministic tool-using support-desk environment, a scripted oracle policy that always solves it, and a fault injector that breaks exactly one thing at a known step, stratifying faults by whether the customer-visible outcome survived (silent) or not (loud). Five judges (programmatic rules, outcome-only, step-rubric at two model sizes, and a self-consistency ensemble) are scored on detection, step localisation, fault typing, calibration, and cost over 400 trajectories. The outcome-only judge catches 84% of loud faults but 45% of silent ones while flagging 33% of correct trajectories; a step-rubric judge reaches 77% silent recall with zero false alarms at 3x the cost. No judge reads the final reply: an invented promise appended to an otherwise perfect trajectory evades the rules entirely and the step judge 82% of the time, and self-consistency triples cost while improving nothing. We argue that judge evaluations must stratify recall by outcome survival, and release the environment, the injector, all raw verdicts, and an analysis pipeline that rebuilds every number offline.

## Metadata
- **Published**: 2026-08-29T10:14:05Z
- **Authors**: Hadi Mohammadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00038v1)