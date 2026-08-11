---
title: Multi-agent discovery of practical quantum LDPC codes
url: http://arxiv.org/abs/2608.08996v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_01-32-34Z_Multi_agentdiscoveryofpracticalquantumLDPCcodes.md
generated_at: 2026-08-10 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a multi-agent framework that autonomously discovers practical quantum low-density parity-check (qLDPC) codes meeting stringent hardware constraints. Within the search space of binary CSS codes with block length up to 400 and weight at most 10, it identifies several high‑performing instances and demonstrates their resilience under depolarizing noise.

## Key Takeaways
- The framework discovers a [[288,16,18]] code at weight 7, a [[288,18,18]] code at weight 9, and a [[234,28,18]] code at weight 10, each achieving leading or competitive rate‑distance performance.  
- It uncovers structurally distinct high‑performing constructions such as a [[336,12,≤24]] candidate and a [[368,18,16]] code, both realized via balanced‑product codes with non‑normal subgroup actions.  
- All discovered codes satisfy the practical constraints \(n\le 400\) and overall weight \(w\le 10\), and they exhibit low logical failure rates when evaluated under a common BP‑OSD decoding protocol.

## Context
This work exemplifies how artificial‑intelligence agents can be employed to solve longstanding combinatorial design problems in quantum information science, moving beyond manual optimization toward systematic, scalable discovery. By integrating specialist proposal and review mechanisms with persistent memory, the approach mirrors real scientific workflows while generating executable code candidates.

## Implications
These finite‑length qLDPC candidates are directly relevant for experimental quantum communication experiments, offering hardware‑relevant designs that balance performance and practicality. Their successful integration into a closed‑loop search framework suggests a scalable model for future quantum code discovery efforts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08996v1)
