---
title: Personalization of Basic and Moral Values Guiding LLM-Controlled Assistant Robots
url: http://arxiv.org/abs/2611.18230v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-13_14-28-47Z_PersonalizationofBasicandMoralValuesGuidingLLM_Con.md
generated_at: 2026-11-16 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how personal assistant robots powered by large language models should be personalized to reflect the values of their individual users rather than a single aggregate human value profile. The authors administered three established psychometric instruments—the Schwartz Values Survey, the Portrait Values Questionnaire, and the Moral Foundations Questionnaire—in parallel self- and robot-targeted versions to 22 potential future users, capturing both their personal values and the values they would want a robot to embody. The study found that participants wanted their robot to score markedly lower on personal-focus values and higher on social-focus values, while moral profiles were nearly identical, and that prompting LLMs to act as robots produced only weak shifts toward the desired value profile.

## Key Takeaways
- Participants consistently wanted their assistant robot to embody a value profile that differed from their own: specifically, they wanted the robot to score lower on personal-focus values (such as self-direction and achievement) and higher on social-focus values (such as benevolence and universalism), suggesting users expect robots to prioritize communal and prosocial orientations over individualistic ones.
- Moral foundations profiles were nearly identical between what participants reported for themselves and what they desired in a robot, indicating that moral reasoning preferences are not a primary axis of personalization for assistant robots, unlike broader value dimensions.
- Benchmarking fifteen contemporary LLMs against the resulting value profiles revealed that prompting models to act as robots produced only weak shifts toward the desired profile, demonstrating that default model behavior and prompt engineering alone are insufficient substitutes for explicit, structured value personalization mechanisms.

## Context
As LLM-powered assistant robots move closer to deployment in everyday domestic and professional settings, the field of AI alignment has largely focused on steering a single model toward a broad aggregate of human values, treating personalization as a secondary concern. This paper addresses a critical gap by treating value personalization as a first-class design requirement for embodied agents, using validated psychometric instruments to quantify what individual users actually want their robots to embody. It bridges human-computer interaction research, moral psychology, and LLM evaluation in a way that prior alignment literature has not systematically attempted.

## Implications
For practitioners building LLM-controlled robots, this work signals that value personalization cannot be achieved through prompt engineering or default model behavior alone; explicit, structured mechanisms for encoding and applying individual user value profiles will be necessary. Industry developers should consider integrating validated psychometric assessment tools into onboarding workflows for assistant robots, and researchers should treat value personalization as a measurable, benchmarkable engineering problem rather than an abstract philosophical concern. The finding that moral profiles are nearly identical while broader value profiles diverge suggests that personalization efforts should focus on value priorities rather than moral reasoning frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.18230v1)
