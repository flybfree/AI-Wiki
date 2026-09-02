---
title: Creative Generation via Multi-Agent Debate: Does Debate Suppress Diversity?
url: http://arxiv.org/abs/2609.00683v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_04-00-42Z_CreativeGenerationviaMulti_AgentDebate_DoesDebateS.md
generated_at: 2026-09-01 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether Multi-Agent Debate suppresses diversity in creative generation tasks. It finds that MAD's convergence-driven design reduces output variety across runs, and proposes Creative-MAD with two interventions to preserve diversity while keeping quality high.

## Key Takeaways
- The theoretical analysis shows that preserving diversity among agents within each debate session is necessary for achieving diverse outputs across independent runs.
- Cognitive Lens Assignment anchors each agent to a distinct persistent cognitive mode to counter identity drift.
- Embedding-based Peer Selection limits each agent's context to its most semantically distant peers, reducing majority pull.

## Context
Creative generation in AI relies on both quality and diversity, yet existing methods often favor one over the other. This work addresses the trade‑off by showing that debate frameworks can unintentionally homogenize outputs across independent generations.

## Implications
For practitioners, Creative-MAD offers a practical way to maintain high‑quality diverse results without sacrificing performance. The approach could be adopted in narrative generation, scientific ideation, and any domain where varied ideas are valuable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00683v1)
