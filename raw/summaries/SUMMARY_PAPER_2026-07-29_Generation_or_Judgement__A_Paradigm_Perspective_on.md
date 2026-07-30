---
title: Generation or Judgement? A Paradigm Perspective on LLM-Based Emotion-Cause Pair Extraction in Conversation
url: http://arxiv.org/abs/2607.26967v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_14-28-55Z_GenerationorJudgement_AParadigmPerspectiveonLLM_Ba.md
generated_at: 2026-07-29 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the way a task is formulated—generating full pair sets versus judging individual candidate pairs—affects LLM performance in emotion‑cause pair extraction (ECPEC). Across 18 controlled comparisons, pairwise judgment consistently outperforms dialogue‑level generation. When explicit pair queries are used, the model correctly identifies 92.7% to 98.1% of emotion‑cause relations.

## Key Takeaways
- Dialogue‑level generation omits many relations, while explicit pair queries capture 92.7%-98.1% of emotion‑cause pairs.
- Pair‑level judgment yields more reliable candidate rankings than binary decisions from a shared threshold.
- An auxiliary retriever that re‑examines ambiguous boundary cases improves F1 by 0.50‑1.46 points with only a 1.49x increase in inference time.

## Context
This study underscores that the granularity of task formulation matters more than raw model ability when extracting relational information from conversational data. It demonstrates that LLMs can recognize emotion‑cause relations but struggle to discover and return complete pair sets, highlighting a gap between generation and judgment paradigms.

## Implications
Practitioners should decompose tasks and use targeted retrieval mechanisms to boost accuracy while keeping computational overhead low. The findings suggest that hybrid generation‑retrieval pipelines are more effective than single‑task approaches for ECPEC applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26967v1)
