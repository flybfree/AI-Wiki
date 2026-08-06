---
title: EA-Graph: Artifact-Anchored Verification Memory for Coding Agents under Upstream Drift
url: http://arxiv.org/abs/2608.04278v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_23-13-32Z_EA_Graph_Artifact_AnchoredVerificationMemoryforCod.md
generated_at: 2026-08-05 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EA‑Graph, an artifact‑anchored memory system for coding agents that stores verification claims linked to specific repository artifacts rather than prose notes. It evaluates this memory against prose notes and no persistent memory across multiple sessions with drift scenarios. The results show EA‑Graph improves provability judgments especially for smaller models.

## Key Takeaways
- EA‑Graph represents artifacts at sub‑path granularity, resolves aliases to leaf definitions, and anchors each claim to the content used to establish it, keeping evidence strength separate from freshness.
- When replacement content is unavailable, the claim becomes unprovable rather than guessed.
- In the Haiku round artifact‑anchored memory outperformed prose notes and no persistent memory in all seven worlds with p = 0.0156.

## Context
Coding agents often rely on provenance information to verify program behavior across sessions, but upstream changes can break this link without explicit updates. Memory systems that preserve claim provenance are needed to maintain reliable verification as code evolves. This work addresses the gap by providing a structured memory that tracks artifact‑level evidence.

## Implications
For practitioners developing long‑running coding agents, EA‑Graph offers a way to keep verification claims grounded in immutable artifacts, reducing false positives after drift. The approach may help narrow capability gaps between model tiers but does not guarantee cross‑model equivalence or efficiency gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04278v1)
