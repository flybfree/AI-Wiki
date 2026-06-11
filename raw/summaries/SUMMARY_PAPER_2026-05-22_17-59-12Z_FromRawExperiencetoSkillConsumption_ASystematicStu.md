---
title: From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills
url: http://arxiv.org/abs/2605.23899v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-22_17-59-12Z_FromRawExperiencetoSkillConsumption_ASystematicStu.md
generated_at: 2026-06-11 10:46
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how model‑generated skills derived from experience affect the performance of language agents across five task domains and finds that while such skills generally help, they can also cause negative transfer; extractor strength does not match consumer ability regardless of model size or baseline difficulty.  

## Key Takeaways
- Model‑generated skills improve average utility but introduce non‑trivial negative transfer between tasks.  
- Extractors and target agents do not behave uniformly when using these skills.  
- Skill usefulness is independent of the extractor’s scale or the underlying task strength.  

## Context  
The rapid rise of skill‑based prompting in large language models relies on distilling human experience into reusable procedures, yet existing research lacks a unified evaluation across generation, extraction, and consumption stages. This study fills that gap by providing a systematic framework.  

## Implications  
Practitioners can design meta‑skills that focus on features linked to real utility, reducing harmful side effects of skill reuse in AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.23899v1)
