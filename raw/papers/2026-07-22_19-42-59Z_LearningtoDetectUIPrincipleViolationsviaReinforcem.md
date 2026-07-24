---
title: Learning to Detect UI Principle Violations via Reinforcement Learning
published: 2026-07-22T19:42:59Z
authors: Nishi Mehta, Swathi Alse, Himani Kumavat, Yue Yu, Pratik Jayarao
url: http://arxiv.org/abs/2607.20690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Detect UI Principle Violations via Reinforcement Learning

## Abstract
Small language models and coding agents increasingly generate web front-end code, yet their outputs are typically evaluated primarily for functional correctness. A generated interface may compile, render, and pass unit tests while still violating established interface quality principles, including accessibility barriers, deceptive design patterns, poor visual hierarchy, and excessive decision complexity. Existing auditing approaches face a trade-off between cost, coverage, and scalability: expert human review provides rich judgment but is slow and expensive; frontier vision-language models offer broader reasoning capabilities but remain costly to deploy at scale; and rule-based tools such as axe-core and Lighthouse are inexpensive but primarily capture mechanically checkable accessibility issues.   We investigate whether a lightweight vision-language model can serve as an effective critic for generated interfaces. We unify 19 interface-quality principles from three complementary sources of HCI knowledge: WCAG 2.2 accessibility standards, deceptive design taxonomies, and established theories of perception, cognition, and interaction. To train this critic, we construct a verified dataset of approximately 10,000 generated web pages by synthetically injecting known violations into clean, LLM-generated Tailwind pages.   Continued reinforcement learning on a 4B vision-language model improves micro-F1 from 36\% to 84\%, with 13 of 19 principles exceeding 80\% F1. The resulting critic can audit generated interfaces, filter low-quality interface training data, and provide a reward signal for design-aware code generation. We release our data-generation recipe and injection/verification prompts to support reproducible evaluation and future work on scalable interface-quality assessment.

## Metadata
- **Published**: 2026-07-22T19:42:59Z
- **Authors**: Nishi Mehta, Swathi Alse, Himani Kumavat, Yue Yu, Pratik Jayarao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20690v1)