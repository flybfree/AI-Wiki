---
title: Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.29588v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_06-19-20Z_CallNeighboursYourself_GraphWalkswithDestination_C.md
generated_at: 2026-08-31 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Call Neighbours Yourself (CNY), a method that lets large language models actively explore graph neighbourhoods during reasoning over text‑attributed graphs. By treating neighbour selection as part of the generation process, CNY improves evidence acquisition and consistently outperforms fixed‑context baselines on standard TAG benchmarks.

## Key Takeaways
- The model learns to decide when to expand candidate neighbours for additional evidence, rather than fixing a static set of accessible nodes before inference.
- Destination‑conditioned on‑policy self‑distillation retroactively evaluates selected neighbours after their content is revealed and converts the resulting change in action preference into an action‑level training signal.
- Experiments show that CNY achieves higher reasoning performance under a unified raw‑text setting and its exploration policy transfers to unseen graphs and new graph‑level tasks.

## Context
Current graph reasoning approaches treat neighbourhood information as given, limiting models’ ability to gather missing evidence. This static view hampers the integration of dynamic knowledge discovery into language models, which is essential for scalable and flexible AI systems that handle diverse textual graphs.

## Implications
For researchers, CNY offers a principled way to embed exploration into generative reasoning, potentially unlocking better performance across varied graph structures. Practitioners can leverage this framework to build more robust applications that require adaptive knowledge gathering from unstructured text‑graph data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29588v1)
