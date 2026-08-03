---
title: Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts
published: 2026-07-31T15:03:09Z
authors: Sergey Salishev
url: http://arxiv.org/abs/2607.29496v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts

## Abstract
We study transcript management for fixed, finite-precision causal Transformers. A transcript is partitioned into channels of bounded blocks. Each transition consults a fixed visible suffix and may append one block, leaving the model, weights, and token protocol unchanged. The operation $P_c:=\PopContext(c)$ deletes the newest block on channel $c$ and exposes its predecessor.   We model the layer by the Transcript-Managed Transducer $\TMTn{k}$: one finite controller, $k$ channels, and per-round actions from stay, push, and pop under a caller-driven status map. Fixed visible windows encode as finite symbols. The pop-free Restricted Transcript-Managed Transducer $\RTMTn{k}$ is the standard append-only layer and, for every fixed $k$, realizes exactly the deterministic finite-state transductions. The same holds for every fixed finite agent population under a monotone protocol that appends, routes, and copies visible blocks.   Admitting $\{P_c\}_{c=1}^k$ restores pop. Newest-first, a pop-enabled channel is a stack; compiling to the Hopcroft--Ullman presentation transfers the classical hierarchy: $\DCFL$ for $k=1$ and $\RE$ for every $k\ge2$. Orchestrated one-channel agents match one controller with $k$ channels, so two pop-enabled transcripts---in one agent or two---suffice for universality. Simulation costs and invariance to fixed block size and visible radius are stated. The bounds fix precision, alphabets, blocks, visibility, controller state, and population; growing exact context, hidden-block access, writable stores, and unbounded \textbf{Spawn} add further state.

## Metadata
- **Published**: 2026-07-31T15:03:09Z
- **Authors**: Sergey Salishev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29496v1)