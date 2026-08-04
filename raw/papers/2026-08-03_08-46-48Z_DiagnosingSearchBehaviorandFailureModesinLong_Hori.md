---
title: Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents
published: 2026-08-03T08:46:48Z
authors: Qi Liu, Jiaxin Mao, Fengbin Zhu, Tat-Seng Chua
url: http://arxiv.org/abs/2608.01913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents

## Abstract
Deep search agents answer difficult information-seeking questions by iteratively issuing search queries to gather supporting evidence, but it remains unclear whether and how greater search effort leads to better answers. We study these questions through a trajectory-level diagnosis of long-horizon search agents. Using human-annotated document-level relevance judgments, we evaluate the evidence retrieved at each search step and separate two stages of agent behavior: what evidence an agent retrieves and how effectively it uses that evidence. This distinction further allows us to decompose failures into retrieval gaps, where the necessary evidence is never found, and utilization gaps, where relevant evidence is retrieved but not used correctly. With the retrieval model and evaluation harness held fixed, we compare six agents on BrowseComp-Plus and further validate our findings on BrowseComp with an open-web search API. Across settings, we find that search effort and answer quality are only weakly aligned. Answer accuracy is better correlated with the quality of retrieved evidence, especially cumulative retrieval recall, than with the number of searches or the amount of context consumed. Useful evidence often appears early in the trajectory, yet agents tend to continue searching, producing a long tail of low-yield retrieval steps. At the query level, exploratory reformulations remain useful, but the best-performing agents issue far fewer redundant queries. Overall, by systematically characterizing the search behavior and failure modes of long-horizon search agents, this work points to practical directions for building better deep research systems, including stronger query formulation, more effective evidence selection and context management, and stopping criteria based on whether sufficient supporting evidence has been retrieved.

## Metadata
- **Published**: 2026-08-03T08:46:48Z
- **Authors**: Qi Liu, Jiaxin Mao, Fengbin Zhu, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01913v1)