---
title: Eternal Sunshine of the Spotless Mind: Systematically Erasing LLM's Memories
published: 2026-09-29T00:11:56Z
authors: Olga Ohrimenko
url: http://arxiv.org/abs/2609.36414v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Eternal Sunshine of the Spotless Mind: Systematically Erasing LLM's Memories

## Abstract
We consider persistent LLMs that accumulate memories of their interactions with a user over time. Such LLMs maintain memories using external storage, which they can query to overcome the limitations of a fixed context window. Such systems have numerous practical applications, as they can draw on all past interactions when responding to user queries.   In this paper, we ask whether LLMs can forget information shared with them upon a user's request. We find that current LLMs fail to delete such information---even when they claim to have forgotten it and even when operating with a limited context. To this end, we consider a new direction of study: Deletion of LLM Memories.   We show that naively removing messages that match a user's deletion request is insufficient, since conversations naturally introduce message dependencies that cause information to persist. To correctly handle deletion requests, we propose the DeLLM framework. It dynamically constructs relevant context for each LLM query and maintains a provenance graph of messages to determine which ones must be removed during deletion. Our experiments show that DeLLM achieves a high deletion rate while maintaining utility.

## Metadata
- **Published**: 2026-09-29T00:11:56Z
- **Authors**: Olga Ohrimenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36414v1)