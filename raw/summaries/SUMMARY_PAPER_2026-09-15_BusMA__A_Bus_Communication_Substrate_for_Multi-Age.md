---
title: BusMA: A Bus Communication Substrate for Multi-Agent Systems
url: http://arxiv.org/abs/2609.15054v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_05-19-55Z_BusMA_ABusCommunicationSubstrateforMulti_AgentSyst.md
generated_at: 2026-09-15 03:22
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces BusMA, a novel communication framework for multi-agent systems designed to overcome the autonomy restrictions and error propagation issues inherent in traditional Hierarchical Manager-Worker and Router-based Message Passing architectures. By leveraging a shared bus channel with four distinct communication intents and a coordinating Chair agent, BusMA enables direct peer-to-peer interaction among worker agents. Extensive evaluations across diverse reasoning and retrieval tasks demonstrate that BusMA consistently outperforms existing state-of-the-art multi-agent paradigms.

## Key Takeaways
- BusMA replaces rigid hierarchical or router-based structures with a decentralized bus architecture, allowing any agent to directly address peers through a shared channel while maintaining local memory and tool access.
- The framework introduces four specialized communication intents—discussion, challenge, guidance, and request for explanation—to enable fine-grained, purpose-driven interactions that reduce misrouting and enhance collaborative problem-solving.
- A dedicated Chair agent continuously monitors the shared memory to orchestrate workflows and drive convergence, with empirical results showing consistent performance gains over HMW

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15054v1)
