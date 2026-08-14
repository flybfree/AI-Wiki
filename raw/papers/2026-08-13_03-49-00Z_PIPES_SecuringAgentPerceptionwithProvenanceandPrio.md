---
title: PIPES: Securing Agent Perception with Provenance and Priors
published: 2026-08-13T03:49:00Z
authors: Sanjay Kariyappa, Severin Klingler, G. Edward Suh
url: http://arxiv.org/abs/2608.12789v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PIPES: Securing Agent Perception with Provenance and Priors

## Abstract
Tool-using agents consume external data from sources with different levels of trust, yet tool responses rarely identify who produced each component or what it should convey. We show that this gap enables state-corruption attacks, in which attacker-controlled content makes environmental claims beyond the informational authority of its response component and corrupts the agent's perceived environment, making the resulting action appear justified to existing guardrails. We introduce PIPES (Provenance-Informed, Prior-Enforced Screening), which screens response units using semantic priors and source provenance. PIPES uses static field contracts when schemas provide stable expectations, and conditions screening of open-ended content on the pre-response trajectory and trusted provenance metadata. It marks units that violate their semantic prior or the provenance hierarchy; deployments may remove, warn, block, or escalate detected violations. We instantiate atomic removal and evaluate PIPES against adaptive PAIR-style attacks. Across the three VitaBench and three AgentDyn splits with Gemma 4 31B IT as the target agent, PIPES reduces average attack success from 84.7% to 2.3%, while preserving average benign utility (92.5% with PIPES versus 90.6% without defense).

## Metadata
- **Published**: 2026-08-13T03:49:00Z
- **Authors**: Sanjay Kariyappa, Severin Klingler, G. Edward Suh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12789v1)