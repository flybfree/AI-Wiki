---
title: Do AI-for-Science Agents Preserve Model Safety?
published: 2026-10-23T01:34:20Z
authors: Michael Yew Chuan Lee, Manya Sriram, N. Benjamin Erichson
url: http://arxiv.org/abs/2610.32045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do AI-for-Science Agents Preserve Model Safety?

## Abstract
AI-for-Science agents are increasingly being used for formulating scientific hypotheses, running autonomous experiments, and interpreting evidence. These agents are constructed by integrating a large language model (LLM) into a domain-specific agent harness, which in turn can improve the LLM's scientific capability and enable the model to orchestrate scientific tools. In this work, we ask whether model safety is preserved when an LLM is integrated in an AI-for-Science agent harness. We evaluate five agent harnesses on 50 harmful chemistry requests. Specifically, we study how the safety behavior changes under direct prompting, two simple adversarial prompting strategies, and an adaptive attack. Across four recent GPT variants, our results show that the agent harness can increase harmful compliance even under direct prompting. More critically, we find that adaptive attacks that are largely unsuccessful against the base LLM suddenly become highly successful after the agent harness is introduced. Our results show that the safety behavior of the base LLM is not durable once a harness is introduced. Thus, as AI-for-Science agents become more capable and autonomous, the community needs to evaluate and align the agent using domain-specific safety benchmarks.

## Metadata
- **Published**: 2026-10-23T01:34:20Z
- **Authors**: Michael Yew Chuan Lee, Manya Sriram, N. Benjamin Erichson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32045v1)