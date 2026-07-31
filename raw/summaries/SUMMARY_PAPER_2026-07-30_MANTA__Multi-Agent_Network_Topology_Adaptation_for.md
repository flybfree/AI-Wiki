---
title: MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems
url: http://arxiv.org/abs/2607.28527v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-01-27Z_MANTA_Multi_AgentNetworkTopologyAdaptationforSelf_.md
generated_at: 2026-07-30 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MANTA, a framework that enables communication topologies in multi-agent systems to adapt automatically during inference. By monitoring collaboration traces and applying bounded structural updates, MANTA improves task performance without altering the interface or agent budget. Evaluated on five benchmarks, MANTA achieves the highest average score of 74.0, surpassing baselines by up to 5.8 points.

## Key Takeaways
- MANTA initializes a task-conditioned topology from prior structural experience before execution, providing a starting point for adaptation.
- The system monitors collaboration traces and applies bounded updates that can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface.
- On PlanCraft, MANTA outperforms all baselines, demonstrating that inference-time self-improvement can extend to the architecture of collaboration itself.

## Context
Current multi-agent systems rely on fixed or offline‑optimized communication topologies, limiting their ability to respond to dynamic tasks. The need for real‑time adaptation arises as agents must handle a wide range of problem domains where static structures become suboptimal. MANTA addresses this gap by integrating self‑evolving network design into the inference pipeline.

## Implications
MANTA’s approach can lead to more robust and efficient multi‑agent collaborations, reducing latency and improving outcomes across diverse applications such as robotics, autonomous planning, and knowledge work. Practitioners may adopt similar feedback‑driven topology adaptation techniques to create systems that continuously optimize their interaction patterns without manual redesign.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28527v1)
