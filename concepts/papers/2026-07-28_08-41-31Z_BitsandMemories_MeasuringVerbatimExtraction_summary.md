# Summary: 2026-07-28_08-41-31Z_BitsandMemories_MeasuringVerbatimExtractionAcrossL.md
Saved: 2026-07-28 20:22
Source: 2026-07-28_08-41-31Z_BitsandMemories_MeasuringVerbatimExtractionAcrossL.md
Model: None

---

## Summary  
The paper proposes a new metric for privacy risk in quantized large language models, focusing on verbatim extraction rather than membership inference. It investigates how quantization affects memorization of training sequences across multiple precision levels and model sizes. By using Pythia models and known memorizable corpora, the authors track verbatim recall while measuring capability loss. They find that quantization selectively forgets some data but not enough to eliminate privacy risk.

## Key Contributions  
- Finding 1: Quantization reduces verbatim memorization faster than it degrades general language capability across all precision levels and model sizes.  
- Finding 2: Even at four‑bit quantization, the largest models still reproduce most memorized sequences with only minor capability loss.  
- Finding 3: The proportion of memorized data that survives quantization grows with model size.

## Methodology  
The authors employ Pythia models (e.g., Pythia‑7B) and a public set of sequences known to be memorized. They evaluate five precision levels from full precision down to four bits, using both GPTQ and bitsandbytes quantization algorithms. For each configuration they measure verbatim extraction rate (percentage of original sequences fully reproduced) and perplexity as a proxy for capability. Experiments are conducted on three model sizes.

## Results  
Across all configurations, verbatim recall drops sharply while perplexity degrades more modestly; at 4‑bit quantization the largest models retain >90 % of memorized sequences with <2 % perplexity increase. The fraction of surviving memorized data scales linearly with model size.

## Significance  
This work shifts focus from membership inference to direct extraction, highlighting that compression does not erase privacy risks and that practitioners should monitor verbatim recall.

## Related Concepts  
Quantization, memory leakage, verbatim extraction, membership inference, perplexity, Pythia models, GPTQ, bitsandbytes.
