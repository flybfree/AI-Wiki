---
title: Spoken Language Models that Think Aloud
published: 2026-09-22T14:25:04Z
authors: Junyi Ao, Kainan Peng, Mingbo Ma, Shun Zhang, Zhenyu Tang, Xutai Ma, Xiang Li, Yinghao Li, Yuancheng Wang, Zhizheng Wu, Haizhou Li, Qing He, Xubo Liu
url: http://arxiv.org/abs/2609.26488v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spoken Language Models that Think Aloud

## Abstract
While Chain-of-Thought (CoT) reasoning has improved the capability of language models, directly applying it to Spoken Language Models (SLMs) may introduce long silent intervals under the serial "think-then-speak" paradigm, disrupting real-time spoken interaction. To address this issue, we propose an asynchronous think-aloud framework for reasoning-based SLMs within the Thinker-Talker architecture. The framework maintains a primary reasoning stream for logical deduction and a lightweight think-aloud stream that generates short, task-grounded progress utterances conditioned on the user input and the evolving reasoning state. A dynamic balance strategy coordinates the two streams at runtime, triggering additional think-aloud speech to avoid silent gaps and canceling pending utterances when the final response becomes ready. Experiments on spoken reasoning and question-answering benchmarks show that our approach substantially reduces user-audible silence during reasoning while maintaining answer accuracy comparable to that of a serial "think-then-speak" baseline, demonstrating the potential of asynchronous think-aloud for responsive interaction in SLMs.

## Metadata
- **Published**: 2026-09-22T14:25:04Z
- **Authors**: Junyi Ao, Kainan Peng, Mingbo Ma, Shun Zhang, Zhenyu Tang, Xutai Ma, Xiang Li, Yinghao Li, Yuancheng Wang, Zhizheng Wu, Haizhou Li, Qing He, Xubo Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26488v1)