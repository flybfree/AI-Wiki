---
title: PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent
published: 2026-08-02T03:48:41Z
authors: Sudipta Paul, Vijay Srinivasan, Vivek Kulkarni, Aounon Kumar, Yashas Malur Saidutta, Wenbo Li, Srinivas Chappidi
url: http://arxiv.org/abs/2608.00969v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent

## Abstract
Existing search-augmented LLM agents are trained using Reinforcement Learning to boost its reasoning capabilities. However, these approaches primarily rely on outcome-level rewards, which provide little supervision over search behavior and overlook agent's ability to decompose complex queries properly. To mitigate this issue, we propose PROGRESS which utilizes teacher-guided coverage reward to explicitly shape decomposed query generation of the policy model. During training, frozen teacher models are used to decompose complex queries into essential search queries. These essential search queries are utilized to guide the search behavior of the policy model. Integrated into an R1-style training framework, our approach provides lightweight guidance over query decomposition decisions without dense process-level supervision. Experiments show that coverage-guided RL improves overall task performance, highlighting the importance of explicitly supervising search strategies in agentic LLMs.

## Metadata
- **Published**: 2026-08-02T03:48:41Z
- **Authors**: Sudipta Paul, Vijay Srinivasan, Vivek Kulkarni, Aounon Kumar, Yashas Malur Saidutta, Wenbo Li, Srinivas Chappidi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00969v1)