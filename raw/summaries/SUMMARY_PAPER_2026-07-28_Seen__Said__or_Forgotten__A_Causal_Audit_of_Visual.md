---
title: Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns
url: http://arxiv.org/abs/2607.25467v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-59-57Z_Seen_Said_orForgotten_ACausalAuditofVisualKVMemory.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when visual knowledge can be safely discarded in a multimodal assistant and introduces the Causal Visual Memory Audit (CVMA) as a test framework to measure this forgetting. Experiments on VisDial and ConvBench show that current attention mechanisms often rank future‑useful regions worse than random, revealing hidden failures in memory management.

## Key Takeaways
- Attention can prioritize irrelevant visual evidence for later turns even when marginal utility is high, indicating poor ranking of future usefulness.
- The audit reveals a second escape route where assistant text replaces image KV for facts already verbalized but not reliably for unstated facts, showing that forgetting depends on whether the fact will be restated verbally.
- Safe forgetting correlates with low future visual dependence or explicit verbalization rather than low current attention.

## Context
Stateful multimodal assistants must balance memory storage and computational efficiency. This work highlights a gap between theoretical assumptions about attention and empirical performance in long‑term knowledge retention across conversation turns.

## Implications
For developers, the findings suggest that designing systems to forget only when visual evidence is no longer needed or can be rephrased verbally could improve both accuracy and resource use. Practitioners should evaluate attention mechanisms with causal audits rather than relying on aggregate scores alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25467v1)
