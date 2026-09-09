---
title: API Benchmark Scores Do Not Reliably Transfer to Chatbot Interfaces
url: http://arxiv.org/abs/2609.08861v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_15-08-37Z_APIBenchmarkScoresDoNotReliablyTransfertoChatbotIn.md
generated_at: 2026-09-08 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether benchmark scores obtained through API calls reliably reflect the performance of deployed chatbot interfaces. By comparing ChatGPT, Claude, and Gemini across seven systems and nine benchmarks, the authors reveal systematic discrepancies between API evaluations and interface evaluations, with APIs scoring significantly higher in accuracy and consistency.

## Key Takeaways
- API evaluations score 3.4 percentage points higher in accuracy and 2.1 percentage points higher in test-retest agreement than corresponding interface evaluations, indicating a measurable performance gap.
- The performance difference for ChatGPT between API and interface access exceeds the model‑generation difference between GPT 5.3 and GPT 5.4, showing that switching access surfaces can degrade performance as much as downgrading a full model generation.
- Varying system prompts, sampling parameters, or reasoning settings does not reliably close the gap, documenting a persistent context‑validity gap.

## Context
Benchmark scores remain a primary metric for evaluating AI models, yet they are often derived from isolated API calls that do not mirror real‑world usage. This study highlights that such metrics may mislead stakeholders about actual system behavior, reinforcing the need for more holistic evaluation practices.

## Implications
For researchers and industry practitioners, relying solely on API benchmark scores can lead to overestimating model capabilities and misguided deployment decisions. Addressing this gap is essential to ensure trustworthy AI systems that perform consistently across different access interfaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08861v1)
