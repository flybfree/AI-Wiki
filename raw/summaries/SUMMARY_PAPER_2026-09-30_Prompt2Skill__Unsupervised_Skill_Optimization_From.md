---
title: Prompt2Skill: Unsupervised Skill Optimization From Natural Language Instructions
url: http://arxiv.org/abs/2609.38593v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_21-53-56Z_Prompt2Skill_UnsupervisedSkillOptimizationFromNatu.md
generated_at: 2026-09-30 20:48
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces Prompt2Skill, a novel framework that automatically generates and optimizes external skills for Large Language Models using only natural-language task descriptions, eliminating the need for expert-authored artifacts or curated in-distribution training data. By deriving task specifications, synthesizing datasets, and employing a closed-loop reflective editing process, the system creates specialized skills tailored to specific model behaviors. Experimental results demonstrate that Prompt2Skill consistently surpasses direct prompting baselines across diverse domains such as question answering and mathematical reasoning, yielding an average performance improvement of 10.8 points on both open-source and frontier models.

## Key Takeaways
- Prompt2Skill operates entirely unsupervised by leveraging natural language instructions to build skills, overcoming the dependency on expensive expert curation and the lack of in-distribution training datasets that hinders previous automated optimization methods relying on reflection techniques.
- The framework employs a multi-stage pipeline where it first extracts task specifications from prompts, then autonomously discovers or synthesizes relevant datasets to facilitate learning, and finally refines the skill through an iterative closed-loop of reflective editing that adapts to the model's specific failure modes.
- Across four distinct domains including reading comprehension

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38593v1)
