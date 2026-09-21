---
title: Steering LLMs Responses Towards Moral Foundations on the Norwegian MFQ-30
url: http://arxiv.org/abs/2609.21636v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_11-25-22Z_SteeringLLMsResponsesTowardsMoralFoundationsontheN.md
generated_at: 2026-09-20 21:15
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates whether Large Language Models (LLMs) exhibit stable moral profiles and if these profiles can be systematically aligned with specific human demographics using psychometric instruments like the Norwegian Moral Foundations Questionnaire (MFQ-30). The study evaluates two distinct steering techniques—prompt-level persona adoption and activation-level ActAdd—to determine how effectively models can be moved toward a target population's mean.

## Key Takeaways
- The researchers used a sample of 1,282 Norwegian respondents to establish a baseline for moral profiles across six open-weight LLMs, testing whether these models could be steered toward specific cultural values.
- Prompt-level persona steering proved effective in narrowing the gap between model outputs and human data, achieving a 44-77% reduction in Mahalanobis distance compared to the target mean without using explicit distributional information from the sample.
- Activation-level intervention via ActAdd at a fixed mid-layer was found to be ineffective for steering specific moral foundations; instead of shifting the profile toward a target, it tended to flatten the model's output.
- The study identified a significant risk regarding "cognitive phantoms," where the same persona used to align models with human values also induced increased engagement or behaviors that were absent at baseline, suggesting that alignment efforts may have unintended side effects on model behavior.

## Context
As AI systems are increasingly deployed globally, understanding and aligning them with diverse cultural values is critical for safety and user experience. This paper contributes to the field by moving beyond general alignment toward specific, measurable psychometric evaluations of how models interpret and express moral foundations.

## Implications
For practitioners and researchers, these findings suggest that while persona-based steering is a viable path for cultural adaptation, it requires careful monitoring for unintended side effects like cognitive phantoms. The research highlights the complexity of "cultural alignment," showing that simply adjusting weights or prompts may not be sufficient to replicate nuanced human moral frameworks without creating artifacts in model behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21636v1)
