---
title: LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions
url: http://arxiv.org/abs/2611.34328v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_13-09-34Z_LUDIUS_ABenchmarkforEmbodiedSocialIntelligenceinEv.md
generated_at: 2026-11-26 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LUDIUS is a benchmark for evaluating how vision-language models exercise social intelligence in everyday human-robot interactions, specifically by interpreting a situation from the perspectives of the people involved and deciding when and how to act. It organizes evaluation around 15 social intelligence skills drawn from social psychology, sociology, and cognitive science, presented as six editions of episodes spanning one simulated week. The authors find that frontier models, and even a smaller model finetuned on generated social-interaction data, perform worst when they must reason about what a resident saw or heard earlier, reconcile competing interests, or fulfill a request within safety constraints and household rules.

## Key Takeaways
- LUDIUS spans 15 social intelligence skills across six editions: three editions each cover all 15 skills in a different household, while the other three focus on multi-person interactions, safety, and context-specific norms, respectively.
- A common evaluation harness supplies each model with the robot's camera views and residents' reactions, retrieves relevant interaction history, and converts the model's tool calls into robot verbal responses and actions, enabling comparison of frontier models and a smaller model finetuned on author-generated social-interaction data.
- Models tend to degrade when they must reason about earlier resident observations, reconcile competing interests, or satisfy requests under safety constraints and household rules, indicating that social judgment remains a bottleneck rather than a solved capability.

## Context
Embodied AI and human-robot interaction increasingly rely on vision-language models to ground language in physical settings, but many benchmarks emphasize perception, planning, or task completion rather than social judgment. LUDIUS matters because it targets the social layer of everyday interaction, where a robot must infer others' perspectives, norms, and constraints instead of merely executing commands. Its design pipeline translates abstract social-intelligence skills into context-specific judgments and observable robot behavior, making the approach relevant beyond the home setting.

## Implications
For researchers, LUDIUS provides a common harness and a reusable design pipeline for measuring and improving social reasoning in embodied agents. For practitioners deploying robots in homes or shared spaces, it surfaces concrete failure modes around memory, competing interests, and safety or norm compliance that should be tested before deployment. The framework also offers a template for constructing social-intelligence benchmarks in other contexts, not only domestic ones.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34328v1)
