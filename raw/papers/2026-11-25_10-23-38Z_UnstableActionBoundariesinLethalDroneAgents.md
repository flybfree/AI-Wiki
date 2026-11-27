---
title: Unstable Action Boundaries in Lethal Drone Agents
published: 2026-11-25T10:23:38Z
authors: Jacques Dumora, André-Louis Rochet, Simon Roburin
url: http://arxiv.org/abs/2611.34121v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unstable Action Boundaries in Lethal Drone Agents

## Abstract
Tool-using large language model (LLM) agents raise safety risks that are not captured by text-only refusal behavior, especially when tools can trigger high-impact actions. This concern is salient in military settings, where autonomous weapons raise the possibility of delegating force decisions to software agents. In this work, we study whether a drone agent's action boundary is stable under changes to the target descriptor. We evaluate recent and popular LLMs in a simulated perception-action pipeline over real-world drone imagery, where models can localize requested targets and invoke a simulated lethal tool. We find two concerning failure modes. First, some LLM agents invoke the lethal tool for ordinary generic descriptors such as \emph{people}, requiring no jailbreak at all. Second, an agent that initially appears conservative under protected descriptors can become unsafe under a simple semantic target shift.

## Metadata
- **Published**: 2026-11-25T10:23:38Z
- **Authors**: Jacques Dumora, André-Louis Rochet, Simon Roburin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.34121v1)