---
title: Separate Field Scoring Protects Unused Tools When Agents Pool Tool-Use Experience
url: http://arxiv.org/abs/2610.30867v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_07-45-24Z_SeparateFieldScoringProtectsUnusedToolsWhenAgentsP.md
generated_at: 2026-10-22 22:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how pooling tool-use experience across multiple agents in a shared tool catalog affects tool retrieval performance, specifically measuring the impact on both tools that have usage examples and held-out tools that have never been used. The author introduces SYNAPSE, a method that scores usage examples as a separate field rather than appending them to tool descriptions, demonstrating that this separation protects held-out tools from retrieval degradation while preserving gains for tools with usage. On StableToolBench, SYNAPSE achieves a held-out Hit@5 of 0.785 compared to 0.683 for a router-based approach that reserves slots for usage, with the advantage holding across all three tested catalogs and both embedders.

## Key Takeaways
- Adding usage examples to the index as extra entries for already-used tools raises Hit@5 for those tools but significantly lowers it for held-out tools that no agent has ever used, with large margins observed on two of three catalogs and with both embedders tested. This reveals a critical failure mode in naive pooling strategies where shared experience actively harms tools that have not yet been encountered.
- SYNAPSE, which scores usage as its own separate field rather than mixing it into tool descriptions, protects held-out tools effectively. The protection persisted even when each tool's usage text was replaced with other tools' text, and a constant score offset for tools with usage produced similar held-out Hit@5 in most settings, suggesting the mechanism is about structural separation rather than content-specific information.
- The gain for tools with usage genuinely requires usage text that is about the correct tool, whereas the router approach retains more of the gain on labeled queries on TOUCAN with both embedders and on ToolRet with one embedder. Splitting usage among ten simulated agents shows pooling helps exactly as much as giving one agent the same records, confirming that the benefit scales with total pooled data regardless of distribution across agents.

## Context
As large language model agents increasingly rely on tool-calling capabilities, the retrieval of appropriate tools from large catalogs has become a bottleneck for agent performance. Multi-agent systems and shared tool registries are becoming common in production deployments, where agents learn from each other's tool-use experiences to improve future retrieval. This paper addresses a previously underexplored risk in that paradigm: the assumption that pooling experience is universally beneficial. By rigorously separating held-out from used tools in evaluation, the work exposes how naive integration of usage data can systematically disadvantage tools that have not yet been used, a scenario that is common in evolving tool ecosystems where new tools are continuously added.

## Implications
For practitioners building multi-agent tool-use systems, this work provides a concrete architectural guideline: usage data should be scored in a separate field rather than appended to tool descriptions, as demonstrated by SYNAPSE. This protects newly added or rarely used tools from being crowded out of retrieval results, which is critical for maintaining catalog coverage as tool inventories grow. The finding that the better choice between SYNAPSE and a slot-reserving router depends on the workload means that system designers must evaluate both approaches against their specific query distributions rather than assuming a single best strategy. The result that splitting usage among ten agents performs identically to concentrating it in one agent also simplifies deployment decisions for distributed agent architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30867v1)
