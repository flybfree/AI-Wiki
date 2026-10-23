---
title: Diagnosing Personalization Failures in Mobile GUI Agents
url: http://arxiv.org/abs/2610.30573v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_01-04-24Z_DiagnosingPersonalizationFailuresinMobileGUIAgents.md
generated_at: 2026-10-22 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PrefDiag-Bench, a diagnostic benchmark designed to evaluate how well personalized GUI agents incorporate user preferences into their sequential decision-making over changing mobile interface states. The authors categorize preferences into five types and build a stage-wise diagnostic framework with 1,664 probes to trace when and where personalization failures occur. Evaluating eleven GUI agent systems reveals that even the best-performing model achieves only 47.17% success on Process preferences, exposing fundamental gaps in how agents select relevant evidence from user history and recognize when preferences should influence execution.

## Key Takeaways
- The benchmark decomposes personalization failures into two distinct dimensions: HOW preferences alter execution strategy (categorized into five preference types) and WHEN they should take effect along the interaction trajectory. This stage-wise diagnostic approach with 1,664 probes moves beyond binary task-success metrics to pinpoint exactly where agents break down in personalized workflows.
- Even top-performing agents like Seed-2.0-Pro achieve only 47.17% on Process preferences under explicit user profiles, and agents struggle particularly with Ranking and Process preferences. Performance on preference-personalized tasks is substantially lower than on non-personalized tasks, revealing that high general completion rates mask critical personalization failures.
- Two core capability bottlenecks are identified: agents fail at selecting relevant evidence from user history and fail at recognizing the correct execution stage at which a preference should take effect. Controlled interventions that explicitly supply relevant evidence improve end-to-end task success by up to 7.06%, suggesting that retrieval and timing recognition are separable, addressable failure modes.

## Context
Mobile GUI agents are rapidly advancing toward practical deployment in app automation, accessibility assistance, and personal digital assistants. However, the field has largely evaluated agents on generic task completion, leaving a critical gap in understanding how agents handle individualized user preferences that must modulate behavior across multi-step interactions. PrefDiag-Bench addresses this gap by providing a structured, fine-grained evaluation methodology that mirrors real-world personalization demands, including both explicit user profiles and implicit behavioral memory logs. This work sits at the intersection of agentic AI, user modeling, and human-computer interaction, pushing evaluation beyond aggregate success rates toward mechanistic understanding of failure modes.

## Implications
For practitioners building personalized mobile assistants, this work demonstrates that current agent architectures are not yet reliable for preference-sensitive workflows, particularly those involving ranking or process-level customization. The identified bottlenecks in evidence selection and timing recognition offer concrete targets for architectural improvements, such as improved memory retrieval modules and stage-aware planning components. For the broader AI research community, PrefDiag-Bench provides a reproducible, open-source evaluation framework that can guide the development of more trustworthy personalized agents and inform safety and reliability standards before these systems reach production deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30573v1)
