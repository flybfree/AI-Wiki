---
title: STAIR: Semantic-Temporal Automaton for Interpretable Reasoning in Temporal Question Answering
published: 2026-08-17T07:59:45Z
authors: Xinlong Dai, Jinchuan Zhang, Lei Gao, Xinzhe Hu, Yuefeng He, Hui Gao
url: http://arxiv.org/abs/2608.16224v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STAIR: Semantic-Temporal Automaton for Interpretable Reasoning in Temporal Question Answering

## Abstract
By leveraging large-scale pretraining, LLMs can interpret diverse temporal expressions and question formulations without task-specific training. However, existing prompt-based neuro-symbolic systems continue to rely on LLMs for both semantic interpretation and exact temporal inference. Consequently, discrete decisions regarding intervals, time anchors, and ordered states remain vulnerable to probabilistic errors and difficult to verify. We present STAIR, a \textbf{S}emantic-\textbf{T}emporal \textbf{A}utomaton for \textbf{I}nterpretable \textbf{R}easoning. STAIR separates semantic interpretation from precise temporal inference: an answer-free LLM adapter maps complex question formulations to normalized temporal intents, while a deterministic temporal automaton with finite control and guarded transitions executes the corresponding policies over canonicalized evidence. Following a rule-first design, STAIR resolves standard questions without invoking an LLM and applies semantic adaptation only when the rule path fails to produce an executable intent. This approach reduces free-form reasoning, making temporal decisions verifiable and interpretable. Specifically, guarded execution supports precise point-time containment and before/after selection, while semantic adaptation handles non-exact intervals and time-anchored queries. Across the TimeQA-Easy, TimeQA-Hard, TempReason-L2, and TempReason-L3 datasets, STAIR consistently outperforms strong baselines in the TQA task using matched model settings, achieving average F1 improvements of 16.57\% and 3.10\% when utilizing the Qwen2.5-7B and GPT-4o-mini models, respectively. Furthermore, ablations and diagnostic analyses demonstrate that STAIR excels at handling both boundary-sensitive and order-sensitive queries, while its guarded execution and semantic adaptation ensure precise point-time reasoning and inexact intervals, respectively.

## Metadata
- **Published**: 2026-08-17T07:59:45Z
- **Authors**: Xinlong Dai, Jinchuan Zhang, Lei Gao, Xinzhe Hu, Yuefeng He, Hui Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16224v1)