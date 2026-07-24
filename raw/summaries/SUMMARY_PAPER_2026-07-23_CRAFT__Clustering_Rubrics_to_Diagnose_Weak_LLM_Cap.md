---
title: CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data
url: http://arxiv.org/abs/2607.16122v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_17-00-38Z_CRAFT_ClusteringRubricstoDiagnoseWeakLLMCapabiliti.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CRAFT, a method that transforms rubric‑based evaluation datasets into model‑specific capability diagnoses and generates targeted fine‑tuning data. By treating each grading criterion as a probe, CRAFT clusters these probes into a hierarchical tree, scores the target model at every node, and selects low‑performing nodes where failures are most evident. The method consistently outperforms baseline approaches on finance and legal benchmarks.

## Key Takeaways
- CRAFT extracts capability descriptions from rubric pairs, clustering them into a hierarchy that isolates granular failure modes rather than prompt or category level issues.
- The hierarchical tree enables dynamic selection of weak capabilities at the finest resolution, allowing precise generation of supervised fine‑tuning data aligned with model weaknesses.
- Experiments on four open source models across finance and legal domains show CRAFT’s ability to improve average performance under temperature decoding, especially in the finance domain.

## Context
Current evaluation pipelines often report where a language model fails but do not explain why, leaving improvement efforts vague. Generating fine‑tuning data based solely on prompt or category failures can be suboptimal because it may not address the underlying capability gaps. CRAFT bridges this gap by providing interpretable, capability‑level diagnostics that guide more effective model refinement.

## Implications
For researchers and practitioners, CRAFT offers a systematic way to diagnose specific weaknesses in LLMs, turning abstract failure metrics into actionable insights. This can accelerate fine‑tuning pipelines, reduce wasted compute on irrelevant data, and lead to higher performing models across specialized domains such as finance and legal services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16122v1)
