---
title: EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory
published: 2026-08-12T22:20:29Z
authors: Le Zhang, Ke Sun
url: http://arxiv.org/abs/2608.12627v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory

## Abstract
Long-horizon egocentric memory transforms continuous first-person video and audio into a searchable record of past experiences. We demonstrate two bottlenecks in existing systems: indices built from context-poor captions are unreliable for agentic search, while retrieval ignores a question's temporal intent. To address both bottlenecks, we introduce EgoCITE (Egocentric Context-augmented Indexing and Time-aware Evidence retrieval), a long-horizon agentic memory framework for egocentric QA. EgoCITE comprises three components. EgoScheme uses local multimodal context to turn fragmentary video captions and speech transcripts into self-contained atomic memory indices. EgoIndex organizes complementary action, activity, utterance, and conversation representations into searchable multi-view memory indices at multiple granularities. EgoRetrv combines semantic search with question-conditioned temporal relevance scoring and curation of retrieved evidence. We evaluate EgoCITE on EgoLifeQA, EgoMem, and EgoR1-Bench in terms of answer accuracy and target-event retrieval alignment. EgoCITE improves accuracy over agentic memory baselines by at least 4.4--14.2\% while achieving 36$\times$ lower cost than long-context LLM agents.

## Metadata
- **Published**: 2026-08-12T22:20:29Z
- **Authors**: Le Zhang, Ke Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12627v1)