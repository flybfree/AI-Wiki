---
title: Language Models Can Control Their Own Attention
url: http://arxiv.org/abs/2609.02737v1
type: paper-summary
date: 2026-09-04
source_paper: 2026-09-02_15-43-38Z_LanguageModelsCanControlTheirOwnAttention.md
generated_at: 2026-09-04 15:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Declarative Attention (DA), a method that lets language models explicitly state which parts of their context they should attend to during generation. By parsing these self‑declared attention modes as tool calls, the inference engine can skip most of the KV cache read, dramatically reducing the number of attended tokens while only incurring minor accuracy losses.

## Key Takeaways
- DA enables intrinsic sparse attention by having the model declare global, focus, or local attention regions without external proxy scores.  
- On off‑the‑shelf models such as Gemma‑4‑31B and Qwen‑3.6‑27B, DA cuts attended tokens by 52 % and 31 % respectively with accuracy drops of only 1.27 pp and 2.75 pp that diminish at larger scales.  
- The protocol partitions decoding into three modes—global (full context), focus (a specific region), and local (recent output)—allowing the model to self‑regulate its attention budget.

## Context
Current large language models must read the entire KV cache for each token, causing quadratic cost in long conversations. Existing mitigation strategies rely on costly extrinsic scoring that still scales linearly with context length. This work shows that models can internally decide relevance, offering a scalable path toward truly sparse attention.

## Implications
DA provides a practical way to lower inference latency and memory usage without sacrificing performance, especially valuable for real‑time applications handling millions of tokens. It also opens research avenues where training could further refine the model’s ability to self‑declare attention, paving the way for more efficient AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02737v1)
