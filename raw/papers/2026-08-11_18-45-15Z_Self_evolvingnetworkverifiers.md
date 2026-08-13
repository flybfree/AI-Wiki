---
title: Self-evolving network verifiers
published: 2026-08-11T18:45:15Z
authors: Ioannis Protogeros, Tibor Schneider, Laurent Vanbever
url: http://arxiv.org/abs/2608.11340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-evolving network verifiers

## Abstract
Symbolic network verifiers can reason about correctness across vast spaces of routing inputs and failures, but only for the protocols and features an expert has encoded by hand. Creating and maintaining a faithful model of the control plane is both difficult and never-ending, since no written source specifies perfectly what a network does: vendor implementations deviate from the RFCs, and behaviour shifts with releases. The burden of constant upkeep ultimately keeps verification out of many networks that need it.   We argue that the model should instead evolve automatically to faithfully capture the actual network behaviour. To achieve that, we leverage the only source that specifies it unambiguously: the router software itself. In a counterexample-guided loop, a coding agent proposes extensions to the verifier's symbolic encoding, while a trusted oracle (e.g., emulated routers) supplies the ground-truth routing state. The agent iteratively refines the network model using each disagreement with the oracle.   As early evidence, a prototype of this system taught a 3,000-line SMT-based verifier three features it did not support: OSPF areas, BGP route reflection, and L3VPN over EVPN, converging autonomously on models that match the oracle, even noticing vendor-specific behaviour. Automating model growth shifts the hard problem from writing verification systems to systematically testing them; we propose a research agenda for trusting and harnessing automatically evolved verifiers.

## Metadata
- **Published**: 2026-08-11T18:45:15Z
- **Authors**: Ioannis Protogeros, Tibor Schneider, Laurent Vanbever
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11340v1)