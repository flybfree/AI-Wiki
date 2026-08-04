---
title: TextNCA: Neural Cellular Automata for Language Modeling via Hierarchical Local Attention
published: 2026-08-03T10:47:05Z
authors: Avni Mittal, Avinash Anand, Ashutosh Kumar, Dikshant Kukreja, Kritarth Prasad, Sushane Dulloo, Erik Cambria, Timothy Liu, Zhengkui Wang, Rajiv Ratn Shah
url: http://arxiv.org/abs/2608.02050v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TextNCA: Neural Cellular Automata for Language Modeling via Hierarchical Local Attention

## Abstract
Can a strictly local, iterated, weight-shared computation primitive support language modelling, and which of those three properties actually drives the model's behaviour? We define \textsc{TextNCA}, a 1D causal windowed-attention realisation of the Neural Cellular Automaton primitive, and study a hierarchical variant that cascades three stages with windows $w \in \{8, 32, 128\}$ and $T_s$ shared-weight iterations per stage, all on WikiText-103 at roughly 30M parameters and 60k training steps. The model does not match a parameter-matched Transformer at this scale (Hier-TextNCA $60.3$ vs.\ Transformer-6L $52.8$ and Transformer-12L $44.7$ PPL), so we treat it as an analytical probe rather than a proposed alternative. The behaviour we observe is largely explained by the staged narrow-to-wide schedule: a non-iterating sliding-window Transformer that reuses the same schedule comes within $+4.1$ PPL of the iterated model, while reversing, flattening, or breaking the monotonic ordering of the schedule costs between $+16.7$ and $+70.8$ PPL. Iteration adds a smaller bounded benefit on top of the schedule, with a clear optimum at $T_s{=}4$ and a U-shaped degradation beyond it. The GRU gate and learned per-step embeddings are required for that benefit to appear, and training with random $T_s$ yields an inference-time iteration-count knob at the cost of substantially higher absolute PPL. We position the work as a controlled reading of which parts of NCA-style computation carry the weight in language modelling.

## Metadata
- **Published**: 2026-08-03T10:47:05Z
- **Authors**: Avni Mittal, Avinash Anand, Ashutosh Kumar, Dikshant Kukreja, Kritarth Prasad, Sushane Dulloo, Erik Cambria, Timothy Liu, Zhengkui Wang, Rajiv Ratn Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02050v1)