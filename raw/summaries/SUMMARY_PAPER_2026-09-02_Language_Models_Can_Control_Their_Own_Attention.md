---
title: Language Models Can Control Their Own Attention
url: http://arxiv.org/abs/2609.02737v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-43-38Z_LanguageModelsCanControlTheirOwnAttention.md
generated_at: 2026-09-02 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Declarative Attention (DA), an intrinsic method that lets language models self‑declare which parts of a long context they should attend to, reducing unnecessary KV cache reads. By splitting generation into global, focus, and local modes the model can skip most of the attention computation while still producing accurate outputs. Across 15 long‑context tasks DA cuts attended tokens by up to 52% on Gemma‑4‑31B with only a small accuracy loss.

## Key Takeaways
- DA replaces extrinsic proxy scoring with intrinsic self‑declarations, eliminating O(N) per step cost.
- The three attention modes (global, focus, local) enable efficient decoding without sacrificing much performance.
- Accuracy drops are modest and diminish as model size increases, showing scalability.

## Context
Long‑context language models face a bottleneck where full KV cache reads dominate inference time. Existing work relies on external scoring that still scans the entire context, limiting scalability to billions of tokens. DA offers an alternative that leverages the model’s own reasoning process to prune attention, aligning with trends toward sparse and efficient attention mechanisms.

## Implications
For developers deploying LLMs in real‑time applications such as chatbots or code assistants, DA can dramatically lower latency and memory usage without retraining. The approach opens a path for training‑based methods that could further compress attention patterns, benefiting both research and industry adoption of long‑context AI systems

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02737v1)
