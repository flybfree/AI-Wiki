---
title: Analysing Self-Harm Representations in Language Models: a Cross-Architecture Study
url: http://arxiv.org/abs/2607.21988v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_05-27-49Z_AnalysingSelf_HarmRepresentationsinLanguageModels_.md
generated_at: 2026-07-26 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper analyzes how large language models encode self-harm content across different architectures and datasets. The study trains linear probes on the X-Sensitive and SH-Detection corpora to locate where self‑harm signals appear in model layers. It also examines contrastive directions of self‑harm representations, finding that Gemma-3-4B encodes them differently than other models.

## Key Takeaways
- Linear probes consistently detect self-harm information in the final 3–7% of network layers, indicating representation stabilizes near the output.
- The most accurate probes are not always linearly separable, showing complex internal patterns rather than simple binary splits.
- Gemma‑3‑4B encodes contrastive self‑harm directions in a more intricate manner compared with other LLMs.

## Context
Self-harm detection in language models is critical for safety systems that aim to intervene or flag at‑risk users. Understanding how these sensitive topics are represented helps researchers design more reliable and ethical AI tools. This work contributes to the broader effort of aligning large models with human well‑being concerns.

## Implications
Practitioners should prioritize monitoring the final layers of LLMs when building detection pipelines, as that is where self‑harm signals concentrate.
The findings suggest developing probes that handle non‑linear representations rather than relying solely on simple linear separability. These insights can guide responsible deployment and governance of AI systems handling high‑risk content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21988v1)
