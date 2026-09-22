---
title: From Capability to Assurance in Autonomous Penetration-Testing Harnesses: A Framework and Reference Implementation
published: 2026-09-19T00:37:49Z
authors: Joas Antonio dos Santos Barbosa
url: http://arxiv.org/abs/2609.22664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Capability to Assurance in Autonomous Penetration-Testing Harnesses: A Framework and Reference Implementation

## Abstract
Research on large language model agents for penetration testing is evaluated almost entirely by capability: whether the agent captures a flag or reproduces a proof of concept. That metric suits a benchmark but is silent on the properties that decide whether an autonomous agent can be used in an authorized engagement: whether a reported finding is true, whether the agent stayed inside its authorized scope, and whether an operator can audit what it did. We call these assurance properties and argue that they belong to the harness, the runtime wrapping the model, and can be enforced in code. This paper makes three contributions. First, we define a framework of five assurance properties (evidence grounding, non destructive claim reduction, computed severity, enforced authorization, and tamper evident accountability), each with a formal model and an explicit acceptance test, connected to prior work in capability based security, tamper evident logging, and software provenance. Second, we position representative systems (PentestGPT, the Cochise reference harness, MAPTA, and the trajectory judge PentestJudge) within the framework using published coding criteria, and identify a consistent assurance gap. Third, we study one open source implementation, NeuroSploit, pinned to an exact commit, reporting its architecture, its complexity cost, and a content addressed artifact bundle from a run against a public deliberately vulnerable target. We execute the deterministic authorization and audit acceptance tests directly and find and report a real enforcement gap, which we reflect by scoring both properties as partial. We therefore claim an initial existence argument that the properties are realizable together, not a comparative performance result, and we specify the multi target, ablation, and adversarial evaluation protocol required to turn the framework obligations into measurements.

## Metadata
- **Published**: 2026-09-19T00:37:49Z
- **Authors**: Joas Antonio dos Santos Barbosa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.22664v1)