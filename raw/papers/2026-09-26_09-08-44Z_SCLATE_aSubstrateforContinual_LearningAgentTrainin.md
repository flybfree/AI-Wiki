---
title: SCLATE: a Substrate for Continual-Learning Agent Training and Evaluation
published: 2026-09-26T09:08:44Z
authors: Youngmok Jung, Sirajul Salekin, Henry Tran, Javier Movellan, Zhao Huang, Manjot Bilkhu
url: http://arxiv.org/abs/2609.32391v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCLATE: a Substrate for Continual-Learning Agent Training and Evaluation

## Abstract
Continual-learning agents are systems of models, harnesses, and memory operating over long multi-session horizons. Evaluating and training them requires interleaving tasks with agent-side events such as session stop and start, crons, and memory consolidation. Yet existing benchmarks and training frameworks schedule only the benchmark's own events, leaving each benchmark and agent pair to build a custom scheduling loop. We present SCLATE, an execution substrate where benchmarks and unmodified agents each add their events to one open event scheduler through an adapter. A hybrid simulated clock runs these events on a shared timeline, flowing in real time while the agent works and skipping idle gaps, which compresses a month-long scenario into hours. SCLATE also serves as a rollout engine that runs any agent's harness and memory unmodified, recording the tokens and log probabilities of every model call through an in-container proxy. We port seven benchmarks to SCLATE and compare ten unmodified harness and memory configurations head to head on ten models. The comparison shows that an added memory system does not reliably beat the harness's native memory and that models differ widely in how they use the same harness and memory. We then post-train Qwen3.5-4B through unmodified harnesses and memory systems. The model learns to use both, reading 6.8x fewer file lines with a 16.7-point higher SWE-bench Verified pass rate, and writing richer memory records, while its held-out MetaClaw accuracy rises by up to 11.8 points.

## Metadata
- **Published**: 2026-09-26T09:08:44Z
- **Authors**: Youngmok Jung, Sirajul Salekin, Henry Tran, Javier Movellan, Zhao Huang, Manjot Bilkhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32391v1)