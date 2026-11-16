---
title: Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents
url: http://arxiv.org/abs/2611.16627v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-12_10-59-40Z_Folio_RecoverableMulti_ResolutionContextFoldingfor.md
generated_at: 2026-11-15 21:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Folio is a context management system for long-horizon language agents that replaces model-written summarization with a programmatic, multi-resolution folding mechanism. It maintains three linked levels of history—short turn notes, event manifests, and full source records—and folds older turns into coarser views without requiring a model to reread and rewrite the history. On 75 LOCA-bench tasks, Folio solved 66 tasks compared to 54 for a model-compaction baseline and 49–59 for Claude Code, Codex, and SoL-Pi, while operating at roughly half the wall-clock time and 2.4 times lower cost.

## Key Takeaways
- Folio eliminates the costly model-written compaction step by structuring history at write time into three linked levels: an L1 short turn note embedded in the model's ordinary reply, an L2 event manifest of every tool call written by the runtime, and L3 captured source records. Because these views already exist, the runtime can fold context programmatically by selecting coarser views for older turns, removing the need for a model to reread and rewrite the history it replaces.
- The fold prints handles that index L2 and L3, enabling recovery tools to access bounded pages, compute over full text in files, and maintain findings in a persistent dossier. This means the agent can still reach the evidence it needs even after older turns have been folded, preserving recoverability rather than irreversibly discarding information.
- Performance benchmarks demonstrate substantial gains: Folio solves 66 of 75 LOCA-bench tasks versus 54 for the same runtime using model-written compaction, completes tasks in about half the working time, costs 2.4 times less, and each fold takes a median of only 0.6 seconds. The fold trigger prices an explicit landing point that includes the retained budget, making compaction decisions deterministic and cost-aware rather than heuristic.

## Context
Long-horizon language agents that chain many tool calls and replies inevitably exceed their context windows, and the dominant mitigation—having a model summarize and rewrite prior history—introduces latency, cost, and information loss at every compaction step. Folio addresses this by treating context management as a runtime engineering problem rather than a model-generation problem, structuring information at capture time so that folding becomes a cheap, deterministic selection among pre-existing views. This positions the work at the intersection of agent orchestration, memory management, and cost optimization, offering a concrete alternative to the summarization-based approaches used by Claude Code, Codex, and similar production agents.

## Implications
For practitioners building production agents, Folio demonstrates that context management can be made deterministic, fast, and dramatically cheaper by shifting the burden from model inference to runtime bookkeeping, which is critical for scaling agent deployments where compaction cost and latency compound across thousands of tasks. The recoverable-handle design also suggests a path toward agents that retain full auditability of their reasoning history, which matters for compliance, debugging, and trust in high-stakes autonomous systems. The benchmark results signal that programmatic folding can outperform model-written compaction on task completion, not just cost, challenging the assumption that a model must rewrite history to preserve agent performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.16627v1)
