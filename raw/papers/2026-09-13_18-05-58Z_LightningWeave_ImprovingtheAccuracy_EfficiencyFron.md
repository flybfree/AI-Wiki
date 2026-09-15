---
title: Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition
published: 2026-09-13T18:05:58Z
authors: Yecheng Wu, Song Han, Han Cai
url: http://arxiv.org/abs/2609.14708v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition

## Abstract
A core goal of efficient reasoning is to improve the accuracy-efficiency frontier. However, jointly improving reasoning accuracy and inference efficiency can be challenging, as the two objectives can favor different reasoning behaviors. Independently post-trained models already offer distinct strengths in accuracy and efficiency. We introduce Lightning Weave, a post-training framework that extracts and composes these independently learned capabilities in a single student through on-policy distillation. Each acquired capability is represented by the policy shift from the model before post-training to the resulting specialist. Lightning Weave combines aligned log-ratio shifts at shared student token states and uses Tilted-Target DOPD to convert the cached signals into a stable learning target. Each anchor pair scores the cached trajectories once, enabling subsequent student training without serving multiple live anchor models concurrently. Across diverse student models and benchmarks in mathematics and code, Lightning Weave substantially improves upon the base students and achieves a state-of-the-art accuracy-efficiency frontier. On Qwen3.5-4B, it raises HMMT 2025 accuracy from 59.2% to 64.0% with 10.7% fewer response tokens, and LiveCodeBench v5 accuracy from 41.7% to 54.2% with 9.6% fewer response tokens. Adjusting the relative strengths of the anchor signals yields a strong empirical accuracy-efficiency Pareto frontier. These results establish Lightning Weave as a new practical route to efficient reasoning through capability composition. Code will be released soon.

## Metadata
- **Published**: 2026-09-13T18:05:58Z
- **Authors**: Yecheng Wu, Song Han, Han Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14708v1)