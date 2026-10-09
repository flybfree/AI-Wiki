---
title: LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models
published: 2026-10-08T05:01:30Z
authors: Surya Shetty, Ulisses Braga-Neto
url: http://arxiv.org/abs/2610.11253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models

## Abstract
Large language model agents are being increasingly deployed as autonomous scientists, designing experiments and inferring mechanistic world models with minimal human oversight. Yet identifiability is often overlooked: when a plateau is reached, the agent needs to know whether it is not yet capable enough or the model simply is not identifiable from the data, in which case no amount of further experimentation of the same kind can help. We propose the Identifiability-Driven Experimental Agent (LLM-IDEA) for closed-loop discovery with an identifiability engine that returns a three-way plateau verdict: capability limit, resolvable within the design class, or certified exhausted. On ODEBench, 60 of the 62 systems with free constants are identifiable at round 0; the RC circuit is certified exhausted for every experiment that protocol can run, and a harvesting model is resolvable by one added initial condition. The identifiability engine reproduces known verdicts on Lotka-Volterra, Van der Pol, Lorenz, and a pharmacokinetic model, where it recommends the intravenous arm pharmacologists use, and it ranks the depth scorer of our own benchmark last among four observation designs. On the DiscoverPhysics benchmark, it finds two public worlds whose explanation rubric rewards a distinction no legal experiment can make, and every model there with accurate trajectories failed the explanation grade (15 of 15, against 5 of 9 in identifiable worlds, p = 0.012). On the Alien Universe, a two-body testbed we propose in which a force law switches between a provably non-identifiable and an identifiable protocol, LLM-IDEA on the identifiable protocol reaches discovery depth at least three on 8/8 seeds versus 1/8 without it. An autonomous discovery agent can thus compute, rather than guess, whether a plateau calls for more search, a better experiment of the same kind, or a different kind of experiment.

## Metadata
- **Published**: 2026-10-08T05:01:30Z
- **Authors**: Surya Shetty, Ulisses Braga-Neto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11253v1)