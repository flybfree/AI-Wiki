---
title: Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents
url: http://arxiv.org/abs/2608.01913v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_08-46-48Z_DiagnosingSearchBehaviorandFailureModesinLong_Hori.md
generated_at: 2026-08-03 23:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how deep search agents allocate effort and whether that effort translates into better answers, using trajectory-level analysis of long‑horizon search behavior. By separating evidence retrieval from its effective use, the authors identify two failure modes: gaps where needed evidence is never found and gaps where retrieved evidence is misused. Experiments on BrowseComp-Plus show a weak correlation between search effort and answer quality.

## Key Takeaways
- The quality of cumulative retrieved evidence, especially early‑stage recall, predicts answer accuracy more than the number of searches or context length consumed.  
- Agents often continue searching after useful evidence appears, generating a long tail of low‑yield retrieval steps that do not improve performance.  
- Exploratory reformulations can be helpful, but top agents issue far fewer redundant queries.

## Context
Deep research systems rely on iterative query issuing to gather supporting documents, yet existing evaluations focus on final answer metrics without probing intermediate behavior. Understanding the breakdown between retrieval and utilization is essential for diagnosing why such systems sometimes fail despite high effort.

## Implications
Practitioners should prioritize stronger query formulation and more effective evidence selection to avoid unnecessary searches. Implementing stopping criteria based on sufficient retrieved evidence can reduce wasted computation, leading to faster, higher‑quality answers in real‑world research agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01913v1)
