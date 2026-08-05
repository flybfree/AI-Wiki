---
title: Distractor-Aware Truncation: Disentangling Context-Length Effects from Signal Loss in Long-Context LLM Benchmarks
published: 2026-08-04T08:08:04Z
authors: Mohsen Arjmandi
url: http://arxiv.org/abs/2608.03297v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distractor-Aware Truncation: Disentangling Context-Length Effects from Signal Loss in Long-Context LLM Benchmarks

## Abstract
A standard claim in the literature on retrieval-augmented and memory-augmented language models is that shorter context is better when the relevant information is preserved. We test this claim by running every sample of two long-context benchmarks -- BABILong and GraphWalks (BFS) -- at four context-retention fractions (100%, 75%, 50%, 25%) under two truncation protocols. The first is the naive protocol implicitly used in much prior work: drop content from the middle of the prompt. The second is distractor-aware: identify the task-relevant content for each sample and drop only the rest. We evaluate three sizes of the Claude family (Haiku 4.5, Sonnet 4.6, Opus 4.7) and, to test cross-provider generality, GPT-5.5 from a different provider; we apply the same protocol to two further benchmarks (MRCR v2, Oolong). Under naive truncation, score collapses monotonically (paired Wilcoxon, Holm-corrected p_adj < 0.05 in all eight BABILong and GraphWalks cells). Under the distractor-aware protocol -- which preserves the signal by construction -- performance is preserved or improves: the two smaller Claude models show statistically significant gains on BABILong, while the larger models (Opus 4.7 and GPT-5.5) sit at their full-context ceiling. The naive collapse and its distractor-aware recovery replicate on GPT-5.5, ruling out a single-provider artifact. The mechanism is direct: under the naive protocol the answer-bearing content survives in fewer than 1% of samples at 25% retention; under the distractor-aware protocol it is preserved by construction. The naive protocol is therefore not a measurement of context-window effects; it is a measurement of how often middle-removal happens to spare the answer. We conclude that future studies of context-length effects must specify how they distinguish signal from distractor, or they are at best ambiguous between two opposite hypotheses.

## Metadata
- **Published**: 2026-08-04T08:08:04Z
- **Authors**: Mohsen Arjmandi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03297v1)