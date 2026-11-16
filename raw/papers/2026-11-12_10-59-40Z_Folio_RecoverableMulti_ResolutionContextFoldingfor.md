---
title: Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents
published: 2026-11-12T10:59:40Z
authors: Yubo Ruan, Tao Peng, Jiao Zhang, Chuanguo Ma, Lei Xu, Han Zhou, Wenwu Wang, Xiafei Lv, Xingjie Zhou, Guiju Fan, Hao Wang, Fenghui Zhang, Mao Miao, Shuo Li
url: http://arxiv.org/abs/2611.16627v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents

## Abstract
Long-horizon language agents accumulate tool results and replies until the history no longer fits the context window. Current agents shrink this history by having a model summarize it, so each compaction rereads and rewrites the history it replaces, and cache-aware triggers decide when to compact while taking the size of the result as given. We present Folio, a context manager that records, folds, and recovers history through one set of handles. While the agent runs, Folio records three linked levels: a short turn note the model writes as part of its ordinary reply (L1), an event manifest of every call written by the runtime (L2), and the captured source records (L3). Because these views already exist, the runtime folds the context programmatically, selecting coarser views for older turns. The fold prints the handles that index L2 and L3, so recovery tools that read bounded pages, compute over full text in files, and keep findings in a persistent dossier reach the evidence the agent needs with little added input. The fold trigger prices an explicit landing point that includes the retained budget. On 75 LOCA-bench tasks with DeepSeek-V4-Pro behind every system, Folio solves 66 tasks against 54 for the same runtime with model-written compaction and 49-59 for Claude Code, Codex, and SoL-Pi, in about half their working time, at 2.4 times lower cost than that runtime; each fold takes a median of 0.6 seconds.

## Metadata
- **Published**: 2026-11-12T10:59:40Z
- **Authors**: Yubo Ruan, Tao Peng, Jiao Zhang, Chuanguo Ma, Lei Xu, Han Zhou, Wenwu Wang, Xiafei Lv, Xingjie Zhou, Guiju Fan, Hao Wang, Fenghui Zhang, Mao Miao, Shuo Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.16627v1)