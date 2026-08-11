# Summary: 2026-08-08_03-36-41Z_RouterSensitivityUnderLightweightFine_TuningIdenti.md
Saved: 2026-08-10 22:48
Source: 2026-08-08_03-36-41Z_RouterSensitivityUnderLightweightFine_TuningIdenti.md
Model: None

---

## Summary  
The paper investigates whether lightweight fine‑tuning can reveal which experts in a Mixture‑of‑Experts (MoE) model are less critical, enabling one‑shot pruning without full activation statistics. By training a tiny LoRA adapter on the router weights and measuring their ℓ₂ norm changes per expert, the authors rank experts by sensitivity to adaptation and remove those with the smallest changes in a single step. This approach achieves substantial compression while preserving or even improving model accuracy compared with conventional magnitude‑based or random pruning.

## Key Contributions  
- **Finding 1:** Lightweight fine‑tuning via LoRA adapters uncovers router‑norm updates that pinpoint which experts are less essential for downstream performance.  
- **Finding 2:** Pruning the least‑changed experts yields higher MMLU‑Pro scores (27.54 % vs. 24.42 % after half‑expert removal) and reduces memory by 49 % while cutting per‑token latency by 37 %.  
- **Finding 3:** The router sensitivity criterion transfers to other MoE models such as Qwen1.5, retaining ~49.7 % mean accuracy across eleven benchmarks when half the experts are removed, outperforming random pruning.

## Methodology  
The authors fine‑tune Mixtral‑8×7B‑Instruct with a lightweight LoRA adapter that injects parameters only into router weights. For each expert they compute the ℓ₂ norm of its router weight change during adaptation. Experts are then ranked by this norm and pruned in one shot, leaving those with larger changes intact. The resulting compressed model is evaluated against baseline methods: all‑module LoRA, IA3 (frozen routers), magnitude‑based pruning, and random pruning.

## Results  
Router‑only LoRA trains only 0.002 % of parameters and outperforms all‑module LoRA at the same expert rank after removing half the experts (27.54 % vs. 24.42 %). Accuracy improves to 28.76 %, matching IA3 which freezes router weights, while additive adapters degrade the signal. Router‑guided MMLU‑Pro accuracy declines quasi‑linearly; at maximal compression it remains ~1.8× better than magnitude or random pruning, with a 49 % memory reduction and 37 % latency improvement. At 25 % compression retention is competitive with full activation statistics.

## Significance  
This work provides a provably motivated, scalable method for expert pruning that leverages lightweight adaptation signals, allowing large‑scale MoE models to retain performance while dramatically cutting storage and inference cost—critical for deployment in resource‑constrained environments.

## Related Concepts  
Mixture‑of‑Experts (MoE), router weights, Lightweight Fine‑Tuning, LoRA adapters, ℓ₂ norm of router changes, expert pruning, activation statistics, memory compression, per‑token latency.
