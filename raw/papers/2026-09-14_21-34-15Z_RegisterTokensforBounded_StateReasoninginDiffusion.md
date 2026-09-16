---
title: Register Tokens for Bounded-State Reasoning in Diffusion Language Models
published: 2026-09-14T21:34:15Z
authors: Albert Ge, Chandan Singh, Yufan Zhuang, Xiaodong Liu, Jianfeng Gao, Frederic Sala
url: http://arxiv.org/abs/2609.16372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Register Tokens for Bounded-State Reasoning in Diffusion Language Models

## Abstract
Masked diffusion language models (dLLMs) generate text by iteratively denoising masked tokens with bidirectional attention. Extending reasoning across generation chunks normally requires keeping earlier generated text in context. We ask whether a dLLM can instead continue reasoning after that text is cleared, using only a fixed-size carried state. We implement this state as a small number of register tokens: dedicated fixed-position tokens whose continuous hidden states are trained to carry reasoning progress across generation chunks. We post-train dLLMs to decode a chunk of text, clear it while preserving the register values, and continue decoding from the prompt and carried state. In our main comparisons on LLaDA and Dream, registers outperform discrete-text carry on every benchmark, with gains of up to 8.5 points on math and 19.5 points on code. Registers are especially effective for bounded code generation, where correct programs usually span several chunks. Finally, registers can be further refined with reinforcement learning on long-horizon reasoning tasks.

## Metadata
- **Published**: 2026-09-14T21:34:15Z
- **Authors**: Albert Ge, Chandan Singh, Yufan Zhuang, Xiaodong Liu, Jianfeng Gao, Frederic Sala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16372v1)