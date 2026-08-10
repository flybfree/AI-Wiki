---
title: I Seek You in Videos: Identity-Conditioned Queries for Person-Centric Video Reasoning
url: http://arxiv.org/abs/2608.07417v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_17-02-02Z_ISeekYouinVideos_Identity_ConditionedQueriesforPer.md
generated_at: 2026-08-09 22:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Identity‑conditioned Queries (ICQ) for person‑centric video reasoning, aiming to match a reference image of a person with complex real‑world videos and answer questions that require identity grounding, behavior understanding, and temporal reasoning. The authors propose ISYV, which includes a benchmark, a large training set, and a model framework, showing that most existing models fail on challenging cross‑domain tasks while the new model improves performance.

## Key Takeaways
- ICQ creates a unified task where video and reference image are jointly conditioned to solve identity grounding, behavior understanding, and long‑horizon tracking challenges.  
- ISYV‑Bench evaluates 1,377 real‑world videos with six difficulty levels, revealing that mainstream MLLMs struggle especially on cross‑domain matching and causal reasoning.  
- The framework leverages shot selection without extra annotations, enabling scalable training and stronger performance than strong baselines.

## Context
Person‑centric video reasoning is crucial for applications such as surveillance, social media analysis, and autonomous driving where understanding who is in a scene over time matters. Existing work often assumes simple video‑text pairs, limiting the ability to handle real‑world complexity and identity continuity across frames.

## Implications
The results suggest that current closed‑source and open‑source MLLMs need architectural changes to better exploit multimodal context for person‑specific tasks. Practitioners can adopt ISYV’s benchmark and training strategy to improve reliability in video analytics systems, reducing misidentification risks in safety‑critical domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07417v1)
