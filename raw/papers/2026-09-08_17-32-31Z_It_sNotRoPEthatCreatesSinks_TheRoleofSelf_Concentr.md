---
title: It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention
published: 2026-09-08T17:32:31Z
authors: Raito Kiya, Satoki Ohashi, Kosuke Sato, Go Kamoda, Ryosuke Takahashi, Yuji Yamamoto, Daiki Shiono, Keisuke Sakaguchi, Goro Kobayashi
url: http://arxiv.org/abs/2609.09085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention

## Abstract
Large Language Models (LLMs) often exhibit "Attention Sink" (AS) and the accompanying "Massive Activations" (MAs) at the initial position of a sequence. These phenomena frequently co-occur, and MAs can pose challenges for low-bit quantization. In this study, we analyze the factors underlying AS and MAs that emerge at the initial position regardless of the token occupying it. Our experiments suggest that self-concentration of attention, resulting from the causal mask, and the subsequent Value-non-mixing in attention outputs contribute to AS and MAs. These findings provide new empirical evidence on the internal dynamics of LLMs, offering insights that may inform future quantization strategies and advance our understanding of the internal mechanisms of attention layers.

## Metadata
- **Published**: 2026-09-08T17:32:31Z
- **Authors**: Raito Kiya, Satoki Ohashi, Kosuke Sato, Go Kamoda, Ryosuke Takahashi, Yuji Yamamoto, Daiki Shiono, Keisuke Sakaguchi, Goro Kobayashi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09085v1)