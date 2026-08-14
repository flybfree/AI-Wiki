---
title: SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents
url: http://arxiv.org/abs/2608.13173v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_12-41-03Z_SkillShapley_Boundary_AdaptiveShapleyValuationforS.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SkillShapley, a Shapley value‑based framework for attributing the contribution of individual steps within language agent skills. By modeling skill‑step attribution as a combinatorial evaluation problem and exploiting empirical insights about reward cliffs and additive step interactions, SkillShapley efficiently identifies high‑ or low‑value steps in benchmark tasks.

## Key Takeaways
- The authors treat each skill step’s impact on task performance as a marginal contribution that can be estimated via Shapley values across diverse coalitions of steps.  
- Their two‑phase approach first discovers informative coalitional regions and then adaptively samples new coalitions to reuse marginal evidence, reducing computational cost while preserving accuracy.  
- Experiments on SkillsBench skills show SkillShapley reliably distinguishes valuable from redundant steps, offering a systematic method for skill design.

## Context
Agent skills are essential for enabling language models to perform complex procedural tasks such as coding or document extraction. Current attribution methods either rely on manual labeling or simple trace analysis, lacking quantitative insight into step importance. This work bridges that gap by applying advanced combinatorial optimization techniques to real‑world skill evaluation.

## Implications
For practitioners developing LLM agents, SkillShapley provides a data‑driven way to refine and optimize skill specifications without extensive human intervention. The method can be integrated into automated skill creation pipelines, leading to more robust and efficient agent workflows across industries that rely on task automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13173v1)
