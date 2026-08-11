---
title: Mitigating Over-Personalization in LLMs via Structured Memory
published: 2026-08-08T19:23:12Z
authors: Hakeem Hannoon, Andrew Zhao, Mihir Narayan, Sharvin Goyal, Ivaxi Sheth
url: http://arxiv.org/abs/2608.08300v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mitigating Over-Personalization in LLMs via Structured Memory

## Abstract
Conversational assistants increasingly rely on persistent long-term memory to personalize responses across sessions. However, when stored user information is reintroduced into the model context, it can also influence responses in inappropriate or unrelated settings. We study two such failure modes in memory-augmented LLMs: cross-domain leakage, where memories from one life domain affect responses in another, and memory-induced sycophancy, where stored user beliefs make models more likely to agree with the user rather than respond truthfully. We apply a simple inference-time modification to how memories are presented to the model, without changing the model or the memory contents. Across seven models on PersistBench, we compare the commonly used all-in context format, where memories are injected as an unstructured list, with structured formats that partition memories by domain. This simple modification consistently reduces cross-domain leakage while preserving utility, with our strongest method reducing leakage by $8.8\%$ on average relative to the baseline.

## Metadata
- **Published**: 2026-08-08T19:23:12Z
- **Authors**: Hakeem Hannoon, Andrew Zhao, Mihir Narayan, Sharvin Goyal, Ivaxi Sheth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08300v1)