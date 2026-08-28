---
title: RuleWeaver: Benchmarking Rule-Centered Scenario Reasoning for Large Language Models
published: 2026-08-27T09:05:11Z
authors: Bohan Yu, Shi-Yang Li, Pengfei Cao, Jun Zhao, Kang Liu
url: http://arxiv.org/abs/2608.26832v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RuleWeaver: Benchmarking Rule-Centered Scenario Reasoning for Large Language Models

## Abstract
Large language models (LLMs) are increasingly applied to specialized domains, where effective use of domain expertise often requires reasoning over complex rules in concrete scenarios. However, existing benchmarks only partially evaluate this capability, as they either focus on output-level instruction constraints or overlook the distinct roles that rules play in scenario reasoning. To address these gaps, this paper introduces RuleWeaver, a benchmark construction framework for evaluating rule-centered scenario reasoning. RuleWeaver starts from corpus-derived IF-THEN Meta Rules, progressively augments them into complex rules, and composes these rules into rule-centered scenario QA instances. Beyond final-answer correctness, RuleWeaver further supports process-level evaluation through rubric-based answer quality, rule recall, and rule precision. Experiments on 11 representative LLMs show that current models still struggle with complex rule-centered scenario reasoning, with even the best-performing model achieving only around 50% of the maximum rubric score. We make our code and dataset available here: https://github.com/SharkSpicy-NLP/RuleWeaver.

## Metadata
- **Published**: 2026-08-27T09:05:11Z
- **Authors**: Bohan Yu, Shi-Yang Li, Pengfei Cao, Jun Zhao, Kang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26832v1)