---
title: Baikal: Structured Search for Deep Research over Data Lakes
published: 2026-07-30T06:05:45Z
authors: Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari, Ashi Sinha, Athulya Anil, Kavitha Srinivas, Horst Samulowitz, Andrew McCallum
url: http://arxiv.org/abs/2607.27726v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Baikal: Structured Search for Deep Research over Data Lakes

## Abstract
Deep research over data lakes requires an LLM agent to investigate evidence across thousands of heterogeneous tables and passages to synthesize a report. Existing methods perform iterative retrieval and generation, letting accumulated context determine what to investigate next, which can overexploit locally promising evidence and fail to cover distinct semantic regions under a fixed budget. To address this, we cast deep research over data lakes as a budgeted search problem and present Baikal - a framework that clusters heterogeneous evidence into semantic regions, then searches over them adaptively to balance exploration and exploitation. Within each selected region, Baikal generates and investigates region-grounded subquestions, using finding quality as rewards to update region-level value estimates and guide search under policies ranging from random and LLM-guided selection to Bayesian $ε$-greedy and UCB. We evaluate Baikal on 15 queries each over HybridQA and TAT-QA data lakes containing 10,993 and 2,757 tables, respectively, together with 227K Wikipedia passages and 13K financial report passages. We assess research quality with a new rubric covering groundedness, relevance, diversity, and utility, and use GPT-5-mini to score Baikal and strong baselines, including DeepSearcher and an OpenCode research agent with retrieval and clustering variants. Across both data lakes, Baikal performs strongly under several region-selection policies; its best configuration improves report scores over the strongest baselines by 28% on HybridQA and 36% on TAT-QA. Our analyses attribute these gains to organizing and exploring semantic evidence regions, which improves groundedness and diversity and yields more useful findings under the same subquestion budget. These results demonstrate the value of structured semantic exploration for systematic research and discovery over heterogeneous data lakes.

## Metadata
- **Published**: 2026-07-30T06:05:45Z
- **Authors**: Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari, Ashi Sinha, Athulya Anil, Kavitha Srinivas, Horst Samulowitz, Andrew McCallum
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27726v1)