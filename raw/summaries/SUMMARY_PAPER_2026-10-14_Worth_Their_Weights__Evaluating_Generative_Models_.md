---
title: Worth Their Weights? Evaluating Generative Models for Discourse Parsing
url: http://arxiv.org/abs/2610.17658v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_03-36-43Z_WorthTheirWeights_EvaluatingGenerativeModelsforDis.md
generated_at: 2026-10-14 01:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether generative language models outperform traditional discriminative models for Rhetorical Structure Theory (RST) discourse parsing. The authors find that at matched parameter counts, discriminative parsers significantly outperform generative ones, though much larger generative models can sometimes surpass them. Notably, generative models demonstrate a particular advantage in elementary discourse unit (EDU) segmentation, yielding new state-of-the-art results on the RST-DT benchmark for both end-to-end parsing and segmentation.

## Key Takeaways
- At matched parameter counts, discriminative parsers based on pretrained encoder-only language models perform substantially better than generative language models for RST parsing, suggesting that the architectural inductive biases of discriminative models remain highly effective for structured discourse analysis tasks.
- Generative models, when scaled to much larger parameter counts, can sometimes outperform discriminative parsers, indicating that sheer model capacity can partially compensate for architectural disadvantages in structured prediction tasks.
- Generative models hold a distinct and notable advantage in elementary discourse unit (EDU) segmentation, achieving new state-of-the-art results on the RST-DT benchmark in both end-to-end parsing and segmentation, which suggests that generative approaches may be particularly well-suited for boundary detection and text segmentation subtasks within discourse parsing pipelines.

## Context
RST parsing has been a longstanding challenge in computational linguistics and natural language processing, historically dominated by discriminative approaches leveraging encoder-only transformer architectures. The rapid proliferation of large generative language models has created uncertainty about whether discourse parsing should be reformulated as a generative sequence-to-sequence task. This paper addresses a critical methodological question in the NLP community: whether the shift toward generative architectures benefits or hinders structured linguistic analysis tasks that require precise, hierarchical output representations.

## Implications
For practitioners building discourse parsing systems, this work suggests that traditional discriminative architectures remain the more efficient and effective choice for most RST parsing applications, particularly when computational resources constrain model size. However, the demonstrated superiority of generative models in EDU segmentation opens a practical pathway for hybrid pipelines that combine discriminative parsing with generative segmentation. For the broader AI research community, these findings caution against assuming that generative models universally outperform task-specific discriminative architectures, highlighting that architectural suitability depends heavily on the specific subtask within a structured prediction pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17658v1)
