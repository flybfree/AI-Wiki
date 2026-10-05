---
title: Dynamic LLM Routers are Often Misguided
published: 2026-10-02T03:42:28Z
authors: Sam Wang, Julia White, Sahibzada Allahyar, Dhruv Atreja, Urchade Zaratiana, Kelton Zhang
url: http://arxiv.org/abs/2610.02762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic LLM Routers are Often Misguided

## Abstract
Dynamic LLM routers promise to cut inference costs by sending each query to the cheapest model that can answer it correctly. We analyze six commercial routers across 14 settings on a diverse benchmark spanning eight task categories, finding that none of them outperforms a router that randomly selects between two well-chosen models at matched cost. Some underperform by more than 10 percentage points. We trace this gap to four patterns prevalent across routers: difficulty blindness, length reversal, semantic matching, and roster suboptimality. We show that the first three are what the standard objective rewards: cost-accuracy Pareto efficiency on realized costs favors escalating moderately hard queries over the hardest ones, shorter queries over longer ones, and routing by a query's source over its difficulty. We also argue that the two assumptions that would justify large rosters, model granularity and model specialization, do not hold empirically. We propose an alternative evaluation methodology that does not reward these patterns, and as a proof of concept, we design a simple two-model router that avoids all four. Nevertheless, its gain over random routing is limited, because a well-chosen roster leaves little to route.

## Metadata
- **Published**: 2026-10-02T03:42:28Z
- **Authors**: Sam Wang, Julia White, Sahibzada Allahyar, Dhruv Atreja, Urchade Zaratiana, Kelton Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02762v1)