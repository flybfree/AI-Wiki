---
title: Right Answer, Wrong Method: Shortcut Hacking Misleads the Evaluation of LLM Reasoning on Frontier Science Benchmarks
published: 2026-08-03T16:21:56Z
authors: Xuan Ren, Weiqi Zhai, Tianle Pu, Yihua Zhu, Yihua Zhu, Hu Wei, Bing Zhao
url: http://arxiv.org/abs/2608.02442v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Right Answer, Wrong Method: Shortcut Hacking Misleads the Evaluation of LLM Reasoning on Frontier Science Benchmarks

## Abstract
Scientific reasoning benchmarks typically evaluate large language models (LLMs) using final-answer accuracy. However, a correct answer does not necessarily demonstrate the reasoning capability targeted by the problem. We identify Solution Hacking, a failure mode in which an LLM reaches the correct answer through invalid shortcuts, such as numerical search, enumeration, guessing, or answer-first verification, without providing a valid task-targeted derivation. We systematically analyze this phenomenon across difficulty levels, scientific domains, and frontier models. Solution hacking increases sharply with benchmark difficulty, from 2.2\% on common problems to 28.3\% on Olympiad-level problems and 37.4\% on HLE. Moreover, 8.2\%-44.1\% of answers credited as correct across frontier models are identified as hacked solutions. We further develop expert-inspired anti-hacking strategies, including an automatic judge and a test-time instruction. The results show that suppressing shortcut behavior substantially reduces reported accuracy while having a smaller effect on correct and non-hacked accuracy. These findings reveal that answer-only evaluation can overestimate the scientific reasoning capabilities of frontier LLMs.

## Metadata
- **Published**: 2026-08-03T16:21:56Z
- **Authors**: Xuan Ren, Weiqi Zhai, Tianle Pu, Yihua Zhu, Yihua Zhu, Hu Wei, Bing Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02442v1)