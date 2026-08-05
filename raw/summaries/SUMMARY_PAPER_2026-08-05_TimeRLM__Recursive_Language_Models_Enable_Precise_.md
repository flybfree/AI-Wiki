---
title: TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series
url: http://arxiv.org/abs/2608.03391v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_09-40-45Z_TimeRLM_RecursiveLanguageModelsEnablePreciseAnomal.md
generated_at: 2026-08-05 01:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TimeRLM, a recursive language model that handles long-context anomaly detection in time series by using external code and vision capabilities to retrieve information. It demonstrates superior performance over existing TSLMs on synthetic benchmarks and real-world data. The approach reduces the number of interaction turns needed for final answers.

## Key Takeaways
- TimeRLM achieves 0.682 IoU for localization, far exceeding baseline scores of at most 0.329, showing precise anomaly retrieval in long sequences.
- It reaches 0.745 on classify-with-evidence tasks, while baselines score only 0.072, indicating strong classification with evidence.
- The post-trained model improves performance and requires about one-third fewer agent interaction turns than the untrained base.

## Context
Long-context anomaly detection is essential for monitoring high-frequency data where anomalies are sparse. Traditional TSLMs suffer from degraded retrieval as context length grows, limiting their usefulness in real applications.

## Implications
This work shows that recursive interaction can overcome long-range limitations, offering a scalable method for precise anomaly localization across domains such as healthcare and finance. Practitioners can adopt this framework to reduce computational overhead while maintaining accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03391v1)
