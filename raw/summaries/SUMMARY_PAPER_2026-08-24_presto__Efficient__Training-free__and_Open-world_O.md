---
title: presto: Efficient, Training-free, and Open-world Object Placement via Imaginary Search
url: http://arxiv.org/abs/2608.21543v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-21_18-32-28Z_presto_Efficient_Training_free_andOpen_worldObject.md
generated_at: 2026-08-24 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Presto, a zero-shot training-free framework for placing objects in images by using an imaginary action space guided by reasoning from a multimodal large language model. The method iteratively refines object position and scale through a coarse-to-fine search strategy, achieving state-of-the-art results on benchmarks that include unseen open-world scenarios. Human evaluations show the MLLM-as-a-judge variant produces more perceptually coherent placements than metric-driven alternatives.

## Key Takeaways
- Presto solves open‑world object placement without any training data by employing an imaginary search space guided by a multimodal large language model.
- The coarse‑to‑fine search strategy enables rapid convergence and high performance across diverse benchmarks.
- Human studies reveal that the MLLM‑as‑a‑judge variant yields placements that align better with human visual judgment than traditional metric‑based evaluations.

## Context
Object placement remains a challenging problem in image generation because it must respect both spatial layout and semantic meaning while handling novel objects and scenes. Existing methods often depend on handcrafted rules or supervised models trained on limited datasets, limiting their adaptability to open‑world contexts where new elements appear.

## Implications
This approach demonstrates that reasoning from large language models can replace costly training pipelines for simple yet critical tasks like object placement. Practitioners in computer vision and generative AI may adopt such reasoning‑driven heuristics to improve interpretability and generalization without retraining models, fostering more flexible deployment of visual generation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21543v1)
