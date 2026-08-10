---
title: PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents
url: http://arxiv.org/abs/2608.07438v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_17-22-29Z_PsychoAgent_AnAffect_SensitiveCognitiveArchitectur.md
generated_at: 2026-08-09 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PsychoAgent, a cognitive architecture that models human-like cognition by separating factual and affective memory within large language model agents. The authors demonstrate that integrating both types of memory through a conflict‑aware executive controller improves retrieval performance compared with baselines that rely only on semantic similarity or single‑memory recall.

## Key Takeaways
- Affective memories are first filtered for semantic relevance, then re‑ranked by salience, allowing emotionally important traces to enter the prompt while preserving topical fit.  
- In three controlled conflict scenarios, PsychoAgent retrieved 0.933 of the most critical memories, outperforming semantic‑affective (0.500) and single‑memory RAG baselines (0.667).  
- Five raters evaluated 27 outputs; after within‑rater standardization, PsychoAgent achieved the highest mean score (+0.22 SD), indicating consistent human‑like conflict effects.

## Context
The work addresses a longstanding challenge in AI: replicating the way humans prioritize emotionally salient information over purely logical relevance during memory retrieval. By modeling this dual‑memory system, researchers aim to make LLM agents more adaptable and contextually aware, moving beyond simple similarity‑based recall toward richer, human‑like cognition.

## Implications
For developers, PsychoAgent offers a framework that can be inspected and tuned to produce outputs reflecting both factual accuracy and emotional weight. In industry applications, this could lead to more empathetic customer service bots or decision‑support systems where affective context matters. Practitioners may integrate the architecture to create agents that better simulate human conflict resolution and memory recall.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07438v1)
