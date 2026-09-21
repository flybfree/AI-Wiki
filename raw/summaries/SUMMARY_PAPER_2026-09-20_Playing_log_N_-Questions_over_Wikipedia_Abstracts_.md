---
title: Playing log(N)-Questions over Wikipedia Abstracts: How Per-Round Errors Compound Under Information Asymmetry
url: http://arxiv.org/abs/2609.19113v2
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-16_17-41-12Z_Playinglog_N__QuestionsoverWikipediaAbstracts_HowP.md
generated_at: 2026-09-20 20:19
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research evaluates frontier language models using a two-agent $\log_2 N$-Questions game to measure how effectively they communicate across an information asymmetry. The study finds that win rates decay geometrically as the number-of-rounds increases, primarily because errors compound over time rather than individual questions becoming progressively harder for the model to answer correctly.

## Key Takeaways
- The research identifies a specific pattern of failure where win rates decay according to $p^{\log_2 N}$ with a success probability of approximately 0.93 per round. This indicates that even high-performing models struggle to maintain perfect accuracy over long chains because the probability of success drops significantly as more rounds are added.
- Analysis shows that per-round failure rates remain relatively flat across different horizons, suggesting that the challenge is not an increase in individual question difficulty but rather the cumulative risk of a single error occurring. Once an error occurs, it becomes undetectable and unrecoverable within the two-agent structure, leading to a total breakdown of the communication chain.
- The study concludes that communication reliability—rather than inference compute or reasoning-token expenditure—is the primary bottleneck for complex tasks. While most frontier models are closely clustered in performance, some specific models show high systematic false-negative rates, highlighting that current advancements in raw power may not yet have solved the problem of consistent multi-turn interaction.

## Context
This paper matters because it shifts the evaluation of AI from static benchmarks to dynamic, interactive environments where agents must maintain coherence over multiple steps. It addresses a fundamental hurdle in creating autonomous systems: ensuring that an agent can reliably relay and receive information without the "chain" breaking due to minor inconsistencies or errors in judgment.

## Implications
For researchers and practitioners, these findings imply that simply scaling compute or increasing reasoning tokens may not be sufficient to solve complex multi-agent coordination problems if the underlying communication reliability remains flawed. Developers should prioritize architectural improvements that mitigate error propagation and focus on enhancing the consistency of model outputs in sequential tasks where a single mistake renders all subsequent steps moot.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19113v2)
