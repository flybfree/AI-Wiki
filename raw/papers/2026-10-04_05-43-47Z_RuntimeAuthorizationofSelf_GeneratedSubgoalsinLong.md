---
title: Runtime Authorization of Self-Generated Subgoals in Long-Horizon Tool-Using AI Agents
published: 2026-10-04T05:43:47Z
authors: Genliang Zhu, Chu Wang
url: http://arxiv.org/abs/2610.04975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Runtime Authorization of Self-Generated Subgoals in Long-Horizon Tool-Using AI Agents

## Abstract
Long-horizon tool-using AI agents create subgoals, replan, delegate work, and compose sibling results. Per-tool permission checks cannot establish that a changing goal graph remains within the principal-approved task. We address this authorization gap in a finite structured domain with one principal and one authorization root. Each proposed goal-graph mutation carries a version-bound witness that its continuation traces, resources, obligations, invariants, and closing condition refine the active root contract; every protected effect is rechecked at an atomic commit boundary. Free-form goal text supplies no authority.   We prove trace-policy and modeled forbidden-state preservation under explicit mediation, abstraction, freshness, and atomicity assumptions, plus conditional root-success preservation, a separation result for memoryless allowlists, exact finite-domain decidability, and universal-safety monotonicity under sound abstraction refinement. An executable model explores 340 states and 419 transitions. Across 96 matched cases covering 25 structural schemas, the complete mechanism commits zero forbidden states in 48 drifted cases and completes all 48 benign counterparts. Two public upstream runtime paths execute 258 native dispatches across 32 cases, with every case-level decision and receipt chain matching. A frozen host-local study covers 129 synthetic one-factor-at-a-time cells, all matching fixed decisions and reasons. A history-aware continuation comparator blocks every modeled bad trace prefix but commits all operations in 11 cases whose violations lie in typed resources, freshness, or explicit-join evidence outside its trace projection. Within the registered structured domains, runtime authorization preserves useful replanning while preventing self-generated subgoals from becoming a source of new authority.

## Metadata
- **Published**: 2026-10-04T05:43:47Z
- **Authors**: Genliang Zhu, Chu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04975v1)