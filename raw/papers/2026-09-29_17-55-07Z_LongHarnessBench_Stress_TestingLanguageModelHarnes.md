---
title: LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning
published: 2026-09-29T17:55:07Z
authors: Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen, Xi Ye
url: http://arxiv.org/abs/2609.38137v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning

## Abstract
Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harnesses, reflected by saturated accuracy across harnesses and largely similar evaluation costs. In this paper, we introduce a benchmark for evaluating both the effectiveness and efficiency of long-context harnesses. Our tasks require diverse retrieval strategies, including lexical search and semantic matching, together with strategic and adaptive reasoning over global and local context. Much of the context is semantically relevant but only a small subset is useful at each step, creating both a challenging search problem and different accuracy--cost tradeoffs across processing strategies. For example, one task requires identifying every person satisfying several conditions using evidence scattered across documents; strategically checking the most selective condition first can narrow the search before verifying the remaining conditions. We evaluate multiple families of frontier language models with four state-of-the-art harnesses. Our benchmarks remain challenging even for strong model--harness combinations: the best reaches 68\% macro-average accuracy across four evaluation suites. More importantly, we find that the same underlying model can exhibit markedly different efficiency under different harnesses. Our results establish efficiency as an important axis for long-context evaluation and provide a testbed for developing harnesses that process context strategically rather than exhaustively.

## Metadata
- **Published**: 2026-09-29T17:55:07Z
- **Authors**: Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen, Xi Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38137v1)