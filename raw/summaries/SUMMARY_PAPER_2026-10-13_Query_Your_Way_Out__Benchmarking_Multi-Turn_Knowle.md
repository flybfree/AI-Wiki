---
title: Query Your Way Out: Benchmarking Multi-Turn Knowledge Reasoning through Generalized Puzzle Solving
url: http://arxiv.org/abs/2610.16133v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-12_03-50-39Z_QueryYourWayOut_BenchmarkingMulti_TurnKnowledgeRea.md
generated_at: 2026-10-13 21:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Active Probing Benchmark (APB), a novel evaluation framework that generalizes puzzle-solving into an interactive multi-turn reasoning task designed to test whether Large Language Models can actively probe for information and infer specialized domain knowledge across 960 target concepts spanning eight academic domains. The central finding is counter-intuitive: most open-source reasoning models significantly underperform their standard instruction-tuned counterparts in interactive settings, revealing a critical failure in leveraging procedural reasoning to access and apply specialized knowledge when information must be acquired incrementally through dialogue.

## Key Takeaways
- The Active Probing Benchmark (APB) reframes concept identification as an interactive reasoning task, requiring models to acquire information through multi-turn active probing and inference rather than relying on static, single-turn prompts. It covers 960 target concepts of specialized difficulty across eight diverse academic domains, making it substantially broader than existing puzzle benchmarks that focus on narrow environments with rigid mechanics and tightly constrained solution targets.
- A striking empirical finding is that most open-source reasoning models significantly underperform their standard instruction counterparts in this interactive setting. This suggests that the procedural reasoning capabilities emphasized in reasoning-tuned models do not translate effectively into interactive environments where information must be actively sought and integrated across multiple turns, exposing a fundamental gap between static reasoning ability and interactive knowledge application.
- APB provides a scalable pipeline for generating benchmarks that probe knowledge reasoning under interaction across diverse settings, offering a methodological template for constructing evaluation tasks that go beyond fixed-input benchmarks and instead test a model's capacity for strategic information gathering, hypothesis testing, and iterative inference under partial information.

## Context
This work sits at the intersection of LLM evaluation methodology, interactive reasoning, and knowledge assessment. Existing benchmarks for reasoning and puzzle-solving tend to operate in closed, static environments where all necessary information is provided upfront, which fails to capture the dynamic, information-gathering behaviors that characterize real-world problem solving. By casting concept identification as an interactive probing task, APB addresses a growing concern in the AI research community: that current evaluation paradigms overestimate model capabilities by removing the very challenges—partial information, sequential decision-making, and knowledge retrieval under uncertainty—that distinguish genuinely capable reasoning systems from pattern-matching systems.

## Implications
For practitioners and model developers, the finding that reasoning-tuned models underperform instruction-tuned models in interactive settings challenges the prevailing assumption that enhanced procedural reasoning automatically improves real-world performance, suggesting that training strategies must explicitly account for interactive information-gathering behaviors rather than optimizing solely for static chain-of-thought outputs. For the broader AI evaluation landscape, APB's scalable generation pipeline offers a template for constructing benchmarks that stress-test models under realistic interactive conditions, potentially reshaping how model capabilities are assessed before deployment in applications requiring iterative user interaction, such as tutoring systems, research assistants, and domain-specific advisory tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16133v1)
