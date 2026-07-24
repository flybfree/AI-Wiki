# Summary: 2026-07-22_12-08-41Z_SolarOpen2TechnicalReport.md
Saved: 2026-07-24 01:48
Source: 2026-07-22_12-08-41Z_SolarOpen2TechnicalReport.md
Model: None

---

## Summary  
The paper introduces Solar Open 2, a 250B‑A15B Mixture‑of‑Experts language model designed for long‑horizon agentic tasks with a 1M‑token context window. It builds on Solar Open 1 by using a hybrid attention stack that interleaves one softmax layer among every three linear‑attention layers, eliminates positional encoding, and employs a gated delta rule extended to negative eigenvalues. The model is trained efficiently through strong initialization from the shared skeleton of Solar Open 1 and high‑value data curation that reduces a 20T pool to a 10T mixture while preserving quality and rarity.

## Key Contributions  
- [Finding 1] The hybrid attention architecture enables a 1M‑token window without positional encoding.  
- [Finding 2] Training from Solar Open 1’s shared skeleton combined with value‑aware data curation yields higher performance per token.  
- [Finding 3] Multi‑teacher On‑Policy Distillation of twelve domain specialists creates a single model that excels on both English and Korean agentic benchmarks.

## Methodology  
The authors approached the problem by first designing an attention stack interleaving one softmax layer among every three linear‑attention layers to manage context length. They leveraged full pre‑training with a 20T pool reduced via mixture‑ratio optimization, preserving quality and rarity. Training started from Solar Open 1’s 5.69B shared skeleton, then fine‑tuned the MoE parameters. After training twelve domain specialists on purpose‑built scenarios, they applied MOPD to merge them into one model.

## Results  
Solar Open 2 outperforms comparable open‑weight models (DeepSeek‑V4‑Flash, MiMo‑V2.5) on MMLU‑Pro, LiveCodeBench, and APEX‑Agents. It also achieves the highest average on Korean benchmarks, including Ko‑GDPval, where it competes with DeepSeek‑V4‑Pro at a fraction of its size (1.6T parameters). The model’s 250B parameter count is supported by efficient MoE scaling.

## Significance  
This work demonstrates that large‑scale MoE models can be made practical for long‑context agentic reasoning while staying cost‑effective, opening doors to real‑world deployment of autonomous agents with minimal compute budget.

## Related Concepts  
Mixture‑of‑Experts (MoE), hybrid attention, delta rule initialization, value‑aware data curation, multi‑teacher distillation, long‑context windowing, agentic benchmarks.
