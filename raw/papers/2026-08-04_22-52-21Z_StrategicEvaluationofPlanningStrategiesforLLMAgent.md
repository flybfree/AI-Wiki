---
title: Strategic Evaluation of Planning Strategies for LLM Agents in Cyber-Physical Systems
published: 2026-08-04T22:52:21Z
authors: J. de Curtò, I. de Zarzà
url: http://arxiv.org/abs/2608.04265v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Strategic Evaluation of Planning Strategies for LLM Agents in Cyber-Physical Systems

## Abstract
Evaluations of LLM planning agents largely ask whether a task succeeds or a declared plan is followed. In strategic cyber-physical systems, a stronger question is whether the planning architecture remains appropriate after autonomous participants respond and physics constrains the outcome. We introduce a controlled, physics-grounded benchmark built around planning-induced control trajectories: the ordered planning operations and directives through which an execution architecture acts on other agents and the physical process. It implements predefined, sequential, hierarchical, and search executors in a smart-grid demand-response system with 40 heterogeneous prosumers and an independently simulated radial feeder. The LLM is bounded to typed policy declaration and short operator messages, while schedule construction, prosumer dynamics, and power flow remain explicit code. The protocol uses paired forced-mode counterfactuals, common random response draws, and event-level deadline feasibility. Three properties follow. Architecture materially changes outcomes: forced search is the oracle in all five baseline seeds. Execution fidelity needs more than mode agreement: objective substitution holds agreement at 1.0 while increasing voltage shortfall by 2.68x. A 144-scenario, 576-episode bank has feasible oracles from three of the four architectures. A prespecified stress-held-out ridge has mean regret 90.7 (95% interval [73.8, 108.6]) and no detectable value over fixed sequential; applying known deadline feasibility before quality prediction cuts regret to 29.0 and improves over fixed sequential by 61.1. An all-feasible ablation does not beat fixed search, localising the remaining challenge to within-feasible quality selection. A five-model extension separates stress-conditioned, state-blind, and invariant declarers; latency tails show that live feasibility should be treated probabilistically.

## Metadata
- **Published**: 2026-08-04T22:52:21Z
- **Authors**: J. de Curtò, I. de Zarzà
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04265v1)