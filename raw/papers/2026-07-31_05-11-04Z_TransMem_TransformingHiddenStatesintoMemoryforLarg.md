---
title: TransMem: Transforming Hidden States into Memory for Large Language Models
published: 2026-07-31T05:11:04Z
authors: Haodong Lei, Junming Liu, Yirong Chen, Pinlong Cai, Botian Shi, Ding Wang, Hongsong Wang
url: http://arxiv.org/abs/2607.29032v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TransMem: Transforming Hidden States into Memory for Large Language Models

## Abstract
Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence distributed across past observations and actions. However, useful information encoded in previously computed representations is often underutilized during subsequent generation. We propose \textbf{TransMem}, a lightweight inference-time parametric memory module that transforms sparse historical hidden states from a frozen LLM backbone into reusable memory representations. TransMem uses a lightweight gating network to dynamically apply the latent intervention to the current hidden states, without repeatedly encoding the preceding context. To learn transferable memory utilization rather than task-specific knowledge, we introduce evidence-conditioned self-distillation. A memory-augmented student processes the full context and matches the predictive distribution of an evidence-only teacher that shares the same frozen backbone. Experiments on LoCoMo, HotpotQA, and MemoryAgentBench demonstrate consistent improvements across different model architectures and scales. TransMem yields gains of 11.58--29.25 $F_1$ on LoCoMo and 10.20--13.03 $F_1$ on HotpotQA, while improving the average MemoryAgentBench accuracy from 29.54\% to 40.00\%. These results establish sparse historical hidden states as an effective and efficient memory substrate for long-context LLM agents. Our code is available at https://github.com/Haodong-Lei-Ray/TransMem.

## Metadata
- **Published**: 2026-07-31T05:11:04Z
- **Authors**: Haodong Lei, Junming Liu, Yirong Chen, Pinlong Cai, Botian Shi, Ding Wang, Hongsong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29032v1)