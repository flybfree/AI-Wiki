---
title: CompressionBench: How can your coding agents compress LLMs?
url: http://arxiv.org/abs/2611.06858v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-04_18-14-50Z_CompressionBench_HowcanyourcodingagentscompressLLM.md
generated_at: 2026-11-08 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CompressionBench is a benchmark that evaluates whether coding agents can autonomously compress large language models under strict storage, time, and inference constraints. The study tests six agents across six model-size settings and finds that 29 of 36 submissions pass independent verification, with the best agent design achieving only a 3.4% perplexity increase over BF16 and 77.33% downstream accuracy compared to 79.56% for uncompressed BF16 models. The results highlight that representation design, experimental judgment, and capability validation are the central challenges agents face when attempting model compression.

## Key Takeaways
- Agents demonstrate iterative improvement capability, successfully lowering perplexity in 21 of 24 revisions at nearly fixed storage budgets, showing that autonomous experimentation loops can drive meaningful compression progress without human intervention in algorithm selection.
- Complete-model feedback fundamentally disrupts local optimization strategies: 17 of 79 prior local rankings were reversed when agents evaluated full-model performance rather than partial or proxy metrics, revealing that agents relying on incomplete signals make systematically wrong decisions about which compression techniques to pursue.
- Perplexity and likelihood-based metrics alone are insufficient for validating compressed models; generation tests and inference tests expose critical failures that likelihood scores miss entirely, meaning agents that optimize only for perplexity produce models that appear compressed successfully but fail in practical deployment scenarios.

## Context
This paper sits at the intersection of recursive self-improvement research and practical LLM deployment efficiency. As AI systems increasingly depend on their own infrastructure and model pipelines, the ability to autonomously compress models becomes a concrete, measurable component of self-improvement loops. CompressionBench provides the first structured evaluation of coding agents performing this specific engineering task, bridging the gap between theoretical compression algorithms and autonomous agent-driven experimentation in a controlled benchmark setting.

## Implications
For practitioners deploying LLMs under hardware constraints, this work signals that coding agents can approach but not yet match human-engineered compression quality, with a measurable accuracy gap remaining. For the broader AI research community, the findings identify specific failure modes—over-reliance on local metrics, inability to validate capability beyond likelihood scores—that must be addressed before agent-driven model compression can be trusted in production pipelines. Industry teams building self-improving AI systems should treat compression validation as a multi-signal problem requiring generation tests, not just perplexity monitoring.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.06858v1)
