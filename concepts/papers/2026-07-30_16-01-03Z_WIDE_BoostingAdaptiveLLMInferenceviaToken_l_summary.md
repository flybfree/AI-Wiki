# Summary: 2026-07-30_16-01-03Z_WIDE_BoostingAdaptiveLLMInferenceviaToken_levelDyn.md
Saved: 2026-07-30 22:18
Source: 2026-07-30_16-01-03Z_WIDE_BoostingAdaptiveLLMInferenceviaToken_levelDyn.md
Model: None

---

## Summary  
The paper introduces **WIDE**, an end‑to‑end differentiable token‑level dynamic width pruning framework for large language models that adapts computation per token across both prefill and decode tasks. It extends prior work beyond layer‑level decisions to neuron‑block granularity, enabling fine‑grained sparse execution while preserving model quality. By combining a two‑stage training pipeline with a hardware‑agnostic kernel co‑design, WIDE learns effective token‑wise sparse patterns that can be applied at 50 % sparsity. The method achieves substantial speedups (up to 4.95× in decoding) and performance boosts compared with state‑of‑the‑art dynamic depth pruning.

## Key Contributions  
- **Finding 1**: WIDE introduces token‑level dynamic width pruning that selects attention‑head groups and FFN‑channel groups per token, achieving better quality retention than static or coarse‑grained methods.  
- **Finding 2**: The two‑stage training pipeline learns effective sparse execution patterns across prefill and decode scenarios, improving accuracy retention at high sparsity levels.  
- **Finding 3**: A co‑design framework decomposes dynamic sparsity into mask reordering (hardware‑agnostic), block‑level skipping, and intra‑block skipping, enabling flexible execution across hardware constraints.

## Methodology  
WIDE is built as an end‑to‑end differentiable model where each token’s computation width is modulated by learnable masks. The first stage optimizes a loss that balances accuracy and sparsity, while the second stage refines pruning patterns via gradient updates. The co‑design framework separates mask reordering (which can be applied uniformly across hardware), block‑level skipping (pruning entire attention blocks), and intra‑block skipping (skipping within blocks), allowing the system to adapt to different execution granularities.

## Results  
At 50 % sparsity, WIDE delivers a **55.1 %** performance boost over the best dynamic depth pruning under calibration‑only settings. In prefill inference it achieves up to **1.98×** kernel‑level speedup and **4.95×** decoding acceleration; end‑to‑end speeds improve by **1.68×** (prefill) and **1.55×** (decode). These results demonstrate that fine‑grained token pruning can provide both high efficiency gains and minimal quality loss.

## Significance  
By targeting individual tokens for dynamic computation allocation, WIDE bridges the gap between theoretical sparsity benefits and practical inference speedups, offering a scalable solution for real‑world LLM deployment across diverse hardware. This work shows that fine‑grained pruning can be both effective and implementable without sacrificing model utility.

## Related Concepts  
token‑level pruning, dynamic width pruning, end‑to‑end differentiable training, kernel co‑design, attention‑head selection, FFN‑channel selection, block‑level skipping, intra‑block skipping, static vs. dynamic sparsity.
