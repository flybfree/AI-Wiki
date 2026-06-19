---
title: "2026 06 11 15 09 32Z Towardinstructions As Code Understandingthe Summary"
date: 2026-06-11
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-11_15-09-32Z_TowardInstructions_as_Code_UnderstandingtheImpacto.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-11 21:00
Source: 2026-06-11_15-09-32Z_TowardInstructions_as_Code_UnderstandingtheImpacto.md
Model: None

---


## Summary  
This paper investigates how instruction files affect the performance of AI‑agents when they submit pull requests (Agentic‑PRs) in software projects. By treating these instructions as a form of “Instructions‑as‑Code,” the authors aim to understand whether clearer, more structured guidance improves merge rates, reduces code churn, and shortens merge time. Their analysis reveals that instruction files can have both positive and negative impacts depending on their length and organization.

## Key Contributions  
-[Finding 1] Specifying instructions for AI‑agents does not uniformly improve outcomes; some projects see a 27.7 % increase in merge rate, while others experience a 26.35 % decrease.  
-[Finding 2] The effect is consistent across multiple dimensions: code churn (number of modified files), effort to merge (merge time and comment count).  
-[Finding 3] Projects that benefit from instruction files tend to have longer, well‑structured instructions with many sections and subsections.

## Methodology  
The authors examined 15,549 agentic PRs collected from 148 projects in the AIDev dataset. They compared each project’s performance before and after instruction file creation across three metrics: merge rate (percentage of merges), code churn (files changed), and effort to merge (merge time and comment volume). By analyzing these pre‑ and post‑instruction snapshots, they identified patterns linking instruction characteristics to PR success.

## Results  
The main experimental results show a mixed impact: 27.7 % of projects improved their merge rate by at least 20 %, while an equal proportion declined it. Moreover, the authors observed that longer instruction files—characterized by higher section and subsection counts—correlate with higher merge rates. However, there is no guarantee that more sections always lead to better outcomes; poorly structured or overly verbose instructions can hinder agents.

## Significance  
These findings underscore that treating instruction files as a software‑engineering artifact (“Instructions‑as‑Code”) requires careful design and validation. Practitioners need guidance on how to formulate effective, concise, and well‑organized instructions to maximize AI‑agent collaboration without introducing unnecessary complexity or risk.

## Related Concepts  
AI agents (e.g., GitHub Copilot), pull requests, instruction files, code churn, merge rate, AIDev dataset, Instructions‑as‑Code.
