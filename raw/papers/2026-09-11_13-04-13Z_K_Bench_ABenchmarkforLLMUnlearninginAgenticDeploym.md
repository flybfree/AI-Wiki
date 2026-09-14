---
title: K-Bench: A Benchmark for LLM Unlearning in Agentic Deployments
published: 2026-09-11T13:04:13Z
authors: Guangsheng Yu, Yanna Jiang, Qin Wang, Baihe Ma, Xu Wang
url: http://arxiv.org/abs/2609.12808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# K-Bench: A Benchmark for LLM Unlearning in Agentic Deployments

## Abstract
Unlearning benchmarks such as TOFU and MUSE certify forgetting by reading the model's final answer, where a model that refuses to answer already counts as having forgotten. We show that this model-level certificate does not transfer once the model is deployed as an agent. We introduce K-Bench, a benchmark that scores LLM unlearning under agentic deployment. K-Bench inspects all six channels a ReAct agent exposes, including its chain-of-thought (CoT), tool calls and tool observations, and elicited summary. A query counts as leaked if the secret appears in any of them. Each experiment places the secret in exactly one of the agent's three sources (the weights, the prompt, or the retrieval store). The K-Score is computed separately for each source and credits forgetting only when the agent remains usable. Clearing the answer channel does not make the secret unrecoverable. On structured retrieval, the secret stays verbatim in the tool-observation channel and the aggregate leak rate is unchanged. When the secret lives in the prompt or the retrieval store, TOFU and MUSE report no leakage, while the deployed agent still leaks it on 22--86\% of queries. When the secret is in the weights, none of the twenty evaluated published methods demonstrably removes it, and only an input-corruption intervention reaches selective forgetting under the evaluated observer. The top-ranked method changes across base models. A refusal-tuning method resists the evaluated extraction without verified knowledge removal.

## Metadata
- **Published**: 2026-09-11T13:04:13Z
- **Authors**: Guangsheng Yu, Yanna Jiang, Qin Wang, Baihe Ma, Xu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12808v1)