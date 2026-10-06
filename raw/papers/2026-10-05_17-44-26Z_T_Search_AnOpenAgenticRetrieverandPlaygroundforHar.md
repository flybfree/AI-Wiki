---
title: T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search
published: 2026-10-05T17:44:26Z
authors: Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev, Danil Taranets, Dmitrii Stoianov, Nikita Gulyakov, Gleb Alektorov, Anatolii Potapov
url: http://arxiv.org/abs/2610.06782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search

## Abstract
We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list of evidence chunks with short justifications, leaving answer generation to a downstream model, so backend and generator can be swapped without retraining. T-Search is built on Qwen3.6-35B-A3B and trained on adversarially filtered synthetic search tasks with round-sliced supervised fine-tuning followed by GSPO on a recall reward. Averaged over seven English and Russian benchmarks with gold evidence annotations, it reaches 56.0 Recall@10 with one rollout, 14.4 points above its base, and 61.3 with three fused rollouts, outperforming larger open models. We release the model, harness, live demo, and three benchmarks, including TRuST, the first native-Russian hard-search benchmark.

## Metadata
- **Published**: 2026-10-05T17:44:26Z
- **Authors**: Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev, Danil Taranets, Dmitrii Stoianov, Nikita Gulyakov, Gleb Alektorov, Anatolii Potapov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06782v1)