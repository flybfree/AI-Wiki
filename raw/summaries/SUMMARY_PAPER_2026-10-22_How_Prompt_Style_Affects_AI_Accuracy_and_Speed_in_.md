---
title: How Prompt Style Affects AI Accuracy and Speed in Competitive Programming
url: http://arxiv.org/abs/2610.30223v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_17-11-18Z_HowPromptStyleAffectsAIAccuracyandSpeedinCompetiti.md
generated_at: 2026-10-22 22:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This exploratory study investigates how different prompt styles influence both accuracy and runtime speed when GPT-5.5 is used to solve competitive programming problems from the International Olympiad in Informatics. The authors tested one prompt per each of nine distinct styles across three accuracy-focused tasks and two NP-hard speed tasks, finding that no single prompt style consistently outperformed others. Instead, the optimal prompt depended on the task type and the statistical measure used to evaluate results, and the study also provides a descriptive comparison against human IOI contestant performance.

## Key Takeaways
- No universal best prompt exists: the strongest prompt style varied depending on whether the task prioritized correctness or runtime speed, and whether performance was assessed using mean or median scores. This means practitioners must match prompt design to their specific objective rather than relying on a single "best practice" prompt template.
- Outlier runs heavily distort mean-based evaluations: many apparent differences in mean scores across prompt styles were driven by a small number of outlier runs, meaning that evaluating prompting strategies through a single aggregate metric can mask substantial variability in effectiveness and lead to misleading conclusions about which style is superior.
- AI performance relative to humans is mixed and task-dependent: when descriptively compared to human IOI contestants working under different conditions, GPT-5.5 exceeded the average contestant on one accuracy task but fell short on the other two, and the study does not claim strict superiority or inferiority, highlighting that AI capabilities in competitive programming remain uneven across problem types.

## Context
Large language models have become widely adopted tools for competitive programming, yet prior research on prompt engineering for this domain has focused almost exclusively on accuracy metrics and has not examined runtime speed or benchmarked results against human performance. This paper fills that gap by extending the evaluation framework to include computational speed on NP-hard problems and by situating AI outputs alongside human contestant outcomes from the IOI. It represents one of the first attempts to provide a multi-dimensional, human-grounded assessment of how prompt phrasing shapes practical AI performance in algorithmic problem-solving.

## Implications
For practitioners building AI-assisted coding pipelines, the findings argue against adopting a single fixed prompt template and instead encourage task-aware prompt design, where the style is selected based on whether the goal is correctness, speed, or a balance of both. For the broader AI research community, the study underscores the importance of using robust statistical methods—such as median-based reporting and outlier analysis—when benchmarking prompting strategies, since mean-based comparisons can produce unreliable rankings. Industry teams deploying LLMs for competitive programming or algorithmic coding challenges should treat prompt style as a tunable parameter calibrated to specific problem classes rather than a solved engineering problem.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30223v1)
