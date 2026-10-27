---
title: FlexA-Mem: Budget-Adaptive Agentic Memory for LLM Agents
published: 2026-10-23T20:34:09Z
authors: Wujiang Xu, Jiaojiao Han, Xi Zhu, Qizheng Zhang, Kaiqu Liang, Yutong Yin, Kai Mei, Dimitris N. Metaxas
url: http://arxiv.org/abs/2610.33274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FlexA-Mem: Budget-Adaptive Agentic Memory for LLM Agents

## Abstract
Large language model (LLM) agents work in scenarios with very different memory needs. A question about past conversations needs the exact facts it names, while a multi-step task needs a trace of the steps already taken together with details that the next step cannot name. Existing memories are each designed and tested for one kind of scenario. Retrieval memories such as A-Mem miss steps that the current query does not express, summaries drop exact strings, and pairing the two fixes the split of the budget in advance. We propose FlexA-Mem, a general memory that writes each unit of history once into an immutable store and renders a fresh memory for every call. The rendered memory is a compact timeline of records plus detail that a fixed rule fits into the remaining room without an LLM call. The detail is either relevant units as raw text or excerpts or the verbatim pieces that best match the query. With one store, FlexA-Mem serves both kinds of scenario. On AppWorld challenge tasks at 4k, it outperforms the second-best method by 11.5%, and on 147 unused tasks with predictions fixed in advance it outperforms A-Mem with a summary by 12.2%. On LongMemEval and LoCoMo, it matches a dedicated keyword retriever that writes no memory, while memories built on text written by an LLM fall far behind at tight budgets. Ablations show that the timeline carries AppWorld completion, whereas recovery mainly saves steps there and decides accuracy on exact facts. Code is available at https://github.com/WujiangXu/Flex-Amem

## Metadata
- **Published**: 2026-10-23T20:34:09Z
- **Authors**: Wujiang Xu, Jiaojiao Han, Xi Zhu, Qizheng Zhang, Kaiqu Liang, Yutong Yin, Kai Mei, Dimitris N. Metaxas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33274v1)