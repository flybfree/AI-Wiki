---
title: Rethinking Automated Program Repair: The Impact of Bug Complexity, Fault Localization, and LLM Cost-efficiency
url: http://arxiv.org/abs/2608.14065v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_08-23-25Z_RethinkingAutomatedProgramRepair_TheImpactofBugCom.md
generated_at: 2026-08-16 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper conducts a comprehensive empirical analysis of LLM‑based Automated Program Repair, examining how repair performance varies with bug complexity, fault localization accuracy, reasoning settings, and computational cost. The study finds that while higher‑cost LLMs can sometimes fix more complex bugs, they do not always provide the best overall cost‑efficiency, highlighting a nontrivial trade‑off between effectiveness and expense.

## Key Takeaways
- Imprecise fault localization substantially widens the performance gap between APR techniques.  
- Higher‑cost LLMs and stronger reasoning settings do not consistently yield better cost‑efficiency, revealing a clear trade‑off between repair effectiveness and computational cost.  
- GPT‑5 repairs 7 and 39 more complex bugs than DeepSeek‑V4‑pro and DeepSeek‑V3.2, respectively; the total repair cost of DeepSeek‑V3.2 shows the best cost‑efficiency performance.

## Context
Automated Program Repair using large language models is an active research area, yet most prior work focuses on overall repair success rates without dissecting the influence of bug complexity or fault localization precision. This paper addresses that gap by employing a multi‑dimensional experimental framework to quantify these factors in real systems.

## Implications
The findings suggest that low‑cost LLMs can achieve satisfactory repair outcomes for many moderately complex bugs, guiding practitioners toward cost‑effective strategies. Practitioners should prioritize accurate fault localization and consider the specific trade‑off between LLM size and computational expense when selecting APR tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14065v1)
