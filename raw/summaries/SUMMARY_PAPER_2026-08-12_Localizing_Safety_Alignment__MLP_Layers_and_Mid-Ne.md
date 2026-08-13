---
title: Localizing Safety Alignment: MLP Layers and Mid-Network Blocks Encode Refusal Behavior in Large Language Models
url: http://arxiv.org/abs/2608.11583v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_02-44-30Z_LocalizingSafetyAlignment_MLPLayersandMid_NetworkB.md
generated_at: 2026-08-12 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates where safety‑aligned refusal behavior is encoded in large language models by transplanting weights from aligned to unaligned base models at different granularities. Experiments show that MLP weight replacements are far more effective than attention or layer‑region swaps, and that refusal parameters concentrate in a specific mid‑network block (layers 8–11). The results also reveal non‑additive effects: adding extra aligned blocks can sometimes reduce refusal performance, and greedy selection of model‑dataset pairs varies with the source benchmark.

## Key Takeaways  
- Replacing MLP parameters recovers substantially more malicious‑prompt refusal than replacing attention parameters, with gains of at least 2.7 times across all benchmarks.  
- Refusal‑relevant parameters consistently concentrate in a mid‑network block spanning layers 8–11, which is selected first in greedy searches over model‑dataset pairs.  
- The composition of safety‑relevant components is non‑additive; adding more aligned blocks can reduce refusal performance, and selective subsets may outperform full MLP transplantation on both malicious and benign prompts.

## Context  
Current safety alignment research often assumes that safety properties are distributed across the entire network, but this view overlooks the possibility of localized encoding. The brittleness observed in large language models suggests that interventions targeting specific parameter groups could be more effective than blanket updates. This work provides empirical evidence for such a focused approach.

## Implications  
For practitioners, the findings point to MLP weights as primary levers for improving refusal behavior and highlight the need to consider benchmark‑specific greedy ordering when designing alignment strategies. Targeted interventions based on these localized insights could lead to more robust and efficient safety alignment in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11583v1)
