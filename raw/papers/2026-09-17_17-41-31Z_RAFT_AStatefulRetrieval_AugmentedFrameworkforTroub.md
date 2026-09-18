---
title: RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents
published: 2026-09-17T17:41:31Z
authors: Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, Zhengyi Chen, Chenyu Diana Zhang, Shanshan Yang, Chittibabu Pacharu
url: http://arxiv.org/abs/2609.20754v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents

## Abstract
Effective troubleshooting agents in enterprise customer support depend on retrieving actionable guidance from similar historical cases, yet existing retrieval-augmented generation (RAG) systems treat support cases as static documents and overlook their multi-stage, stateful nature. We introduce RAFT (Retrieval-Augmented Framework for Troubleshooting Agents), a stateful RAG framework that abstracts each closed historical case into a directed chain of timeline entries and retrieves at the entry level, surfacing cases whose intermediate states match the active case and returning the parent-case trajectory anchored at the matched state; an optional case-level graph links cases through a configurable similarity representation. We evaluate this retrieval layer directly, which, unlike evaluating a full agent system, requires no production deployment. Because public multi-stage troubleshooting data is extremely rare, we pair a synthetic benchmark built from Microsoft Learn Windows Server documentation with real Apache Jira issues carrying human-created duplicate labels. RAFT improves Case Hit over vanilla RAG and GraphRAG baselines at every stage of case progress, with statistically significant gains over the strongest baseline; the Jira results provide directional evidence that the advantage transfers to real case histories. We release our benchmark, implementation, and the Apache Jira evaluation set.

## Metadata
- **Published**: 2026-09-17T17:41:31Z
- **Authors**: Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, Zhengyi Chen, Chenyu Diana Zhang, Shanshan Yang, Chittibabu Pacharu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.20754v1)