---
title: A Systematic Investigation of Bias in Large Language Models for Advertising Relevance
url: http://arxiv.org/abs/2610.07544v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_00-18-07Z_ASystematicInvestigationofBiasinLargeLanguageModel.md
generated_at: 2026-10-06 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models used to assess advertising relevance exhibit systematic bias when judging query-ad pairs. It uses counterfactual experiments to test how advertiser identity, possible popularity, input language, and demographic wording can change relevance judgments from GPT-4o and a Qwen-7B relevance model. The study finds that such factors can alter assessments and that some demographic comparisons reveal stereotype-consistent patterns, while mitigation effectiveness depends on query relevance and training-label distribution.

## Key Takeaways
- The paper treats LLM relevance judging as a fairness-sensitive task rather than a purely accuracy task, showing that changing advertiser identity or possible popularity can shift categorical relevance judgments even when the underlying query and advertisement content remain comparable.
- Input language is another causal lever: experiments with real advertising logs show that the language of queries or advertisements can affect model assessments, suggesting that multilingual advertising systems may produce inconsistent relevance decisions across languages.
- Synthetic demographic probes reveal stereotype-consistent behavior in sensitive domains such as employment, housing, and credit, especially around gender and occupation, and mitigation during inference or training is not uniformly effective because it depends on whether advertiser information is relevant to the query and how advertiser labels are distributed in training data.

## Context
As LLMs are increasingly deployed in advertising pipelines for query-ad matching, ranking, and automated evaluation, their judgments can directly influence which ads are shown, ranked, or suppressed. This paper matters because it connects LLM evaluation research with fairness auditing in a high-stakes commercial setting, where small systematic biases can affect advertiser access, consumer exposure, and platform trust.

## Implications
For advertising practitioners, the findings provide a practical framework for auditing LLM relevance systems before deployment, especially when advertiser metadata, language variation, or demographic wording may influence decisions. The results also suggest that mitigation should be tailored to the task: prompt or inference controls may help only when advertiser information is genuinely relevant, while training-data balance and label distribution are critical for durable fairness improvements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07544v1)
