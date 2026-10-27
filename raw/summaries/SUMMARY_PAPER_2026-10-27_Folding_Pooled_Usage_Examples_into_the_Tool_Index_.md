---
title: Folding Pooled Usage Examples into the Tool Index Lowers Retrieval of Unused Tools
url: http://arxiv.org/abs/2610.30867v2
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-22_07-45-24Z_FoldingPooledUsageExamplesintotheToolIndexLowersRe.md
generated_at: 2026-10-27 00:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how pooling usage examples into a shared tool-search index ("folding") affects the retrieval of tools that no agent in a multi-agent system has yet used. The author finds that folding sharply reduces the top-five retrieval rate of unused tools—dropping from 73% to 40% on StableToolBench—and proposes ZoE (Z-scores over Evidence), a scoring rule that separates documentation scores from usage scores so that tools without prior usage retain their documentation-based ranking. Across three catalogs and two embedding models, ZoE consistently outperforms a router-based alternative for retrieving unused tools.

## Key Takeaways
- Folding each pooled usage example into the search index as an extra entry for its associated tool helps tools that already have examples but significantly harms tools with no prior usage; on StableToolBench with the primary embedding model, the share of queries where a needed unused tool appears in the top five results falls from 73% to 40%, demonstrating a severe retrieval penalty for cold-start tools.
- ZoE (Z-scores over Evidence) addresses this by scoring a tool's documentation and its usage evidence separately, ensuring that a tool lacking usage examples keeps its full documentation score rather than being diluted by the absence of usage matches. This approach outperforms a router that reserves dedicated result slots for usage matches across all three tested catalogs and both embedding models.
- The author cautions that evaluations of pooled agent experience must report retrieval performance for tools no agent has used separately from aggregate averages, because averaging masks the systematic disadvantage that unused tools suffer under folding-based indexing, and a simpler constant-offset rule showed no detected difference from ZoE for unused tools in post hoc comparisons.

## Context
Modern AI agent systems increasingly rely on large tool catalogs and retrieval-based tool selection, where agents search documentation or usage logs to identify the right tool for a task. Multi-agent architectures that share a common tool index can accumulate pooled usage examples to improve tool discovery for frequently used tools. However, this paper highlights a critical blind spot in that paradigm: the very mechanism that helps popular tools can systematically suppress tools that have not yet been exercised, creating a feedback loop that entrenches existing tool usage and hinders exploration of new capabilities.

## Implications
For practitioners building multi-agent tool-use systems, this work warns that naive pooling of usage examples into a shared retrieval index can silently degrade the discoverability of new or rarely used tools, potentially locking agent teams into a narrow subset of available capabilities. The ZoE scoring rule and the recommendation to report unused-tool retrieval separately offer concrete guidance for designing fairer tool-retrieval pipelines and for evaluating agent benchmarks without masking cold-start failures, which is especially relevant as tool catalogs grow in enterprise and open-source agent frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30867v2)
