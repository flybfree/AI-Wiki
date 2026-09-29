---
title: Do Coding Agents Reuse Existing Code or Reinvent the Wheel?
url: http://arxiv.org/abs/2609.35357v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_15-04-27Z_DoCodingAgentsReuseExistingCodeorReinventtheWheel.md
generated_at: 2026-09-29 02:07
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces RepoReuse, a multi-turn benchmark designed to audit whether coding agents reuse existing code in real repositories or redundantly reinvent functionality during iterative development tasks. An extensive evaluation reveals that while functional pass rates remain stable, agents progressively fail to explore relevant repository code and their own workspace history, resulting in duplicated logic appearing in 50.8% of task chains by turn five and highlighting severe deficiencies invisible to standard correctness metrics.

## Key Takeaways
- The authors present RepoReuse, a scalable benchmark constructed through an automated pipeline that combines AST-based dependency graphs with execution-verified task synthesis to measure reuse rates, recall, and cross-turn structural redundancy in real repositories where workspaces accumulate across turns and requirements are revealed incrementally.
- Audits of 3,000 turns show that coding agents progressively stop exploring relevant repository code and increasingly ignore their own available history even when fully present in the workspace, leading to duplicated logic persisting in over half of task chains by turn five despite functional success.
- Standard pass rates barely move while redundancy accumulates, demonstrating that current evaluation frameworks are blind to structural inefficiencies and underscoring the urgent need for metrics that capture code reuse behavior alongside functional correctness to prevent unsupervised accumulation of technical debt.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35357v1)
