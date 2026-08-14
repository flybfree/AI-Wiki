---
title: EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory
url: http://arxiv.org/abs/2608.12627v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_22-20-29Z_EgoCITE_Context_AugmentedIndexingandTime_AwareRetr.md
generated_at: 2026-08-13 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
EgoCITE tackles two major limitations in long‑horizon egocentric memory: unreliable indexing caused by sparse captions and retrieval that ignores a question’s temporal intent. The proposed framework improves answer accuracy over baselines by 4.4–14.2 % while reducing computational cost to 36× lower than large‑context LLM agents.

## Key Takeaways
- EgoScheme creates atomic memory indices from local multimodal context, turning fragmented video captions and speech transcripts into reliable searchable units.
- EgoIndex organizes complementary representations across multiple granularities, enabling efficient multi‑view indexing of actions, activities, utterances, and conversations.
- EgoRetrv merges semantic search with question‑conditioned temporal relevance scoring to curate evidence that aligns with the user’s time‑aware intent.

## Context
Current agentic memory systems struggle because they rely on coarse captions that lose fine‑grained information and ignore when a query is meant to retrieve past events. This gap limits the usefulness of long‑term personal video or audio logs for tasks like answering personal questions.

## Implications
EgoCITE’s cost‑effective, temporally aware retrieval could enable affordable, scalable personal assistants that understand user intent over time. Practitioners may adopt its modular indexing to build richer egocentric memory services without heavy LLM usage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12627v1)
