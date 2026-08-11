---
title: Linearized 2-Simplicial Attention
url: http://arxiv.org/abs/2608.09307v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-53-30Z_Linearized2_SimplicialAttention.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a linearized version of 2-simplicial attention that rewrites the trilinear score as an inner product between a composite query and a key, allowing the sum over one token axis to resemble ordinary softmax attention. By approximating this sum with positive random features and storing the past in a fixed-size state while keeping only a short window of recent tokens explicit, it achieves linear cost per sequence length yet retains global reach. The authors combine this with Kimi Delta Attention to build a model that uses no softmax attention at all. Under matched compute, the model attains the highest mean downstream accuracy among compared architectures and reduces LAMBADA perplexity from 715.6 to 602.6 at 16k context.

## Key Takeaways
- The trilinear score is linearized into an inner product between a composite query and a key, enabling the sum over one axis to match ordinary softmax attention.
- Positive random features approximate the sum, allowing storage of the entire past in a fixed-size state while only recent tokens are explicit.
- This design yields linear cost per sequence length with global reach, surpassing windowed 2-simplicial attention.

## Context
Attention mechanisms dominate large language models, but their quadratic complexity limits context lengths. Efficient alternatives that maintain long-range dependencies are crucial for scalable AI systems. This work demonstrates a method that balances speed and global context, addressing a key bottleneck in model design.

## Implications
For practitioners, the linearized 2-simplicial attention offers a path to build models with longer contexts at lower compute cost, enabling deployment on resource-constrained hardware. The integration with Kimi Delta Attention eliminates softmax entirely, simplifying training and inference pipelines while improving performance metrics such as accuracy and perplexity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09307v1)
