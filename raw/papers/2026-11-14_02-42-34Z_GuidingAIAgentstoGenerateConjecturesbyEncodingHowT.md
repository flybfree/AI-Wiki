---
title: Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another
published: 2026-11-14T02:42:34Z
authors: Hita Kambhamettu, Daniel Krashen, Lyle Ungar
url: http://arxiv.org/abs/2611.19108v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another

## Abstract
Recently, LLMs have been making headlines, and headway, in mathematical research. Much of this work focuses on proving existing open conjectures. Deciding what to prove is harder and less studied, because of the lack of a clear criterion for what makes a conjecture worth pursuing. We present a method for conjecture generation that builds on the observation that mathematical theorems build on one another: new theorems can modify the setting or hypotheses of earlier theorems, strengthen their conclusions, or extend their scope. We encode these relationships in a new kind of graph, the Theorem Evolution Graph (TEG), which we instantiate as an online search method for LLM agents. An agent builds a TEG in two steps: (1) identifying relevant theorems from papers found by following citations backward and forward from a seed paper; and (2) comparing those theorems to record how one builds on another. LLM judges and an expert mathematician preferred TEG-generated conjectures over those from an unconstrained baseline. LLM judges favored TEG conjectures for significance, ambition, and insight, and favored baseline conjectures for plausibility. Ablations suggest a benefit from constructing and using a TEG even when the available papers are fixed.

## Metadata
- **Published**: 2026-11-14T02:42:34Z
- **Authors**: Hita Kambhamettu, Daniel Krashen, Lyle Ungar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.19108v1)