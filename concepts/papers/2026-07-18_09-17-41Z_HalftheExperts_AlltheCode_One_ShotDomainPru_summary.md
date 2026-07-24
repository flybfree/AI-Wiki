# Summary: 2026-07-18_09-17-41Z_HalftheExperts_AlltheCode_One_ShotDomainPruningofM.md
Saved: 2026-07-24 00:04
Source: 2026-07-18_09-17-41Z_HalftheExperts_AlltheCode_One_ShotDomainPruningofM.md
Model: None

---

## Summary  
The paper investigates how many expert subnetworks can be removed from open‑weight mixture‑of‑experts (MoE) coding models while preserving their ability to generate correct code. It evaluates two state‑of‑the‑art MoE families—Qwen3.6‑35B‑A3B and Gemma‑4‑26B‑A4B—using five expert‑pruning strategies and measures impact on the primary HumanEval benchmark as well as perplexity across full and quantized models. The study finds that up to half of the experts can be pruned with no statistically detectable loss on code generation, yet the damage is largely confined to non‑coding abilities. It also demonstrates that perplexity, a common compression metric, often overestimates model degradation after aggressive pruning.

## Key Contributions  
- **Finding 1:** Up to 50 % of expert subnetworks can be removed from both Qwen3.6‑35B‑A3B and Gemma‑4‑26B‑A4B without a statistically detectable loss on the HumanEval coding benchmark, indicating that half the experts are dispensable for core code generation.  
- **Finding 2:** The optimal pruning strategy differs between the two models, showing that domain‑specific validation is required; a recipe validated on one family does not automatically apply to another.  
- **Finding 3:** Perplexity metrics overestimate compression penalties; a lightweight fine‑tune can recover roughly half of the lost performance, and aggressive pruning only outperforms quantization when the latter would need to drop below three bits per weight.

## Methodology  
The authors selected two open‑weight MoE models from distinct families and applied five selection strategies: random expert removal, importance‑based pruning, causal expert importance, failure attribution, and an agentic evaluation where each model repairs its failures via execution feedback. For each strategy they measured (i) code correctness on HumanEval, (ii) perplexity of the full versus quantized models, and (iii) performance after a brief fine‑tune. Quantization was performed at 3 bits per weight to compare compression efficiency.

## Results  
Half the experts can be pruned with no statistically detectable loss in human‑written code generation; the primary degradation is observed on auxiliary tasks. Perplexity of the pruned model exceeds that of the original, confirming poor calibration. A lightweight fine‑tune recovers about 50 % of the lost perplexity score. When quantizing to three bits per weight, aggressive pruning yields comparable compression gains, whereas quantization at higher bit depths does not. Five attempts to overturn these results—guided by better calibration, guarded selection, causal expert importance, failure attribution, and agentic repair—all fail to improve upon the baseline.

## Significance  
The work proves that MoE coding models can be efficiently compressed for typical developer hardware without sacrificing core functionality, challenging the reliance on perplexity as a sole quality metric. It underscores the necessity of task‑specific validation and demonstrates that expert pruning is a viable, model‑family dependent optimization technique.

## Related Concepts  
- Mixture-of‑Experts (MoE) architectures  
- Expert pruning strategies  
- Quantization (bits per weight)  
- Perplexity as a compression metric  
- HumanEval benchmark for code generation  
- Calibration of model outputs  
- Lightweight fine‑tuning for recovery  
- Agentic feedback loops in reinforcement learning
