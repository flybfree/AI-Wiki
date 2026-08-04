---
title: CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits
url: http://arxiv.org/abs/2608.01805v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-13-00Z_CockpitHAT_Dependency_Graph_DrivenHierarchicalAttr.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CockpitHAT, a hierarchical attribution framework for embodied multi-agent cockpits that replaces positional windows with dependency-distance thresholds from interaction DAGs, integrates multi-channel evidence via an embodied adapter, and applies a safety-uplift to high-risk failures. On benchmark data it achieves higher agent-level and step-exact accuracies than prior text-only methods.

## Key Takeaways
- CockpitHAT replaces positional windows with dependency-distance thresholds from interaction DAGs, focusing on semantic proximity rather than fixed offsets.
- It integrates multi-channel evidence (dialogue, vehicle-state, environmental, memory) through an embodied adapter to capture richer context.
- The safety-uplift mechanism raises confidence-weighted analyst consensus for high-risk failures labeled ISO 26262 ASIL severity.

## Context
Current LLM multi-agent systems often produce text that is syntactically correct yet leads to unsafe physical actions in safety-critical environments like automotive cockpits, highlighting a need for attribution methods that consider dependency structure and real-world evidence. This work addresses that gap by building a framework tailored to embodied settings.

## Implications
The results demonstrate that dependency-aware, multi-channel, risk-calibrated attribution can significantly improve failure diagnosis accuracy, offering a practical approach for developers of autonomous vehicle systems who must balance performance with safety compliance. Practitioners can leverage CockpitHAT to refine model behavior and meet regulatory standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01805v1)
