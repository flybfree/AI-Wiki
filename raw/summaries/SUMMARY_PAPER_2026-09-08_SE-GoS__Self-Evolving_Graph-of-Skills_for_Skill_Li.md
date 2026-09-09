---
title: SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale
url: http://arxiv.org/abs/2609.08228v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_04-20-11Z_SE_GoS_Self_EvolvingGraph_of_SkillsforSkillLibrary.md
generated_at: 2026-09-08 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SE-GoS, a training-free method that evolves an existing Graph-of-Skills graph using execution traces while keeping the original retrieval pipeline unchanged. It improves task reward and reduces input tokens compared with loading all skills fully. Across three LLMs on SkillsBench, SE-GoS consistently raises performance.

## Key Takeaways
- topology evolution discovers and prunes skill relationships from execution evidence, creating a more compact graph.
- edge-weight evolution reinforces retrieval-relevant relationships based on historical effectiveness, strengthening the signal for recall.
- description evolution optimizes retrieval-facing skill descriptions using feedback, making them clearer to the model.

## Context
Skill libraries are essential for large language models but retrieving thousands of skills is computationally costly. Traditional static graphs do not adapt as new tasks arise or as execution data accumulates. This work shows that historical traces can be used to continuously improve these structures without retraining.

## Implications
Practitioners can maintain a dynamic skill infrastructure that scales with usage, reducing latency and improving task success. The approach offers a maintenance‑free upgrade path for existing retrieval systems, aligning LLM deployment efficiency with evolving user needs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08228v1)
