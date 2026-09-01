---
title: A Causal Model for Locating and Unlocking Sandbagging in Model Organisms
published: 2026-08-29T22:39:59Z
authors: Hong Kiat Tan, Linh Le, David Williams-King
url: http://arxiv.org/abs/2608.29461v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Causal Model for Locating and Unlocking Sandbagging in Model Organisms

## Abstract
Sandbagging models strategically underperform on evaluations while retaining the capabilities being measured. The evaluations that guide frontier-model deployment and governance then understate what these models can do. To understand the mechanism, we propose a causal model of how sandbagging is carried in the residual stream. Early layers write the sandbagging intent onto a single axis of the stream, and a later layer reads that axis and commits the answer. We study three instruction-tuned models (Qwen2.5-7B, Llama-3-8B, and Mistral-7B) and four ways of installing a sandbagging lock (prompting, fine-tuning, reinforcement learning, and circuit breaking). Each lock decides from the prompt whether to sandbag, and the fine-tuned and circuit-broken locks answer honestly whenever a password appears. The causal model predicts a window of layers, after the last sandbagging write and before the answer commit, in which a single-layer reference graft of the sandbagging axis to its honest value restores the full capability. The single-layer graft recovers the capability in 28 of the 33 runs of the prompted, fine-tuned, and RL-trained locks, with a median held-out recovery of 96%. The circuit-broken lock rewrites the whole state through a band of layers, and the single-layer graft fails at every layer. We therefore introduce a second intervention, context grafting, which replays the password's cached key/value activations so that every layer's attention reads them as additional context. Context grafting provably and empirically restores the full capability on all three models, and the recovery is surprisingly insensitive to the exact password content. More broadly, an auditor can use this causal model to design interventional auditing techniques for sandbagging models.

## Metadata
- **Published**: 2026-08-29T22:39:59Z
- **Authors**: Hong Kiat Tan, Linh Le, David Williams-King
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29461v1)