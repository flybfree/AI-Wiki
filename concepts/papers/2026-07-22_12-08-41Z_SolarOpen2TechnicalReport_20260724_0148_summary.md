# Summary: 2026-07-22_12-08-41Z_SolarOpen2TechnicalReport.md
Saved: 2026-07-24 01:48
Source: 2026-07-22_12-08-41Z_SolarOpen2TechnicalReport.md
Model: None

---

## Summary  
Solar Open 2 is a 250B‑parameter mixture‑of‑experts (MoE) language model designed to support long‑horizon agentic tasks while fitting within a fixed compute budget. It achieves a 1 million‑token context window using a hybrid attention stack that interleaves softmax layers with linear‑attention layers and employs a gated delta rule for negative eigenvalues, eliminating positional encodings. The model is trained efficiently by leveraging the 5.69B shared skeleton from Solar Open 1 and by curating high‑value data through quality‑ and rarity‑aware selection, then consolidates twelve domain specialists via Multi‑teacher On‑Policy Distillation (MOPD).  

## Key Contributions  
- [Finding 1] The hybrid attention stack enables a 1M‑token window without positional encodings, using gated delta rules for negative eigenvalues.  
- [Finding 2] Training efficiency is achieved via a strong starting point (transfer from Solar Open 1) and high‑value data curation that optimizes quality and rarity while preserving token budget.  
- [Finding 3] Agentic competence is built by training twelve domain specialists and merging them through MOPD, resulting in performance comparable to top open‑weight models on English benchmarks and superior on Korean benchmarks at a fraction of the size.  

## Methodology  
The authors adopt a MoE architecture where each expert operates within a linear‑attention block, with one softmax layer placed every three blocks to balance capacity and cost. Positional information is omitted; instead, a gated delta rule handles negative eigenvalues to maintain stability. Training proceeds in two phases: (1) fine‑tuning the 5.69B shared skeleton from Solar Open 1 while pre‑training on a curated 10T mixture derived from a 20T pool using quality‑ and rarity‑aware selection; (2) training twelve domain specialists on purpose‑built scenarios, then consolidating them via MOPD—a multi‑teacher on‑policy distillation that preserves task‑specific knowledge.  

## Results  
On English benchmarks, Solar Open 2 outperforms MMLU‑Pro, LiveCodeBench, and the APEX‑Agents suite, matching DeepSeek‑V4‑Flash and MiMo‑V2.5 while maintaining competitive scores elsewhere. In Korean evaluations it sets new records on fast‑tier closed APIs and remains within a sixth of DeepSeek‑V4‑Pro’s performance (1.6 T parameters) at less than 0.06 B parameters, demonstrating strong efficiency.  

## Significance  
Solar Open 2 demonstrates that large‑scale MoE models can be made both long‑context capable and computationally efficient, opening the door to open‑weight agentic agents that rival proprietary systems without prohibitive cost. Its hybrid attention design and value‑focused data curation set new standards for scaling language models under fixed compute budgets.  

## Related Concepts  
MoE (Mixture‑of‑Experts), hybrid attention stack, gated delta rule, positional encoding elimination, high‑value data curation, mixture‑ratio optimization, Multi‑teacher On‑Policy Distillation (MOPD), long‑context window, token budgeting.
