---
title: Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills
url: http://arxiv.org/abs/2609.02749v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-49-41Z_Repo_To_Skill_DistillingGitHubRepositoriesIntoAI4A.md
generated_at: 2026-09-02 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces DisCo, a skill‑powered research agent that distills GitHub repositories into compact AI skills for autonomous agents. It creates both task‑agnostic libraries and task‑specific skills, enabling higher benchmark scores than agents without this knowledge distillation.  

## Key Takeaways  
- The AREX‑Skill Library contains 5,000+ verified skills distilled from 1,000 widely used ML repositories organized into 20 areas and 178 capability families.  
- Adding these skills to a GPT‑5.5‑backed research agent raises MLE‑bench performance by 134.3% while keeping the execution budget fixed.  
- The gains arise from providing distilled operational context that replaces manual knowledge discovery during each run.  

## Context  
Autonomous agents aim to perform end‑to‑end machine‑learning research but lack domain‑specific know‑how encoded in repositories, which are too large for direct use. This work bridges the gap by converting textual repository content into reusable skill objects.  

## Implications  
Practitioners can reuse these skills across diverse tasks without re‑implementing knowledge, accelerating AI research pipelines. The approach also demonstrates that lightweight skill integration can significantly boost benchmark results in a fixed compute budget.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02749v1)
