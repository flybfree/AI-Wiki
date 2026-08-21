---
title: Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees
url: http://arxiv.org/abs/2608.19993v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_13-08-17Z_OptimalSkillSelectionforLLMAgentswithProvableBicri.md
generated_at: 2026-08-20 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of selecting reusable skill documents for LLM agents within a limited token budget, showing that independent scoring and greedy packing lead to suboptimal or wasteful selections. The authors formulate skill selection as an optimization problem maximizing benefit under a hard token constraint and introduce Best Prefix Selection (BPS), which achieves a provable bicriteria (1‑1/e, 1) approximation with optimal coefficient.

## Key Takeaways
- Skill selection is modeled as a submodular maximization minus context penalty, turning the task into an optimization problem that balances benefit and token cost.  
- BPS provides a polynomial‑time algorithm with a bicriteria (1‑1/e, 1) approximation guarantee, which is optimal in polynomial time for this specific problem.  
- On a contamination‑controlled BigCodeBench variant, BPS yields a task success rate of 0.73, far exceeding baselines that achieve only 0.20–0.52 while using 28 % fewer tokens.

## Context
LLM agents increasingly rely on reusable skill documents to perform tasks efficiently, but the current selection methods ignore both token budget constraints and the cumulative impact of redundant or poorly chosen skills. This gap limits performance and inflates computational costs in real‑world deployments where context windows are scarce.

## Implications
The proposed bicriteria guarantee offers a principled way to allocate limited tokens toward high‑impact skills, improving task success while conserving resources. Practitioners can adopt BPS to design more reliable skill routers that balance relevance and cost, leading to faster, cheaper, and higher‑performing LLM agents in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19993v1)
