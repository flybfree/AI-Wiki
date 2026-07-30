---
title: Knowledge before Reasoning: EC-Reason-Bench, a Training-Free Diagnostic Benchmark for LLM Enzyme Classification
published: 2026-07-29T02:16:09Z
authors: Linyu Li, Zhi Jin, Yichi Zhang, Dongming Jin, Yuanpeng He, Huanyao Zhang, Xuan Zhang, Gadeng Luosang, Nyima Tashi
url: http://arxiv.org/abs/2607.26397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Knowledge before Reasoning: EC-Reason-Bench, a Training-Free Diagnostic Benchmark for LLM Enzyme Classification

## Abstract
Enzyme function prediction is a hierarchical, knowledge-intensive form of protein function classification. Existing benchmarks expose an anomaly: general LLMs often get the coarse first level right, yet once asked for a complete EC number their accuracy at levels two through four drops to almost zero, while specialized models and tools stay usable. We propose EC-Reason-Bench, a training-free, diagnostic evaluation protocol built to answer two questions: why general LLMs score close to nothing on EC number prediction, and how much of that loss can be recovered without updating a single weight. We break enzyme classification ability into four orthogonal levers that can each be measured on their own: output structure, external knowledge, reasoning structure, and reasoning robustness. We test each lever with an inference-time method against a shared zero-shot baseline reproducing previously reported near-zero performance. Experiments with several strong reasoning LLMs yield four main findings. First, external knowledge is decisive and must precede reasoning: uniformly low closed-book performance rises sharply with open-book access, narrowing model gaps. Second, in closed-book settings, whether cascading and chain-of-thought help or hurt depends on a model's tendency to abstain. Third, once evidence is available the aggregate score of the best LLM setting is indistinguishable from simply voting the EC numbers of the nearest retrieved neighbors; that tie is an artifact of averaging, and it hides a large gain on adversarial evidence set against an equally large loss on multi-functional enzymes. Reasoning over evidence therefore acts as an arbiter of conflicting neighbors rather than as a source of knowledge, and no single-number leaderboard can see it. Fourth, accuracy obeys a law of homology availability.

## Metadata
- **Published**: 2026-07-29T02:16:09Z
- **Authors**: Linyu Li, Zhi Jin, Yichi Zhang, Dongming Jin, Yuanpeng He, Huanyao Zhang, Xuan Zhang, Gadeng Luosang, Nyima Tashi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26397v1)