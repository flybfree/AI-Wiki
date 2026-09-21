---
title: Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents
published: 2026-09-18T16:57:14Z
authors: Hafsa Akbar, Daniel Platnick, Marjan Alirezaie, Hossein Rahnama
url: http://arxiv.org/abs/2609.21997v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents

## Abstract
LLM agents in social simulation revise their opinions implicitly, in context: how open an agent is to persuasion can neither be specified nor verified, and collective outcomes inherit the model's training prior. We introduce Bayesian Chronicle Agents (BCA), a minimal belief layer separating \emph{what} an agent believes from \emph{how} it speaks. Each stance is a probability, updated by one Bayesian step per utterance heard. A single prior-strength parameter $κ$ encodes stubbornness, modeled after its role in Friedkin--Johnsen (FJ) opinion dynamics. We then sweep this parameter to yield three canonical regimes of opinion dynamics on demand (consensus, persistent disagreement, committed-minority influence), with persistent disagreement matching the FJ closed-form fixed points at $R^2\!=\!0.93$--$0.99$. We further show that prescribed $κ$ remains recoverable after the language round-trip, with perfect rank-order recovery across all four models. Explicit belief also makes simulation auditable: the layer surfaces systematic per-model stance biases that end-to-end simulation would silently absorb.

## Metadata
- **Published**: 2026-09-18T16:57:14Z
- **Authors**: Hafsa Akbar, Daniel Platnick, Marjan Alirezaie, Hossein Rahnama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21997v1)