---
title: ToolRosetta: Surface-Form Invariance of Tool-Call Guards
published: 2026-10-16T17:14:13Z
authors: Hasan Demirkiran, Jens Ernstberger
url: http://arxiv.org/abs/2610.24055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolRosetta: Surface-Form Invariance of Tool-Call Guards

## Abstract
Step-level guards for tool-using agents are evaluated on tidy JSON tool calls, but deployed coding agents act through execute_bash and execute_code tools whose payloads are strings. We introduce ToolRosetta, which re-renders every candidate action in the AgentDojo and AgentHarm splits of TS-Bench as a Python call, as a shell command, and without the agent's rationale. The renderings are produced by code and verified by round-trip parsing, so the user request, the history, the label and the action's effect stay fixed while only the surface form changes. Across eleven guards with two placebo controls, frontier and strong open-weight guards are stable: no frontier error rate moves by more than 3.4 points. Four of five specialized agent guards are not: under the shell form their false-positive rates rise by 21 to 47 points on AgentDojo, and TS-Guard's by 38 points on its own home benchmark, blocking between a third and nine in ten benign actions; the fifth, StepGuard, does not move. A small open guard drifts five points more permissive. Removing the agent's rationale moves most guards whose input carries it, in guard-specific directions. A request-blind control on one guard shows that the rationale is where intent is read from. A parser that restores the canonical call in front of the guard removes the effect for these renderings, by construction. Benchmark accuracy on JSON calls does not predict a guard's operating point behind a code-acting agent.

## Metadata
- **Published**: 2026-10-16T17:14:13Z
- **Authors**: Hasan Demirkiran, Jens Ernstberger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24055v1)