---
title: Diversity over Scale: Recursive Self-Improvement with Ensembles of Small Open-Weight Models
published: 2026-11-20T23:46:36Z
authors: Navapat Nananukul, Mayank Kejriwal
url: http://arxiv.org/abs/2611.28420v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diversity over Scale: Recursive Self-Improvement with Ensembles of Small Open-Weight Models

## Abstract
The advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. Recursive self-improvement (RSI) loops, in which a language model repeatedly rewrites a program and builds on its previous version, now perform well in machine-learning tasks, but they rely on frontier models and hundreds of calls per run. Small open-weight models are far cheaper, yet when used alone, their programs often crash and their improvements stall. We propose DiVE (diverse models evolve), an ensemble method for RSI that aims to improve creativity and diversity of generated solutions. DiVE uses three components: a shared memory, a failure log, and best-idea-wins rounds. This allows models to write candidate solutions from the same context and retain the best idea at each iteration. On 22 MLE-bench Lite competitions, an ensemble of five 8-12B open-weight models has 25.4% less test error than its average member and 16.7% less than Llama 3.3 70B, and comes within 7.1% of Qwen 3.5 122B-A10B at 75% of its cost. Diversity among small models can thus stand in for part of the scale that RSI relies on.

## Metadata
- **Published**: 2026-11-20T23:46:36Z
- **Authors**: Navapat Nananukul, Mayank Kejriwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.28420v1)