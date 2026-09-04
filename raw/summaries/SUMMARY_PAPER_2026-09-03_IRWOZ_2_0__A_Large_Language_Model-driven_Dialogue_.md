---
title: IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations
url: http://arxiv.org/abs/2609.04030v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_16-08-57Z_IRWOZ2_0_ALargeLanguageModel_drivenDialogueDataset.md
generated_at: 2026-09-03 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper presents IRWOZ 2.0, a revised dataset for industrial robot dialogues that leverages large language model generation to clean and expand the original noisy data. The new version contains 390 dialogues across four domains—Assembly, Delivery, Position, and Relocation—and achieves higher state‑tracking performance as shown by GPT‑2 BLEU‑4 scores rising from 0.1651 to 0.5604.

## Key Takeaways  
- The dataset was expanded from its initial size to include 390 high‑quality dialogues, each manually corrected for errors and verified by domain experts.  
- Automated typo removal using LLM techniques eliminated many noise artifacts that previously degraded state tracking accuracy.  
- Benchmark results show GPT‑2’s BLEU‑4 score rose from 0.1651 to 0.5604, indicating a substantial improvement in dialogue modeling.

## Context  
In AI research, datasets are often the bottleneck that limits model performance; noisy or incomplete data can cause models to fail in real‑world scenarios. By integrating LLM preprocessing, IRWOZ 2.0 demonstrates how automated quality control can be a scalable solution for industrial robotics.

## Implications  
Industrial manufacturers can now train more robust HRI systems with cleaner interaction logs, reducing the need for extensive manual annotation. The improved dataset also serves as a benchmark for future LLM applications in robotics, encouraging broader adoption of AI‑enhanced dialogue tools and fostering collaboration between academia and industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04030v1)
