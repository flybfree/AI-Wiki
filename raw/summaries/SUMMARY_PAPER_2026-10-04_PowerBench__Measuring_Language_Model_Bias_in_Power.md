---
title: PowerBench: Measuring Language Model Bias in Power-shifting Requests
url: http://arxiv.org/abs/2610.02303v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_17-57-25Z_PowerBench_MeasuringLanguageModelBiasinPower_shift.md
generated_at: 2026-10-04 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PowerBench is a novel evaluation framework designed to measure systematic biases in how language models respond to power-shifting requests, distinguishing between self-empowerment, disempowerment, and power grabbing scenarios. The authors build and open-source a curated dataset varying power domains, contexts, affected party scale, and user power standing, then evaluate 24 models from both US and Chinese developers across multiple experimental conditions. The central finding is that models exhibit consistent refusal asymmetries: they refuse power grabbing more than disempowerment, disempowerment more than self-empowerment, and show nationality-based biases favoring the US in specific power configurations.

## Key Takeaways
- Models demonstrate a clear refusal hierarchy across power-shifting request types: power grabbing is refused most frequently, followed by disempowerment, with self-empowerment being the most readily accommodated. Furthermore, refusal rates for power grabbing increase as the scale of the affected party grows from an individual to an entire society, suggesting models are more cautious about large-scale power redistribution.
- Nationality-based bias is pronounced: models are biased toward helping others take power from the US while resisting helping US users take power from others, yet they favor the US when it gains power without anyone losing. This reveals a complex, non-trivial pattern of geopolitical preference embedded in model behavior.
- When the user requesting power shifts is an AI agent rather than a human, refusal rates increase significantly, particularly for power grabbing against an individual. Additionally, request language introduces model-specific refusal biases that largely cancel out on average across the full model set, indicating that language effects are heterogeneous rather than uniform.

## Context
As language models become embedded in everyday decision-making, governance, and resource allocation systems, their differential willingness to grant or deny power-shifting requests can compound into large-scale societal effects. Prior evaluation frameworks have focused on toxicity, safety, or general capability benchmarks, but have not systematically measured how models distribute assistance across power dynamics. PowerBench fills this gap by operationalizing power relations as measurable request categories and introducing controlled experimental conditions that isolate nationality, agent identity, and language as confounding variables.

## Implications
For model developers and AI safety practitioners, PowerBench provides a concrete, reproducible benchmark for auditing geopolitical and identity-based biases that could shape who receives assistance at scale. Industry stakeholders deploying LLMs in policy, legal, or economic contexts should use such evaluations to detect whether their models systematically privilege certain nationalities or power configurations. The open-source dataset and multi-language evaluation protocol also enable researchers to track whether these asymmetries persist, worsen, or diminish in future model generations, making bias in power allocation a measurable engineering concern rather than a speculative one.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02303v1)
