---
title: Keep Your Receipts: Trustworthy Cleanup of Agent-Built Knowledge Graphs
url: http://arxiv.org/abs/2610.17719v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_04-51-28Z_KeepYourReceipts_TrustworthyCleanupofAgent_BuiltKn.md
generated_at: 2026-10-14 00:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PolyGraph, a method for trustworthy cleanup of agent-built knowledge graphs by having the graph constructor emit "receipts"—alternative bundles of source evidence claimed sufficient to justify each artifact—at creation time. Cleanup then reduces to deterministic set arithmetic over these receipts rather than requiring model calls, and a re-derivation audit validates receipt trustworthiness. The approach cuts contaminated queries from 32.2% down to 0.4–0.8% while preserving 99.8–100% of the recall a perfect maintainer would achieve.

## Key Takeaways
- Existing deployed pipelines that delete only directly extracted facts barely help: under a real retraction, contaminated queries drop only from 32.2% to 28.0%, and under predicate revocation they change nothing. Rebuilding the graph is also not a viable repair strategy because a sampling constructor produces wildly different outputs across runs—two builds of the same 300-document corpus differ in 29,475 artifacts, which is five times the 6,248 artifacts affected by removing 61 retracted documents.
- PolyGraph's core mechanism is asking the constructor to emit receipts at creation time: for every artifact, alternative bundles of source evidence, each claimed sufficient on its own. Cleanup then becomes pure set arithmetic over these receipts with zero model calls, making maintenance deterministic and auditable. A re-derivation audit—deleting cited evidence and testing whether the constructor still produces the artifact—validates whether a receipt is trustworthy.
- Receipt shape matters critically for trustworthiness. Merge receipts, each backing one narrow claim, agree with re-derivation 68% and 85% of the time. Summary receipts elicited per sentence but stored as a flat list for the whole text are wrong about two-thirds of the time, almost always by retaining dead content. Switching to one receipt per sentence achieves 100% and 88% faithfulness and allows cleanup to preserve 33 of 35 touched summaries. These results hold across a second oracle model, a claim-blind prompt, ten additional deletions, a second domain, and a second constructor.

## Context
As LLM-based agents increasingly rely on knowledge graphs as persistent memory, the construction side has become tractable while the maintenance side remains unsolved. This paper addresses a fundamental gap in the agent-memory lifecycle: what happens to downstream artifacts—entity merges, entailed edges, community summaries—when upstream sources are retracted, overruled, or erased. It reframes knowledge-graph maintenance from a model-dependent, heuristic problem into a deterministic bookkeeping problem, which is a significant conceptual shift for the agent-memory research community.

## Implications
For practitioners deploying agent systems at scale, PolyGraph offers a path to reliable knowledge-graph maintenance without additional inference cost, since cleanup is set arithmetic over receipts rather than model calls. The finding that receipt granularity (per-sentence vs. per-document) determines trustworthiness provides a concrete design guideline for any system that builds structured memory from language models. The near-perfect recall preservation alongside a 40-fold reduction in contaminated queries suggests that trustworthy cleanup is achievable in production pipelines, potentially enabling agents to operate over long-lived, evolving knowledge bases without accumulating stale or contradictory information.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17719v1)
