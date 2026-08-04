---
title: One QK Channel, Many Sources: Guarding Low-Precision Attention Collapse
url: http://arxiv.org/abs/2608.02091v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-50-06Z_OneQKChannel_ManySources_GuardingLow_PrecisionAtte.md
generated_at: 2026-08-03 23:28
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates why bfloat16 transformers abruptly collapse after many training steps and shows that distinct low‑precision errors can trigger the same failure through a shared query‑key (QK) channel. By reproducing GPT‑2 collapse in the streaming‑softmax accumulator, it demonstrates that fixing only the QK projection restores stability while the source fault remains active.

## Key Takeaways  
- Distinct low‑precision errors cause identical attention collapse via a spectral runaway of the QK channel.  
- Correcting solely the QK channel stabilizes training even though the original error source is still present.  
- A dormant controller called QK‑Guard activates parameter‑free QK normalization when logit saturation begins, matching always‑on QK normalization over 60 k steps.

## Context  
Transformer models increasingly rely on low‑precision arithmetic for scalability, yet accumulation errors can destabilize training. Understanding whether these failures stem from isolated components or shared pathways is crucial for reliable large‑scale AI systems.

## Implications  
Designing interventions at the shared QK locus rather than repairing each fault source independently offers a more robust strategy for model scaling and deployment across different GPU architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02091v1)
