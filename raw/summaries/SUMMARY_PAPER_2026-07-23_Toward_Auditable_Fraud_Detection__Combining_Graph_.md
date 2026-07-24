---
title: Toward Auditable Fraud Detection: Combining Graph Features, Model Explanations, and Agentic Case Investigation
url: http://arxiv.org/abs/2607.19266v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_16-37-41Z_TowardAuditableFraudDetection_CombiningGraphFeatur.md
generated_at: 2026-07-23 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a layered fraud detection pipeline that integrates gradient‑boosted classifiers, graph features, anomaly signals, TreeSHAP explanations and an LLM investigation agent to handle uncertain cases. It finds that after correcting a simulator bias baseline performance does not improve on average precision but gains ranking within intermediate scores; engineered structural features recover many injected frauds while the tabular model misses them, and the LLM agent underperforms direct thresholding despite using its explanations.

## Key Takeaways
- The pipeline’s components only benefit specific subsets of cases, with graph features and anomaly signals improving recall on uncertain classifier outputs but not overall average precision.
- Engineered structural features recover a large portion of injected multi‑account fraud rings that the tabular baseline misses, indicating their value in targeted scenarios.
- The LLM investigation agent produces coherent rationales but its decision accuracy is lower than simple thresholding, showing that model explanations do not guarantee better outcomes.

## Context
Fraud detection systems face pressure to scale with transaction volume while providing auditability. Recent work emphasizes explainable AI and multi‑modal inputs such as graph structures and anomaly signals, yet few studies evaluate how these layers interact in real‑world pipelines. This research contributes a systematic view of when each layer adds value.

## Implications
Practitioners should treat layered models as modular tools rather than assuming cumulative benefit; feature engineering may be crucial for specific fraud patterns while automated agents need careful validation to avoid amplifying errors. The findings guide design choices that balance explainability with performance in complex fraud ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19266v1)
