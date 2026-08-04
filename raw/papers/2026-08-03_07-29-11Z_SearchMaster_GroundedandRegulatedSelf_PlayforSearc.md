---
title: SearchMaster: Grounded and Regulated Self-Play for Search Agents
published: 2026-08-03T07:29:11Z
authors: Wentao Tan, Qiong Cao, Jiaqi Wang, Nan Duan
url: http://arxiv.org/abs/2608.01822v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SearchMaster: Grounded and Regulated Self-Play for Search Agents

## Abstract
Training LLM-based search agents requires high-quality search data: tasks that demand genuine multi-hop retrieval and trajectories that use search tools effectively. Existing pipelines often depend on human-written tasks, expert demonstrations, or stronger teacher models. We present SearchMaster, a self-play framework that trains a single LLM from search tasks it generates, solves, and verifies in a local search environment. The key challenge is that self-generated tasks and rollouts can yield misleading signals: pseudo multi-hop questions, success-rate difficulty estimates that ignore search depth, and rollouts with excessive opening but little targeted evidence acquisition. SearchMaster addresses these failure modes with three controls. An Evidence-Chain Generator (ECG) grounds task generation in explicit cross-document evidence chains to reduce pseudo multi-hop questions. A Search-Depth Reward (SDR) scores task difficulty by the search depth of successful rollouts rather than success rate alone, keeping retained tasks search-intensive. An Over-Opening Penalty (OOP) regulates tool use by discouraging excessive document opening, avoiding long but shallow browsing. Verified Proposer and Solver rollouts are then jointly optimized with GRPO. Across six deep-search benchmarks, SearchMaster improves a Qwen3.5-9B backbone from 38.19% to 51.52% average accuracy, with a 30.1-point gain on BrowseComp-Plus. These results show that grounded and regulated self-play can provide effective search-agent training data without human-labeled QA pairs or expert demonstrations. The code is available at https://github.com/WentaoTan/SearchMaster.

## Metadata
- **Published**: 2026-08-03T07:29:11Z
- **Authors**: Wentao Tan, Qiong Cao, Jiaqi Wang, Nan Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01822v1)