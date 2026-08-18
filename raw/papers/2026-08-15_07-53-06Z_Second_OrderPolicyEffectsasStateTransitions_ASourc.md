---
title: Second-Order Policy Effects as State Transitions: A Source-Linked Benchmark for Policy Simulation
published: 2026-08-15T07:53:06Z
authors: Wesley Shu
url: http://arxiv.org/abs/2608.15101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Second-Order Policy Effects as State Transitions: A Source-Linked Benchmark for Policy Simulation

## Abstract
Policy evaluation often estimates direct benefits and costs while treating the institutional environment as fixed. In practice, a policy changes the system it enters: actors adapt, enforcement capacity shifts, burdens move, and new equilibria form around capture, gaming, compliance theater, irreversibility, and repair costs. We formalize this as second-order policy-effect prediction and present a source-linked benchmark for policy simulation. The benchmark contains 96 named public-policy cases across eight domains and four balanced action classes: implement, modify, pilot, and block. Each case includes source locators and state variables for benefit, capture, gaming, burden shift, instability, uncertainty, irreversibility, distributional risk, and implementation capacity. The runner regenerates method outputs and aggregate results from the case table, and the simulator never reads the expert action target. We report a protocol-based transition-channel audit with recall, precision, F1-style efficiency, and selective top-channel stress diagnostics, so universal channel coverage is not mistaken for field validation. The side-effect simulator achieves mean policy-effect quality of 0.945, compared with 0.838 for the risk-register baseline and 0.879 for the causal-loop baseline. Its advantage is concentrated in side-effect recall and aggregate transition scoring; it does not dominate the best structured baselines on exact policy-action choice. The evidence remains benchmark-based, but supports a bounded claim: transition-state variables make policy simulators more sensitive to downstream institutional effects.

## Metadata
- **Published**: 2026-08-15T07:53:06Z
- **Authors**: Wesley Shu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15101v1)