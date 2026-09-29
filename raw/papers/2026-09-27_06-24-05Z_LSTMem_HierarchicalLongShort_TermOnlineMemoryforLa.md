---
title: LSTMem: Hierarchical Long Short-Term Online Memory for Large Language Models
published: 2026-09-27T06:24:05Z
authors: Xianglong Shi, Ruijie Yang, Sirui Zhao, Shukang Yin, Zihao Bian, Tinghao Yi, Enhong Chen
url: http://arxiv.org/abs/2609.33268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LSTMem: Hierarchical Long Short-Term Online Memory for Large Language Models

## Abstract
Large language models increasingly serve as long-horizon assistants and agents, where they must both accumulate information across interactions and make the relevant parts available when later requests depend on them. Existing compact online memories typically use a single persistent state both to accumulate history and to serve readout, so what the memory stores cannot be controlled separately from what it exposes to the current computation. We propose LSTMem, an LSTM-inspired online memory that instead equips each layer of a frozen LLM with two matrix-valued states: a cell state that accumulates history and a hidden state whose readouts correct the backbone's attention. Input and forget gates control what the cell stores, while an output gate separately controls what the cell exposes through the hidden state. LSTMem further connects memory across depth through forward hidden-state propagation and block-end feedback, and uses higher-layer reconstruction gradients to refine lower-layer cell states before rebuilding hidden states from shallow to deep layers. Across memory benchmarks on Qwen3-4B-Instruct, LSTMem consistently improves MemoryAgentBench, LoCoMo, and HotpotQA over the plain backbone. Comparisons further show that the LSTM-based memory formulation outperforms an associative-memory counterpart, while removing cross-layer hidden-memory propagation degrades performance. These results demonstrate the benefits of separating memory accumulation from memory expression and organizing memory hierarchically across model depth. The code is available at https://github.com/Longchentong/LSTMem.

## Metadata
- **Published**: 2026-09-27T06:24:05Z
- **Authors**: Xianglong Shi, Ruijie Yang, Sirui Zhao, Shukang Yin, Zihao Bian, Tinghao Yi, Enhong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33268v1)