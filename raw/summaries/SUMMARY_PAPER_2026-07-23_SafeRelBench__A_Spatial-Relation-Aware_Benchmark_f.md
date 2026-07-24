---
title: SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents
url: http://arxiv.org/abs/2607.14543v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_03-59-44Z_SafeRelBench_ASpatial_Relation_AwareBenchmarkforPr.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SAFERELBENCH, a benchmark that evaluates seven VLM‑driven embodied agents on 507 executable samples testing spatial relations. It reveals that agents often succeed at tasks while violating safety constraints such as support or containment. The results highlight a gap between task completion and process‑level safety compliance.

## Key Takeaways
- SAFERELBENCH provides 248 spatial‑relation samples and 259 non‑spatial control samples to test safety before risk‑prone actions.
- Agents frequently complete tasks but ignore spatial safety constraints, indicating unsafe reasoning about object relations.
- The benchmark demonstrates that process‑level safety is not captured by static risk recognition alone.

## Context
In embodied AI, integrating vision‑language models with physical interaction remains a challenge because safety depends on dynamic scene changes beyond simple object detection. Prior benchmarks focus on end‑state outcomes or refusal of unsafe instructions, overlooking intermediate spatial risks.

## Implications
For industry, this signals that safe robot deployment requires more than perception and planning; it needs explicit modeling of how objects relate to each other during interaction. Practitioners should adopt benchmark frameworks that probe process‑level safety to guide model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14543v1)
