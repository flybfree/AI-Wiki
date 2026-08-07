# Summary: 2026-08-06_15-41-02Z_SAGA_Score_WeightedAdaptiveGenerationAlignmentforL.md
Saved: 2026-08-06 22:19
Source: 2026-08-06_15-41-02Z_SAGA_Score_WeightedAdaptiveGenerationAlignmentforL.md
Model: None

---

## Summary  
The paper introduces **SAGA**, a parser‑guided preference optimisation framework that substitutes costly human annotations with dependency‑parser supervision for low‑resource Nordic languages. It builds an adaptive generation alignment system that converts parser judgments into DPO preference pairs, blends parser quality with lexical diversity in a composite reward, and filters out noisy or low‑information pairs using a reward‑gap criterion while monitoring reward hacking. Experiments on Danish, Icelandic, and Norwegian Bokmål demonstrate consistent gains in grammatical quality without any human labels. The results show that parser‑derived supervision can reliably improve language models for morphologically rich languages where high‑quality parsers are available.

## Key Contributions  
- [Finding 1] SAGA replaces human preference labels with dependency‑parser supervision to generate DPO preference pairs.  
- [Finding 2] A composite reward that combines parser quality and lexical diversity is used, filtered by a reward‑gap criterion to remove low‑information pairs.  
- [Finding 3] Reward‑hacking monitoring ensures reliable supervision throughout the training process.

## Methodology  
The authors employ GPT‑SW3‑1.3B as the base model for Danish, Icelandic, and Norwegian Bokmål. Synthetic preference pairs are created by parsing each generated sentence with Stanza’s dependency parser; a score is assigned based on parse success probability and lexical diversity of the output tokens. These scores feed into DPO to align generation toward the preferred pair. Pairs whose reward gap falls below a threshold are discarded, and a drift detector flags any sudden reward changes that could indicate hacking. The whole pipeline runs in a single training pass per language.

## Results  
Danish parse success rises from 69 % to **93.8 %**; Icelandic gains **+4.5 percentage points** on an independent Stanza evaluation (three‑run mean +3.3 pp); Norwegian Bokmål improves by **+28 percentage points**. In pairwise native‑speaker comparisons, SAGA outputs are preferred in **80 %** of trials, indicating strong grammatical quality.

## Significance  
This work proves that parser‑derived supervision can effectively align generation for morphologically complex low‑resource languages, dramatically reducing the need for expensive human preference annotations and enabling scalable, reproducible alignment across Nordic tongues. It opens a practical path to high‑quality language model improvement without relying on costly annotation pipelines.

## Related Concepts  
- Preference optimisation (DPO)  
- Dependency parsing supervision  
- Reward‑gap filtering  
- Reward hacking detection  
- Token‑level lexical diversity scoring  
- Morphologically rich language modeling
