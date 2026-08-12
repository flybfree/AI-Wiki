---
title: From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models
published: 2026-08-11T03:58:23Z
authors: Si'an Xie, Jiaxun Liu, Biao Yang, Wei Yuan, Fan Yang, Tingting Gao, Ming Wu
url: http://arxiv.org/abs/2608.10444v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models

## Abstract
Large language models (LLMs) have made substantial progress on reasoning tasks that require increasingly long and complex inferential chains. This progress primarily reflects reasoning depth. A complementary and comparatively unexamined capability is reasoning breadth: exploring multiple semantic directions in parallel and integrating the resulting clues into one coherent answer. We introduce MPAR-Bench, a bilingual English-Chinese benchmark that isolates reasoning breadth through multi-point associative reasoning. Inspired by the cooperative game Just One, each item asks a model to recover a hidden target from several independently generated, semantically diverse clues. We construct 1,000 items using a multi-agent clue-generation pipeline, embedding-based diversity filtering, and human verification. Only the answer space is drawn from public word lists, whereas every clue set is generated from scratch. Beyond exact-match accuracy, we evaluate models using accuracy, ANLS, embedding similarity, reasoning-trace verification, and four perturbations: clue masking, order shuffling, distractor injection, and multi-step clues. Across evaluated models, perturbations reduce accuracy by 9-18 percentage points in English and 5-12 percentage points in Chinese. Thinking mode improves standard-setting accuracy, especially in English, but does not consistently reduce sensitivity to perturbations. Case-level analysis also shows that extended reasoning can overturn an initially correct hypothesis. These results indicate that greater reasoning depth does not automatically confer robust reasoning breadth, and that reasoning breadth remains largely uncovered by current benchmarks.

## Metadata
- **Published**: 2026-08-11T03:58:23Z
- **Authors**: Si'an Xie, Jiaxun Liu, Biao Yang, Wei Yuan, Fan Yang, Tingting Gao, Ming Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10444v1)