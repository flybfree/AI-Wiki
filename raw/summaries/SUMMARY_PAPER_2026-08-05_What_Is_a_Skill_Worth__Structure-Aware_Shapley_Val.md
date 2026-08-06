---
title: What Is a Skill Worth? Structure-Aware Shapley Valuation of Agent Skills
url: http://arxiv.org/abs/2608.04562v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_07-56-26Z_WhatIsaSkillWorth_Structure_AwareShapleyValuationo.md
generated_at: 2026-08-05 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes SkillSV, a structure‑aware Shapley valuation framework that assigns credit to the internal units of an agent’s skill such as rules, examples, scripts, and heuristics. By modeling dependencies, hierarchy, and context cost, SkillSV evaluates only valid counterfactual skills on held‑out tasks and recovers unit interactions while preserving aggregate skill lift.

## Key Takeaways  
- Skill valuation is distinct from data or prompt‑span valuation because skill units are structured, have internal dependencies, and consume limited prompt space.  
- SkillSV uses paired deletion with length‑neutral padding to separate content value from context cost, enabling a rollout‑budgeted estimator for noisy agent evaluations.  
- On four benchmarks the method recovers unit interactions, preserves the total skill lift, and provides guidance for safe pruning and compression.

## Context  
Automated feedback loops increasingly optimize agents by treating skills as atomic units, yet their internal composition is rarely quantified. This work addresses a gap in AI research where structured artifacts are undervalued, highlighting the need for methods that respect hierarchical dependencies and context constraints.

## Implications  
Practitioners can leverage SkillSV to prioritize which skill components to retain or compress during model fine‑tuning, leading to more efficient and explainable agents. The framework also offers a principled way to audit skill contributions, supporting responsible AI development where accountability matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04562v1)
