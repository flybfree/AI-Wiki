---
title: Causal Structure is Inducible but Functionally Decoupled: The Routing/Readout Boundary of a Typed Mechanism Library
published: 2026-08-12T08:10:01Z
authors: Xining Xun
url: http://arxiv.org/abs/2608.11767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal Structure is Inducible but Functionally Decoupled: The Routing/Readout Boundary of a Typed Mechanism Library

## Abstract
When a language model answers an interventional question, the computation it must perform depends on the type of evidence the query requires. We report a decoupling in how a transformer organizes causal knowledge: slot-by-type structure induced by type-level supervision organizes routing, yet remains functionally decoupled from answer readout. We establish this with a typed mechanism library -- discrete mechanism slots partitioned by evidence type, auditable at the state level -- on a causal-world benchmark with exact interventional ground truth, under a frozen protocol, at two scales (22.6M and 125M). Four preregistered findings. (i) Origin. Slot-by-type organization is induced by type-level supervision: absent in architecturally identical unsupervised controls, not buyable by content-free gating labels, and statistically attributable to the supervision signal, replicating at 125M under a powered preregistered protocol (all nine cells passed). (ii) Boundary. The induced structure is a typed routing index with a sharp routing/readout boundary: slot codes scaffold routing but do not drive answer readout ($|Δ\hat{y}| \le 3.4\times10^{-6}$, zero collateral, three seeds, stable across a 5.6x scale window) -- we therefore make no behavioral-editability claim. (iii) Cost. The structure is free: LM quality matches a parameter-matched monolith within 0.0082 nats. (iv) Trust. The library state is exactly local under edit and bit-exactly revertible -- 250 single-edit and 1,000 stacked reverts per seed, zero failures. We further find that the unsupervised null itself moves with scale, so comparisons reusing a null calibrated at one scale may be confounded at another. Every claim is tied to a preregistered, machine-checkable criterion archived before the data it governs; the full audit trail, including one criterion we failed and how the frozen protocol handled it, is released as an appendix.

## Metadata
- **Published**: 2026-08-12T08:10:01Z
- **Authors**: Xining Xun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11767v1)