---
title: G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs
url: http://arxiv.org/abs/2608.19964v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_12-35-12Z_G_MARK_GroundedMulti_AgentReasoningforCooperativeD.md
generated_at: 2026-08-20 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces G-MARK, a framework that transforms cooperative object observations into provenance‑aware knowledge graphs to preserve detailed information about which agent saw an object, its visibility state, and any conflicts. The approach improves occlusion reasoning accuracy by 42.2%, reduces control‑selection error by 13.1%, while keeping trajectory planning comparable with a communication payload 25.6 times smaller.

## Key Takeaways
- G-MARK creates explicit knowledge graphs that retain object hypotheses, source attribution, ego versus partner visibility, uncertainty, conflicts, spatial relations, and planning context.  
- The framework derives lightweight task heads from these KGs for object reasoning, motion prediction, control selection, and trajectory forecasting.  
- Compared to baselines, G-MARK achieves a 42.2 % boost in occlusion reasoning accuracy, a 13.1 % reduction in control‑selection error, and maintains comparable trajectory planning performance with much smaller structured data.

## Context
In autonomous driving, partial observability forces systems to rely on shared perception among connected vehicles. Existing methods often compress this multi‑agent evidence into latent features or hidden states, obscuring provenance and leading to suboptimal decisions. G-MARK addresses this by making the reasoning process transparent through knowledge graphs.

## Implications
The transparency of provenance information can improve safety and reliability in cooperative driving scenarios. Practitioners will benefit from reduced communication overhead while gaining clearer insight into conflicting observations, fostering more robust and trustworthy autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19964v1)
