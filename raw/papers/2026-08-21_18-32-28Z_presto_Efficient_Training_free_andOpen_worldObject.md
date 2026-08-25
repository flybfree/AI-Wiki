---
title: presto: Efficient, Training-free, and Open-world Object Placement via Imaginary Search
published: 2026-08-21T18:32:28Z
authors: Weixuan Ding, Shang Liu, Hanyu Pei, Zeyan Liu
url: http://arxiv.org/abs/2608.21543v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# presto: Efficient, Training-free, and Open-world Object Placement via Imaginary Search

## Abstract
Object placement is critical in image composition, requiring spatially and semantically coherent positioning of objects within diverse scenes. Existing approaches typically rely on hand-crafted rules or supervised learning on limited datasets, which restricts their generalization and interpretability, especially in open-world scenarios involving novel objects and scenes. In this work, we reformulate open-world object placement as a heuristic search task guided by reasoning from a Multimodal Large Language Model (MLLM). We introduce \textsf{presto}, a zero-shot, training-free framework that operates within an imaginary action space to iteratively refine object position and scale. Our coarse-to-fine search strategy ensures fast convergence, and we evaluate two decision-making variants: Metric-guided Selection and MLLM-as-a-judge. Experiments across multiple benchmarks show that \textsf{presto}~achieves state-of-the-art performance, particularly in previously unseen, open-world settings. Human studies further reveal that the MLLM-as-a-judge variant produces more perceptually coherent placements than metric-driven approaches, highlighting a gap between standard evaluation metrics and human visual judgment.

## Metadata
- **Published**: 2026-08-21T18:32:28Z
- **Authors**: Weixuan Ding, Shang Liu, Hanyu Pei, Zeyan Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21543v1)