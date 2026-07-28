---
title: Multi-primitive in-memory computing for Monte Carlo tree search
published: 2026-07-24T19:17:37Z
authors: Tergel Molom-Ochir, Benjamin F. Morris, Yintao He, Archit Gajjar, Giacomo Pedretti, Hai Helen Li, Yiran Chen, Jim Ignowski, Aishwarya Natarajan
url: http://arxiv.org/abs/2607.22869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-primitive in-memory computing for Monte Carlo tree search

## Abstract
Monte Carlo tree search (MCTS) enables artificial intelligence (AI) decision-making, but requires 55-300 W on conventional processors, limiting edge deployment. In-memory computing (IMC) is energy-efficient on regular workloads but has been considered incompatible with irregular multi-phase algorithms. We introduce phase-to-primitive decomposition, which reformulates each algorithmic phase as a hardware-native IMC primitive. Applied to MCTS, selection, expansion, rollout and backpropagation map to content-addressable memory, combinational logic, a resistive random-access memory (RRAM) crossbar and static random-access memory, keeping search on chip. At 22 nm with fabricated RRAM-array parameters, IMC-MCTS consumes ~60 mW for 9x9 Go, achieving 96x energy efficiency over a central processing unit (CPU) and 65x-2,059x over an H100 graphics processing unit (GPU). It reaches a European Go Federation rating within sample-size uncertainty of open-source Go engines (Pachi-UCT and Michi-C). The same substrate runs eight applications across four AI domains.

## Metadata
- **Published**: 2026-07-24T19:17:37Z
- **Authors**: Tergel Molom-Ochir, Benjamin F. Morris, Yintao He, Archit Gajjar, Giacomo Pedretti, Hai Helen Li, Yiran Chen, Jim Ignowski, Aishwarya Natarajan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22869v1)