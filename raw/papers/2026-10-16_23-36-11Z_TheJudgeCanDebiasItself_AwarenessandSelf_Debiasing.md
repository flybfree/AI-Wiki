---
title: The Judge Can Debias Itself: Awareness and Self-Debiasing for Reliable LLM-as-a-Judge
published: 2026-10-16T23:36:11Z
authors: Youbing Yin, Jingyu Wu, Anoop Kumar, Scott Novotney, Daben Liu, Erin Babinsky
url: http://arxiv.org/abs/2610.24320v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Judge Can Debias Itself: Awareness and Self-Debiasing for Reliable LLM-as-a-Judge

## Abstract
LLM-as-a-Judge systems are increasingly employed for automated evaluation, yet remain susceptible to systematic biases that undermine their reliability. We demonstrate that the judge can effectively debias itself without additional training. We propose two lightweight strategies: bias-aware prompting, which explicitly alerts the judge to potential target biases prior to evaluation, and self-debiasing, in which the judge critiques the initial judgment for bias influence. To broaden the evaluation scope, we introduce three novel benchmarks--authority bias (fabricated citations), confidence bias (assertive phrasing), and formatting bias (structured presentation)--and evaluate across seven bias types in total. Across three frontier models, self-debiasing improves performance in 20 out of 21 model-bias combinations with gains up to 15 percentage points, while bias-aware prompting also yields consistent improvements. The recent fine-tuned external critic, however, does not generalize as reliably to the newly-introduced bias types (degradation observed in 5 out of 9 cases). Our findings demonstrate that prompting a judge to reason about bias, either preemptively or retrospectively, is a robust and generalizable approach for enhancing evaluation integrity.

## Metadata
- **Published**: 2026-10-16T23:36:11Z
- **Authors**: Youbing Yin, Jingyu Wu, Anoop Kumar, Scott Novotney, Daben Liu, Erin Babinsky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24320v1)