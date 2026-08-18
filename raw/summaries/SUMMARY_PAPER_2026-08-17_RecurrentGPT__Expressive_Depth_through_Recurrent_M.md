---
title: RecurrentGPT: Expressive Depth through Recurrent Modulation in Transformers
url: http://arxiv.org/abs/2608.15062v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_06-22-00Z_RecurrentGPT_ExpressiveDepththroughRecurrentModula.md
generated_at: 2026-08-17 21:39
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes RecurrentGPT, a recurrent depth transformer that reuses a fixed set of layers across repeated iterations to balance expressivity and memory efficiency. Under isoFLOPS constraints it matches a 12‑layer GPT‑2 Small while using fewer parameters, and under isoPARAMS deeper recurrence improves validation loss.

## Key Takeaways
- A single shared core iterated R times with fixed prelude and coda blocks reduces parameter count compared to deep unique layers.  
- Under isoFLOPS a 3‑layer RecurrentGPT achieves GPT‑2 Small accuracy with similar FLOPs, showing depth reuse works across scales.  
- At medium scale the model overtakes dense GPT‑2 when token budget is doubled, indicating adaptive reuse yields better performance.

## Context
Transformer scaling faces trade‑offs between memory and quality; prior solutions either sacrifice expressivity or inflate parameters. RecurrentGPT offers a principled depth‑reuse strategy that aligns with gated recurrent mechanisms, offering a new way to compress models without losing capability.

## Implications
Researchers can design smaller, faster inference pipelines while maintaining high accuracy, reducing hardware costs and latency. Practitioners may adopt this architecture for edge deployment where parameter budgets are tight yet performance remains competitive.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15062v1)
